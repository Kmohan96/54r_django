import email
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import StudentNew,Users
from django.contrib.auth.hashers import make_password,check_password
import jwt
from django.conf import settings
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo
# Create your views here.
def sample(request):
    return HttpResponse("hello world")
def jsonresponse(request):
    data={"name":"Saiteja","age":22}
    return JsonResponse(data)
def dynamicresponse(request):
    name1=request.GET.get("name1",'')
    return HttpResponse(f"hello {name1}")

def dynamicresponse1(request):
    name1=request.GET.get("name1","Mohansaiteja")
    city=request.GET.get("city","Hyderabad")
    return HttpResponse(f"hello {name1} from {city}")

def add(request):
    a = request.GET.get("a", 0)
    b = request.GET.get("b", 0)
    result = int(a) + int(b)
    return HttpResponse(f"sum:{result}")

def sub(request):
    a=request.GET.get("a",0)
    b=request.GET.get("b",0)
    result = int(a) - int(b)
    return HttpResponse(f"sum:{result}")


def mult(request):
    a=request.GET.get("a",0)
    b=request.GET.get("b",0)
    result = int(a) * int(b)
    return HttpResponse(f"sum:{result}")


def div(request):
    a=request.GET.get("a",0)
    b=request.GET.get("b",0)
    result = int(a)//int(b)
    return HttpResponse(f"sum:{result}")



def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status": "ok", "db": "connected"})
    except Exception as e:
        return JsonResponse({"status": "error", "db": str(e)})
    

# @csrf_exempt
# def addStudent(request):
#     print(request.method)
#     if request.method == "POST":
#         data=json.loads(request.body)
#         student=StudentNew.objects.create(
#             name=data.get('name'),
#             age=data.get("age"),
#             email=data.get("email")
#             )
#         return JsonResponse({"status":"success","id":student.id},status=200)
#     return JsonResponse({"error":"use post method"},status=400)


@csrf_exempt
def addStudent(request):
    print("METHOD:", request.method)

    # # Handle GET request
    # if request.method == "GET":
    #     result=list(StudentNew.objects.values())
    #     print(result)
    #     return JsonResponse({"status": "ok","data":result}, status=200)
    if request.method == "GET":
      student_id = request.GET.get("id")  # get id from ?id= in URL
      if student_id:
        try:
            student = StudentNew.objects.get(id=student_id)
            result = {
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "age": student.age,
                # add other fields as needed
            }
            return JsonResponse({"status": "ok", "data": result}, status=200)
        except StudentNew.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Student not found"}, status=404)
      else:
        result = list(StudentNew.objects.values())
        return JsonResponse({"status": "ok", "data": result}, status=200)


    # Handle POST request
    elif request.method == "POST":
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        data = json.loads(request.body.decode('utf-8'))

        student = StudentNew.objects.create(
            name=data.get("name"),
            age=data.get("age"),
            email=data.get("email")
        )

        return JsonResponse({"status": "success", "id": student.id}, status=200)

    #  Handle PUT request
    elif request.method == "PUT":
        data = json.loads(request.body.decode('utf-8'))
        ref_id=data.get("id") #getting id
        new_email=data.get("email")#getting email
        existing_student=StudentNew.objects.get(id=ref_id) #fetched the object as  per id

        existing_student.email=new_email
        existing_student.save()

        #fetched updated data-it is just to show the updated data in response
        updated_data=StudentNew.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status": "data updated successfully", "updated_data": updated_data}, status=200)

    # Handle DELETE request
    elif request.method == "DELETE":
        data = json.loads(request.body.decode('utf-8'))
        ref_id = data.get("id")  # getting id
        get_deleting_data=StudentNew.objects.filter(id=ref_id).values().first()
        to_be_delete = StudentNew.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status": "success","message":"student record deleted successfully","deleted_data": get_deleting_data}, status=200)

    #  Handle any other HTTP method
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)




#filtering age>20
@csrf_exempt
def addStudent_age_20(request):
    print("METHOD:", request.method)
    if request.method == "GET":
            students = StudentNew.objects.filter(age__gt=20)
            result = list(students.values())
            return JsonResponse({"status": "ok", "data": result}, status=200)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)
            


#ordering by name
@csrf_exempt
def orderbyname(request):
    if request.method == "GET":
        students = StudentNew.objects.order_by('name')  # ascending order (A → Z)
        result = list(students.values())
        return JsonResponse({"status": "ok", "data": result}, status=200)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)



def job1(request):  #http://127.0.0.1:8000/job1/?ssc=True&medically_fit=True&age=24
    return JsonResponse({"message":"u have successfully applied for job1"},status=200) 
def job2(request):
    return JsonResponse({"message":"u have successfully applied for job2"},status=200)


@csrf_exempt
def signUp(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get('username'),
            email=data.get("email"),
            password=make_password(data.get("password"))
            )
        return JsonResponse({"status":'success'},status=200)
    

@csrf_exempt
def login(request):
    if request.method=="POST":
        data=request.POST
        print(data)
        username=data.get('username')
        password=data.get("password")        
        try:
            user=Users.objects.get(username=username)
            issued_time=datetime.now(ZoneInfo("Asia/Kolkata"))
            expired_time=issued_time+timedelta(minutes=25)
            if check_password(password,user.password):
                payload={"username":username,"email":user.email,"id":user.id,"exp":expired_time}
                token=jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
                return JsonResponse({"status":'successfully loggedin',"token":token,"issued_time":issued_time,"expired at":expired_time,"expired_in":int((expired_time-issued_time).total_seconds()/60)},status=200)
            else:
                return JsonResponse({"status":'failure','message':'invalid password'},status=400)
        except Users.DoesNotExist:
            return JsonResponse({"status":'failure','message':'user not found'},status=400)

    
@csrf_exempt
def check(request):
    hashed="pbkdf2_sha256$870000$kWTc8jejxY7sxq3VpC0W9d$FFIqhFO/HLsIUyIGOdCc3Y2RO9qIa07MJOq+aOdsncQ="
    ipdata=request.POST
    print(ipdata)
    #hashed=make_password(ipdata.get("ip"))  #in form iam sending data ip="mohan"
    x=check_password(ipdata.get("ip"),hashed)
    print(x)
    return JsonResponse({"status":"success","data":x},status=200)



@csrf_exempt
def passwordchange(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        username = data.get("username")
        try:
            user = Users.objects.get(username=username)  # check in DB
            new_password = data.get("password")
            hashed_new_password = make_password(new_password)
            user.password = hashed_new_password
            user.save()
            return JsonResponse({"status": "success", "message": "Your password is updated successfully"},status=200)
        except Users.DoesNotExist:
            return JsonResponse(
                {"status": "failure", "message": "User not found"},status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def getallusers(request):
    if request.method=="GET":
        users=list(Users.objects.values())
        print(request.token_data,"token_data in view")
        print(request.token_data.get("username"),"username from token")
        print(users,"users list")
        for i in users:
            print(i["username"],"username from users list")
            if i["username"]==request.token_data.get("username"):
                return JsonResponse({"status":"success","loggin_user":request.token_data,"data":users},status=200)    
        else:
            return JsonResponse({"error":"unauthorized access"},status=401)
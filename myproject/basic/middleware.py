from django.http import JsonResponse
import json
import re
class basicMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request,"hello")
        if (request.path == '/add/'):
          print(request.method,"method")
          print(request.path)
        response = self.get_response(request)
        return response 

class SscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["/job1/","/job2/"]):
            ssc_result=request.GET.get("ssc")
            print(ssc_result,'hello')
            if(ssc_result !='True'):
                return  JsonResponse({"error":"u should qualify atleast ssc for applying this job"},status=400)
        return self.get_response(request)

class MedicalFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path == "/job1/"):
            medical_fit_result=request.GET.get("medically_fit")
            if(medical_fit_result !='True'):
                return JsonResponse({"error":"u not medically fit to apply for this job role"},status=400)
        return self.get_response(request)
 
class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path in ["/job1/","/job2/"]):
            Age_checker=int(request.GET.get("age",17))
            if Age_checker >25 or Age_checker<18 :
                return JsonResponse({"error":"age must be in b/w 18 and 25"},status=400)
        return self.get_response(request)

class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path == "/signUp/"):
            data=json.loads(request.body)
            username=data.get("username","")
            #checks username is empty or not
            if not username:
                return JsonResponse({"error":"username is required"},status=400)
            #checks length    
            if len(username)<3 or len(username)>20:
                return JsonResponse({"error":"username should contains 3 to 20 characters"},status=400)
            #checks starting and ending
            if username[0] in "._" or username[-1] in "._":
                return JsonResponse({"error":"username should not starts or ends with . or _"},status=400) 
            #checks allowed characters
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
                return JsonResponse({"error":"username  should contains letters,numbers,dot,underscore"},status=400)
            #checks .. and  __
            if ".." in username or "__" in username:
                return JsonResponse({"error:cannot have .. or __"},status=400)   
        return self.get_response(request)  
    

class Emailmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path == "/signUp/"):
            data=json.loads(request.body)
            email=data.get("email","")
            if not email:
              return JsonResponse({"error":"email is required"},status=400)
            if not re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email):
              return JsonResponse({"error":"email should be in abc123@gmail.com"},status=400)
        
        return self.get_response(request)

class Passwordmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path == "/signUp/"):
            data=json.loads(request.body)
            password=data.get("password","")
            if not password:
              return JsonResponse({"error":"email is required"},status=400)
            if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):    #Aa12345@
               return JsonResponse({"error": "Password is not strong"}, status=400)
        return self.get_response(request)



 
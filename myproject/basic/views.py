from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
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
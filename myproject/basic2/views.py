from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def bs2(request):
    return JsonResponse({"data":"this is new app"})
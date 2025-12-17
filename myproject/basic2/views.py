from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Movie_details
def bs2(request):
    return JsonResponse({"data":"this is new app"})


products = [
    {
        "id": 1,
        "name": "Mobile Phone",
        "category": "ElectRoniCs",
        "price": 25000,
        "stock": 15,
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Laptop",
        "category": "Electronics",
        "price": 65000,
        "stock": 8,
        "rating": 4.7
    },
    {
        "id": 3,
        "name": "Headphones",
        "category": "Accessories",
        "price": 3000,
        "stock": 30,
        "rating": 4.2
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "category": "Wearables",
        "price": 12000,
        "stock": 10,
        "rating": 4.4
    },
    {
        "id": 5,
        "name": "Bluetooth Speaker",
        "category": "Audio",
        "price": 5000,
        "stock": 20,
        "rating": 4.3
    }
]

#pathparams
def productbyid(request,id):
    for product in products:
        if product["id"]==id:
            return JsonResponse(product)
    return JsonResponse({"error":"product not found"})

def productByCategory(request,ctg):
    for product in products:
        if product["category"].lower()==ctg.lower():
            return JsonResponse(product)
    return JsonResponse({"error":"product not found"})

def moviebyid(request,id):
    Movie=get_object_or_404(Movie_details,id=id)
    movie_result={"id":Movie.id,"name":Movie.movie_name}
    return JsonResponse({"status":"success","data":movie_result})
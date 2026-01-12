from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PaymentDetails


@method_decorator(csrf_exempt,name='dispatch')
class DemoClass(View):
    def get(self,request):
        return JsonResponse({"info":"get"})
    def post(self,request):
        return JsonResponse({"info":"post"})
    def put(self,request):
        return JsonResponse({"info":"put"})
    def delete(self,request):
        return JsonResponse({"info":"delete"})
    

@method_decorator(csrf_exempt,name='dispatch')
class PaymentInfo(View):
    def post(self,request):
        try:
            data=json.loads(request.body)
            payment= PaymentDetails.objects.create(           
                payment_status=data["status"],
                amount=data["amount"],
                payment_mode=data["mode"],
                user_email=data["email"],
                order_id=data["order_id"]                                      
            )
            return JsonResponse({'message':'posted successfully',"transactionid":str(payment.transaction_id)},status=201,safe=False)
        except Exception as e:
            return JsonResponse({"msg":"error"},status=400)
          


        
  
  
#   "order_id": "ord124",
#   "email": "mohan@gmail.com",
#   "amount": "60000.00",
#   "status": "ok",
#   "mode":"online"
  

    def get(self,request):
        try:
            mydatabase=list(PaymentDetails.objects.values())
            return JsonResponse({"data":mydatabase,"msg":"successfully fetched"},status=200)
        except Exception as e:
            return JsonResponse({"msg":"error"},status=400)
        
    def put(self,request):
        try:
            data=json.loads(request.body)
            order_id=data.get("order_id")
            new_email=data.get("email")
            existing_data=PaymentDetails.objects.get(order_id=order_id)
            existing_data.user_email=new_email
            existing_data.save()
            return JsonResponse({"status":"data updated successfully"},status=200)
        except Exception as e:
            return JsonResponse({"msg":"error"},status=400)
    def delete(self,request):
        try:
            data=json.loads(request.body)
            order_id=data.get("order_id")
            existing_data=PaymentDetails.objects.get(order_id=order_id)
            existing_data.delete()
            return JsonResponse({"status":"data deleted successfully"},status=200)
        except Exception as e:
            return JsonResponse({"msg":"error"},status=400)
    

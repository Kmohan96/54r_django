from django.http import JsonResponse
class helpermixin:
    def greetingmessage(self):
        return "All the best"
    
class responsemixin:
    def success(self,name):
        return JsonResponse({"message":f"successfully done by {name}",} )
    def error(self,name):
        return JsonResponse({"message":f"some error occured because of {name}"})
    

class jsonresponsemixins:
    def success(self,data):
        return JsonResponse({"status":"ok","message":"records fetched successfully","result":data})
    def error(self):
        return JsonResponse({"status":"error","message":"something went wrong"})
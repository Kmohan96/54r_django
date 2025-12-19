from django.db import models
import uuid

class PaymentDetails(models.Model):
    transaction_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    order_id=models.CharField(max_length=100)
    user_email=models.EmailField(unique=True)
    payment_mode=models.CharField(max_length=50)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    currency=models.CharField(max_length=50,default='INR')
    paidtime=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=50)

#while generating uuid we can follow few algorithms

# UUID1,UUID4,UUID5--->versions

# 1982546455-->generates a uuid-->UUID1 
# random comb of chars and num--->UUID4 
# generate as per the name--->uui5
from django.db import models

 

class KYC(models.Model):
    First_name=models.CharField(max_length=100)
    Middle_name=models.CharField(max_length=50, null="True",blank="True")
    Last_name=models.CharField(max_length=50)
    Husband_name=models.CharField(max_length=50)
    DOB=models.DateField()
    Age= models.IntegerField()
    Last_period_date=models.DateField()
    Address=models.CharField(max_length=50)



class health_parameter(models.Model):
    upper_bp=models.IntegerField()
    lower_bp=models.IntegerField()
    blood_sugar=models.FloatField()
    body_temp=models.FloatField()
    

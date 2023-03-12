from django.db import models

 

class KYC(models.Model):
    First_name=models.CharField(max_length=50)
    Middle_name=models.CharField(max_length=50, null="True",blank="True")
    Last_name=models.CharField(max_length=50)
    DOB=models.DateField()
    Age= models.IntegerField()
    Address=models.CharField(max_length=50)
    Last_period_date=models.DateField()



class health_parameter(models.Model):
    upper_bp=models.IntegerField()
    lower_bp=models.IntegerField()
    blood_sugar=models.FloatField()
    body_temp=models.FloatField()
    heart_rate=models.IntegerField()

from django.db import models

 

class KYC(models.Model):
    First_name=models.CharField(max_length=100)
    Middle_name=models.CharField(max_length=50, null="True",blank="True")
    Last_name=models.CharField(max_length=50)
    Husband_name=models.CharField(max_length=50,null="True",blank="True")
    Date_of_birth=models.DateField()
    Age= models.IntegerField()
    Last_period_date=models.DateField()
    Address=models.CharField(max_length=50,null="True",blank="True")



class health_parameter(models.Model):
    Systolic_BP=models.IntegerField()
    Diastolic_BP=models.IntegerField()
    Blood_Sugar=models.FloatField()
    Body_Temperature=models.FloatField()
    Result=models.CharField( max_length=50,null="True",blank="True")
    

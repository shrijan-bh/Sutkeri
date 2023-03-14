from django.contrib import admin
from sutkeriapp.models import KYC,health_parameter

class kycadmin(admin.ModelAdmin):
    list_display=("First_name","Middle_name","Last_name","Husband_name","Date_of_birth","Age","Last_period_date","Address")

admin.site.register(KYC,kycadmin)

class healthdataadmin(admin.ModelAdmin):
    list_display=("Systolic_BP","Diastolic_BP","Blood_Sugar","Body_Temperature","Result")

admin.site.register(health_parameter,healthdataadmin)

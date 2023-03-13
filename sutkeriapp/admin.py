from django.contrib import admin
from sutkeriapp.models import KYC,health_parameter

class kycadmin(admin.ModelAdmin):
    list_display=("First_name","Middle_name","Last_name","Husband_name","DOB","Age","Last_period_date","Address")

admin.site.register(KYC,kycadmin)

class healthdataadmin(admin.ModelAdmin):
    list_display=("upper_bp","lower_bp","blood_sugar","body_temp")

admin.site.register(health_parameter,healthdataadmin)

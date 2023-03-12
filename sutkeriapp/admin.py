from django.contrib import admin
from sutkeriapp.models import KYC,health_parameter

class kycadmin(admin.ModelAdmin):
    list_display=("First_name","Middle_name","Last_name","DOB","Age","Address","Last_period_date")

admin.site.register(KYC,kycadmin)

class healthdataadmin(admin.ModelAdmin):
    list_display=("upper_bp","lower_bp","blood_sugar","body_temp","heart_rate")

admin.site.register(health_parameter,healthdataadmin)

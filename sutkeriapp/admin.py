from django.contrib import admin
from sutkeriapp.models import KYC

class kycadmin(admin.ModelAdmin):
    list_display=("First_name","Middle_name","Last_name","DOB","Age","Address","Last_period_date")

admin.site.register(KYC,kycadmin)


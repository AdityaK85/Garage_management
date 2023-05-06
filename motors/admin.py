from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class vehicles(ImportExportModelAdmin):
    list_display = ("fk_user", "veh_name", "veh_year", "veh_reg_date", "veh_reg_no","created_date")
    pass

class quoatation_pattern(ImportExportModelAdmin):
    list_display = ("cust_name", "quotation_no", "cust_addr", "quot_date","cust_phone", "veh_reg_no", "notes", "job_name", "rates","note", "items", "availale_qty","qty", "price", "total_price", "allTotal")

admin.site.register(user_login)
admin.site.register(add_new_cust)
admin.site.register(vehicle_details, vehicles)
admin.site.register(quotations, quoatation_pattern)
admin.site.register(veh_parts)
admin.site.register(importExcel)
admin.site.register(job_machanic)
admin.site.register(machanic_name)
admin.site.register(New_job_order)
admin.site.register(add_mechanics)
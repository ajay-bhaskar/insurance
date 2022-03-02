# Register your models here.

from django.contrib import admin
from .models import insuranceData

class dataSet(admin.ModelAdmin):
    list_filter = ['customer_region']
    search_fields = ['policy_id']

admin.site.register(insuranceData, dataSet)

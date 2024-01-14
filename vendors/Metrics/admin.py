from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(SubscriptionPlan)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'purchased_at', 'duration_months','expired_at','payment')
    # readonly_fields = ('','')
    
@admin.register(CustomUser)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'company_name','profile_picture','phone_number','address','bio','subscription_plan')
    # readonly_fields = ('','')
    
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'contact_details', 'address','on_time_delivery_rate','vendor_code')
    readonly_fields = ('vendor_code','on_time_delivery_rate')


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id','po_number','vendor','order_date','delivery_date','items','quantity')
    readonly_fields = ('id','po_number',)

@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')

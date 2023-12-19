from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_on_time_delivery_rate(sender, instance, **kwargs):
    print("instance-=-=-=-=-",instance)
    print("kwargs-=-=-=-=-",kwargs)
    vendor = instance.vendor
    if kwargs.get('created', False) or kwargs.get('update_fields', None):
        complete_orders = PurchaseOrder.objects.filter(vendor = vendor, status = 'completed',
                                                    delivery_date__lte=instance.delivery_date).count()
        
        total_completed_orders = PurchaseOrder.objects.filter(vendor=vendor,status='completed').count()

        on_time_delivery_rate = (complete_orders / total_completed_orders) * 100 if total_completed_orders != 0 else 100
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save()
    print("Signals -->> Purchase order created")
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_on_time_delivery_rate(sender, instance, created, **kwargs):
    if created:
        vendor = instance.vendor

        complete_orders = PurchaseOrder.objects.filter(vendor = vendor, status = 'completed',
                                                       delivery_date__lte=instance.delivery_date).count()
        
        total_completed_orders = PurchaseOrder.objects.filter(vendor=vendor,status='completed').count()

        on_time_delivery_rate = ()
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save()
        print("Purchase order created")
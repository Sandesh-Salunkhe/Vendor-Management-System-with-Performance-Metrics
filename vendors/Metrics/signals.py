from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor, CustomUser, SubscriptionPlan
import time
from django.utils import timezone
import datetime
import random
import string


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
    

@receiver(post_save, sender=CustomUser)
def set_free_plan(sender, instance, *args, **kwargs):
    if kwargs.get('created', False):
        plan = SubscriptionPlan.objects.get(name="Free Plan")
        instance.subscription_plan = plan
        instance.purchased_at = timezone.now()
        instance.expired_at = instance.purchased_at + datetime.timedelta(days=30.44 * plan.duration_months)        
        instance.save()



@receiver(pre_save, sender=Vendor)
def generate_vendor_code(sender, instance, **kwargs):
    if not instance.vendor_code:
        timestamp = str(int(time.time()))
        random_chars = ''.join(random.choices(
            string.ascii_uppercase + string.ascii_lowercase, k=6))
        instance.vendor_code = timestamp + random_chars
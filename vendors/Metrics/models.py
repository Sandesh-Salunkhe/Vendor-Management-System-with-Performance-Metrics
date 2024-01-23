from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
import random
import string
import time
import uuid
# Create your models here.

# PLAN = (
#     ("BASIC,", "Basic"),
#     ("PRO,", "Pro"),
#     ("ENTERPRISE", "Enterprise")
# )


class SubscriptionPlan(models.Model):
    # name = models.CharField(max_length=50, default=PLAN[0][1], choices=PLAN)
    name = models.CharField(max_length=50)
    duration_months = models.IntegerField()
    price = models.IntegerField()
    



class CustomUser(AbstractUser):
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(max_length=100)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)
    purchased_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(auto_now_add=True)
    payment = models.BooleanField(default=False)
    def __str__(self):
        return self.username

    # def __str__(self):
    #     return f"{self.name} - {self.duration_months} months"

    def save(self, *args, **kwargs):
        # Set the expired_at field based on the current time and duration
        if not self.expired_at:
            self.expired_at = timezone.now() + datetime.timedelta(
                days=30.44 * self.duration_months
            )
        super().save(*args, **kwargs)

class Vendor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=None, null=True)
    quality_rating_avg = models.FloatField(default=None, null=True)
    average_response_time = models.FloatField(default=None, null=True)
    fulfillment_rate = models.FloatField(default=None, null=True)

    def __str__(self):
        return self.user




STATUS = (
    ("PENDING,", "pending"),
    ("COMPLETED,", "completed"),
    ("CANCELED", "canceled")
)


def generate_purchaser_code():
    code = uuid.uuid1().hex[0:]
    if PurchaseOrder.objects.filter(po_number=code).exists():
        return generate_purchaser_code
    return code


class PurchaseOrder(models.Model):
    po_number = models.CharField(
        max_length=50, unique=True, default=generate_purchaser_code)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=50, default=STATUS[0][1], choices=STATUS)
    quality_rating = models.FloatField(default=None, null=True)
    issue_date = models.DateTimeField(default=None, null=True)
    acknowledgment_date = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}"


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=None, null=True)
    quality_rating_avg = models.FloatField(default=None, null=True)
    average_response_time = models.FloatField(default=None, null=True)
    fulfillment_rate = models.FloatField(default=None, null=True)

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"

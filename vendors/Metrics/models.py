from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string
import time
import uuid
# Create your models here.


class VendorUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username


def generate_vendor_code():
    timestamp = str(int(time.time()))
    random_chars = ''.join(random.choices(
        string.ascii_uppercase+string.ascii_lowercase, k=6))
    if Vendor.objects.filter(vendor_code=timestamp+random_chars).exists():
        return generate_vendor_code
    return timestamp+random_chars


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(
        max_length=50, unique=True, default=generate_vendor_code)
    on_time_delivery_rate = models.FloatField(default=None, null=True)
    quality_rating_avg = models.FloatField(default=None, null=True)
    average_response_time = models.FloatField(default=None, null=True)
    fulfillment_rate = models.FloatField(default=None, null=True)

    def __str__(self):
        return self.name


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

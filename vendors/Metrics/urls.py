from django.urls import path
from .views import *
urlpatterns = [
    path('vendors/', VendorList.as_view(), name='vendor-list'),
    path('vendors/<int:vendor_id>/', VendorDetail.as_view(), name='vendor-detail'),
]

from django.urls import path
from .views import *
urlpatterns = [
    path('api/vendors/', VendorList.as_view(), name='vendor-list'),
    path('api/vendors/<int:vendor_id>/', VendorDetail.as_view(), name='vendor-detail'),
]

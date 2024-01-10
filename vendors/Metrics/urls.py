from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    
    path('faqs/', faqs_view, name='faqs'),
    path('about/', about_view, name='about'),
    path('login/', TokenObtainPairView, name='login'),
    path('sign_up/', signup_view, name='signup'),


    #  Vendor Profile Management:
    path('vendors/', VendorList.as_view(), name='vendor-list'),
    path('vendors/<int:vendor_id>/', VendorDetail.as_view(), name='vendor-detail'),

    # Purchase Order Tracking:
    path('purchase_orders/', PurchaseOrderList.as_view(), name='order-list'),
    path('purchase_orders/<int:po_id>/', PurchaseOrderDetail.as_view(), name='order-detail'),
]

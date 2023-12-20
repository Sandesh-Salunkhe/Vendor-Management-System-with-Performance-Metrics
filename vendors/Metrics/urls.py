from django.urls import path
from .views import *
urlpatterns = [
    #  Vendor Profile Management:
    path('vendors/', VendorList.as_view(), name='vendor-list'),
    path('vendors/<int:vendor_id>/', VendorDetail.as_view(), name='vendor-detail'),

    # Purchase Order Tracking:
    path('purchase_orders/', PurchaseOrderList.as_view(), name='order-list'),
    path('purchase_orders/<int:po_id>/', PurchaseOrderDetail.as_view(), name='order-detail'),
]

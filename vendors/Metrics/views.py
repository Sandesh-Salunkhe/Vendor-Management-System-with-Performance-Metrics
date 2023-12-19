from django.http import JsonResponse, response
from rest_framework.views import APIView
from .serializers import VendorSerializer, PurchaseOrderSerializer
from .models import Vendor, PurchaseOrder
from django.db import connection 
from django.shortcuts import get_object_or_404

class VendorList(APIView):
    serializer_class = VendorSerializer
    
    def get(self, request):
        all_vendors = Vendor.objects.all()
        vendors_data = VendorSerializer(all_vendors, many=True)
        return JsonResponse({'Success': True, 'data': vendors_data.data})

    def post(self, request):
        vendor_name = request.data.get('vendor_name')
        contact_details = request.data.get('contact_details')
        address = request.data.get('address')
        
        vendor_creation = Vendor.objects.create(name=vendor_name, contact_details=contact_details, address=address)
        
        return JsonResponse({'Success': True, 'Message': 'Vendor Profile Created Successfully.'})

class VendorDetail(APIView):
    serializer_class = VendorSerializer

    def get_vendor(self, vendor_id):
        vendor = get_object_or_404(Vendor, id=vendor_id)
        return vendor
    
    def get(self, request, vendor_id:int):
        vendor = self.get_vendor(vendor_id)
        serializer = VendorSerializer(vendor)
        return JsonResponse({'Success': True, 'data': serializer.data})

    def put(self, request, vendor_id:int):
        vendor = self.get_vendor(vendor_id)

        name = request.data.get('vendor_name', vendor.name)
        contact_details = request.data.get('contact_details', vendor.contact_details)
        address = request.data.get('address', vendor.address)

        vendor.name = name
        vendor.contact_details = contact_details
        vendor.address = address
        vendor.save()

        return JsonResponse({'Success': True, 'Message': 'Vendor Profile Updated Successfully.'})
    
    def delete(self, request, vendor_id:int):
        remove_vendor = self.get_vendor(vendor_id)
        remove_vendor.delete()
        return JsonResponse({'Success': True, 'Message': 'Vendor Profile Deleted Successfully.'})


class PurchaseOrderList(APIView):

    serializer_class = PurchaseOrderSerializer
    
    def get(self, request):
        po_data = PurchaseOrder.objects.all()
        seralizer = PurchaseOrderSerializer(po_data, many=True)
        return JsonResponse({'Success': True, 'data':seralizer.data, 'Message': 'Purchase Orders List.'})
    

#     def post(self, request):
#         # Your implementation for creating a new vendor

class PurchaseOrderDetail(APIView):
    serializer_class = PurchaseOrderSerializer
    
#     def get(self, request, vendor_id):
#         # Your implementation for retrieving a specific vendor

#     def put(self, request, vendor_id):
#         # Your implementation for updating a specific vendor

#     def delete(self, request, vendor_id):
#         # Your implementation for deleting a specific vendor


from django.http import JsonResponse, Response
from rest_framework.views import APIView
from .serializers import VendorSerializer
from .models import Vendor
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
    
    def get(self, request, vendor_id:int):
        vendor = get_object_or_404(Vendor, id=vendor_id)
        serializer = VendorSerializer(vendor)
        return JsonResponse({'Success': True, 'data': serializer.data})

    def put(self, request, vendor_id:int):
        vendor = get_object_or_404(Vendor, id=vendor_id)

        name = request.data.get('name', vendor.name)
        contact_details = request.data.get('contact_details', vendor.contact_details)
        address = request.data.get('address', vendor.address)

        vendor.name = name
        vendor.contact_details = contact_details
        vendor.address = address
        vendor.save()

        return JsonResponse({'Success': True, 'Message': 'Vendor Profile Updated Successfully.'})
    
    def delete(self, request, vendor_id:int):
        remove_vendor = get_object_or_404(Vendor, id=vendor_id)
        remove_vendor.delete()
        return JsonResponse({'Success': True, 'Message': 'Vendor Profile Deleted Successfully.'})


class PurchaseOrder(APIView):

    def get(self, request):

        return Response({"Success": True, 'Message': "Purchase Order"})


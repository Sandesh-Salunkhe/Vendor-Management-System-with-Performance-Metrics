from django.http import JsonResponse, response
from rest_framework.views import APIView
from .serializers import VendorSerializer, PurchaseOrderSerializer
from .models import Vendor, PurchaseOrder
from django.db import connection 
from django.shortcuts import get_object_or_404

class VendorList(APIView):
    serializer_class = VendorSerializer
    
    def get(self, request):
        try:
            all_vendors = Vendor.objects.all()
            vendors_data = VendorSerializer(all_vendors, many=True)
            return JsonResponse({'Success': True, 'data': vendors_data.data})
        except :
            return JsonResponse({'Success': False, 'data': 'Vendors Not Found.'})

    def post(self, request):
        vendor_name = request.data.get('vendor_name')
        contact_details = request.data.get('contact_details')
        address = request.data.get('address')
        
        try:
            vendor, created = Vendor.objects.get_or_create(
                name=vendor_name,
                contact_details=contact_details,
                address=address
            )

            if created:
                return JsonResponse({'Success': True, 'Message': 'Vendor Profile Created Successfully.'})
            else:
                return JsonResponse({'Success': False, 'Message': 'Vendor Profile Already Exists.'})

        except Exception as e:
            return JsonResponse({'Success': False, 'Message': f'Error: {str(e)}'})
        
class VendorDetail(APIView):
    serializer_class = VendorSerializer

    def get_vendor(self, vendor_id):
        return get_object_or_404(Vendor, id=vendor_id)
    
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

        if remove_vendor:
            remove_vendor.delete()
            return JsonResponse({'Success': True, 'Message': 'Vendor Profile Deleted Successfully.'})
        else:
            return JsonResponse({'Success': False, 'Message': 'Vendor Profile Not Found.'}, status=404)


class PurchaseOrderList(APIView):
    serializer_class = PurchaseOrderSerializer

    def get_vendor(self, vendor_id):
        return get_object_or_404(Vendor, id=vendor_id)
    
    def get(self, request):
        po_data = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(po_data, many=True)
        return JsonResponse({'Success': True, 'data': serializer.data, 'Message': 'Purchase Orders List.'})
    
    def post(self, request):
        vendor_id = request.data.get('vendor_id')
        items = request.data.get('items')
        quantity = request.data.get('quantity')
        order_date = request.data.get('order_date')
        issue_date = request.data.get('issue_date')
        acknowledgment_date = request.data.get('acknowledgment_date')
        delivery_date = request.data.get('delivery_date')

        vendor = self.get_vendor(vendor_id)

        if vendor:
            po_data = PurchaseOrder(
                vendor=vendor,
                order_date=order_date,
                delivery_date=delivery_date,
                acknowledgment_date=acknowledgment_date,
                issue_date=issue_date,
                items=items,
                quantity=quantity,
                status='pending'
            )
            po_data.save()

            return JsonResponse({'Success': True, 'Message': 'Purchase Order Data Created Successfully'})
        else:
            return JsonResponse({'Success': False, 'Message': 'Vendor not found.'}, status=404)

class PurchaseOrderDetail(APIView):
    serializer_class = PurchaseOrderSerializer
    
#     def get(self, request, vendor_id):
#         # Your implementation for retrieving a specific vendor

#     def put(self, request, vendor_id):
#         # Your implementation for updating a specific vendor

#     def delete(self, request, vendor_id):
#         # Your implementation for deleting a specific vendor


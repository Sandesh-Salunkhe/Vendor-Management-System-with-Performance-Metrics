from django.http import JsonResponse
from rest_framework.response import Response
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
        except:
            return Response({'Success': False, 'data': 'Vendors Not Found.'})

    def post(self, request):

        vendor = self.serializer_class(data=request.data)
        if vendor.is_valid():
            vendor.save()
            return JsonResponse({'Success': True, 'Message': 'Vendor Profile Created Successfully.'})
        return JsonResponse({'Success': False, 'Message': vendor.errors})
           

class VendorDetail(APIView):
    serializer_class = VendorSerializer

    def get_vendor(self, vendor_id):
        return get_object_or_404(Vendor, id=vendor_id)

    def get(self, request, vendor_id: int):
        vendor = self.get_vendor(vendor_id)
        serializer = VendorSerializer(vendor)
        return JsonResponse({'Success': True, 'data': serializer.data})

    def put(self, request, vendor_id: int):
        vendor = self.get_object(vendor_id)
        serializer = self.serializer_class(vendor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'Success': True, 'Message': 'Vendor Profile Updated Successfully.'})
        return JsonResponse({'Success': False, 'Message': serializer.errors})

    def delete(self, request, vendor_id: int):
        remove_vendor = self.get_vendor(vendor_id)

        if remove_vendor:
            remove_vendor.delete()
            return JsonResponse({'Success': True, 'Message': 'Vendor Profile Deleted Successfully.'})
        else:
            return Response({'Success': False, 'Message': 'Vendor Profile Not Found.'}, status=404)


class PurchaseOrderList(APIView):
    serializer_class = PurchaseOrderSerializer

    def get_vendor(self, vendor_id):
        return get_object_or_404(Vendor, id=vendor_id)

    def get(self, request):
        po_data = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(po_data, many=True)
        return JsonResponse({'Success': True, 'data': serializer.data, 'Message': 'Purchase Orders List.'})

    def post(self, request):

        serialiser = self.serializer_class(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'Success': True, 'Message': 'Purchase Order Data Created Successfully'})
        return Response({'Success': False, 'Message': serialiser.errors}, status=404)


class PurchaseOrderDetail(APIView):
    serializer_class = PurchaseOrderSerializer

#     def get(self, request, vendor_id):
#         # Your implementation for retrieving a specific vendor

#     def put(self, request, vendor_id):
#         # Your implementation for updating a specific vendor

#     def delete(self, request, vendor_id):
#         # Your implementation for deleting a specific vendor

from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response, JsonResponse
from rest_framework.views import APIView
 
# Create your views here.

class Vendor(APIView):
    serializer_class = VendorSerializer
    
    def get_vendor(self, vendor_id):
        vendor_details = Vendor.objects.filter(id=vendor_id).first()
        return vendor_details
    
    def get(self, request, vendor_id:int = None):
        if vendor_id != None:
           if self.get_object(vendor_code):
              vendor = self.get_vendor(vendor_id)
              serializer = VendorSerializer(vendor)
              return JsonResponse({'Success': True, 'data': serializer.data})
            return JsonResponse({'Success': False, 'data': serializer.data})

        all_vendors = Vendor.objects.all()
        vendors_data = VendorSerializer(all_vendors,many=True)
        return JsonResponse({'Success': True, 'data': vendors_data.data})
    
    def post(self, request):
        
        vendor_name = request.POST.get('vendor_name')
        contact_details = request.POST.get('contact_details')
        address = request.POST.get('address')
        
        vendor_creation = Vendor.objeect.create(name = vendor_name, contact_details = contact_details, address = address)
        
        
        return JsonResponse({'Success': True, 'Message':'Vendor Profile Created Successfully.'})
    
    def put(self,request,vendor_id:int):
        
        name = request.POST.get('name')
        contact_details = request.POST.get('contact_details')
        address = request.POST.get('address')

        Vendor.objects.get(id = vendor_id).update(
            name = name,
            contact_details = contact_details,
            address = address
        )
     
        return JsonResponse({'Success': True, 'Message':'Vendor Profile Created Successfully.'})
    
    def delete(self,vendor_id:int):
        remove_vendor = Vendor.objects.get(id= vendor_id)
        if remove_vendor:
           remove_vendor.delete()
           return JsonResponse({'Success': True, 'Message':'Vendor Profile Deleted Successfully.'})
        return JsonResponse({'Success': False, 'Message':'Vendor Profile Not Found.'})

       

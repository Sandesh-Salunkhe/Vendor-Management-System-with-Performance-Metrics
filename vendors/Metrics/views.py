from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response, JsonResponse
from rest_framework.views import APIView
 
# Create your views here.

class Vendor(APIView):
    serializer_class = VendorSerializer
    
    def get_vendor(self, vendor_id):
        vendor_details = VendorSerializer(vendor_id)
        return vendor_details
    
    def get(self, request, vendor_id):
        vendor = self.get_vendor(vendor_id)
        serializer = VendorSerializer(vendor)
        
        return JsonResponse({'Success': True, 'data': serializer.data})
    
    def get(self, request):
        
        all_vendor = VendorSerializer(many=True)
        
        return JsonResponse({'Success': True, 'data': all_vendor})
    
    def post(self, request):
        
        vendor_name = request.POST.get('vendor_name')
        contact_details = request.POST.get('contact_details')
        address = request.POST.get('address')
        
        vendor_creation = Vendor.objeect.create(name = vendor_name, contact_details = contact_details, address = address)
        
        
        return JsonResponse({'Success': True, 'Message':'Vendor Profile Created Successfully.'})
    
    def put(self, request):
        
        vendor_name = request.POST.get('vendor_name')
        contact_details = request.POST.get('contact_details')
        address = request.POST.get('address')
        
        vendor_creation = Vendor.objeect.create(name = vendor_name, contact_details = contact_details, address = address)
        
        
        return JsonResponse({'Success': True, 'Message':'Vendor Profile Created Successfully.'})
    
    def delete(self, request, vendor_id):
         
        vendor_creation = Vendor.objeect.create(id = vendor_id)
        
        
        return JsonResponse({'Success': True, 'Message':'Vendor Profile Created Successfully.'})
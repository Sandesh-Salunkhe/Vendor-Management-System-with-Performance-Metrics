from rest_framework import serializers
from .models import *




class VendorSerializer(serializers.ModelSerializer):

    class Meta:
       model = Vendor
       fields = ('name','contact_details','address',)
       
    def to_representation(self, obj):
        data = super(VendorSerializer, self).to_representation(obj)
        data['vendor_code'] = obj.vendor_code
        data['on_time_delivery_rate'] = obj.on_time_delivery_rate
        return data

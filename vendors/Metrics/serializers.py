from rest_framework import serializers
from .models import *


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'contact_details', 'address',)

    def to_representation(self, obj):
        data = super(VendorSerializer, self).to_representation(obj)
        data['vendor_code'] = obj.vendor_code
        data['on_time_delivery_rate'] = obj.on_time_delivery_rate
        return data


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        

class HistoricalSerializer(serializers.ModelSerializer):
    class Meta:
        models = HistoricalPerformance
        fields = ('id','vendor','date','on_time_delivery_rate', 'quality_rating_avg' )
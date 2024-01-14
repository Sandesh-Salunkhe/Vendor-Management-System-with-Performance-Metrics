from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        
    # The create method is overridden to handle the password hashing and user creation.
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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
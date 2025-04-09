from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(allow_blank = True)

    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_name(self, value):
        if not value.strip() or value is None:
            raise serializers.ValidationError('Name is required')
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return value
    
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Quantity must be greater than 0')
        return value
from rest_framework import serializers
from .import models

class Product_Serializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='stock_quantity')
    class Meta:
        model = models.Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Product name field cannot be empty.")
        return value
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value
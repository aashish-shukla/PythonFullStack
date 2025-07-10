from rest_framework import serializers
from .models import Product, Category, ProductCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'created_at', 'updated_at']

class ProductCategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = ProductCategory
        fields = ['id', 'product', 'category']

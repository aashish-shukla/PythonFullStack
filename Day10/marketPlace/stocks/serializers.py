from rest_framework import serializers
from .models import Stock, Portfolio

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'symbol', 'name', 'current_price', 'market_cap', 'created_at', 'updated_at']

class PortfolioSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    
    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'stock', 'shares', 'purchase_price', 'purchase_date']
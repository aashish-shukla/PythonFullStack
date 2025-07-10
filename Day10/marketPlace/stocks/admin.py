from django.contrib import admin
from .models import Stock, Portfolio

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'name', 'current_price', 'market_cap', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['symbol', 'name']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['user', 'stock', 'shares', 'purchase_price', 'purchase_date']
    list_filter = ['purchase_date', 'stock']
    search_fields = ['user__username', 'stock__symbol']

from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.stock_list, name='stock_list'),
    path('stocks/create/', views.stock_create, name='stock_create'),
    path('stocks/<int:pk>/edit/', views.stock_update, name='stock_update'),
    path('stocks/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('stocks/search/', views.stock_search, name='stock_search'),
    path('stocks/<str:ticker>/buy/', views.buy_stock, name='buy_stock'),
    path('stocks/<str:ticker>/watch/', views.watch_stock, name='watch_stock'),
]
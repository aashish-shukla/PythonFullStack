from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Product, Category, ProductCategory
from .serializers import ProductSerializer, CategorySerializer, ProductCategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
            
        return queryset
    
    @action(detail=True, methods=['post'])
    def add_to_category(self, request, pk=None):
        product = self.get_object()
        category_id = request.data.get('category_id')
        
        try:
            category = Category.objects.get(id=category_id)
            product_category, created = ProductCategory.objects.get_or_create(
                product=product, 
                category=category
            )
            
            if created:
                return Response({'message': 'Product added to category successfully'})
            else:
                return Response({'message': 'Product already in this category'}, 
                              status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, 
                          status=status.HTTP_404_NOT_FOUND)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(productcategory__category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
from django.shortcuts import get_object_or_404
from products.models import User
from products.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
from constance import config
from constance.signals import config_updated
from django.dispatch import receiver

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # GET /api/products
        queryset = list(Product.objects.all().values())

        # Check if request contains any query parameters
        if request.query_params:
            # Get the value of the query parameter
            search = request.query_params.get('search', None)
            if search is not None:  
                # Search on the fields title, price, store
                queryset = list(Product.objects.filter(title__icontains=search).values())
                queryset += list(Product.objects.filter(price__icontains=search).values())
                queryset += list(Product.objects.filter(store__icontains=search).values())
                # Remove duplicates
                queryset = list({v['id']:v for v in queryset}.values())
        serializer = ProductSerializer(queryset, many=True)
        
        return JsonResponse(queryset, safe=False, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None): # GET /api/products/:id
        queryset = Product.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Create a product", responses={404: 'slug not found'})
    def create(self, request): # POST /api/products
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None): # PUT /api/products/:id
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None): # DELETE /api/products/:id
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
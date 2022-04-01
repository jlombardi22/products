from rest_framework.decorators import api_view
from rest_framework.response import Response
from products import serializers
from .serializers import ProductSerializer
from models import Product
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


from products.models import Product


@api_view(['GET'])
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

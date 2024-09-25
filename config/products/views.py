from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer  # Убедитесь, что имя сериализатора правильное
from django.shortcuts import get_object_or_404


class ProductListCreateApiView(APIView):
    def get(self, request):
        products = Product.objects.all()  # Используйте множественное число для переменной
        serializers = ProductSerializer(products, many=True)  # Правильное имя сериализатора
        return Response(serializers.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)  # Получаем данные из тела запроса
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Используйте константу для статуса
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)  # Получаем продукт
        serializer = ProductSerializer(product)  # Создаем сериализатор с продуктом
        return Response(serializer.data)  # Возвращаем данные

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # Используйте константу для статуса

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialiizers
#     serializer_class = ProductSerialiizers


# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialiizers

# class ProductRetrieveView(generics.RetrieveAPIView):
#     queryset= Product.objects.all()
#     serializer_class = ProductSerialiizers

# class ProductCreateView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialiizers

# class ProductDeleteView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialiizers

# class ProductUpdateView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialiizers
from django.contrib import admin
from .models import ProductImage, Product

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
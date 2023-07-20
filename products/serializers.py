from rest_framework import serializers

from products.models import Product, ExtraImage

from admin_settings.serializers import Category_Serializer, SubCategory_Serializer

class Product_Extra_images(serializers.ModelSerializer):
    model = ExtraImage
    fields = ['pk', 'image']

class Product_Serializer(serializers.ModelSerializer):
    model = Product
    fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data ['category'] = Category_Serializer(instance.category).data if instance.category else '-'
        data ['subcategory'] = SubCategory_Serializer(instance.subcategory).data if instance.subcategory else '-'
        data ['extra_images'] = Product_Extra_images(instance.extra_images.all(), many=True).data
        return data
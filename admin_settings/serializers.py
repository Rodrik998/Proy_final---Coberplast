from rest_framework import serializers

from admin_settings.models import Category, SubCategory


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        category = Category.objects.get(id = data['category'])
        data['category'] = Category_Serializer(category).data
        return data
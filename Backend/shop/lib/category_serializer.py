from ..models import CategoryTable, SubCategoryTable
from rest_framework import serializers


class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTable
        fields = '__all__'


class CategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTable
        fields = ('shop_id', 'category', 'category_id')
        extra_kwargs = {
            'shop_id': {'required': True},
            'category': {'required': True}
        }


class CategoryPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTable
        fields = ('shop_id', 'category_id', 'category', 'is_active')

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


class SubCategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryTable
        fields = ('category_id', 'sub_category', 'sub_category_id')
        extra_kwargs = {
            'category_id': {'required': True},
            'sub_category': {'required': True}
        }


class SubCategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryTable
        fields = '__all__'


class SubCategoryPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryTable
        fields = ('category_id', 'sub_category_id', 'sub_category', 'is_active')

    def update(self, instance, validated_data):
        instance.sub_category = validated_data.get('sub_category', instance.sub_category)
        instance.save()
        return instance

from ..models import ItemTypes, ItemInfo
from rest_framework import serializers


class ItemTypeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTypes
        fields = '__all__'


class ItemTypePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTypes
        fields = '__all__'
        extra_kwargs = {
            'sub_category_id': {'required': True},
            'item_types': {'required': True}
        }


class ItemTypePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTypes
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.item_types = validated_data.get('item_types', instance.item_types)
        instance.save()
        return instance


class ItemInfoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInfo
        fields = '__all__'


class ItemInfoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInfo
        fields = '__all__'
        extra_kwargs = {
            'item_types_id': {'required': True},
            'item_name': {'required': True},
            'item_unit_price': {'required': True},
            'item_image': {'required': True},
            'item_unit': {'required': True},
            'item_minimum_qty': {'required': True}
        }


class ItemInfoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInfo
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.item_types_id = validated_data.get('item_types_id', instance.item_types_id)
        instance.item_name = validated_data.get('item_name', instance.item_name)
        instance.item_unit_price = validated_data.get('item_unit_price', instance.item_unit_price)
        instance.item_image = validated_data.get('item_image', instance.item_image)
        instance.item_unit = validated_data.get('item_unit', instance.item_unit)
        instance.item_minimum_qty = validated_data.get('item_minimum_qty', instance.item_minimum_qty)
        instance.save()
        return instance

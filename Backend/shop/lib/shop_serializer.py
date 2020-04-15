from ..models import ShopInfo
from rest_framework import serializers


class ShopRegisterSerializer(serializers.ModelSerializer):

    def validate_shop_email(self, value):
        if ShopInfo.objects.filter(shop_email=value).exists():
            raise serializers.ValidationError('already exists')
        return value

    class Meta:
        model = ShopInfo
        fields = ('shop_desc', 'shop_address', 'shop_email', 'shop_phone_1', 'shop_phone_2',
                  'shop_token', 'shop_id', 'shop_password')
        extra_kwargs = {
            'shop_desc': {'required': True},
            'shop_address': {'required': True},
            'shop_email': {'required': True},
            'shop_phone_1': {'required': True},
            'shop_phone_2': {'required': True},
            'shop_password': {'required': True},
        }


class ShopLoginSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        if ShopInfo.objects.filter(shop_email=value).exists():
            pass
        else:
            raise serializers.ValidationError('Email id doesnot exist')
        return value

    def validate_password(self, value):
        data = self.get_initial()
        shop_email = data.get('shop_email')
        if ShopInfo.objects.filter(shop_email=shop_email, shop_password=value).exists():
            pass
        else:
            raise serializers.ValidationError('password doesnot match')
        return value

    def validate(self, data):
        shop_credo = ShopInfo.objects.filter(shop_password=data.get('shop_password'),
                                             shop_email=data.get('shop_email')).get()
        data['shop_token'] = shop_credo.shop_token
        return shop_credo

    class Meta:
        model = ShopInfo
        fields = ('shop_email', 'shop_password', 'shop_token', 'shop_id')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopInfo
        fields = ('shop_desc', 'shop_address', 'shop_email', 'shop_phone_1', 'shop_phone_2', 'shop_id')


class ShopPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopInfo
        fields = ('shop_desc', 'shop_address', 'shop_email', 'shop_phone_1', 'shop_phone_2', 'shop_id')

    def update(self, instance, validated_data):
        instance.shop_desc = validated_data.get('shop_desc', instance.shop_desc)
        instance.shop_address = validated_data.get('shop_address', instance.shop_address)
        instance.shop_phone_1 = validated_data.get('shop_phone_1', instance.shop_phone_1)
        instance.shop_phone_2 = validated_data.get('shop_phone_2', instance.shop_phone_2)
        instance.save()
        return instance


def shop_get_serializer():
    info = []
    for shop in ShopInfo.objects.filter(is_active=1):
        shop_info = {
            'shop_desc': shop.shop_desc,
            'shop_address': shop.shop_address,
            'shop_email': shop.shop_email,
            'shop_phone_1': shop.shop_phone_1,
            'shop_phone_2': shop.shop_phone_2,
            'shop_id': shop.shop_id,
            'shop_token': shop.shop_token

        }
        info.append(shop_info)
    return {'data': info}

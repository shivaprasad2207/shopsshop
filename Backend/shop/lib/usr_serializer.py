from ..models import UsrInfo
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):

    def validate_usr_email(self, value):
        if UsrInfo.objects.filter(usr_email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value

    class Meta:
        model = UsrInfo
        fields = ('usr_email', 'usr_f_name', 'usr_l_name', 'usr_phone', 'usr_address',
                  'usr_password', 'shop_id', 'usr_token')
        extra_kwargs = {
            'usr_email': {'required': True},
            'usr_f_name': {'required': True},
            'usr_l_name': {'required': True},
            'usr_phone': {'required': True},
            'usr_address': {'required': True},
            'usr_password': {'required': True},
            'shop_id': {'required': True},
            'usr_token': {'required': True},
        }


class UsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsrInfo
        fields = ('usr_email', 'usr_f_name', 'usr_l_name', 'usr_phone', 'usr_address', 'usr_id')


class UsrPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsrInfo
        fields = ('usr_f_name', 'usr_l_name', 'usr_phone', 'usr_address', 'usr_id')

    def update(self, instance, validated_data):
        instance.usr_f_name = validated_data.get('usr_f_name', instance.usr_f_name)
        instance.usr_l_name = validated_data.get('usr_l_name', instance.usr_l_name)
        instance.usr_phone = validated_data.get('usr_phone', instance.usr_phone)
        instance.usr_address = validated_data.get('usr_address', instance.usr_address)
        instance.save()
        return instance

from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from ..models import ShopInfo, UsrInfo
from .usr_serializer import UserRegisterSerializer, UsrSerializer, UsrPutSerializer
import hashlib


class Utilities():
    @classmethod
    def to_normal_dict1(cls, my_dict):
        my_ret_dict = {}
        for k, v in dict(my_dict).items():
            if v:
                my_ret_dict[k] = v
        return my_ret_dict

    @classmethod
    def to_normal_dict(cls, my_dict):
        my_ret_dict = {}
        for k, v in dict(my_dict).items():
            if v:
                my_ret_dict[k] = v[0]
        return my_ret_dict


class UsrAuth(APIView):
    """
    Register a new user.
    """

    def get(self, request, format=None):
        data = request.data
        shop = ShopInfo.objects.get(shop_token=request.GET['shop_token'], is_active=1)
        data['shop_id'] = shop.shop_id
        data['usr_email'] = request.GET['usr_email']
        data['usr_password'] = hashlib.md5(request.GET['usr_password'].encode('utf-8')).hexdigest()
        serializer = UsrSerializer(data=data)
        if serializer.is_valid():
            serializer.validate(data)
            data = serializer.data
            data.pop('usr_email')
            data['shop_token'] = request.GET['shop_token']
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsrRegister(APIView):
    """
    Register a new User.
    """

    def post(self, request, format=None):
        data = request.data
        shop_token = data['shop_token']
        passwd = hashlib.md5(data['usr_password'].encode('utf-8')).hexdigest()
        data = Utilities.to_normal_dict(request.data)
        data['usr_token'] = self.getOrCreateToken()
        data['usr_password'] = passwd
        shop_info = ShopInfo.objects.filter(shop_token=shop_token).get()
        data['shop_id'] = shop_info.shop_id
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            [data.pop(k) for k in list(data.keys()) if k != 'usr_token']
            print(data)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def getOrCreateToken(self):
        return get_random_string(length=6).upper()


class Usr(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return UsrInfo.objects.get(usr_id=pk, is_active=1)
        except UsrInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UsrSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        data = request.data
        serializer = UsrPutSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk, request)
        user.is_active = 0
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

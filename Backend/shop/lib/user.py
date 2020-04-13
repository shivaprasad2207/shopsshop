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


class UsrRegister(APIView):
    """
    Register a new User.
    """

    def post(self, request, format=None):
        data = request.data
        data['usr_token'] = self.getOrCreateToken()
        data['usr_password'] = hashlib.md5(data['usr_password'].encode('utf-8')).hexdigest()
        shop_info = ShopInfo.objects.filter(shop_token=data['shop_token']).get()
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



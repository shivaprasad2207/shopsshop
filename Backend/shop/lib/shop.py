from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from django.http.response import HttpResponse
from ..models import ShopInfo, CategoryTable, SubCategoryTable
from .shop_serializer import ShopRegisterSerializer, ShopLoginSerializer, ShopSerializer, ShopPutSerializer, \
    shop_get_serializer
import hashlib

class Utilities():
    @classmethod
    def to_normal_dict1(cls,my_dict):
        my_ret_dict = {}
        for k , v in dict(my_dict).items():
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

class Menu(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return ShopInfo.objects.get(shop_id=pk, is_active=1)
        except ShopInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        info = []
        for category in CategoryTable.objects.filter(shop_id=pk, is_active=1):
            categoryDict = {
                'category': category.category,
                'link': '/shop/' + str(pk) + '/category/' + str(category.category_id) + '/',
                'subcategories': []
            }
            for subcategory in SubCategoryTable.objects.filter(category_id=category.category_id, is_active=1):
                categoryDict['subcategories'].append({
                    'sub_category_id' : subcategory.sub_category_id,
                    'sub_category': subcategory.sub_category,
                    'link': '/category/' + str(category.category_id) + '/subcategory/' + str(subcategory.sub_category_id) + '/',
                })

            info.append(categoryDict)
        return Response({'data': info})


class ShopRegister(APIView):
    """
    Register a new Shop.
    """

    def post(self, request, format=None):
        passwd = hashlib.md5(request.data['shop_password'].encode('utf-8')).hexdigest()
        data = Utilities.to_normal_dict(request.data)
        data['shop_token'] = self.getOrCreateToken()
        data['shop_password'] = passwd
        serializer = ShopRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            [data.pop(k) for k in list(data.keys()) if k != 'shop_token']
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def getOrCreateToken(self):
        return get_random_string(length=6).upper()

    def get(self, request, format=None):
        serializer = shop_get_serializer()
        return Response(serializer)


class ShopLogin(APIView):
    """
    Login to the Shop for Shop Admin.
    """

    def get(self, request, format=None):
        data = request.data
        data['shop_email'] = request.GET['shop_email']
        data['shop_password'] = hashlib.md5(request.GET['shop_password'].encode('utf-8')).hexdigest()
        serializer = ShopLoginSerializer(data=data)
        if serializer.is_valid():
            serializer.validate(data)
            data = serializer.data
            data.pop('shop_password')
            data.pop('shop_email')
            re = Response(data, status=status.HTTP_201_CREATED)
            re.set_cookie("__MY_SHOP__shop_id", data['shop_id'])
           # re.set_cookie("__MY_SHOP__shop_token", data['shop_token'])
            return re
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Shop(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return ShopInfo.objects.get(shop_id=pk, is_active=1)
        except ShopInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        shop = self.get_object(pk)
        shop = ShopSerializer(shop)
        return Response(shop.data)

    def put(self, request, pk, format=None):
        shop = self.get_object(pk)
        data = request.data
        serializer = ShopPutSerializer(shop, data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shop = self.get_object(pk, request)
        shop.is_active = 0
        shop.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShopMenu(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return ShopInfo.objects.get(shop_id=pk, is_active=1)
        except ShopInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        info = []
        for category in CategoryTable.objects.filter(shop_id=pk, is_active=1):
            categoryDict = {}
            print(category.category)
        return Response("AAAAA")

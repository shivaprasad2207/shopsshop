from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CategoryTable, SubCategoryTable
from .category_serializer import CategoryGetSerializer, CategoryPostSerializer, CategoryPutSerializer, \
    SubCategoryPostSerializer, SubCategoryGetSerializer, SubCategoryPutSerializer

class Utilities():
    @classmethod
    def to_normal_dict(cls,my_dict):
        my_ret_dict = {}
        for k , v in dict(my_dict).items():
            my_ret_dict[k] = v[0]
        return my_ret_dict

class Categories(APIView):
    """
    List all categories, or create a new category.
    """

    def get(self, request, shop_id, format=None):
        users = CategoryTable.objects.filter(is_active=1, shop_id=shop_id)
        serializer = CategoryGetSerializer(users, many=True)
        serializer_data = []
        for data in serializer.data:
            t_dict = dict(data)
            t_dict['link'] = '/shop/' + str(t_dict['shop_id']) + '/category/' + str(t_dict['category_id']) + '/'
            serializer_data.append(t_dict)
        return Response({'data':serializer_data})

    def post(self, request, shop_id, format=None):
        data = Utilities.to_normal_dict(request.data)
        data['shop_id'] = str(shop_id)
        serializer = CategoryPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Category(APIView):
    """
    Retrieve, update or delete a category instance.
    """

    def get_object(self, shop_id, category_id):
        try:
            return CategoryTable.objects.get(shop_id=shop_id, category_id=category_id, is_active=1)
        except CategoryTable.DoesNotExist:
            raise Http404

    def get(self, request, shop_id, category_id, format=None):
        category = self.get_object(shop_id, category_id)
        category = CategoryGetSerializer(category)
        t_dict = category.data
        t_dict['link'] = '/shop/' + str(t_dict['shop_id']) + '/category/' + str(t_dict['category_id']) + '/'
        return Response(t_dict)

    def put(self, request, shop_id, category_id, format=None):
        category = self.get_object(shop_id, category_id)
        data = request.data
        serializer = CategoryPutSerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, shop_id, category_id, format=None):
        category = self.get_object(shop_id, category_id)
        category.is_active = 0
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubCategories(APIView):
    """
    List all categories, or create a new category.
    """

    def get(self, request, category_id, format=None):
        sub_category = SubCategoryTable.objects.filter(is_active=1, category_id=category_id)
        serializer = SubCategoryGetSerializer(sub_category, many=True)
        serializer_data = []
        for data in serializer.data:
            t_dict = dict(data)
            t_dict['link'] = '/category/' + str(t_dict['category_id']) + '/subcategory/' + str(t_dict['sub_category_id']) + '/'
            serializer_data.append(t_dict)
        return Response({'data': serializer_data})

    def post(self, request, category_id, format=None):
        data = Utilities.to_normal_dict(request.data)
        data['category_id'] = str(category_id)
        serializer = SubCategoryPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubCategory(APIView):
    """
        Retrieve, update or delete a sub category instance.
    """

    def get_object(self, category_id, sub_category_id):
        try:
            return SubCategoryTable.objects.get(category_id=category_id, sub_category_id=sub_category_id, is_active=1)
        except CategoryTable.DoesNotExist:
            raise Http404

    def get(self, request, category_id, sub_category_id, format=None):
        sub_category = self.get_object(category_id, sub_category_id)
        sub_category = SubCategoryGetSerializer(sub_category)
        t_dict = sub_category.data
        t_dict['link'] = '/category/' + str(t_dict['category_id']) + '/subcategory/' + str(t_dict['sub_category_id'])\
                         + '/'
        return Response(t_dict)

    def put(self, request, category_id, sub_category_id, format=None):
        sub_category = self.get_object(category_id, sub_category_id)
        data = request.data
        data['category_id'] = category_id
        serializer = SubCategoryPutSerializer(sub_category, data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id, sub_category_id, format=None):
        sub_category = self.get_object(category_id, sub_category_id)
        sub_category.is_active = 0
        sub_category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
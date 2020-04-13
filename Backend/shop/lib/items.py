from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from rest_framework import status
from ..models import ItemTypes, ItemInfo
from .item_serializer import ItemTypeGetSerializer, ItemTypePutSerializer, ItemTypePostSerializer, \
    ItemInfoPostSerializer, ItemInfoGetSerializer, ItemInfoPutSerializer

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


class ItemTypeView(APIView):
    """
    List all categories, or create a new category.
    """

    def get(self, request, sub_category_id, format=None):
        itemtype = ItemTypes.objects.filter(is_active=1, sub_category_id=sub_category_id)
        serializer = ItemTypeGetSerializer(itemtype, many=True)
        serializer_data = []
        for data in serializer.data:
            t_dict = dict(data)
            t_dict['link'] = '/subcategory/' + str(t_dict['sub_category_id']) + '/itemtype/' + \
                             str(t_dict['item_types_id']) + '/'
            serializer_data.append(t_dict)
        return Response({'data': serializer_data})

    def post(self, request, sub_category_id, format=None):
        data = Utilities.to_normal_dict(request.data)
        data['sub_category_id'] = str(sub_category_id)
        serializer = ItemTypePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemTypeListView(APIView):
    """
            Retrieve, update or delete a sub category instance.
    """

    def get_object(self, sub_category_id, item_types_id):
        try:
            return ItemTypes.objects.get(sub_category_id=sub_category_id, item_types_id=item_types_id, is_active=1)
        except ItemTypes.DoesNotExist:
            raise Http404

    def get(self, request, sub_category_id, item_types_id, format=None):
        item_type = self.get_object(sub_category_id, item_types_id)
        item_type = ItemTypeGetSerializer(item_type)
        t_dict = item_type.data
        t_dict['link'] = '/subcategory/' + str(t_dict['sub_category_id']) + '/itemtype/' + str(t_dict['item_types_id'])\
                         + '/'
        return Response(t_dict)

    def put(self, request, sub_category_id, item_types_id, format=None):
        item_type = self.get_object(sub_category_id, item_types_id)
        data = request.data
        data['sub_category_id'] = sub_category_id
        serializer = ItemTypePutSerializer(item_type, data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, sub_category_id, item_types_id, format=None):
        item_type = self.get_object(sub_category_id, item_types_id)
        item_type.is_active = 0
        item_type.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemInfoView(APIView):
    """
    List all categories, or create a new category.
    """

    def get(self, request, item_types_id, format=None):
        iteminfo = ItemInfo.objects.filter(is_active=1, item_types_id=item_types_id)
        serializer = ItemInfoGetSerializer(iteminfo, many=True)
        serializer_data = []
        for data in serializer.data:
            t_dict = dict(data)
            t_dict['link'] = '/itemtype/' + str(t_dict['item_types_id']) + '/iteminfo/' + str(t_dict['item_types_id'])\
                             + '/'
            serializer_data.append(t_dict)
        return Response({'data':serializer_data})

    def post(self, request, item_types_id, format=None):
        data = Utilities.to_normal_dict(request.data)
        data['item_types_id'] = str(item_types_id)
        data['item_image'] = self._getOrCreateToken()
        serializer = ItemInfoPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _getOrCreateToken(self):
        return get_random_string(length=8).upper()


class ItemInfoListView(APIView):
    """
            Retrieve, update or delete a sub category instance.
    """

    def get_object(self, item_types_id, item_info_id):
        try:
            return ItemInfo.objects.get(item_types_id=item_types_id, item_info_id=item_info_id, is_active=1)
        except ItemTypes.DoesNotExist:
            raise Http404

    def get(self, request, item_types_id, item_info_id, format=None):
        item_type = self.get_object(item_types_id, item_info_id)
        item_type = ItemInfoGetSerializer(item_type)
        t_dict = item_type.data
        t_dict['link'] = '/itemtype/' + str(t_dict['item_types_id']) + '/iteminfo/' + str(t_dict['item_info_id'])\
                         + '/'
        return Response(t_dict)

    def put(self, request, item_types_id, item_info_id, format=None):
        item_type = self.get_object(item_types_id, item_info_id)
        data = Utilities.to_normal_dict1(request.data)
        data['item_types_id'] = str(item_types_id)
        serializer = ItemInfoPutSerializer(item_type, data=data)
        if serializer.is_valid():
            serializer.save()
            rep = serializer.data
            return Response(rep, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_types_id, item_info_id, format=None):
        item_type = self.get_object(item_types_id, item_info_id)
        item_type.is_active = 0
        item_type.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

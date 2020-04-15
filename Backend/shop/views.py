from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from .lib import user as Usr
from .lib import shop as Shop
from .lib import categories
from .lib import items


class ShopRegister(Shop.ShopRegister):
    pass


class ShopMenu(Shop.Menu):
    pass


class ShopLogin(Shop.ShopLogin):
    pass


class Shop(Shop.Shop):
    pass


class UsrAuth(Usr.UsrAuth):
    pass


class UsrRegister(Usr.UsrRegister):
    pass


class Usr(Usr.Usr):
    pass


class Categories(categories.Categories):
    pass


class Category(categories.Category):
    pass


class SubCategories(categories.SubCategories):
    pass


class SubCategory(categories.SubCategory):
    pass


class ItemType(items.ItemTypeView):
    pass


class ItemTypes(items.ItemTypeListView):
    pass


class ItemInfo(items.ItemInfoView):
    pass


class Item(items.ItemInfoListView):
    pass

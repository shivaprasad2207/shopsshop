"""shopsshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new-shop/', views.ShopRegister.as_view()),
    path('shops/', views.ShopRegister.as_view()),
    path('shop-login', views.ShopLogin.as_view()),
    path('shop/<int:pk>/', views.Shop.as_view()),
    path('shop-menu/<int:pk>/', views.ShopMenu.as_view()),
    path('usr-login/', views.UsrRegister.as_view()),
    path('usr-auth', views.UsrAuth.as_view()),
    path('usr/<int:pk>/', views.Usr.as_view()),
    path('shop/<int:shop_id>/category/', views.Categories.as_view()),
    path('shop/<int:shop_id>/category/<int:category_id>/', views.Category.as_view()),
    path('category/<int:category_id>/subcategory/', views.SubCategories.as_view()),
    path('category/<int:category_id>/subcategory/<int:sub_category_id>/', views.SubCategory.as_view()),
    path('subcategory/<int:sub_category_id>/itemtype/', views.ItemType.as_view()),
    path('subcategory/<int:sub_category_id>/itemtype/<int:item_types_id>/', views.ItemTypes.as_view()),
    path('itemtype/<int:item_types_id>/iteminfo/', views.ItemInfo.as_view()),
    path('itemtype/<int:item_types_id>/iteminfo/<int:item_info_id>/', views.Item.as_view()),
]

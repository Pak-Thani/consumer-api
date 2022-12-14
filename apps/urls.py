"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from custom_sections.views import ListCustomSectionView, DetailCustomSectionView
from product.views import ProductView, SearchProductView
from banner.views import BannerView, JsonView
from category.views import CategoryView, DetailCategoryView
from transaction.views import TransactionView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/custom-sections/<slug>', DetailCustomSectionView.as_view()),
    path('api/banner/<slug>', BannerView.as_view()),
    path('api/json', JsonView.as_view()),
    path('api/custom-sections/', ListCustomSectionView.as_view()),
    path('api/product/<slug>', ProductView.as_view()),
    path('api/search/<keyword>', SearchProductView.as_view()),
    path('api/category/', CategoryView.as_view()),
    path('api/category/<slug>', DetailCategoryView.as_view()),
    path('api/transaction/', TransactionView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
"""classic_green URL Configuration

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
from django.urls import path,include
from rest_framework import routers                    # add this
from services import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import include, url
#from django.urls import path

router = routers.DefaultRouter()                      # add this
router.register(r'items', views.item_view, 'items')
router.register(r'category', views.itemcat_view, 'category')
router.register(r'offers', views.OfferView, 'offers')
router.register(r'variant', views.variant_view, 'variant')
# router.register(r'query/(?P<queryName>.*)', views.QueryView, 'query')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    url(r'api/queryItem/(?P<queryName>.*)', views.ItemCatQueryView.as_view(),name= 'query'),
    url(r'api/queryVariant/(?P<queryName>.*)', views.variantQueryView.as_view(),name= 'query'),
    #url(r'^api/(plants|gifts|offers|variant|category)/media/(?P<path>.*)$', serve, 
    #{'document_root': settings.MEDIA_ROOT}),
    url(r'media/(?P<path>.*)$', serve, 
    {'document_root': settings.MEDIA_ROOT}),
    url(r'^home/(login)',serve, {'document_root': settings.MEDIA_ROOT})
    #path('',include('services.urls')
]

 
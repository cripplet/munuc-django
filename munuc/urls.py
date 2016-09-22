"""munuc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include

from rest_framework import routers
from munuc_api.public import views

from django.contrib import admin


api_public_router = routers.DefaultRouter()
api_public_router.register(r'committees', views.CommitteeViewSet)
api_public_router.register(r'countries', views.CountryViewSet)
api_public_router.register(r'usg_groups', views.USGGroupViewSet)

urlpatterns = [
    url(r'^api/public/', include(api_public_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

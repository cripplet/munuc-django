from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from rest_framework import viewsets
from munuc.munuc_api.serializers import UserSerializer
from munuc.munuc_api.serializers import GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

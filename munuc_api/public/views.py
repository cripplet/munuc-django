from django.shortcuts import render

from rest_framework import viewsets

from munuc_api.models import USGGroup
from munuc_api.models import Committee
from munuc_api.models import Country

from munuc_api.public.serializers import USGGroupSerializer
from munuc_api.public.serializers import CommitteeSerializer
from munuc_api.public.serializers import CountrySerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class USGGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = USGGroup.objects.all()
    serializer_class = USGGroupSerializer


class CommitteeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer

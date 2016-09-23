from django.shortcuts import render

from rest_framework import viewsets

from munuc_api.models import Committee
from munuc_api.models import CommitteeStaffer
from munuc_api.models import Delegation
from munuc_api.models import InternalUser
from munuc_api.models import USGGroup

from munuc_api.public.serializers import CommitteeSerializer
from munuc_api.public.serializers import CommitteeStafferSerializer
from munuc_api.public.serializers import DelegationSerializer
from munuc_api.public.serializers import InternalUserSerializer
from munuc_api.public.serializers import USGGroupSerializer


class CommitteeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer


class CommitteeStafferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CommitteeStaffer.objects.all()
    serializer_class = CommitteeStafferSerializer


class DelegationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Delegation.objects.all()
    serializer_class = DelegationSerializer


class InternalUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InternalUser.objects.all()
    serializer_class = InternalUserSerializer


class USGGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = USGGroup.objects.all()
    serializer_class = USGGroupSerializer

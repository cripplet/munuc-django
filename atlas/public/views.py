from django.shortcuts import render

from rest_framework import viewsets

from atlas.models import Committee
from atlas.models import CommitteeStaffer
from atlas.models import Delegation
from atlas.models import InternalUser
from atlas.models import USGGroup

from atlas.public.serializers import CommitteeSerializer
from atlas.public.serializers import CommitteeStafferSerializer
from atlas.public.serializers import DelegationSerializer
from atlas.public.serializers import InternalUserSerializer
from atlas.public.serializers import USGGroupSerializer


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

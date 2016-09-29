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


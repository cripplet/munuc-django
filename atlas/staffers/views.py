from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins

from atlas.models import Committee
from atlas.models import CommitteeStaffer
from atlas.models import Delegation
from atlas.models import InternalUser
from atlas.models import USGGroup

from atlas.staffers.serializers import CommitteeSerializer

from atlas.staffers.permissions import CommitteeStafferPermission


class EditModelViewSet(mixins.RetrieveModelMixin, 
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    pass

class CommitteeViewSet(EditModelViewSet):
    permission_classes = (CommitteeStafferPermission, )
    serializer_class = CommitteeSerializer

    def get_queryset(self):
      user = self.request.user
      committee_staffer = CommitteeStaffer.objects.get(user=user)
      return Committee.objects.filter(staffers=committee_staffer)

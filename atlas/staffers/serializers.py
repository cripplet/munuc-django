from rest_framework import serializers

from atlas.models import Committee
from atlas.models import CommitteeStaffer
from atlas.models import Delegation
from atlas.models import InternalUser
from atlas.models import BaseUser
from atlas.models import USGGroup


class InternalUserSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='staffers:internaluser-detail', read_only=True)
  first_name = serializers.CharField(source='user.first_name', read_only=True)
  last_name = serializers.CharField(source='user.last_name', read_only=True)
  usg_group = serializers.HyperlinkedRelatedField(view_name='staffers:usggroup-detail', read_only=True)

  class Meta:
    model = InternalUser
    read_only = True
    exclude = ('user',)


class CommitteeStafferSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='staffers:committeestaffer-detail', read_only=True)
  first_name = serializers.CharField(source='user.first_name', read_only=True)
  last_name = serializers.CharField(source='user.last_name', read_only=True)
  committee = serializers.HyperlinkedRelatedField(view_name='staffers:committee-detail', read_only=True)

  class Meta:
    model = CommitteeStaffer
    read_only = True
    exclude = ('user', 'email',)


class DelegationSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='staffers:delegation-detail', read_only=True)
  committees = serializers.HyperlinkedRelatedField(many=True, view_name='staffers:committee-detail', read_only=True)
  class Meta:
    model = Delegation
    read_only = True


class CommitteeSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='staffers:committee-detail', read_only=True)
  # delegations = serializers.HyperlinkedRelatedField(many=True, view_name='staffers:delegation-detail', read_only=True)
  # staffers = serializers.HyperlinkedRelatedField(many=True, view_name='staffers:committeestaffer-detail', read_only=True)
  # usg_group = serializers.HyperlinkedRelatedField(view_name='staffers:usggroup-detail', read_only=True)

  class Meta:
    model = Committee
    read_only = True
    exclude = ('delegations', 'usg_group')


class USGGroupSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='staffers:usggroup-detail', read_only=True)
  committees = serializers.HyperlinkedRelatedField(many=True, view_name='staffers:committee-detail', read_only=True)
  usg = serializers.HyperlinkedRelatedField(view_name='staffers:internaluser-detail', read_only=True)

  class Meta:
    model = USGGroup
    read_only = True

from rest_framework import serializers

from atlas.models import Committee


class CommitteeSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='staffers:committee-detail', read_only=True)
  # delegations = serializers.HyperlinkedRelatedField(many=True, view_name='staffers:delegation-detail', read_only=True)
  # staffers = serializers.HyperlinkedRelatedField(many=True, view_name='staffers:committeestaffer-detail', read_only=True)
  # usg_group = serializers.HyperlinkedRelatedField(view_name='staffers:usggroup-detail', read_only=True)

  class Meta:
    model = Committee
    read_only = True
    exclude = ('delegations', 'usg_group')

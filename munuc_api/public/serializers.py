from rest_framework import serializers

from munuc_api.models import Committee
from munuc_api.models import Country
from munuc_api.models import USGGroup


class CountrySerializer(serializers.HyperlinkedModelSerializer):
  committees = serializers.HyperlinkedRelatedField(many=True, view_name='committee-detail', read_only=True)
  class Meta:
    model = Country
    read_only_fields = ('name',)


class CommitteeSerializer(serializers.HyperlinkedModelSerializer):
  countries = serializers.HyperlinkedRelatedField(many=True, view_name='country-detail', read_only=True)
  class Meta:
    model = Committee
    read_only_fields = ('name', 'abbreviation', 'blurb', 'usg_group', 'countries')


class USGGroupSerializer(serializers.HyperlinkedModelSerializer):
  committees = serializers.HyperlinkedRelatedField(many=True, view_name='committee-detail', read_only=True)
  # committees = CommitteeSerializer(many=True)
  class Meta:
    model = USGGroup
    read_only_fields = ('name', 'abbreviation', 'blurb', 'committees')

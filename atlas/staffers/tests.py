import json

from rest_framework import status

from atlas.tests import BaseTestCase
from atlas.staffers import serializers

from atlas.models import Committee
from atlas.models import CommitteeStaffer
from atlas.models import Delegation
from atlas.models import USGGroup


class TestStaffersApi(BaseTestCase):
  def _create_sample_usg_group(self):
    """Creates sample USGGroup instance.

    Only call in tests which do not directly test USGGroup creation.
    """
    usg = self.create_internal_user('USG', 'bsmithgall')
    usg_group = USGGroup.objects.create(usg=usg, name='General Assembly', abbreviation='GA')
    usg_group.save()
    return usg_group

  def _create_sample_committee(self):
    usg_group = self._create_sample_usg_group()
    committee = Committee.objects.create(
        name='Legal Committee',
        abbreviation='legal',
        usg_group=usg_group,
        email='legal@munuc.org',
    )
    committee.save()
    return committee

  def test_committees_get(self):
    usg_group = self._create_sample_usg_group()
    committee = Committee.objects.create(
        name='Legal Committee',
        abbreviation='legal',
        usg_group=usg_group,
        email='legal@munuc.org',
    )
    committee.save()
    self.create_staffer('Chair', 'mzhang', committee)
    self.assertEquals(self.client.get('/staffers/committees/').status_code, status.HTTP_403_FORBIDDEN)

    expected = {
        'name': 'Legal Committee',
        'url': '%s/staffers/committees/%d/' % (self.url_base, committee.id),
        'abbreviation': 'legal',
        'email': 'legal@munuc.org',
        'blurb': '',
    }

    self.client.login(username='mzhang', password='password')
    response = self.client.get('/staffers/committees/').json()
    self.assertEquals(len(response), 1)
    self.assertEquals(response[0], expected)

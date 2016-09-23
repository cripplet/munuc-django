import json

from munuc_api.tests import BaseTestCase
from munuc_api.public import serializers

from munuc_api.models import Committee
from munuc_api.models import Delegation
from munuc_api.models import USGGroup


class TestPublicApi(BaseTestCase):
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

  def test_excom_get(self):
    user = self.create_internal_user(
        'SecGen', 'rtrevor', first_name='Reece', last_name='Trevor')
    response = self.client.get('/public/excom/').json()

    expected = {
        'first_name': 'Reece',
        'last_name': 'Trevor',
        'role': 'SecGen',
        'prefix': 'Mr.',
        'suffix': '',
        'email': 'secgen@munuc.org',
        'usg_group': None,
        'blurb': 'Some blurb',
        'url': '%s/public/excom/%d/' % (self.url_base, user.id),
    }

    self.assertEquals(len(response), 1)
    self.assertEquals(response[0], expected)

  def test_usg_group_get(self):
    usg = self.create_internal_user('USG', 'rtrevor')
    usg_group = USGGroup.objects.create(usg=usg, name='General Assembly', abbreviation='GA')
    usg_group.save()
    response = self.client.get('/public/usg_groups/').json()

    expected = {
        'committees': [],
        'name': 'General Assembly',
        'abbreviation': 'GA',
        'blurb': '',
        'url': '%s/public/usg_groups/%d/' % (self.url_base, usg_group.id),
        'usg': '%s/public/excom/%d/' % (self.url_base, usg.id),
    }

    self.assertEquals(len(response), 1)
    self.assertEquals(response[0], expected)

  def test_delegations_get(self):
    delegation = Delegation.objects.create(name='Taiwan')
    delegation.save()
    response = self.client.get('/public/delegations/').json()

    expected = {
        'committees': [],
        'name': 'Taiwan',
        'url': '%s/public/delegations/%d/' % (self.url_base, delegation.id),
    }

    self.assertEquals(len(response), 1)
    self.assertEquals(response[0], expected)

    committee = self._create_sample_committee()
    delegation.committees.add(committee)
    response = self.client.get('/public/delegations/').json()

    expected['committees'] = [
            '%s/public/committees/%d/' % (self.url_base, committee.id)
    ]

    self.assertEquals(len(response), 1)
    self.assertEquals(response[0], expected)

  def test_committees_get(self):
    usg_group = self._create_sample_usg_group()
    committee = Committee.objects.create(
        name='Legal Committee',
        abbreviation='legal',
        usg_group=usg_group,
        email='legal@munuc.org',
    )
    committee.save()
    response = self.client.get('/public/committees/').json()

    expected = {
        'staffers': [],
        'name': 'Legal Committee',
        'delegations': [],
        'url': '%s/public/committees/%d/' % (self.url_base, committee.id),
        'usg_group': '%s/public/usg_groups/%d/' % (self.url_base, usg_group.id),
        'abbreviation': 'legal',
        'email': 'legal@munuc.org',
        'blurb': '',
    }

    self.assertEquals(len(response), 1)
    self.assertEquals(response[0], expected)

    delegation = Delegation.objects.create(name='China')
    committee.delegations.add(delegation)
    committee.save()
    staffer = self.create_staffer(
        role='Chair',
        username='mzhang',
        committee=committee,
    )
    response = self.client.get('/public/committees/').json()

    expected['staffers'] = [
        '%s/public/staffers/%d/' % (self.url_base, staffer.id),
    ]
    expected['delegations'] = [
        '%s/public/delegations/%d/' % (self.url_base, delegation.id),
    ]

    self.assertEquals(len(response), 1)
    self.assertEquals(response[0], expected)

  def test_staffer_get(self):
    committee = self._create_sample_committee()
    staffer = self.create_staffer(
        role='Chair',
        username='mzhang',
        first_name='Minke',
        last_name='Zhang',
        committee=committee,
    )
    response = self.client.get('/public/staffers/').json()

    expected = {
        'url': '%s/public/staffers/%d/' % (self.url_base, staffer.id),
        'committee': '%s/public/committees/%d/' % (self.url_base, committee.id),
        'prefix': 'Mr.',
        'suffix': '',
        'role': 'Chair',
        'first_name': 'Minke',
        'last_name': 'Zhang',
    }

    self.assertEquals(len(response), 1)
    self.assertEquals(response[0], expected)

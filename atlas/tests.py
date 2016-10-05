from django.test import override_settings
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from atlas.models import InternalUser
from atlas.models import USGGroup
from atlas.models import Delegation
from atlas.models import Committee
from atlas.models import CommitteeStaffer


@override_settings(ROOT_URLCONF='atlas.urls')
class BaseTestCase(APITestCase):
  def setUp(self):
    super(BaseTestCase, self).setUp()
    self.factory = APIRequestFactory()
    self.client = APIClient()
    self.url_base = 'http://testserver'

  def _create_user(self, username, first_name, last_name, password=''):
    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password)
    user.save()
    return user

  def create_staffer(self, role, username, committee, first_name='', last_name=''):
    prefix = 'Mr.'
    email = '%s@munuc.org' % username
    password = 'password'
    staffer = CommitteeStaffer.objects.create(
        user=self._create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        ),
        prefix=prefix,
        role=role,
        committee=committee,
        email=email,
    )
    staffer.save()
    return staffer
    
  def create_internal_user(self, role, username, first_name='', last_name=''):
    prefix = 'Mr.'
    password = 'password'
    blurb = 'Some blurb'
    email = ('%s@munuc.org' % role).lower()
    internal_user = InternalUser.objects.create(
        user=self._create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        ),
        prefix=prefix,
        role=role,
        blurb=blurb,
        email=email,
    )
    return internal_user

  def tearDown(self):
    InternalUser.objects.all().delete()
    USGGroup.objects.all().delete()
    Delegation.objects.all().delete()
    Committee.objects.all().delete()
    CommitteeStaffer.objects.all().delete()
    super(BaseTestCase, self).tearDown()


class GroupTest(BaseTestCase):
  def test_internal_user(self):
    user = self.create_internal_user('USG', 'mzhang')
    self.assertIn(Group.objects.get(name='internal_user'), user.user.groups.all())

  def test_staffer(self):
    usg = self.create_internal_user('USG', 'bsmithgall')
    usg_group = USGGroup.objects.create(usg=usg, name='General Assembly', abbreviation='GA')
    usg_group.save()
    committee = Committee.objects.create(
        name='Legal Committee',
        abbreviation='legal',
        usg_group=usg_group,
        email='legal@munuc.org',
    )
    committee.save()
    user = self.create_staffer('Chair', 'mzhang', committee)
    self.assertIn(Group.objects.get(name='committee_staffer'), user.user.groups.all())

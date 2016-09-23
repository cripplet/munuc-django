from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


@receiver(pre_save)
def pre_save_handler(sender, instance, *args, **kwargs):
    instance.full_clean()


class BaseUser(models.Model):
  class Meta:
    abstract = True

  PREFIX_CHOICES = (
      ('Mr.', 'Mr.'),
      ('Mrs.', 'Mrs.'),
      ('Ms.', 'Ms.'),
      ('Mx.', 'Mx.'),
      ('Dr.', 'Dr.'),
  )
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  prefix = models.CharField(max_length=4, choices=PREFIX_CHOICES)
  suffix = models.CharField(max_length=16, blank=True)


class Accountant(BaseUser):
  class Meta:
    abstract = True
#  permission = models.BooleanField(default=False)


class InternalUser(Accountant):
  ROLE_CHOICES = (
      ('SecGen', 'Secretary General'),
      ('COO', 'Chief Operating Officer'),
      ('CFO', 'Chief Financial Officer'),
      ('CTO', 'Chief Technical Officer'),
      ('CAO', 'Chief Administrative Officer'),
      ('COS', 'Chief of Staff'),
      ('MAL', 'Member at Large'),
      ('USG', 'Under-Secretary-General'),
  )
  role = models.CharField(max_length=8, choices=ROLE_CHOICES)
  blurb = models.TextField(blank=True)
  email = models.EmailField(unique=True)


# class Minion(Accountant):
#   ROLE_CHOICES = (
#       ('Adminion', 'Administrative Helper'),
#       ('Techminion', 'Technology Helper'),
#       ('Deputy Director of Technology', 'Chief CTO Assistant'),
#   )
#   role = models.CharField(max_length=255, choices=ROLE_CHOICES)
#   parent = models.ForeignKey(InternalUser, related_name='minions')
#   email = models.EmailField(unique=True)


# class Advisor(Accountant):
#   registration = models.ForeignKey(Registration, related_name='advisors')
#   email = models.EmailField(unique=True)


# class Chaperone(BaseUser):
#   registration = models.ForeignKey(Registration, related_name='chaperones')


class USGGroup(models.Model):
  name = models.CharField(max_length=255, unique=True)
  abbreviation = models.CharField(max_length=8, unique=True)
  blurb = models.TextField(blank=True)
  usg = models.OneToOneField(InternalUser, related_name='usg_group')


class Delegation(models.Model):
  name = models.CharField(max_length=255, unique=True)


class Committee(models.Model):
  name = models.CharField(max_length=255, unique=True)
  abbreviation = models.CharField(max_length=8, unique=True)
  email = models.EmailField(unique=True)
  blurb = models.TextField(blank=True)
  usg_group = models.ForeignKey(
      USGGroup, on_delete=models.CASCADE,
      related_name='committees')
  delegations = models.ManyToManyField(Delegation, blank=True, related_name='committees')


class CommitteeStaffer(BaseUser):
  ROLE_CHOICES = (
      ('Chair', 'Chair'),
      ('Moderator', 'Moderator'),
      ('Staffer', 'Staffer'),
      ('Crisis Director', 'Crisis Director'),
  )
  role = models.CharField(max_length=255, choices=ROLE_CHOICES)
  committee = models.ForeignKey(Committee, related_name='staffers')
  email = models.EmailField(unique=True)


# class Delegate(BaseUser):
#   committee = models.ForeignKey(Committee, related_name='delegates')
#   delegation = models.ForeignKey(Delegation, related_name='delegates')
#   registration = models.ForeignKey(Registration, related_name='delegates')

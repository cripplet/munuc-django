from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class USGGroup(models.Model):
  name = models.CharField(max_length=255, unique=True, blank=False)
  abbreviation = models.CharField(max_length=8, unique=True, blank=False)
  blurb = models.TextField(default='')


class Country(models.Model):
  class Meta:
    verbose_name_plural = 'countries'
  name = models.CharField(max_length=255, unique=True, blank=False)


class Committee(models.Model):
  name = models.CharField(max_length=255, unique=True, blank=False)
  abbreviation = models.CharField(max_length=8, unique=True, blank=False)
  blurb = models.TextField(default='')
  usg_group = models.ForeignKey(
      USGGroup, on_delete=models.CASCADE, blank=False,
      related_name='committees')
  countries = models.ManyToManyField(Country, related_name='committees')


class ExtendedUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)

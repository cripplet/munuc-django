from django.contrib import admin

from .models import Committee
from .models import Country
from .models import USGGroup


admin.site.register(Committee)
admin.site.register(Country)
admin.site.register(USGGroup)

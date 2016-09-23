from django.contrib import admin

from .models import Committee
from .models import CommitteeStaffer
from .models import Delegation
from .models import InternalUser
from .models import USGGroup


admin.site.register(Committee)
admin.site.register(CommitteeStaffer)
admin.site.register(Delegation)
admin.site.register(InternalUser)
admin.site.register(USGGroup)

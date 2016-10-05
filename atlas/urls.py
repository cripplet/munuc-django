from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'docs/', include('rest_framework_docs.urls')),
    url(r'public/', include('atlas.public.urls', namespace='public')),
    url(r'staffers/', include('atlas.staffers.urls', namespace='staffers')),
]

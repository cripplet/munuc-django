from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'docs/', include('rest_framework_docs.urls')),
    url(r'public/', include('munuc_api.public.urls', namespace='public')),
]

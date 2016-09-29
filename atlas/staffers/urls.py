rom rest_framework import routers
from atlas.staffers import views


router = routers.DefaultRouter()
router.register(r'committees', views.CommitteeViewSet, base_name='committee')

urlpatterns = router.urls

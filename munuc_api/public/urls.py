from rest_framework import routers
from munuc_api.public import views


router = routers.DefaultRouter()
router.register(r'committees', views.CommitteeViewSet, base_name='committee')
router.register(r'staffers', views.CommitteeStafferViewSet, base_name='committeestaffer')
router.register(r'delegations', views.DelegationViewSet, base_name='delegation')
router.register(r'usg_groups', views.USGGroupViewSet, base_name='usggroup')
router.register(r'excom', views.InternalUserViewSet, base_name='internaluser')

urlpatterns = router.urls

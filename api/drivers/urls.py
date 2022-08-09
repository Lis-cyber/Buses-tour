from rest_framework import routers
from .views import DriverViewSet


app_name = 'drivers'

router = routers.SimpleRouter()
router.register('drivers', DriverViewSet)

urlpatterns = router.urls

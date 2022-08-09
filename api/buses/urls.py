from rest_framework import routers
from .views import BusViewSet


app_name = 'buses'

router = routers.SimpleRouter()
router.register('buses', BusViewSet)

urlpatterns = router.urls

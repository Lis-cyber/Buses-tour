from rest_framework import routers
from .views import PassengerViewSet

app_name = 'passengers'

router = routers.SimpleRouter()
router.register('passengers', PassengerViewSet)

urlpatterns = router.urls

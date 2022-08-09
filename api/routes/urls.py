from rest_framework import routers
from .views import RouteViewSet


app_name = 'routes'

router = routers.SimpleRouter()
router.register('routes', RouteViewSet)

urlpatterns = router.urls

# from django.urls import path
# from buses import views

# from django.conf.urls.static import static
# from django.conf import settings

# app_name = 'buses'

# urlpatterns = [
#     path(r'buses', views.busApi),
#     path(r'buses/<int:id>', views.busApi),
# ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from rest_framework import routers
from .views import BusViewSet


app_name = 'buses'

router = routers.SimpleRouter()
router.register('buses', BusViewSet)

urlpatterns = router.urls



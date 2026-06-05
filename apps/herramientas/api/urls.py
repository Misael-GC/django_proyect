from rest_framework.routers import DefaultRouter
from .views import HerramientaViewSet

router = DefaultRouter()
router.register(r'', HerramientaViewSet, basename='herramienta')
urlpatterns = router.urls
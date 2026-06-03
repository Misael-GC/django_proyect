from rest_framework.routers import DefaultRouter
from .views import ToolViewSet

router = DefaultRouter()
router.register(r'tools', ToolViewSet, basename='tool')
urlpatterns = router.urls
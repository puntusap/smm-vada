from rest_framework.routers import DefaultRouter
from .views import TokenViewSet

router = DefaultRouter()
router.register(r'tokens', TokenViewSet, basename='token')
urlpatterns = router.urls

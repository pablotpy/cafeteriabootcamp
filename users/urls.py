from rest_framework import routers
from .views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')


urlpatterns = router.urls
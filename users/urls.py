from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

app_name = UsersConfig.name

urlpatterns = router.urls
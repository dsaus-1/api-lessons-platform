from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import UserViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

app_name = UsersConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    ] + router.urls
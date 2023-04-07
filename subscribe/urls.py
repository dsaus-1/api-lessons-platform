from subscribe.apps import SubscribeConfig
from django.urls import path

from subscribe.views import SubscribeCreateAPIView, SubscribeDestroyAPIView

app_name = SubscribeConfig.name

urlpatterns = [
    path('subscribed/', SubscribeCreateAPIView.as_view(), name='subscribed'),
    path('unsubscribed/<int:pk>/', SubscribeDestroyAPIView.as_view(), name='unsubscribed'),
]
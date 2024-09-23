from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LottoPickViewSet, UserViewSet

router = DefaultRouter()
router.register(r'lottopicks', LottoPickViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

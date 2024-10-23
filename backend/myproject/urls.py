from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='criar_usuario')
urlpatterns = [
    path("api/", include(router.urls)),
]

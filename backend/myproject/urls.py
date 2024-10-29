from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import UserViewSet,LoginView
from django.contrib.auth import views as auth_views
from django.contrib import admin

router = DefaultRouter()
router.register(r'', UserViewSet, basename='criar_usuario')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/criar_user/", include(router.urls)),
    path("api/login", LoginView.as_view()),
    path("api/redefinir_senha/", include("usuarios.urls_password_reset"))
]

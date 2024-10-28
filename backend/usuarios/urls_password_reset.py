# usuarios/urls_reset.py
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Envio de e-mail
    path('enviado/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Confirmação de envio
    path('<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Redefinição
    path('completo/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Sucesso
]

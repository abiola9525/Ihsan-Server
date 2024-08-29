from django.urls import path
from account import views

urlpatterns = [
    path('account/register/', views.register_user, name='register-user'),
]

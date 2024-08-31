from django.urls import path
from account import views

urlpatterns = [
    path('account/register/', views.register_user, name='register-user'),
    path('account/confirm/', views.confirm_email, name='confirm-email'),
    path('account/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]

from django.urls import path
from account import views

urlpatterns = [
    path('account/register/', views.register_user, name='register-user'),
    path('account/confirm/', views.confirm_email, name='confirm-email'),
    path('account/<int:pk>/update-status/', views.update_user_status, name='update-user-eval-status'),
    path('account/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('decode-token/', views.decode_jwt, name='decode_token'),
    
]

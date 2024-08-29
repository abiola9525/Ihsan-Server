from django.urls import path
from school import views

urlpatterns = [
    # Course URLs
    path('courses/', views.course_list_create, name='course-list-create'),
    path('courses/<int:pk>/', views.course_detail, name='course-detail-update-delete'),
    
    # Module URLs
    path('modules/', views.module_list_create, name='module-list-create'),
    path('modules/<int:pk>/', views.module_detail, name='module-detail-update-delete'),
    
    # Topic URLs
    path('topics/', views.topic_list_create, name='topic-list-create'),
    path('topics/<int:pk>/', views.topic_detail, name='topic-detail-update-delete'),
    
    # Quiz URLs
    path('quizzes/', views.quiz_list_create, name='quiz-list-create'),
    path('quizzes/<int:pk>/', views.quiz_detail, name='quiz-detail-update-delete'),
    
    # Question URLs
    path('questions/', views.question_list_create, name='question-list-create'),
    path('questions/<int:pk>/', views.question_detail, name='question-detail-update-delete'),
    
    # Answer URLs
    path('answers/', views.answer_list_create, name='answer-list-create'),
    path('answers/<int:pk>/', views.answer_detail, name='answer-detail-update-delete'),
    
    # User Module Score URLs
    path('user-module-scores/', views.user_module_score_list_create, name='user-module-score-list-create'),
    path('user-module-scores/<int:pk>/', views.user_module_score_detail, name='user-module-score-detail-update-delete'),
    
    # Payment Transaction URLs
    path('payment-transactions/', views.payment_transaction_list_create, name='payment-transaction-list-create'),
    path('payment-transactions/<int:pk>/', views.payment_transaction_detail, name='payment-transaction-detail-update-delete'),
]

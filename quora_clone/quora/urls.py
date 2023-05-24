from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-question/', views.create_question, name='create_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
]

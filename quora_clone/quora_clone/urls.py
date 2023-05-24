"""
URL configuration for quora_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from quora import views as quora_views

urlpatterns = [
    path('', quora_views.home, name='home'),
    path('post_question/', quora_views.post_question, name='post_question'),
    path('answer_question/<int:question_id>/', quora_views.answer_question, name='answer_question'),
    path('like_answer/<int:answer_id>/', quora_views.like_answer, name='like_answer'),
    path('login/', quora_views.user_login, name='login'),
    path('logout/', quora_views.user_logout, name='logout'),
    path('register/', quora_views.register, name='register'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]


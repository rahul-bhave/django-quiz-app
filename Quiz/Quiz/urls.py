"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
app_name = "App"

urlpatterns = [
 path("", views.login, name="login"),
 path("login", views.login, name="login"),
 path("dashboard", views.dashboard, name="dashboard"),
 path("quiz", views.quiz, name="quiz"),
 path("register", views.register, name="register"),
 path("create-quiz", views.create_quiz, name="create-quiz"),
 path("create-questions", views.create_question, name="create-question"),
 path("answer-quiz/<slug>", views.answer_quiz, name="answer-quiz"),
]
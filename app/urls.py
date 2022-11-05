from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('forum/<int:id>/', views.content, name='content'),
]

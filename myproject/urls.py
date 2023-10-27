from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.hello, name='hello'),  # Маршрут для корневого URL
    path('hello/', views.hello, name='hello'),
]

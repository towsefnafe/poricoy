from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.portfolio, name='portfolio'),
]

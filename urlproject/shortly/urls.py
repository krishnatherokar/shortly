from django.urls import path
from shortly import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('<str:code>/', views.redirectPage)
]
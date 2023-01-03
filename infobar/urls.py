from django.urls import path
from infobar import views

urlpatterns = [
    path('', views.home, name='home'),
]

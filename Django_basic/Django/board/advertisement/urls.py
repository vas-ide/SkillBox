from django.urls import path
from .import views


urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path('advertisement/', views.advertisement_upd, name='advertisement_upd'),
]
from django.urls import path
from .import views


urlpatterns = [
    # path("", views.advertisement_list, name='advertisement_list'),
    # path("", views.get_client_ip, name='advertisement_list'),
    path("advertisement/",  views.advertisement_upd,  name='advertisement_upd'),
    path("advertisement/", views.get_client_ip, name='advertisement_upd'),
    path("repair/", views.repair, name='repair'),
    path("veterinary/", views.veterinary, name='veterinary'),
    path("plumber/", views.plumber, name='plumber'),
    path("construction/", views.construction, name='constructional'),
    path("excavator/", views.excavator, name='excavator'),
]
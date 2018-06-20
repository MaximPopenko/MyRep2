from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
]



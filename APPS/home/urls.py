from django.conf.urls import url
from APPS.home import views

urlpatterns = [
    url('home/',views.index),
]

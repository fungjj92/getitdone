from django.conf.urls import url
from list import views

urlpatterns = [
    url(r'^$', views.listPage, name="list"),
]
from django.conf.urls import url
from list import views

urlpatterns = [
    url(r'^$', views.index, name="list"), #main, index. ONLY VISUAL VIEW
    url(r'^list/new', views.addTask), # AJAX VISUALIZATIONS VV
    url(r'^list/completed', views.completeTask),
    url(r'^list/delete', views.deleteTask)
]
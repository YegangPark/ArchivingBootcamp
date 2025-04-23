from django.urls import path
from . import views

app_name = "vidios"

urlpatterns = [

    path("", views.index, name="index"),
    path("query", views.lecture_search, name='query'),

]
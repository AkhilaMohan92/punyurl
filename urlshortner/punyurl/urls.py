from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("generate_short_id/", views.generate_short_id, name='generate_short_id'),
    path("<str:shorturl>", views.find_url, name='find_url'),
]
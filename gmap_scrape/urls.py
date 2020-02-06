from django.urls import path
from . import views

app_name = 'gmap_scrape'
urlpatterns = [
    path('', views.index, name='index'),
    path('form',views.form, name='form'),
]

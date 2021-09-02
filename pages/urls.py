from django.urls import path
from . import views

# We need to link our pages routes here
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]

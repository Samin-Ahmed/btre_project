from django.urls import path
from . import views

# We need to link our accounts routes here. Anything we link in this URLs.py we must link in the main URLs.py in BTRE.
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]

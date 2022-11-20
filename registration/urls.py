from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), # views.index is pointing to the home function in views.py file
    path('signup/', views.signup, name='signup'), # views.signup is pointing to the home function in views.py file
    path('login/', views.login, name='login'), # views.login is pointing to the home function in views.py file
    path('home/', views.home, name='home'), # views.home is pointing to the home function in views.py file
]

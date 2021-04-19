from .views import *
from django.urls import path


urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>', get_category, name='category'),
]
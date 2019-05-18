from django.urls import path
from . import views

urlpatterns = [
    path('', views.historialnotas, name='comment_list'),

]


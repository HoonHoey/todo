from . import views
from django.urls import path, include
urlpatterns = [
    path('', views.index, name='index'),
    path('studendts', views.students, name='studendts'),
    path('scores', views.score, name='scores')
]
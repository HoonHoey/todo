from . import views
from django.urls import path, include

app_name="second"

urlpatterns = [
    path('', views.index, name='index'),
    path('favorite', views.favorite, name='favorite'),
    path('todo', views.todo, name='todo'),
    path('favorite/<seq>', views.favorite_detail, name='favorite_detail')
]


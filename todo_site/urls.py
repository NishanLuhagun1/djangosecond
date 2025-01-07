from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('del/<str:item_id>', views.remove, name='del'),
]

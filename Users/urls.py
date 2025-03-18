from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'), 
    #path('', views.index),
    path('hello/<str:username>',views.hello),
    path('about/', views.about),
    path('projects', views.projects),
    path('tasks/<int:id>',views.tasks)
]

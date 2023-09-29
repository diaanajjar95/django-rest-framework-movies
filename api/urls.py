from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:id>/', views.movie_detail),
    path('genres/', views.genre_list),
    path('genres/<int:id>/', views.genre_detail),
    path('directors/', views.director_list),
    path('directors/<int:id>/', views.director_detail),
    path('actors/', views.actor_list),
    path('actors/<int:id>/', views.actor_detail),
    path('directors/<int:id>/', views.director_detail),
    path('writers/', views.writer_list),
    path('writers/<int:id>/', views.writer_detail),
]



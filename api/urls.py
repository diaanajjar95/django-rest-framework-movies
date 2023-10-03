from django.urls import path
from . import views

urlpatterns = [
    # path('movies/', views.movie_list),
    path('movies/', views.MovieList.as_view()),
    # path('movies/<int:id>/', views.movie_detail),
    path('movies/<int:id>/', views.MovieDetail.as_view()),
    # path('genres/', views.genre_list),
    path('genres/', views.GenreList.as_view()),
    # path('genres/<int:id>/', views.genre_detail),
    path('genres/<int:id>/', views.GenreDetail.as_view()),
    # path('directors/', views.director_list),
    path('directors/', views.DirectorList.as_view()),
    # path('directors/<int:id>/', views.director_detail),
    path('directors/<int:id>/', views.DirectorDetail.as_view()),
    # path('actors/', views.actor_list),
    path('actors/', views.ActorList.as_view()),
    # path('actors/<int:id>/', views.actor_detail),
    path('actors/<int:id>/', views.ActoreDetail.as_view()),
    # path('directors/<int:id>/', views.director_detail),
    # path('writers/', views.writer_list),
    path('writers/', views.WriterList.as_view()),
    # path('writers/<int:id>/', views.writer_detail),
    path('writers/<int:id>/', views.WriterDetail.as_view()),
]



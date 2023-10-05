from .models import Movie,Genre,Actor,Director,Writer
from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer,GenreSerializer,CreateMovieSerializer, WriterSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListAPIView
from rest_framework.viewsets import ModelViewSet


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenereViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'  # this is the make this view take the url parameter as id not as pk 


class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'id'


class WriterViewSet(ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'id'
    

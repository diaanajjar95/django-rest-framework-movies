from .models import Movie,Genre,Actor,Director, Review,Writer
from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer,GenreSerializer,CreateMovieSerializer, ReviewSerializer, WriterSerializer
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
    

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(movie_id=self.kwargs['movie_pk'])

    def get_serializer_context(self):
        return {'movie_id':self.kwargs['movie_pk']}
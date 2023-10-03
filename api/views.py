from .models import Movie,Genre,Actor,Director,Writer
from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer,GenreSerializer,CreateMovieSerializer, WriterSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListAPIView

class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


    # def get_queryset(self):
    #     return Movie.objects.all()
    

    # def get_serializer_class(self):
    #     return MovieSerializer


class MovieDetail(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreList(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id' # this is the make this view take the url parameter as id not as pk 



class DirectorList(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer



class DirectorDetail(RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'



class ActorList(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class ActoreDetail(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'id'



class WriterList(ListAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer



class WriterDetail(RetrieveAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'id'

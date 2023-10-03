from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie,Genre,Actor,Director,Writer
from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer,GenreSerializer,CreateMovieSerializer, WriterSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView


class MovieList(APIView):
    def get(self,request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CreateMovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         queryset = Movie.objects.all()
#         serializer = MovieSerializer(queryset,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CreateMovieSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

class MovieDetail(APIView):
    def get(self,request,id):
        movie = get_object_or_404(Movie,pk=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# @api_view()
# def movie_detail(request,id):
#     movie = get_object_or_404(Movie,pk=id)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)




class GenreList(APIView):
    def get(self,request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# @api_view(['GET','POST'])
# def genre_list(request):
#     if request.method == 'GET':
#         queryset = Genre.objects.all()
#         serializer = GenreSerializer(queryset,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = GenreSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

class GenreDetail(APIView):
    def get(self,request,id):
        genre = get_object_or_404(Genre,pk=id)
        serialier = GenreSerializer(genre)
        return Response(serialier.data)
    
    def patch(self,request,id):
        genre = get_object_or_404(Genre,pk=id)
        serialier = GenreSerializer(genre,data=request.data)
        serialier.is_valid(raise_exception=True)
        serialier.save()
        return Response(serialier.data)




# @api_view(['GET','PATCH'])
# def genre_detail(request,id):
#     genre = get_object_or_404(Genre,pk=id)
#     if request.method == 'GET':
#         serialier = GenreSerializer(genre)
#         return Response(serialier.data)
#     elif request.method == 'PATCH':
#         serialier = GenreSerializer(genre,data=request.data)
#         serialier.is_valid(raise_exception=True)
#         serialier.save()
#         return Response(serialier.data)
    



class DirectorList(APIView):
    def get(self,request):
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset,many=True)
        return Response(serializer.data)



# @api_view()
# def director_list(request):
#     queryset = Director.objects.all()
#     serializer = DirectorSerializer(queryset,many=True)
#     return Response(serializer.data)


class DirectorDetail(APIView):
    def get(self,request,id):
        director = get_object_or_404(Director,pk=id)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)


# @api_view()
# def director_detail(request,id):
#     director = get_object_or_404(Director,pk=id)
#     serializer = DirectorSerializer(director)
#     return Response(serializer.data)


class ActorList(APIView):
    def get(self,request):
        queryset = Actor.objects.all()
        serializer = ActorSerializer(queryset,many=True)
        return Response(serializer.data)

# @api_view()
# def actor_list(request):
#     queryset = Actor.objects.all()
#     serializer = ActorSerializer(queryset,many=True)
#     return Response(serializer.data)




class ActoreDetail(APIView):
    def get(self,request,id):
        actor = get_object_or_404(Actor,pk=id)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)


# @api_view()
# def actor_detail(requerst,id):
#     actor = get_object_or_404(Actor,pk=id)
#     serializer = ActorSerializer(actor)
#     return Response(serializer.data)




class WriterList(APIView):
    def get(self,request):
        queryset = Writer.objects.all()
        serializer = WriterSerializer(queryset,many=True)
        return Response(serializer.data)


# @api_view()
# def writer_list(request):
#     queryset = Writer.objects.all()
#     serializer = WriterSerializer(queryset,many=True)
#     return Response(serializer.data)



class WriterDetail(APIView):
    def get(self,request,id):
        writer = get_object_or_404(Writer,pk=id)
        serializer = WriterSerializer(writer)
        return Response(serializer.data)


# @api_view()
# def writer_detail(requerst,id):
#     writer = get_object_or_404(Writer,pk=id)
#     serializer = WriterSerializer(writer)
#     return Response(serializer.data)



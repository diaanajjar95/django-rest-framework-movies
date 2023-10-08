from rest_framework import serializers
from .models import Genre, Movie,Director,Actor, Review,Writer



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','title']





class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director 
        fields = '__all__'




class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor 
        fields = '__all__'





class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer 
        fields = '__all__'




class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','description','genre','director','actors','writers']



        

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    director = DirectorSerializer()
    actors = ActorSerializer(many=True)
    writers = WriterSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id','title','description','genre','director','actors','writers']




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description']

    
    def create(self, validated_data):
        movie_id = self.context['movie_id']
        return Review.objects.create(movie_id=movie_id,**validated_data)



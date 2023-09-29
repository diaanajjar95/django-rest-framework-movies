

from django.db import models


# Models :
# 1- Movie
# 2- Actor
# 3- Director
# 4- Writer
# 5- Genre
# 6- Review


# an GENRE can has multiple MOVIE objects, and an MOVIE can belong to one GENRE object. (One To Many)
# an ACTOR can act in multiple MOVIE, and an MOVIE can has multiple ACTOR objects. (Many To Many)
# an MOVIE can be Directed by one DIRECTOR, and an DIRECTOR can direct multiple MOVIE objects. (One To Many)
# an MOVIE can be Written by multiple WRITER objects, and an WRITER can write multiple MOVIE objects. (Many To Many)


# https://docs.djangoproject.com/en/4.2/topics/db/examples/one_to_one/
# https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/
# https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/
# https://www.django-rest-framework.org/
# https://medium.com/powered-by-django/how-to-install-launch-django-windows-bad876b9422


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    



class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    about = models.CharField(max_length=999)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name
    




class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    about = models.CharField(max_length=999)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name
    




class Writer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    about = models.CharField(max_length=999)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name
    



    

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE) # Many-To-One
    director = models.ForeignKey(Director,on_delete=models.CASCADE) # Many-To-One
    actors = models.ManyToManyField(Actor) # Many-To-Many
    writers = models.ManyToManyField(Writer) # Many-To-Many

    def __str__(self) -> str:
        return self.title



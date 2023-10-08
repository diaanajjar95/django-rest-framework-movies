from django.urls import path
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('movies',views.MovieViewSet)
router.register('genres',views.GenereViewSet)
router.register('directors',views.DirectorViewSet)
router.register('actors',views.ActorViewSet)
router.register('writers',views.WriterViewSet)

movies_router = routers.NestedDefaultRouter(router,'movies',lookup = 'movie') # the arguments respectively parent router, parent prefix, lookup parameter  
movies_router.register('reviews',views.ReviewViewSet,basename='movie-reviews') # registering the child resouce , the arguments respectively prefix, viewset, basename which is used as prefix for generating the name of URL patterns  

urlpatterns = router.urls + movies_router.urls


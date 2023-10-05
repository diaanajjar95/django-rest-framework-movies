from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('movies',views.MovieViewSet)
router.register('genres',views.GenereViewSet)
router.register('directors',views.DirectorViewSet)
router.register('actors',views.ActorViewSet)
router.register('writers',views.WriterViewSet)

urlpatterns = router.urls


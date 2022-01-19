from django.urls import path
from . import views
from .AstroInfo import issLocation, astroPhotoDay, marsPhotos

urlpatterns = [
    path('', views.home, name='home'),
    path('ISSLocation/', issLocation.isslocation, name='ISSLocation'),
    path('astroPhotoDay/', astroPhotoDay.astroPhotoOftheDay, name = 'astroPhotoDay'),
    path('astroPhotoYesterday/', astroPhotoDay.astroPhotoOfYesterday, name = 'astroPhotoOfYesterday'),
    path('marsPhotos/', marsPhotos.marsPhotos, name='marsPhotos'),
]
from django.urls import path
from . import views
from .AstroInfo import issLocation


urlpatterns = [
    path('', views.home, name='home'),
    path('ISSLocation/', issLocation.isslocation, name='ISSLocation')
]
from .views import *
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('new', index),
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', isAuthenticated.as_view()),
    path('current-song', CurrentSong.as_view()),
    path('pause', PauseSong.as_view()),
    path('play', PlaySong.as_view()),
    path('skip-song', SkipSong.as_view())
]

print('spotify')
from django.urls import path
from .views import *

urlpatterns = [
     path('letters/', LetterCreateAPIView.as_view(), name='letter-create'),
     path('teams/<int:team_id>/letters/', TeamLetterListAPIView.as_view(), name='team-letters'),
     path('tracks/', TrackListAPIView.as_view(), name='track-list'),
     path('tracks/<int:track_id>/teams/', TeamByTrackAPIView.as_view(), name='track-teams'),
]

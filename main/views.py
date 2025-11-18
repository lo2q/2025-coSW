from django.shortcuts import render
from rest_framework import generics
from django.db.models import Q
from .models import *
from .serializers import *

# Create your views here.

# 편지 쓰기 (POST /letters/)
class LetterCreateAPIView(generics.CreateAPIView):
     queryset = Letter.objects.all()
     serializer_class = LetterSerializer


# 멘토별 편지 리스트 조회 (GET /teams/<team_id>/letters/)
class TeamLetterListAPIView(generics.ListAPIView):
     serializer_class = LetterSerializer
     
     def get_queryset(self):
          team_id = self.kwargs['team_id']
          base_letters = list(Letter.objects.filter(team__team_id=team_id))
          track4_letters = list(
               Letter.objects.filter(team__track__track_id=4)
          )

          combined = base_letters + track4_letters

          return combined

     
# 트랙 전체 조회
class TrackListAPIView(generics.ListAPIView):
     queryset = Track.objects.all()
     serializer_class = TrackSerializer


# 트랙별 팀 조회
class TeamByTrackAPIView(generics.ListAPIView):
     serializer_class = TeamSerializer

     def get_queryset(self):
          track_id = self.kwargs['track_id']
          return Team.objects.filter(track_id=track_id)

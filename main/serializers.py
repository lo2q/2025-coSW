from rest_framework import serializers
from .models import *


class LetterSerializer(serializers.ModelSerializer):
     class Meta:
          model = Letter
          fields = ['letter_id', 'team', 'writer', 'content']
          read_only_fields = ['letter_id']

class TrackSerializer(serializers.ModelSerializer):
     class Meta:
          model = Track
          fields = ['track_id', 'name']


class TeamSerializer(serializers.ModelSerializer):
     class Meta:
          model = Team
          fields = ['team_id', 'name1', 'name2', 'track']

from django.contrib import admin
from .models import Track, Team, Letter


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('track_id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('track_id',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'track', 'name1', 'name2')
    list_filter = ('track',)
    search_fields = ('name1', 'name2')
    ordering = ('team_id',)


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('letter_id', 'team', 'writer')
    list_filter = ('team',)
    search_fields = ('writer', 'content')
    ordering = ('letter_id',)

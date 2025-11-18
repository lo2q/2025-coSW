from django.db import models


class Track(models.Model):
     TRACK_CHOICES = (
          ('PD', 'PD'),
          ('BE', 'BE'),
          ('FE', 'FE'),
          ('ALL', 'ALL'),
     )

     track_id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=10, choices=TRACK_CHOICES)

     def __str__(self):
          return self.name


class Team(models.Model):
     team_id = models.AutoField(primary_key=True)
     track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='teams')

     name1 = models.CharField(max_length=100)
     name2 = models.CharField(max_length=100, blank=True, null=True)

     def __str__(self):
          return f"{self.team_id} - {self.track.name}"


class Letter(models.Model):
     letter_id = models.AutoField(primary_key=True)
     team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='letters')

     writer = models.CharField(max_length=100)
     content = models.TextField()

     def __str__(self):
          return f"Letter {self.letter_id} by {self.writer}"

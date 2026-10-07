from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    def __str__(self):
        return self.artist_name

class Album(models.Model):
    album_title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='cover/')
    release_date = models.DateField()
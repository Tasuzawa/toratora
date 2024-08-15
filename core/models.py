import uuid
from django.db import models
from core.utils import *


# Create your models here.
class Studio(models.Model):
    id_studio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_studio = models.CharField(max_length=255)
    negara = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.nama_studio
    
class Genre(models.Model):
    id_gendre = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_genre = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_genre
    
class Penulis(models.Model):
    id_penulis = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_penulis = models.CharField(max_length=255)
    biografi = models.TextField()
    social_media = models.URLField()

    def __str__(self):
        return self.nama_penulis

    
class Anime(models.Model):
    id_anime = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    cover = models.ImageField(upload_to=anime_cover_path)
    tanggal_rilis = models.DateField()
    genres = models.ManyToManyField(Genre)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    penulis = models.ForeignKey(Penulis,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.judul
    
    
class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    nomor_episode = models.PositiveIntegerField()
    judul_episode = models.CharField(max_length=255)
    tanggal_rilis = models.DateField()
    durasi = models.DurationField(null=True, blank=True)
    deskripsi = models.TextField(null=True, blank=True)
    video_url_360p = models.URLField(null=True, blank=True)
    video_url_720p = models.URLField(null=True, blank=True)
    video_url_1080p = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to=episode_thumbnail_path)
    
    
    class Meta:
        ordering = ['nomor_episode']

    def __str__(self):
        return f'{self.anime.judul} - Episode {self.nomor_episode}'

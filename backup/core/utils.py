from django.utils.text import slugify
from core.models import *

def anime_cover_path(instance, filename):
    nama_file = slugify(instance.judul)
    ext = filename.split('.')[-1]
    filename = f'{nama_file}.{ext}'
    
    return f'anime/{instance.id_anime}/cover/{filename}'

def episode_thumbnail_path(instance, filename):
    nama_file = slugify(instance.judul_episode)
    ext = filename.split('.')[-1]
    filename = f'{nama_file}.{ext}'
    
    return f'anime/{instance.anime.id_anime}/episode/{instance.nomor_episode}/thumbnail/{filename}'
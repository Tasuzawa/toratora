from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from core.datadummy import *

# Create your views here.
def main(request):
    render_template = 'main.html'
    context = {
        'anime_complete':anime_complete,
    }
    return render(request,render_template,context)

def animeDetail(request):
    render_template = 'animeDetail.html'
    
    context = {
        'anime_episode': anime_episode,
    }
    return render(request,render_template,context)

def animePlayEpisode(request):
    render_template = 'animePlayEpisode.html'
    context = {
        'anime_episode': anime_episode,
        'reaksi': reaksi,
    }
    return render(request,render_template,context)

def animeJadwalRilis(request):
    render_template = 'animeJadwalRilis.html'
    
    jadwal_senin = [anime for anime in anime_rilis if anime['day'] == 'Senin' ]
    jadwal_selasa = [anime for anime in anime_rilis if anime['day'] == 'Selasa' ]
    jadwal_rabu = [anime for anime in anime_rilis if anime['day'] == 'Rabu' ]
    jadwal_kamis = [anime for anime in anime_rilis if anime['day'] == 'Kamis' ]
    jadwal_jumat = [anime for anime in anime_rilis if anime['day'] == 'Jumat' ]
    jadwal_sabtu = [anime for anime in anime_rilis if anime['day'] == 'Sabtu' ]
    jadwal_minggu = [anime for anime in anime_rilis if anime['day'] == 'Minggu' ]
    
    context = {
        'jadwal_senin': jadwal_senin,
        'jadwal_selasa': jadwal_selasa,
        'jadwal_rabu': jadwal_rabu,
        'jadwal_kamis': jadwal_kamis,
        'jadwal_jumat': jadwal_jumat,
        'jadwal_sabtu': jadwal_sabtu,
        'jadwal_minggu': jadwal_minggu,
    }
    return render(request,render_template,context)

def animeDaftarList(request):
    render_template = 'animeDaftarList.html'
    
    huruf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    anime_all = [anime for anime in anime_complete2 if anime['title'].startswith('A')]
    anime_a = [anime for anime in anime_complete2 if anime['title'].startswith('A')]
    anime_b = [anime for anime in anime_complete2 if anime['title'].startswith('B')]
    anime_c = [anime for anime in anime_complete2 if anime['title'].startswith('C')]
    anime_d = [anime for anime in anime_complete2 if anime['title'].startswith('D')]
    anime_e = [anime for anime in anime_complete2 if anime['title'].startswith('E')]
    anime_f = [anime for anime in anime_complete2 if anime['title'].startswith('F')]
    anime_g = [anime for anime in anime_complete2 if anime['title'].startswith('G')]
    anime_h = [anime for anime in anime_complete2 if anime['title'].startswith('H')]
    anime_i = [anime for anime in anime_complete2 if anime['title'].startswith('I')]
    anime_j = [anime for anime in anime_complete2 if anime['title'].startswith('J')]
    anime_k = [anime for anime in anime_complete2 if anime['title'].startswith('K')]
    anime_l = [anime for anime in anime_complete2 if anime['title'].startswith('L')]
    anime_m = [anime for anime in anime_complete2 if anime['title'].startswith('M')]
    anime_n = [anime for anime in anime_complete2 if anime['title'].startswith('N')]
    anime_o = [anime for anime in anime_complete2 if anime['title'].startswith('O')]
    anime_p = [anime for anime in anime_complete2 if anime['title'].startswith('P')]
    anime_q = [anime for anime in anime_complete2 if anime['title'].startswith('Q')]
    anime_r = [anime for anime in anime_complete2 if anime['title'].startswith('R')]
    anime_s = [anime for anime in anime_complete2 if anime['title'].startswith('S')]
    anime_t = [anime for anime in anime_complete2 if anime['title'].startswith('T')]
    anime_u = [anime for anime in anime_complete2 if anime['title'].startswith('U')]
    anime_v = [anime for anime in anime_complete2 if anime['title'].startswith('V')]
    anime_w = [anime for anime in anime_complete2 if anime['title'].startswith('W')]
    anime_x = [anime for anime in anime_complete2 if anime['title'].startswith('X')]
    anime_y = [anime for anime in anime_complete2 if anime['title'].startswith('Y')]
    anime_z = [anime for anime in anime_complete2 if anime['title'].startswith('Z')]
    
    context = {
        'huruf': huruf,
        'anime_all': anime_all,
        'anime_a': anime_a, 
        'anime_b': anime_b, 
        'anime_c': anime_c, 
        'anime_d': anime_d, 
        'anime_e': anime_e, 
        'anime_f': anime_f, 
        'anime_g': anime_g, 
        'anime_h': anime_h, 
        'anime_i': anime_i, 
        'anime_j': anime_j, 
        'anime_k': anime_k, 
        'anime_l': anime_l, 
        'anime_m': anime_m, 
        'anime_n': anime_n, 
        'anime_o': anime_o, 
        'anime_p': anime_p, 
        'anime_q': anime_q, 
        'anime_r': anime_r, 
        'anime_s': anime_s, 
        'anime_t': anime_t, 
        'anime_u': anime_u, 
        'anime_v': anime_v, 
        'anime_w': anime_w, 
        'anime_x': anime_x, 
        'anime_y': anime_y, 
        'anime_z': anime_z,
        
    }
    
    return render(request, render_template, context)

def animeGenreList(request):
    render_template = 'animeGenreList.html'
    genres = [
        "Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror",
        "Mystery", "Romance", "Sci-Fi", "Slice of Life", "Sports", "Thriller",
        "Shounen", "Shoujo", "Seinen", "Josei", "Isekai", "Supernatural",
        "Historical", "Magical Girl", "Mecha", "Music", "Psychological"
    ]
    
    genre_slugs = {genre: slugify(genres) for genre in genres}
    context = {
        'anime_by_genre': anime_by_genre,
        'genres': genres,
        'genre_slugs': genre_slugs,
    }
    return render(request, render_template, context)

def animeGenreDetail(request, genre_slug):
    render_template = "animeGenreDetail.html"
    genre = get_object_or_404(genres, genre_slug=genre_slugs)
    
    anime_by_genres = [anime for anime in anime_by_genre if genre in anime['genres']]
    
    context = {
        'anime_by_genres': anime_by_genres,
        'genre': genre,
    }
    
    return render(request)
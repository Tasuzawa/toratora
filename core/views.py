from django.shortcuts import render
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
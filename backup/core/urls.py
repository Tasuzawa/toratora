from django.urls import path 

from core import views

urlpatterns = [
    path('',views.main,name='main'),
    path('anime/kage-no-jitsuryokusha-ni-naritakute/',views.animeDetail,name='animedetail'),
    path('kage-no-jitsuryokusha-ni-naritakute/episode-1/resolusi=480p',views.animePlayEpisode,name='animeplay'),
    path('anime/jadwal-rilis/',views.animeJadwalRilis,name='animejadwalrilis'),
    path('anime/list/',views.animeDaftarList,name='animedaftarlist'),
    path('genre/',views.animeGenreList,name='animegenrelist'),
    path('genre/<slug:slug>/', views.animeGenreDetail, name='animegenredetail'),
]

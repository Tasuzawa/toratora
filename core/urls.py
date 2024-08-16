from django.urls import path 

from core import views

urlpatterns = [
    path('',views.main,name='main'),
    path('anime/detail/',views.animeDetail,name='animedetail'),
]

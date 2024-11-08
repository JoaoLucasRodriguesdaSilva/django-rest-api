from django.urls import path
from . import views

urlpatterns = [
    path('musics/', views.MusicList.as_view(), name='music-list'),
    path('music/<int:pk>/', views.MusicDetail.as_view(), name='music-detail'),

    path('albuns/', views.AlbumList.as_view()),
    path('album/<int:pk>/', views.AlbumDetail.as_view()),

    path('bands/', views.BandList.as_view()),
    path('band/<int:pk>/', views.BandDetail.as_view()),

    path('members/', views.MemberList.as_view()),
    path('member/<int:pk>/', views.MemberDetail.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('<int:pk>/', views.album_detail, name='album_detail'),
    path('artist_list/', views.artist_list, name='artist_list'),
    path('artist_create/', views.artist_create, name='artist_create'),
    path('album_create/', views.album_create, name='album_create'),
    path('<int:pk>/delete/', views.album_delete, name='album_delete'),
]
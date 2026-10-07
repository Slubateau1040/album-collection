from django.shortcuts import render, get_object_or_404
from .models import Album, Artist
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'album/album_list.html', context)

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album/album_detail.html', {'album': album})

def artist_create(request):
    if request.method == 'POST':
        artist_name = request.POST['artist_name']
        Artist.objects.create(artist_name=artist_name)
        return HttpResponseRedirect(reverse('artist_list'))
    else:
        return render(request, 'album/artist_create.html')

def artist_list(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'album/artist_list.html', context)

def album_create(request):
    if request.method == 'POST':
        album_name = request.POST['album_name']
        artist_id = request.POST['artist']
        cover = request.FILES['cover']
        date = request.POST['date']
        Album.objects.create(album_name=album_name, artist_id=artist_id, cover=cover, date=date)
        return HttpResponseRedirect(reverse('album_list'))
    else:
        artists = Artist.objects.all()
        return render(request, 'album/album_create.html', {'artists': artists})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return HttpResponseRedirect(reverse('album_list'))
    return HttpResponseRedirect(reverse('album_list', args=[album.pk]))
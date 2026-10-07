from django.shortcuts import render, get_object_or_404
from .models import Album, Artist

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'album/album_list.html', context)

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album/album_detail.html', {'album': album})
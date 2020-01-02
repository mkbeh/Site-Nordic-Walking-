from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import PhotoAlbum, VideoAlbum
from blog.utils import get_pagination_page


def albums_list(request):
    album_specific_data = {'photo': (PhotoAlbum, 'Фото альбомы'), 'video': (VideoAlbum, 'Видео альбомы')}
    album_type = request.path.split('/')[2]
    album_obj, album_type = album_specific_data.get(album_type)

    albums = album_obj.objects.all().order_by('-created')
    page = get_pagination_page(request, albums)

    return render(
        request,
        'gallery/album.html',
        {'albums': page.object_list, 'page': page, 'album_type': album_type}
    )


@cache_page(10*60)
def album_detail(request, album_type, album_name):
    album_specific_data = {'photo': (PhotoAlbum, 50), 'video': (VideoAlbum, 4)}
    album_obj, num_pages = album_specific_data.get(album_type)
    obj = get_object_or_404(album_obj, name=album_name)

    if album_type == 'photo':
        files = obj.images_set.all()
        template = 'gallery/photo_detail.html'
    else:
        files = obj.videos_set.all()
        template = 'gallery/video_detail.html'

    page = get_pagination_page(request, files, num_pages)

    return render(
        request,
        template,
        {'album_name': album_name, 'files': page.object_list, 'page': page, 'total_files': len(files)}
    )

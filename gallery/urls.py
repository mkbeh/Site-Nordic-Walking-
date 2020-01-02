from django.urls import path

from .views import albums_list, album_detail


app_name = 'gallery'

urlpatterns = [
    path('<str:album_type>/<str:album_name>/', album_detail, name='album_detail'),
    path('video/', albums_list, name='video_albums'),
    path('photo/', albums_list, name='photo_albums'),
]

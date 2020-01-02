from django.contrib import admin

from .models import PhotoAlbum, VideoAlbum, Images, Videos


class BaseAlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created')
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('created',)


class ImagesInline(admin.TabularInline):
    model = Images
    fields = ('file', )


@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(BaseAlbumAdmin):
    inlines = (ImagesInline, )


class VideosInline(admin.TabularInline):
    model = Videos
    fields = ('file', )


@admin.register(VideoAlbum)
class VideoAlbumAdmin(BaseAlbumAdmin):
    inlines = (VideosInline, )

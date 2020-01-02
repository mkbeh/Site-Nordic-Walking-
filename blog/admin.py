from django.contrib import admin

from .models import Post, Category, Instructor, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status', 'category')
    list_filter = ('status', 'publish', 'category')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('initials',)
    ordering = ('initials',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user_name', 'body')

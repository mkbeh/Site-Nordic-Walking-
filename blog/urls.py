from django.urls import path

from .views import index, post_detail, about_event, instructors_list, search_posts


app_name = 'blog'

urlpatterns = [
    # path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/<str:query>/', search_posts, name='search_posts'),
    path('instructors/', instructors_list, name='instructors_list'),
    path('news/', about_event, name='news'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('', index, name='index'),
]

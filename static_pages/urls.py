from django.urls import path

from .views import static_page


app_name = 'static_pages'

urlpatterns = [
    path('<str:page_name>', static_page, name='static_page')
]

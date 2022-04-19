from django.urls import path

from music_app.web.views import home_page, create_album, album_details, edit_album, delete_album, profile_details, \
    create_profile, delete_profile

urlpatterns = (
    path('', home_page, name='home page'),

    path('album/add/', create_album, name='create album'),
    path('album/details /<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),

    path('profile/details/', profile_details, name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
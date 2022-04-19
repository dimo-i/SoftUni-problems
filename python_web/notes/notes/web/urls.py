from django.urls import path

from notes.web.views import show_home, add_note, edit_note, delete_note, details_page, profile_page, create_profile, \
    delete_profile

urlpatterns = (
    path('', show_home, name='show home'), # - home page
    path('add/', add_note, name='add note'), # add - add note page
    path('edit/<int:pk>/', edit_note, name='edit note'), # edit /:id - edit note page
    path('delete/<int:pk>/', delete_note, name='delete note'), # delete /:id - delete note page
    path('details/<int:pk>/', details_page, name='details page' ), # details /:id - note details page

    path('profile/', profile_page, name='profile page' ), # profile - profile page
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile')
)
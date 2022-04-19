from django.urls import path

from online_library.web.views import home_page, add_book_page, edit_book_page, book_details_page, profile_page, \
    edit_profile_page, delete_profile_page, create_profile, delete_book

urlpatterns = (
    path('', home_page, name='home page'),

    path('add/', add_book_page, name='add book page'),
    path('edit/<int:pk>/', edit_book_page, name='edit book page'),
    path('details/<int:pk>/', book_details_page, name='book details page'),
    path('delete/<int:pk>', delete_book, name='delete book'),

    path('profile/', profile_page, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile_page, name='edit profile'),
    path('profile/delete/', delete_profile_page, name='delete profile'),
)

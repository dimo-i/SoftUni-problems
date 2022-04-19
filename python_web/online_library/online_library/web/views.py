from django.shortcuts import render, redirect


# Create your views here.
from online_library.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateBookForm, EditBookForm
from online_library.web.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    books = Book.objects.all()
    context = {
        'profile': profile,
        'books': books,

    }
    return render(request, 'home-with-profile.html', context)


def add_book_page(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = CreateBookForm()

    context = {
        'form': form
    }
    return render(request, 'add-book.html', context)


def edit_book_page(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = EditBookForm(instance=book)

    context = {
        'form': form,
        'book': book,
        'profile': profile,
    }

    return render(request, 'edit-book.html', context)


def book_details_page(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()

    context = {
        'book': book,
        'profile': profile
    }

    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home page')



def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def profile_page(request):
    profile = get_profile()
    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'profile.html', context)


def edit_profile_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)

def delete_profile_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


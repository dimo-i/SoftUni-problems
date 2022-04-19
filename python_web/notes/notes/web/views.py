from django.shortcuts import render, redirect


# Create your views here.
from notes.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes.web.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)



def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateNoteForm()

    context = {
        'form': form
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)

def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)


def details_page(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def profile_page(request):
    profile = get_profile()
    note = Note.objects.all()
    all_notes = len(note)

    context = {
        'profile': profile,
        'all_notes': all_notes,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    profile.delete()
    Note.objects.all().delete()
    return redirect('show home')




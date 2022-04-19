import os

from django import forms

from online_library.web.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'image_url')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'image_url')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].disabled = True

    def save(self, commit=True):
        # image_path = self.instance.image.path
        if commit:
            self.instance.delete()
            Book.objects.all().delete()
        # os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')

        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type'
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')

        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type'
        }

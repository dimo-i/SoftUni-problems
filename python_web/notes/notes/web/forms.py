import os

from django import forms

from notes.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image_url')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Profile Image',
        }


# class DeleteProfileForm(forms.ModelForm):
#
#     def save(self, commit=True):
#         image_path = self.instance.image.path
#         self.instance.delete()
#         Note.objects.all().delete()
#         os.remove(image_path)
#         return self.instance
#
#     class Meta:
#         model = Profile
#         fields = ()


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')

        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image',
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
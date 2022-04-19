from django import forms

from music_app.web.models import Profile, Album


# TODO Create Placeholders form Profile and Album

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                }
            )
        }

        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age'
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),

            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            )
        }

        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')

        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class DeleteAlbumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')

        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price',
        }

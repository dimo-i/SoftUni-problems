from django import forms

from recipes.web.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')

        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time(Minutes)',
        }


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')



class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
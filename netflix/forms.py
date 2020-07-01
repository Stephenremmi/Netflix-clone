from django import forms
from .models import Film

class NetflixLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NetflixFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        exclude = ['director', 'rel_date']
        widgets = {
            'film_star': forms.CheckboxSelectMultiple(),
        }
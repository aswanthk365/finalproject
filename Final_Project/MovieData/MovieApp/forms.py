from django import forms
from . models import Movies


class DateInput(forms.DateInput):
    input_type = 'date'

class AddMoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['category','movie_tittle','movie_poster','movie_trailer','description','relese_date','actors']
        widgets = {
            'relese_date': DateInput(),
        }
        

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = ReviewRating
#         fields = ['subject','review','rating']
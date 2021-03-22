from django import forms
from .models import AddMovieModel

class MovieForm(forms.ModelForm):
    
    class Meta:
        model = AddMovieModel
        fields = ["m_name","m_kind","m_year","m_actors","m_rank","m_content","m_image"]


from django import forms
from django.forms import ModelForm
from .models import Author

class AuthorForm(ModelForm):
    date_created= forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model = Author
        fields = '__all__'
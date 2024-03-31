from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Books, Author


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Оберіть автора")

    # Додали валідатори для поля year
    year = forms.IntegerField(validators=[
        MinValueValidator(1000),  # Мінімальний рік
        MaxValueValidator(2024)  # Максимальний рік
    ])

    class Meta:
        model = Books
        fields = ['title', 'author', 'year']
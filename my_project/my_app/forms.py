from django import forms
from .models import AppReview, BookReview

class AppReviewForm(forms.Form):
    nickname = forms.CharField(label='Ник', max_length=50)
    email = forms.EmailField(label='Email')
    stars = forms.ChoiceField(
        label='Количество звёзд', 
        choices=[(str(i), f'{i} звезда') for i in range(1, 6)],
        widget=forms.Select
    )
    review = forms.CharField(
        label='Описание вашего опыта',
        widget=forms.Textarea,
        max_length=500
    )

    def clean_stars(self):
        stars = int(self.cleaned_data['stars'])
        if not (1 <= stars <= 5):
            raise forms.ValidationError("Количество звёзд должно быть от 1 до 5.")
        return stars
    
    # class Meta:
    #     model = AppReview
    #     fields = "__all__"

class BookReviewForm(forms.Form):
    nickname = forms.CharField(label='Ник', max_length=50)
    rating = forms.IntegerField(label='Ваш рейтинг книги', min_value=0, max_value=100)
    review = forms.CharField(label='Рецензия на книгу', widget=forms.Textarea)
    contains_spoilers = forms.BooleanField(label='Содержит спойлеры', required=False)

    # class Meta:
    #     model = BookReview
    #     fields = "__all__"

class PersonSearchForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=100)
    city = forms.CharField(label='Город', max_length=50)

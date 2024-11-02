from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class AppReview(models.Model):
    nickname = models.CharField("Ник", max_length=50)
    email = models.EmailField("Email")
    stars = models.IntegerField(
        "Количество звёзд",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField("Описание вашего опыта использования приложения", max_length=500)

    def __str__(self):
        return f"{self.nickname} - {self.stars} звёзд"
    
class BookReview(models.Model):
    nickname = models.CharField("Ник", max_length=50)
    rating = models.IntegerField(
        "Рейтинг книги",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Рейтинг от 0 до 100"
    )
    review = models.TextField("Рецензия на книгу", max_length=1000)
    contains_spoilers = models.BooleanField("Содержит спойлеры", default=False)

    def __str__(self):
        return f"{self.nickname} - {self.rating}/100"
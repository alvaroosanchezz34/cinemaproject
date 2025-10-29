from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError

# Clase Pelicula

class Movie(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=1000)
    genre = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField(validators=[MinValueValidator(1900, message="The year of release must not be earlier than 1900")])
    duration = models.IntegerField(
        validators=[
            MinValueValidator(1, message="The duration must be between 1 and 500 minutes"),
            MaxValueValidator(500, message="The duration must be between 1 and 500 minutes")
        ])
    release_date = models.DateField()
    announcement_date = models.DateField()
    has_subtitles = models.BooleanField()
    subtitles_language = models.CharField(max_length=50, blank=True)
    imdb = models.URLField(blank=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0.0, message="The average rating must be between 0,0 and 10,0"),
            MaxValueValidator(10.0, message="The average rating must be between 0,0 and 10,0")
        ],
    )
    def clean(self):
        super().clean()
        # Validar que la fecha de anuncio sea anterior a la fecha de estreno
        if self.announcement_date and self.release_date:
            if self.announcement_date >= self.release_date:
                raise ValidationError({
                    "announcement_date": "The announcement date must be before the release date"
                })
        # Validar idioma de subtítulos si has_subtitles es True
        if self.has_subtitles and not self.subtitles_language:
            raise ValidationError({
                "subtitles_language": "Please specify a language"
            })

    def __str__(self):
        return self.title
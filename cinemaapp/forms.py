from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        labels = {
            "title": "Title of the movie",
            "synopsis": "Short plot summary",
            "genre": "Movie genre",
            "director": "Director’s full name",
            "release_year": "Year of release",
            "duration": "Duration (in minutes)",
            "release_date": "Release date",
            "announcement_date": "Announcement date",
            "has_subtitles": "Has subtitles",
            "subtitles_language": "Subtitles language",
            "imdb": "IMDB URL",
            "rating": "Average rating (0-10)",
        }
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "announcement_date": forms.DateInput(attrs={"type": "date"}),
            "synopsis": forms.Textarea(attrs={"rows": 4}),
        }
        error_messages = {
            "title": {
                "required": "The title of the movie is required",
                "max_length": "The title of the movie must not be more than 100 characters long"
            },
            "genre": {
                "required": "The genre of the movie is required"
            },
            "release_date": {
                "required": "The releas date is required"
            },
        }
        def clean(self):
            cleaned_data = super().clean()
            announcement = cleaned_data.get("announcement_date")
            release = cleaned_data.get("release_date")
            has_subtitles = cleaned_data.get("has_subtitles")
            subtitles_language = cleaned_data.get("subtitles_language")

            if announcement and release and announcement >= release:
                self.add_error("announcement_date", "The announcement date must be before the release date")
            if has_subtitles and not subtitles_language:
                self.add_error("subtitles_language", "Please specify a language")

            return cleaned_data

import pytest
from datetime import datetime
from src.models import Movie
from src.exceptions import InvalidYearError, InvalidRatingError

class TestMovieModel:
    def test_valid_movie(self):
        movie = Movie(
            title="Inception",
            year=2010,
            director="Christopher Nolan",
            rating=8.8
        )
        assert movie.title == "Inception"

    def test_invalid_year(self):
        with pytest.raises(InvalidYearError):
            Movie(
                title="Old Movie",
                year=1800,
                director="Unknown",
                rating=5.0
            )

    def test_invalid_rating(self):
        with pytest.raises(InvalidRatingError):
            Movie(
                title="Bad Movie",
                year=2000,
                director="Unknown",
                rating=11.0
            )
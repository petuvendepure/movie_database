class MovieDatabaseError(Exception):
    """Base exception for all movie database errors"""
    pass

class InvalidYearError(MovieDatabaseError):
    def __init__(self, min_year: int, max_year: int):
        super().__init__(f"El año debe estar entre {min_year} y {max_year}")

class InvalidRatingError(MovieDatabaseError):
    def __init__(self):
        super().__init__("El rating debe estar entre 0 y 10")

class CountryNotFoundError(MovieDatabaseError):
    def __init__(self, country: str):
        super().__init__(f"País no encontrado: {country}")
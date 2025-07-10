from pathlib import Path

class Config:
    CSV_PATH = Path("data/movies_dataset.csv")
    COUNTRIES_CSV = Path("data/paises_mundo.csv")
    DEFAULT_RATING = 5.0
    MIN_YEAR = 1888
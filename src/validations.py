import pandas as pd
from src.config import Config
from src.exceptions import CountryNotFoundError

class Validations:
    def __init__(self):
        self.countries_df = self._load_countries()

    def _load_countries(self) -> pd.DataFrame:
        try:
            return pd.read_csv(Config.COUNTRIES_CSV)
        except FileNotFoundError:
            raise FileNotFoundError("Archivo de países no encontrado")

    def validate_country(self, country: str) -> bool:
        if country not in self.countries_df['nombre'].values:
            raise CountryNotFoundError(country)
        return True

    def validate_movie_data(self, data: dict) -> bool:
        # Puedes añadir validaciones adicionales aquí
        return True
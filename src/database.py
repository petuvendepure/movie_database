import pandas as pd
from pathlib import Path
from typing import Dict, List, Optional
from src.models import Movie
from src.config import Config
from src.exceptions import MovieDatabaseError
import logging

logger = logging.getLogger(__name__)

class MovieDatabase:
    def __init__(self):
        self.df = self._load_or_create_db()
        
    def _load_or_create_db(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(Config.CSV_PATH)
            if df.empty:
                return self._create_empty_df()
            return df
        except FileNotFoundError:
            logger.info("Creando nueva base de datos")
            return self._create_empty_df()
        except Exception as e:
            raise MovieDatabaseError(f"Error cargando base de datos: {str(e)}")

    def _create_empty_df(self) -> pd.DataFrame:
        return pd.DataFrame(columns=[f.title for f in Movie.model_fields.values()])

    def save(self) -> None:
        try:
            Config.CSV_PATH.parent.mkdir(exist_ok=True)
            self.df.to_csv(Config.CSV_PATH, index=False)
        except Exception as e:
            raise MovieDatabaseError(f"Error guardando base de datos: {str(e)}")

    def add_movie(self, movie_data: Dict) -> int:
        next_id = self._get_next_id()
        movie = Movie(**{**movie_data, 'id': next_id})
        
        new_row = pd.DataFrame([movie.model_dump()])
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        
        logger.info(f"Película agregada con ID: {next_id}")
        return next_id

    def _get_next_id(self) -> int:
        if self.df.empty or 'id' not in self.df.columns:
            return 1
        return self.df['id'].max() + 1

    def filter_movies(self, **filters) -> pd.DataFrame:
        filtered = self.df.copy()
        for key, value in filters.items():
            if value is not None and key in filtered.columns:
                if isinstance(value, str):
                    filtered = filtered[filtered[key].str.lower().str.contains(value.lower())]
                else:
                    filtered = filtered[filtered[key] == value]
        return filtered
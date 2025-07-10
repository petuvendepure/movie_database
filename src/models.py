from pydantic import BaseModel, field_validator, Field
from typing import Optional
from datetime import datetime
from src.config import Config
from src.exceptions import InvalidYearError, InvalidRatingError

class Movie(BaseModel):
    """Modelo que representa una película en la base de datos."""
    id: int = Field(default=0, description="ID único secuencial")
    title: str = Field(..., min_length=1, max_length=200)
    year: int = Field(..., gt=Config.MIN_YEAR)
    director: str = Field(..., min_length=3, max_length=100)
    genre: Optional[str] = Field(default="Desconocido", max_length=50)
    rating: Optional[float] = Field(default=Config.DEFAULT_RATING, ge=0, le=10)
    duration: Optional[int] = Field(default=90, gt=0)
    country: Optional[str] = Field(default="Desconocido", max_length=50)
    language: Optional[str] = Field(default="Inglés", max_length=30)
    oscar_nominations: Optional[int] = Field(default=0, ge=0)

    @field_validator('year')
    def validate_year(cls, v):
        current_year = datetime.now().year
        if v < Config.MIN_YEAR or v > current_year + 2:
            raise InvalidYearError(min_year=Config.MIN_YEAR, max_year=current_year + 2)
        return v
    
    @field_validator('rating')
    def validate_rating(cls, v):
        if v is not None and (v < 0 or v > 10):
            raise InvalidRatingError()
        return v
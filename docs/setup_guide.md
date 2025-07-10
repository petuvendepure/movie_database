# Guía de Configuración Detallada

## Requisitos del Sistema

- Python 3.9+
- 100MB de espacio libre
- Permisos de escritura en el directorio de datos

## Configuración Inicial

1. Copiar archivos de datos a la ubicación correcta:
```bash
mkdir -p data
cp /ruta/a/tus/datos/*.csv data/
```

2. Configurar variables de entorno:
```ini
# .env
DATA_PATH=./data
DEFAULT_LANGUAGE=Español
```

3. Inicializar base de datos:
```python
from src.database import MovieDatabase
db = MovieDatabase()
db.initialize_sample_data()
```
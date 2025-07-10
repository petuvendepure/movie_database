# 🎬 Sistema de Gestión de Películas [![PyPI Version](https://img.shields.io/pypi/v/movie-database)]

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


Un sistema completo para gestionar tu colección de películas con validación de datos y búsqueda avanzada.

## 📋 Tabla de Contenidos
- [Características](#-características)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Configuración](#-configuración)
- [Pruebas](#-pruebas)
- [Contribución](#-contribución)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

## ✨ Características

- ✅ Añadir películas con validación automática
- 🔍 Búsqueda avanzada por múltiples criterios
- 📊 Visualización tabular de resultados
- 🌎 Validación de países
- 💾 Persistencia de datos en CSV
- 🛠️ Interfaz de línea de comandos intuitiva

## 🛠️ Instalación

### Requisitos
- Python 3.9 o superior
- Pip para gestión de paquetesf

### Pasos
1. Clonar el repositorio:

```bash

git clone https://github.com/petuniavendepure/movie_database.git
cd movie_database

```
2. Crear entorno Virtual(Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
## 🚀 Uso
```bash
python -m src.cli
```
## 📚 Estructura del Proyecto
```bash
movie_database/
│
├── src/                          # Código fuente principal
│   ├── __init__.py               # Hace que src sea un paquete Python
│   ├── cli.py                    # Interfaz de línea de comandos principal
│   ├── database.py               # Lógica de base de datos
│   ├── models.py                 # Modelos Pydantic
│   ├── validations.py            # Validaciones de datos
│   └── exceptions.py             # Excepciones personalizadas
│
├── data/                         # Datos de la aplicación
│   ├── movies_dataset.csv        # Dataset inicial de películas
│   └── paises_mundo.csv          # Lista de países válidos
│
├── tests/                        # Pruebas unitarias
│   ├── __init__.py
│   ├── test_models.py
│   └── test_database.py
│
├── docs/                         # Documentación adicional
│   ├── setup_guide.md            # Guía de instalación
│   └── api_reference.md          # Referencia de API
│
├── .gitignore                    # Archivos a ignorar en Git
├── README.md                     # Documentación principal
├── requirements.txt              # Dependencias requeridas
├── pyproject.toml                # Configuración del proyecto
└── setup.py                      # Configuración de paquete (opcional)
```
## ⚙️ Configuración

El sistema se configura mediante `src/config.py`:

```python
# Rutas de archivos
CSV_PATH = "data/movies_dataset.csv"  # Ubicación del archivo CSV principal
COUNTRIES_CSV = "data/paises_mundo.csv"  # Archivo de países válidos

# Valores por defecto
DEFAULT_RATING = 5.0  # Puntuación predeterminada para nuevas películas
MIN_YEAR = 1888  # Año mínimo permitido
```
## 🧪 Ejecución de Pruebas
1. Ejecutar el suite de pruebas:
```bash
pytest tests/
```
2. Para pruebas específicas
```bash
pytest tests/test_models.py -v  # Pruebas de modelos
pytest tests/test_database.py   # Pruebas de base de datos
```
## 🤝 Contribución
1. Haz fork del proyecto
2. Crea tu rama (git checkout -b feature/nueva-funcionalidad)
3. Haz commit de tus cambios (git commit -m 'Añade nueva funcionalidad')
4. Haz push a la rama (git push origin feature/nueva-funcionalidad)
5. Abre un Pull Request

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

## 📬 Contacto
* Autor : Saúl Figueroa Alonso
* Email : petuniavendepure@gmail.com
* GitHub : petuvendepure


from tabulate import tabulate
from src.database import MovieDatabase
from src.validations import Validations
from src.exceptions import MovieDatabaseError
import logging

logger = logging.getLogger(__name__)

class MovieCLI:
    def __init__(self):
        self.db = MovieDatabase()
        self.validator = Validations()

    def run(self):
        print("¡Bienvenido al Sistema de Películas!")
        while True:
            self._display_menu()
            choice = input("\nSeleccione una opción: ").lower()
            
            try:
                if choice in ('a', '1'):
                    self._add_movie_flow()
                elif choice in ('l', '2'):
                    self._list_movies()
                elif choice in ('f', '3'):
                    self._filter_movies_flow()
                elif choice in ('q', '4'):
                    self._exit_flow()
                    break
                else:
                    print("Opción inválida, intente nuevamente")
            except MovieDatabaseError as e:
                logger.error(f"Error: {str(e)}")
                print(f"\nError: {str(e)}")

    def _display_menu(self):
        print("\n--- Movie Database ---")
        print("1. (a) Agregar película")
        print("2. (l) Listar películas")
        print("3. (f) Buscar películas")
        print("4. (q) Salir")

    def _add_movie_flow(self):
        print("\n--- Agregar Nueva Película ---")
        movie_data = {
            'title': input("Título: "),
            'year': int(input("Año: ")),
            'director': input("Director: "),
            'genre': input("Género (opcional): ") or None,
            'rating': float(input("Rating (0-10): ")),
            'duration': int(input("Duración (minutos): ")),
            'country': input("País: "),
            'language': input("Idioma: "),
            'oscar_nominations': int(input("Nominaciones a Oscar: "))
        }
        
        self.validator.validate_country(movie_data['country'])
        movie_id = self.db.add_movie(movie_data)
        self.db.save()
        print(f"\nPelícula agregada exitosamente con ID: {movie_id}")

    def _list_movies(self):
        print("\n--- Todas las Películas ---")
        if self.db.df.empty:
            print("No hay películas en la base de datos.")
            return
        
        print(tabulate(self.db.df, headers='keys', tablefmt='grid', showindex=False))
        print(f"\nTotal: {len(self.db.df)} películas")

    def _filter_movies_flow(self):
        print("\n--- Buscar Películas ---")
        filters = {}
        if input("¿Buscar por título? (s/n): ").lower() == 's':
            filters['title'] = input("Título: ")
        # Añadir más filtros según necesidad...
        
        filtered = self.db.filter_movies(**filters)
        self._display_results(filtered)

    def _display_results(self, df):
        if df.empty:
            print("\nNo se encontraron películas con esos criterios")
        else:
            print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
            print(f"\nEncontradas: {len(df)} películas")

    def _exit_flow(self):
        self.db.save()
        print("\nSaliendo del sistema... ¡Hasta pronto!")
if __name__ == "__main__":
 # Configura logging básico
    logging.basicConfig(level=logging.INFO)
    
    # Crea y ejecuta la aplicación
    app = MovieCLI()
    app.run()
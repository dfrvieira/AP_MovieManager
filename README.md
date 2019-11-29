# Movie Manager

## Estrutura dos dicionários

        director = {
            'name': String
        }

        actor = {
            'name': String
        }

        movie = {
            'title': String,
            'genre': String,
            'rating': float,
            'description': String,
            'director': director,
            'actors': [actor]
        }

        movie_manager = {
            'directors': [director],
            'actors': [actor],
            'movies': [movies]
        }

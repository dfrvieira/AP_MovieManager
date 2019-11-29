# Movie Manager

## Estrutura dos dicionários
realizador = {
    'nome': String
}

ator = {
    'nome': String
}

filme = {
    'titulo': String,
    'genero': String,
    'rating': float,
    'sinopse': String,
    'realizador': realizador,
    'atores': [ator]
}

movie_manager = {
    'directors': [realizador],
    'atores': [ator],
    'filmes': [filmes]
}

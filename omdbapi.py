import requests as rq

diccionario_index = {
    "Asignatura" : "Informática",
    "Universidad" : "UCEMA",
    "Año lectivo" : 2022,
    "Grupo" : 1,
    "Integrantes" : [
        "Agustina","Pilar","Morena","Delfina"
    ],
    "api consultada" : "The Movie DB",
    "documentación de la api": "https://developers.themoviedb.org/3/getting-started/introduction",
    "endpoints de la api de terceros" : {
        "lista de peliculas" : "localhost:4000/movies/",
        "lista de programas de televisión" : "localhost:4000/tvshows/",
        "lista de generos de peliculas" : "localhost:4000/genres/movie",
        "lista de generos de programas de televisión" : "localhost:4000/genres/tv",
        "lista de peliculas según palabra buscada" : "localhost:4000/movie/<<movie_name>>",
        "lista de programa de televisión según palabra buscada" : "localhost:4000/tv/<<tvshow_name>>",
        "descripción api" : "localhost:4000/",
    },
}
  
class thirdPartyAPI():

    def __init__(self,apiKey):
        self.apiKey = apiKey

    def index(self):
        return diccionario_index

    def getMovies(self):
        return rq.get("https://api.themoviedb.org/3/movie/top_rated?api_key="+self.apiKey+"&language=es-AR&page=1").json()

    def getTVShows(self):
        return rq.get("https://api.themoviedb.org/3/tv/popular?api_key="+self.apiKey+"&language=es-AR&page=1").json()

    def getGenres(self,movie_or_tvshow):
        return rq.get("https://api.themoviedb.org/3/genre/"+movie_or_tvshow+"/list?api_key="+self.apiKey+"&language=es-AR").json()
        
    def getMovie(self,movie_name):
        return rq.get("https://api.themoviedb.org/3/search/movie?api_key="+self.apiKey+"&language=es-AR&query="+movie_name+"&page=1").json()

    def getTVShow(self,tvshow_name):
        return rq.get("https://api.themoviedb.org/3/search/tv?api_key="+self.apiKey+"&language=es-AR&query="+tvshow_name+"&page=1").json()

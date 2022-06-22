import requests as rq

class ThirdPartyAPI:

    def __init__(self,apiKey):
        self.apiKey = apiKey

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

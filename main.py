from flask import Flask, jsonify, request
from omdbapi import thirdPartyAPI
from mydb import ownapi as mydb

app = Flask(__name__)

# # Rutas de consultas a la API de terceros TheMovieDB

apiKey = ""

@app.route('/', methods=['GET'])
def index():
    dicc = {
        "terceros" : thirdPartyAPI(apiKey).index(),
        "propio" : {
            "endpoints" : {
                "localhost:4000/create-user" : "create-user (POST)",
                "localhost:4000/users" : "get-users (GET)",
                "localhost:4000/user/<<user_name>>" : "get-user-by-name (GET)",
                "localhost:4000/user/<<user_id>>" : "get-user-by-id (GET)",
                "localhost:4000/edit-user/<<user_id>>/<<user_name>>" : "update-user (PUT)",
                "localhost:4000/delete-user/<<user_id>>" : "delete-user (DELETE)",
            }
        }
    }
    return jsonify(dicc)

@app.route('/movies/', methods=['GET'])
def getMovies():
    return jsonify(thirdPartyAPI(apiKey).getMovies())

@app.route('/tvshows/', methods=['GET'])
def getTVShows():
    return jsonify(thirdPartyAPI(apiKey).getTVShows())

@app.route('/genres/<string:genre_type>', methods=['GET'])
def getGenresMovie(genre_type:str="movie"):
    return jsonify(thirdPartyAPI(apiKey).getGenres(genre_type))

@app.route('/movie/<string:movie_name>', methods=['GET'])
def getMovie(movie_name):
    return jsonify(thirdPartyAPI(apiKey).getMovie(movie_name))

@app.route('/tvshow/<string:tvshow_name>', methods=['GET'])
def getTVShow(tvshow_name):
    return jsonify(thirdPartyAPI(apiKey).getTVShow(tvshow_name))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Rutas API propia
@app.route('/create-user', methods=['POST'])
def createUser():
    return jsonify(mydb.create_user(request.json['nombre']))

@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify(mydb.get_users())

@app.route('/user/name/<string:user_name>', methods=['GET'])
def getUserByName(user_name):
    return jsonify(mydb.get_users_by_name(user_name))

@app.route('/user/id/<string:user_id>', methods=['GET'])
def getUserByID(user_id):
    return jsonify(mydb.get_user_by_id(user_id))

@app.route('/edit-user/<string:user_id>/<string:user_name>', methods=['PUT'])
def editUser(user_id,user_name):
    return jsonify(mydb.update_user(user_id,user_name))

@app.route('/delete-user/<string:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    return jsonify(mydb.delete_user(user_id))

if __name__ == "__main__":
    app.run(debug = True, port = 4000)
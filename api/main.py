from flask import Flask, Response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#   Read env variables from config.py
# app.config.from_object('config.Config')

#   Testing if it worked
@app.route('/test')
def index():
    movies = []
    movie = dict()
    movie['id'] = 657
    movie['genres'] =[ "Action","Adventure","Thriller"]
    movie["overview"] ="Agent 007 is back in the second installment of the James Bond series, this time battling a secret crime organization known as SPECTRE. Russians Rosa Klebb and Kronsteen are out to snatch a decoding device known as the Lektor, using the ravishing Tatiana to lure Bond into helping them. Bond willingly travels to meet Tatiana in Istanbul, where he must rely on his wits to escape with his life in a series of deadly encounters with the enemy"
    movie["release_year"] = 1963
    movie["popularity"] = 7.1
    movie["title"] = "From Russia with Love"
    movie["is_movie"] = True
    movie["poster_path"] = "https://image.tmdb.org/t/p/w500/xTle7ThbHKQgQYKcyKZ02gfSYIe.jpg"
    movie1 = dict()
    movie1['genres'] =[ "Action","Adventure","Drama", "Adventure"]
    movie1['id'] = 967
    movie1["overview"] = "The rebellious Thracian Spartacus, born and raised a slave, is sold to Gladiator trainer Batiatus. After weeks of being trained to kill for the arena, Spartacus turns on his owners and leads the other slaves in rebellion. As the rebels move from town to town, their numbers swell as escaped slaves join their ranks. Under the leadership of Spartacus, they make their way to southern Italy, where they will cross the sea and return to their homes."
    movie1["release_year"] = 1960
    movie1["popularity"] = 7.5
    movie1["title"] = "Spartacus"
    movie1["is_movie"] = True
    movie1["poster_path"] = "https://image.tmdb.org/t/p/w500/iWZ6NcDJOBNJ0YycZ0CLC6TMQcg.jpg"
    movies.append(movie)
    movies.append(movie1)
    return jsonify(movies)
app.run()

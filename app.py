from flask import Flask, render_template, redirect, url_for, flash
import os

app = Flask(__name__)
app.debug = True
movie_names = ["Inception", "Real Steel", "The Godfather", "The Martian", "The Nun"]
movie_list = os.listdir('./static/movies')
movie_mapping = {i: j for i, j in zip(movie_names, movie_list)}
posters = os.listdir('./static/posters')


@app.route('/', methods=['POST', 'GET'])
def hello():
    return render_template('index.html', movie_mapping=movie_mapping, posters=posters, zip=zip)


@app.route('/stream/<id>', methods=['POST', 'GET'])
def stream(id):
    id = '/static/movies/{}'.format(id)
    return render_template('stream_movie.html', link=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

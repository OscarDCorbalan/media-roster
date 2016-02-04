import data
from media import Video, Movie, TvShow, Book
from pymongo import MongoClient


client = MongoClient("mongodb://HIDDEN:HIDDEN@ds055505.mongolab.com:55505/fswd_media")
db = client.fswd_media

col_movies = db.movies
col_tvshows = db.tvshows
col_books = db.books

col_movies.remove()
col_tvshows.remove()
col_books.remove()

for media in data.getMedia() :
    if isinstance(media, Movie):
        print "Inserting Movie:", media.title
        col_movies.insert_one({
            "title": media.title,
            "storyline": media.description,
            "genre": media.genre,
            "poster": media.image,
            "trailer": media.preview,
            "rating": media.rating,
            "duration": media.duration,
            "release_date": media.release_date,
            "director": media.director,
            "cast": media.cast
        })
    elif isinstance(media, TvShow):
        print "Inserting TvShow:", media.title
        col_tvshows.insert_one({
            "title": media.title,
            "storyline": media.description,
            "genre": media.genre,
            "poster": media.image,
            "trailer": media.preview,
            "rating": media.rating,
            "duration": media.duration,
            "seasons": media.seasons,
            "episodes": media.episodes,
            "channel": media.channel
        })
    elif isinstance(media, Book):
        print "Inserting Book:", media.title
        col_books.insert_one({
            "title": media.title,
            "storyline": media.description,
            "genre": media.genre,
            "image": media.image,
            "rating": media.rating,
            "author": media.author,
            "year": media.year,
            "preview": media.preview,
            "pages": media.pages,
            "editor": media.editor,
            "isbn": media.isbn
        })

client.close()
print "Finished"

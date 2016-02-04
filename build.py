# This simple script first retrieves a list of our favourite medias from
# a MongoDB database we called 'fswd_media'

import data
import web
import media
from pymongo import MongoClient

# First connect to our database and retrieve the db object
client = MongoClient("mongodb://fswd_media_user:readonly@ds055505.mongolab.com:55505/fswd_media")
db = client.fswd_media


# Then create an empty list where we'll put our medias...
list_medias = []

# ...and a Media factory
factory = media.Factory()


# Now query the database collections and instantiate an object from every
# document retrieved
for doc in db.movies.find():
    list_medias.append( factory.create(media.Movie, doc) )

for doc in db.tvshows.find():
    list_medias.append( factory.create(media.TvShow, doc) )

for doc in db.books.find():
    list_medias.append( factory.create(media.Book, doc) )


# Make sure to close the MongoDB connection once we're finished with it
client.close()


# To finish, just pass the media list to the function that will build the html
web.open_media_page(list_medias)

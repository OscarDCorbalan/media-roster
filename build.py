import data
import web

# This simple script first retrieves a list with all our Media instances created in data.py...
media = data.getMedia()
# ... and then passes it to this function found in web.py
web.open_media_page(media)

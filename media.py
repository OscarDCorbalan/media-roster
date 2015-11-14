import webbrowser

class Media():
    def __init__(self, title, description, genre, image):
        self.title = title
        self.description  = description
        self.genre = genre
        self.image = image
        self.rating = "N/A"

class Video(Media):
    """This class stores information related to audiovisual media (movies, tv shows...)"""
    _VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

    def __init__(self, video_title, video_description, video_genre, video_image, video_preview, video_rating, video_duration=None):
        Media.__init__(self, video_title, video_description, video_genre, video_image)
        # Duration is a property of audiovisual media
        self.duration = video_duration
        self.preview = video_preview
        if video_rating in self._VALID_RATINGS:
            self.rating = video_rating
        else:
            self.rating = "N/A"

class Movie(Video):
    """This class stores information related to movies"""
    def __init__(self, movie_title, movie_storyline, movie_genre, movie_poster, movie_trailer, movie_rating, movie_duration, movie_release_date, movie_director, movie_cast):
        Video.__init__(self, movie_title, movie_storyline, movie_genre, movie_poster, movie_trailer, movie_rating, movie_duration)
        self.type = "Movie"
        self.release_date = movie_release_date
        self.director = movie_director
        self.cast = movie_cast

class TvShow(Video):
    """This class stores information related to TV shows"""
    def __init__(self, show_title, show_description, show_genre, show_poster, show_trailer, show_rating, show_duration, show_seasons, show_episodes, show_channel):
        Video.__init__(self, show_title, show_description, show_genre, show_poster, show_trailer, show_rating, show_duration )
        self.seasons = show_seasons
        self.episodes = show_episodes
        self.channel = show_channel
        self.type = "TV Show"

class Book(Media):
    """This class stores information related to Books"""
    def __init__(self, book_title, book_description, book_genre, book_cover, book_author, book_year, book_pages, book_editor, book_isbn):
        Media.__init__(self, book_title, book_description, book_genre, book_cover)
        self.type = "Book"
        self.author = book_author
        self.year = book_year
        self.preview = book_cover
        self.pages = book_pages
        self.editor = book_editor
        self.isbn = book_isbn

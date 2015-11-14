import webbrowser

class Media():
    _VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]
    def __init__(self, title, description, genre, image, rating):
        self.title = title
        self.description  = description
        self.genre = genre
        self.image = image
        if rating in self._VALID_RATINGS:
            self.rating = rating
        else:
            self.rating = "N/A"

class Video(Media):
    """This class stores information related to audiovisual media (movies, tv shows...)"""
    def __init__(self, video_title, video_description, video_genre, video_image, video_preview, video_rating, video_duration=None):
        Media.__init__(self, video_title, video_description, video_genre, video_image, video_rating)
        # Duration is a property of audiovisual media
        self.duration = video_duration
        self.preview = video_preview

class Movie(Video):
    """This class stores information related to movies"""
    def __init__(self, movie_title, movie_storyline, movie_genre, movie_poster, movie_trailer, movie_rating, movie_duration, movie_release_date, movie_director):
        Video.__init__(self, movie_title, movie_storyline, movie_genre, movie_poster, movie_trailer, movie_rating, movie_duration)
        self.type = "Movie"
        self.release_date = movie_release_date
        self.director = movie_director

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
    def __init__(self, book_title, book_description, book_genre, book_cover):
        Media.__init(self, book_title, book_description, book_genre, book_cover)

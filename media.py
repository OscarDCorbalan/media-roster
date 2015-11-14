import webbrowser

class Media():
    """This class represents a generic Media object. It's meant to be subclassed anad there should be no reason to create an instance of it.

    Attributes:
        title: (String) title or name of this media.
        description: (String) synopsis or description of this media.
        genre: (List<String>) genre or genres that apply to this media.
        image: (String) url with an image of this media. Optimum size for correct rezising is 430x630 pixels.
        rating: (String) always null. Subclasses should implement ratings according to their used classification.
    """

    def __init__(self, title, description, genre, image):
        """Inits Media with the parameters passed and a null rating."""
        self.title = title
        self.description  = description
        self.genre = genre
        self.image = image
        self.rating = None

class Video(Media):
    """This class inerhits from Media and represents an audiovisual media (movies, tv shows...).

    Attributes:
        video_title: (String) title of this video.
        video_description: (String) synopsis or description of this video.
        video_genre: (List<String>) genre or genres that apply to this video.
        video_image: (String) url with an image of this video. Optimum size for correct rezising is 430x630 pixels.
        video_preview: (String) Youtube url of the video or a preview of it.
        video_rating: (String) rating of the Motion Picture Association. See _VALID_RATINGS for valid values.
        video_duration: (Number) duration in minutes of the video.
    """

    _VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

    def __init__(self, video_title, video_description, video_genre, video_image, video_preview, video_rating, video_duration):
        """Inits Video with the parameters passed. If rating is not in _VALID_RATINGS, sets it to null."""
        Media.__init__(self, video_title, video_description, video_genre, video_image)
        self.duration = video_duration
        self.preview = video_preview
        if video_rating in self._VALID_RATINGS:
            self.rating = video_rating
        else:
            self.rating = None

class Movie(Video):
    """This class inerhits from Video and represents a movie.

    Attributes:
        movie_title: (String) movie title.
        movie_storyline: (String) synopsis of the movie.
        movie_genre: (List<String>) genre or genres that apply to this movie.
        movie_poster: (String) url with an image of the movie's poster. Optimum size for correct rezising is 430x630 pixels.
        movie_trailer: (String) Youtube url with a trailer of the movie, or the full movie if it's free.
        movie_rating: (String) rating of the Motion Picture Association. See Video._VALID_RATINGS for valid values.
        movie_duration: (Number) duration in minutes of the movie.
        movie_release_date: (String) release date of the movie.
        movie_director: (String) name of the director.
        movie_cast: (List<String>) list with the names of the cast.
    """

    def __init__(self, movie_title, movie_storyline, movie_genre, movie_poster, movie_trailer, movie_rating, movie_duration, movie_release_date, movie_director, movie_cast):
        """Inits a Movie instance with the parameters passed. """
        Video.__init__(self, movie_title, movie_storyline, movie_genre, movie_poster, movie_trailer, movie_rating, movie_duration)
        self.type = "Movie"
        self.release_date = movie_release_date
        self.director = movie_director
        self.cast = movie_cast

class TvShow(Video):
    """This class inerhits from Video and represents an episodic TV show or TV series.

    Attributes:
        show_title: (String) TV show name.
        show_description: (String) description or synposis.
        show_genre: (List<String>) genre or genres that apply.
        show_poster: (String) url with an image of the show's poster. Optimum size for correct rezising is 430x630 pixels.
        show_trailer: (String) Youtube url with a trailer of the movie, or the full movie if it's free.
        show_rating: (String) rating of the Motion Picture Association. See Video._VALID_RATINGS for valid values.
        show_duration: (Number) duration in minutes of an episode.
        show_seasons: (Number) total number of seasons of the TV show.
        show_episodes: (String) total number of episodes, accounting all seasons.
        show_channel: (String) name of the channel that originally aired the show.
    """

    def __init__(self, show_title, show_description, show_genre, show_poster, show_trailer, show_rating, show_duration, show_seasons, show_episodes, show_channel):
        """Inits a Movie instance with the parameters passed. """
        Video.__init__(self, show_title, show_description, show_genre, show_poster, show_trailer, show_rating, show_duration )
        self.seasons = show_seasons
        self.episodes = show_episodes
        self.channel = show_channel
        self.type = "TV Show"

class Book(Media):
    """This class inerhits from Media and represents a book.

    Attributes:
        book_title: (String) book title.
        book_description: (String) description or synposis.
        book_genre: (List<String>) genre or genres that apply.
        book_cover: (String) url with an image of the book's cover. Optimum size for correct rezising is 430x630 pixels.
        book_author: (String) name of the book's author.
        book_editor: (String) editor that originally published the book.
        book_year: (Number) year of the original edition.
        book_pages: (Number) number of pages of the original edition
        book_isbn: (String) ISBN of the book.
    """

    def __init__(self, book_title, book_description, book_genre, book_cover, book_author, book_editor, book_year, book_pages, book_isbn):
        """Inits a Book instance with the parameters passed. """
        Media.__init__(self, book_title, book_description, book_genre, book_cover)
        self.type = "Book"
        self.author = book_author
        self.year = book_year
        self.preview = book_cover
        self.pages = book_pages
        self.editor = book_editor
        self.isbn = book_isbn

import webbrowser

class Video():
    """This class stores information related to audiovisual media (movies, tv shows...)"""

    _VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, video_title, video_preview, video_duration=None):
        self.title = video_title
        self.self_duration = video_duration
        self.preview = video_preview

class Movie(Video):
    """This class stores information related to movies"""

    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_trailer_youtube_url, movie_duration=None):
        Video.__init__(self, movie_title, movie_trailer_youtube_url, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url

class TvShow(Video):
    """This class stores information related to TV shows"""
    def __init__(self, show_title, _duration, tvShow_season, tvShow_season_episode, show_tv_station):
        Video.__init(show_title, show_duration)
        self.season = show_season
        self.episode = show.episode
        self.tv_station = show_tv_station

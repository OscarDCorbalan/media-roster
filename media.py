import webbrowser

class Video():
    """This class stores information related to video media"""
    _VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init(self, video_title, video_duration):
        self.title = video_title
        self.self_duration = video_duration

class Movie():
    """This class stores information related to movies"""

    #def __init__(self, movie_title, movie_duration, movie_trailer_youtube_url, movie_storyline, movie_poster_image_url):
    def __init__(self, movie_title, movie_trailer_youtube_url, movie_storyline, movie_poster_image_url):
        #Parent.__init(movie_title, movie_duration, movie_trailer_youtube_url)

        self.title = movie_title

        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

class TvShow(Video):
    """This class stores information related to TV shows"""
    def __init(self, show_title, _duration, tvShow_season, tvShow_season_episode, show_tv_station):
        Parent.__init(show_title, show_duration)
        self.season = show_season
        self.episode = show.episode
        self.tv_station = show_tv_station

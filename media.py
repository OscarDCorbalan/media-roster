import webbrowser

class Media():
    _VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title, description, image):
        self.title = title
        self.description  = description
        self.image = image

class Video(Media):
    """This class stores information related to audiovisual media (movies, tv shows...)"""
    def __init__(self, video_title, video_description, video_image, video_preview, video_duration=None):
        Media.__init__(self, video_title, video_description, video_image)
        # Duration is a property of audiovisual media
        self.duration = video_duration
        self.preview = video_preview

class Movie(Video):
    """This class stores information related to movies"""
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer_youtube_url, movie_duration=None):
        Video.__init__(self, movie_title, movie_storyline, movie_poster, movie_trailer_youtube_url, movie_duration)

class TvShow(Video):
    """This class stores information related to TV shows"""
    def __init__(self, show_title, show_description, show_duration, show_season, show_season_episode, show_tv_station):
        Video.__init(self, show_title, show_description, show_duration)
        self.season = show_season
        self.episode = show.episode
        self.tv_station = show_tv_station

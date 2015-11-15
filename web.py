import webbrowser
import os
import re
from media import Video, Movie, TvShow, Book

# There are two sections in this script. 1st we have the variables that contain
# html and {tags}, that are formated with the functions in the 2nd section.

# Page header. Contains references to scripts and stylesheets used.
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My media collection</title>

    <!-- Stylesheets -->
    <link rel="stylesheet"
    href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">

    <!-- Javascripts -->
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script
    src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js">
    </script>
    <script src="js/interactions.js" async></script>

    <! Favicon. The conditional 'if IE' is for on older IE versions. -->
    <!--[if IE]><link rel="shortcut icon" href="img/favicon.png"><![endif]-->
    <link rel=icon href="img/favicon.png" sizes="16x16" type="image/png">
</head>
'''

# The main page layout and title bar
# In the #lightsoff modal, we have two inner hidden divs and we display one or
# the another (via JS) depending on the element to be shown:
#   the #trailer-video-container is used to show youtube videos,
#   the #media-extended-container" is used to show texts and images.
# In {media_tiles} goes the content generated using media_tile_content
main_page_content = '''
    <body>
        <div class="modal" id="lightsoff">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close"
                    data-dismiss="modal" aria-hidden="true">
                        <img src="img/cross.png"/>
                    </a>
                    <div id="trailer-video-container"
                    class="scale-media display-none"></div>
                    <div id="media-extended-container"
                    class="scale-media display-none"></div>
                </div>
            </div>
        </div>

        <!-- Main Page Content -->
        <div class="container">
            <div class="navbar navbar-inverse navbar-fixed-top"
            role="navigation">
                <div class="container">
                    <div class="navbar-header">
                        <a id="navbar-title" class="navbar-brand" href="#">
                            <img src="img/favicon.png"/>
                            My media collection: movies, tv shows, books...
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
            {media_tiles}
        </div>
    </body>
</html>
'''

# A single media entry html template composed of various elements. Note we use
# bootstrap (col-xx-y) to have responsive tiles. What's everything:
# -The span around the image is used to show a tooltip when hovering
#  an image .Clicking on the image to open it full-size in a modal.
#  The reason of using a span around the img is because we can't have two
#  'data-toggle' (tooltip and modal) attributes in the same element.
# -The .media info contains the basic information of the Media: title, type,
#  genre and a '+' icon to show more information and if there's a youtube
#  a movie icon that opens the trailer when clicked.
# -The {media_rating} shows the rating in a corner of the tile.
# -The last .media-info-extended div contains hidden html that is shown in a
#  modal when clicking the '+' icon.
media_tile_content = '''
<article class="col-lg-4 col-md-6 col-sm-12 col-xs-12 media-tile">
    <div class="media-wrapper">
        <span class="pull-left" title="Augment"
        data-toggle="tooltip" data-placement="bottom">
            <img class="media-image pointer" src="img/media/{media_image}"
            data-target="#lightsoff" data-toggle="modal"/>
        </span>
        <div class="media-info">
            <h3>{media_title}</h3>
            <p><strong>Type</strong>: {media_type}<br/>
            <strong>Genre</strong>: {media_genre}</p>
            <span data-toggle="tooltip" data-placement="top" title="View more">
                <span class="glyphicon glyphicon-plus-sign pointer"
                aria-hidden="true" data-target="#lightsoff" data-toggle="modal">
                </span>
            </span>
            {media_preview}
        </div>
        {media_rating}
        <div class="media-info-extended display-none">
            <img class="media-image pull-left" src="img/media/{media_image}">
            <p>{media_description}</p>
            {media_tile_extended}
        </div>
    </div>
</article>
'''

# This is the code that puts the rating over a colored background in a
# corner of the media box
media_rating_div = '''
<div class="media-rating-background">
    <span class="media-rating text-center">{media_rating}</span>
</div>
'''

# Movie icon that when clicked shows the trailer.
media_preview_span = '''
    <span data-toggle="tooltip" data-placement="top" title="View preview">
        <span class="glyphicon glyphicon-film pointer" aria-hidden="true"
        data-trailer-youtube-id={media_preview} data-toggle="modal"
        data-target="#lightsoff"></span>
    </span>
'''

# Info of a Movie.
media_extended_movie = '''
    <p><strong>Release</strong>: {movie_release}.<br/>
    <strong>Director</strong>: {movie_director}.<br/>
    <strong>Duration</strong>: {movie_duration} minutes.<br/>
    <strong>Cast</strong>: {movie_cast}.</p>
'''

# Info of a TV show.
media_extended_tvshow = '''
    <p><strong>Channel</strong>: {show_channel}.<br/>
    <strong>Seasons</strong>: {show_seasons}.<br/>
    <strong>Episodes</strong>: {show_episodes}.<br/>
    <strong>Avg. duration</strong>: {show_duration} minutes.</p>
'''

# Info of a Book.
media_extended_book = '''
    <p><strong>Author</strong>: {book_author}.<br/>
    <strong>Published</strong>: {book_year}.<br/>
    <strong>Editor</strong>: {book_editor}.<br/>
    <strong>Pages</strong>: {book_pages} pp.<br/>
    <strong>ISBN</strong>: {book_isbn}.</p>
'''

def create_media_tiles_content(medias):
    """Generates a tile box for every media passed.

    Args:
        medias: List of Media instances.

    Returns:
        Resulting html code of running every media through
        the code in media_tile_content.
    """
    content = ''
    for media in medias:
        # 1) Generate class-specific info and save it in extension
        extension = ''
        if isinstance(media, Movie):
            extension += media_extended_movie.format(
                movie_release = media.release_date,
                movie_duration = media.duration,
                movie_director = media.director,
                # movie.cast is a list, so join it separating with commas
                movie_cast = ", ".join(media.cast))
        elif isinstance(media, TvShow):
            extension += media_extended_tvshow.format(
                show_channel = media.channel,
                show_seasons = media.seasons,
                show_episodes = media.episodes,
                show_duration = media.duration)
        elif isinstance(media, Book):
            extension += media_extended_book.format(
                book_author = media.author,
                book_year = media.year,
                book_pages = media.pages,
                book_editor = media.editor,
                book_isbn = media.isbn)

        # 2) Generate media rating, if the media has one, and save it in rating.
        rating = ''
        if media.rating is not None:
            rating = media_rating_div.format(media_rating = media.rating)

        # 3) Generate video preview button if object is of sub/class Video
        preview = ''
        if isinstance(media, Video):
            preview = media_preview_span.format(
                media_preview = getYoutubeId(media.preview))

        # 4) Generate info common to all medias and append any info generated.
        # Note that we are concatenating all tiles using the '+=' operator.
        content += media_tile_content.format(
            media_title = media.title,
            media_type = media.type,
            media_description = media.description,
            media_image = media.image,
            media_preview = preview,
            media_rating = rating,
            media_genre = ", ".join(media.genre),
            media_tile_extended = extension)
    return content

def getYoutubeId(youtubeURL):
    """Extract the youtube ID from the youtubeURL.

    Uses regular expresions to extract the id of ayoutube url.
    For example, given:
        https://www.youtube.com/watch?v=Gw85iUE4Ro8
    The id is Gw85iUE4Ro8.

    Args:
        youtubeURL: The full url of a youtube video.

    Returns:
        The id in the youtubeURL.
    """

    id_match = re.search(r'(?<=v=)[^&#]+', youtubeURL)
    id_match = id_match or re.search(r'(?<=be/)[^&#]+', youtubeURL)
    preview = (id_match.group(0) if id_match else None)
    return preview

def open_media_page(media):
    """Generates an index.html page with the info passed.

    For every Media in the list, it generates a box that shows
    an image, title, type and genre, plus content that depends
    on the type of media.

    When finished, opens the generated index.html.

    Args:
        media: List of Media instances.
    """
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the media tiles placeholder generated content
    rendered_content = main_page_content.format(
        media_tiles = create_media_tiles_content(media))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)

    webbrowser.open('file://' + url, new=2)

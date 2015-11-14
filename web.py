import webbrowser
import os
import re
from media import Video, Movie, TvShow

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My media collection</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="js/interactions.js" async></script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
    <body>
        <div class="modal" id="lightsoff">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                        <img src="img/cross.png"/>
                    </a>
                    <div class="scale-media display-none" id="trailer-video-container"></div>
                    <div class="scale-media display-none" id="media-extended-container"></div>
                </div>
            </div>
        </div>

        <!-- Main Page Content -->
        <div class="container">
            <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                <div class="container">
                    <div class="navbar-header">
                        <a id="navbar-title" class="navbar-brand" href="#">My media collection: movies, tv shows, books...</a>
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


# A single media entry html template
media_tile_content = '''
<article class="col-lg-4 col-md-6 col-sm-12 col-xs-12 media-tile">
    <div class="media-wrapper">
        <img class="media-image" src="{media_image}">
        <div class="media-info">
            <h3>{media_title}</h3>
            <p><strong>Type</strong>: {media_type}<br/>
            <strong>Genre</strong>: {media_genre}</p>
            <span data-toggle="tooltip" data-placement="top" title="View more">
                <span class="glyphicon glyphicon-plus-sign pointer" aria-hidden="true" data-target="#lightsoff" data-toggle="modal"></span>
            </span>
            <span data-toggle="tooltip" data-placement="top" title="View preview">
                <span class="glyphicon glyphicon-film pointer" aria-hidden="true" data-trailer-youtube-id={media_preview} data-toggle="modal" data-target="#lightsoff"></span>
            </span>
            <div class="media-rating-background">
                <span class="media-rating text-center">{media_rating}</span>
            </div>
        </div>
        <div class="media-info-extended display-none">
            <img class="media-image" src="{media_image}">
            <p>{media_description}</p>
            {media_tile_extended}
        </div>
    </div>
</article>
'''

media_extended_movie = '''
    <p><strong>Release</strong>: {movie_release}.<br/>
    <strong>Duration</strong>: {movie_duration} minutes.</p>

'''
media_extended_tvshow = '''
    <p><strong>Channel</strong>: {show_channel}.<br/>
    <strong>Seasons</strong>: {show_seasons}.<br/>
    <strong>Episodes</strong>: {show_episodes}.<br/>
    <strong>Avg. duration</strong>: {show_duration} minutes.</p>
'''
def create_media_tiles_content(medias):
    # The HTML content for this section of the page
    content = ''
    for media in medias:
        extension = ''
        # Generate class-specific info
        if isinstance(media, Movie):
            extension += media_extended_movie.format(
                movie_release = media.release_date,
                movie_duration = media.duration)

        if isinstance(media, TvShow):
            extension += media_extended_tvshow.format(
                media_title = media.title,
                show_channel = media.channel,
                show_seasons = media.seasons,
                show_episodes = media.episodes,
                show_duration = media.duration)

        # Generate common info; append the tile for the media with its content filled in
        content += media_tile_content.format(
            media_title = media.title,
            media_type = media.type,
            media_description = media.description,
            media_image = media.image,
            media_rating = media.rating,
            media_preview = media.preview,
            media_genre = media.genre,
            media_tile_extended = extension)
    return content

def getYoutubeId(youtubeURL):
    # Extract the youtube ID from the url
    youtube_id_match = re.search(r'(?<=v=)[^&#]+', youtubeURL)
    youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', youtubeURL)
    preview = (youtube_id_match.group(0) if youtube_id_match else None)
    return preview

def open_media_page(media):
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

    #TODO uncomment this for project handout
    #webbrowser.open('file://' + url, new=2)

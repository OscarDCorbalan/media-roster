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
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="css/style.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.media-trailer', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="img/cross.png"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container-fluid">
          <div class="navbar-header">
            <a id="navbar-title" class="navbar-brand" href="#">My media collection: movies, tv shows, books...</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid">
      {media_tiles}
    </div>
  </body>
</html>
'''


# A single media entry html template
media_tile_content = '''
<div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 media-tile">
    <div class="media-wrapper">
        <img class="media-image" src="{media_image}">
        <div class="media-info">
            <div class="media-rating-background">
                <span class="media-rating text-center">{media_rating}</span>
            </div>
            <p>{media_description}</p>
        </div>
        <div class="media-info-extended">
            <h3>{media_title}</h3>
            <p>{media_type} - {media_genre}</p>
            {media_tile_extended}
        </div>
    </div>
</div>
'''

media_extended_movie = '''
    <p><a class="media-trailer" href=# data-trailer-youtube-id={media_preview} data-toggle="modal" data-target="#trailer">Trailer</a></p>
'''
media_extended_tvshow = '''
    <p>Original channel: <strong>{show_channel}</p>
    <p>{media_title} consists of {show_seasons} seasons and {show_episodes} episodes, with an average duration of {show_duration} min. </p>
'''
def create_media_tiles_content(medias):
    # The HTML content for this section of the page
    content = ''
    for media in medias:
        extension = ''
        if isinstance(media, Video):
            youtubeId = getYoutubeId(media.preview)
            extension += media_extended_movie.format(media_preview = youtubeId)

        if isinstance(media, TvShow):
            extension += media_extended_tvshow.format(
                media_title = media.title,
                show_channel = media.channel,
                show_seasons = media.seasons,
                show_episodes = media.episodes,
                show_duration = media.duration)

        # Append the tile for the media with its content filled in
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

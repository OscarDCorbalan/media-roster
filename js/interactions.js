'use strict';

// Initialize Bootstrap tooltips. See http://getbootstrap.com/javascript/#modals
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

// Show detailed media info when the '+' button is clicked
$(document).on('click', '.glyphicon-plus-sign', function(event){
    // Find the <article> container
    var article = event.target;
    while(article.nodeName.toUpperCase() != 'ARTICLE'){
        article = article.parentNode;
    }

    // Get its media-extension <div>
    const html = $(article).find('.media-info-extended')[0].innerHTML;

    // Append it to the modal
    const container = $('#media-extended-container')
    container.empty().append(html)
    container.removeClass('display-none');
});// Show detailed media info when the '+' button is clicked

// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $('#trailer-video-container').empty();
    $('#media-extended-container').addClass('display-none');
    $('#trailer-video-container').addClass('display-none');
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.glyphicon-film', function (event) {
    // Get the youtube video ID
    const trailerYouTubeId = $(this).attr('data-trailer-youtube-id')

    // Create the src url
    const sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

    // Append it to the modal
    const container = $('#trailer-video-container');
    container.empty().append($('<iframe></iframe>', {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));
    container.removeClass('display-none');
});

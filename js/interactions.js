'use strict';

// Initialize Bootstrap tooltips. See http://getbootstrap.com/javascript/#modals
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

// When clicking an image preview, open it full-screen on a modal
$(document).on('click', '.media-image', function(event){
    // Create a new image with the same src of the clicked one (that is, reference the same image)
    var img = $('<img/>', {
        class: 'width-100',
        src: event.target.src
    });

    // And append it to the modal
    const container = $('#media-extended-container');
    container.empty().append(img);
    container.removeClass('display-none');
});

// When clicking the 'b' glyph/icon, show detailed media info on a modal
$(document).on('click', '.glyphicon-plus-sign', function(event){
    // Find the <article> container of the icon clicked
    var article = event.target;
    while(article.nodeName.toUpperCase() != 'ARTICLE'){
        article = article.parentNode;
    }

    // Get the html in the hidden <div> that contains the detailed info
    const html = $(article).find('.media-info-extended')[0].innerHTML;

    // And append its content to the modal
    const container = $('#media-extended-container')
    container.empty().append(html)
    container.removeClass('display-none');
});

// When clicking the film glyph/icon, open the video in a modal and start playing the video.
$(document).on('click', '.glyphicon-film', function (event) {
    // Get the youtube video ID from the data attribute
    const trailerYouTubeId = $(this).attr('data-trailer-youtube-id')

    // Create the src url for the embedded video. Note the autoplay=1.
    const sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

    // Append to the modal an iframe with the embedded video url
    const container = $('#trailer-video-container');
    container.empty().append($('<iframe></iframe>', {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));
    container.removeClass('display-none');
});

// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $('#trailer-video-container').empty();
    $('#media-extended-container').addClass('display-none');
    $('#trailer-video-container').addClass('display-none');
});

'use strict';


function truncate_card_description() {
    let videos = document.querySelectorAll('[' + 'data-oembed-url' + ']');

    for (let i = 0; i < videos.length; i++) {
        videos[i].nextElementSibling.remove();
        videos[i].remove();
    }
}


// Entry point
truncate_card_description();


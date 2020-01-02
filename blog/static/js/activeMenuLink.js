'use strict';


function set_active_section_style(link) {
    let link_section = link.getAttribute('section');

    if (link_section) {
        let sections = document.querySelectorAll('[' + 'section' + ']');

        for (let i = 0; i < sections.length; i++) {
            let section = sections[i].getAttribute('section');

            if (section === (link_section + 'Section')) {
                sections[i].style.color = '#00008B'
            }
        }
    }
}


function set_active_link_style(url_pathname, link) {
    if (url_pathname === window.location.pathname) {
            link.style.color = '#00008B';
            set_active_section_style(link);
        }
}


function active_link_handler() {
    let links = document.querySelectorAll('.list__links');

   for (let i = 0; i < links.length; i++) {
        let url_pathname = links[i].getAttribute('href');
        set_active_link_style(url_pathname, links[i])
   }
}


// Entry point.
active_link_handler();

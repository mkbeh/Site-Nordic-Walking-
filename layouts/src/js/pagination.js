'use strict';


let PAGINATION_CONTAINER = document.querySelector('.paginationContainer');

if (!PAGINATION_CONTAINER) {
    throw 'Pagination on this page does not exist.';
}

if (PAGINATION_CONTAINER.children.length < 12) {
    throw 'The number of paginator child elements is not enough to use the script.'
}

let CONTAINER_CHILDREN = PAGINATION_CONTAINER.children;
let CHILDREN_TOTAL_NUM = CONTAINER_CHILDREN.length - 2;     // exclude buttons `Previous` and `Next`
let CURRENT_PAGE = Number(window.location.search.split('=')[1]);

let VISIBLE_PAGINATION_ITEMS_NUM = 3;      // 1 - current item and 2 items next to the current item
let HIDE_RIGHT_FROM = CURRENT_PAGE + VISIBLE_PAGINATION_ITEMS_NUM;


function insert_dots(insert_index) {
    let ellipsis = document.createElement('span');
    ellipsis.textContent = '...';

    PAGINATION_CONTAINER.insertBefore(ellipsis, CONTAINER_CHILDREN[insert_index]);
}


function insert_dots_handler() {
    let dots_insert_index = CURRENT_PAGE + VISIBLE_PAGINATION_ITEMS_NUM;

    if (dots_insert_index < CHILDREN_TOTAL_NUM) {
        insert_dots(dots_insert_index)
    }
}


function hide_pagination_elements(start, stop) {
    for (let i = start; i < stop; i++) {
        CONTAINER_CHILDREN[i].style.display = 'none';
    }
}


function pagination_elements_handler() {
    if (isNaN(CURRENT_PAGE)) {
        CURRENT_PAGE = 1;
        HIDE_RIGHT_FROM = CURRENT_PAGE + VISIBLE_PAGINATION_ITEMS_NUM;
    }

    if (CHILDREN_TOTAL_NUM - CURRENT_PAGE > VISIBLE_PAGINATION_ITEMS_NUM) {
        hide_pagination_elements(1, CURRENT_PAGE);
        hide_pagination_elements(HIDE_RIGHT_FROM, CHILDREN_TOTAL_NUM);

        insert_dots_handler();
    } else {
        hide_pagination_elements(2, CURRENT_PAGE);

        insert_dots(CURRENT_PAGE)
    }
}


// Entry point.
pagination_elements_handler();

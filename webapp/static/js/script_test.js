$(document).ready(function() {
    setInterval(getNewComments, 3000);

    function getNewComments() {
    let count_comments = $('.card').length;
    let post_id = window.location.pathname.slice(10);
    $.get('/articles/get_comment_update',
    {'post_id': post_id,
    'current_count_comments': count_comments
    },
    addComment
    )};
    function addComment(data) {
    for (let comment of data['new_comments']) {
        $('.comments').append(`<div class="card">
        <div class="card-header">${comment.user}</div>
        <div>Только что</div>
        <div class="card-body">
        <blockquote class="blockquote mb-0">
        <p>${comment.text}</p>
        </blockquote>
        </div>
        </div>`);
        }
        }
});
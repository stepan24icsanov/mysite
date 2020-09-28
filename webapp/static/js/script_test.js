$(document).ready(function() {
    let socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
    console.log('User connected');
    });

    socket.on('message', function(comment) {
        $('.comments').append(`<div class="card">
        <div class="card-header">${comment[0]}</div>
        <div>${moment.utc(comment[2]).local().format('HH:mm | D MMMM YYYY года')}</div>
        <div class="card-body">
        <blockquote class="blockquote mb-0">
        <p>${comment[1]}</p>
        </blockquote>
        </div>
        </div>`);
        console.log(comment);
    });

    $('#comments').on('submit', function() {
        socket.send($('#text').val());
    });
});
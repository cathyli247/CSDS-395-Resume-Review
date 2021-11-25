$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();
    

    $.ajax({
        type: 'POST',
        url: '/send',
        data: {
            username: $('#username').val(),
            room_id: $('#room_id').val(),
            message: $('#message').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            //alert(data)
        }
    });
    document.getElementById('message').value = ''
});


$(document).ready(function () {

    setInterval(function () {
        var room = $('input#test').val();
        $.ajax({
            type: 'GET',
            url: "/getMessages/" +room+ "/",
            success: function (response) {
                console.log(response);
                $("#display").empty();
                for (var key in response.messages) {
                    // var temp = "<li class='clearfix'><div class= 'message-data text-right'><span class='message-data-time'>" + response.messages[key].date + "</span><img src=" + response.messages[key].account.avatar.url + "alt='avatar'></div><div class='message other-message float-right'>" + response.messages[key].value + "</div></li>";
                    var temp = "<li class='clearfix'><div class= 'message-data text-right'><span class='message-data-time'>" + response.messages[key].date + "</span></div><div class='message other-message float-right'>" + response.messages[key].value + "</div></li>";
                    $("#display").append(temp);
                }
            },
            error: function (response) {
                alert('An error occured')
            }
        });
    }, 1000);
})
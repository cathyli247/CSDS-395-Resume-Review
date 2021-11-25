$(document).on('click', '#submit', function (e) {
    e.preventDefault();
    const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: 'POST',
        url: '/send',
        headers: {'X-CSRFToken': csrftoken},
        data: {
            username: $('#current_account_id').val(),
            room_id: $('#room_id').val(),
            message: $('#message').val(),
        },
        success: function (data) {
            //alert(data)
        }
    });
    document.getElementById('message').value = ''
});


$(document).ready(function () {
    if (typeof ($('input#room_id').val()) === undefined || $('input#room_id').val()=='') {
    }
    else{
        setInterval(function () {
            var room = $('input#room_id').val();
            $.ajax({
                type: 'GET',
                url: "/getMessages/?room=" +room,
                success: function (response) {
                    const messages = JSON.parse(response);
                    console.log(messages);
                    $("#display").empty();
                    for (var i = 0; i < messages['messages'].length; i++) {
                        var temp = '';
                        var key = messages['messages'][i];
                        if (key['account_id'] == $('input#current_account_id').val()){
                            temp += "<div class='chat-message-right mb-4'><div><img src="+ key['avatar_url'] + " class='rounded-circle mr-1'width='40' height='40'><div class='text-muted small text-nowrap mt-2'>" +key['date']+"</div></div><div class='flex-shrink-1 bg-light rounded py-2 px-3 mr-3'><div class='font-weight-bold mb-1'>"+key['account_name']+"</div>"+ key['value'] +"</div></div>";
                        }
                        else {
                            temp += "<div class='chat-message-left mb-4'><div><img src="+ key['avatar_url'] + " class='rounded-circle mr-1'width='40' height='40'><div class='text-muted small text-nowrap mt-2'>" +key['date']+"</div></div><div class='flex-shrink-1 bg-light rounded py-2 px-3 mr-3'><div class='font-weight-bold mb-1'>"+key['account_name']+"</div>"+ key['value'] +"</div></div>";
                        }
                        $("#display").append(temp);
                    }
                },
                error: function (response) {
                    alert('An error occurred');
                }
            });
        }, 1000);
    }

})
$( document ).ready(function() {
    init_page();
});

$(document).on('click','#edit',function(){
    $('.info').hide();
    $('.edit').show();
});

$(document).on('click','#cancel',function(){
    $('.info').show();
    $('.edit').hide();
});

$(document).on('click','#update',function(){
    if (checkValidity()) {
//        sendRequest();
        $( "#submit" ).click();
    }
    else {
        $('.err-msg').show();
    }
});

function init_page() {
    $('.info').show();
    $('.edit').hide();
    $('.err-msg').hide();
    $('input#id_first_name').val($('#info_first_name').text().replace(/\s/g,''));
    $('input#id_last_name').val($('#info_last_name').text().replace(/\s/g,''));
    $('input#id_phone_number').val($('#info_phone_number').text().replace(/\s/g,''));
    $('#id_major').val($('#info_major').text().trim());
    $('#id_academic_standing').val($('#info_academic_standing').text().replace(/\s/g,''));
}

function checkValidity() {
    if (!($("input#id_first_name").val() && $("input#id_last_name").val() && $("input#id_phone_number").val())) {
        return false;
    }
    return true;
}

//function sendRequest() {
//    var frm = $('#profile-form');
//    $.ajax({
//                type: frm.attr('method'),
//                url: frm.attr('action'),
//                data: frm.serialize(),
//                success: function (data) {
//                    location.reload();
//                },
//                error: function(data) {
//                    console.log('failed');
//                }
//    });
//}

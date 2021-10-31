$( document ).ready(function() {
    var info = document.getElementById("order-state-hidden");
    $('.ratingSection').show();
    if (info.innerText == 'Completed') {
        $('#ratingSection').show();
        $('#cancel-btn').hide();
    }
    else {
        
        $('#ratingSection').hide();
        $('#cancel-btn').show();
    }

});

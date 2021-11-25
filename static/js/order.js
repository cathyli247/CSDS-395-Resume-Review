$( document ).ready(function() {
        switchTable();
        $("li#order" ).addClass("active");
        $('.Pending').addClass("text-warning");
        $('.Completed').addClass("text-success");
        $('.Accepted').addClass("text-info");
        $('.Canceled').addClass("text-danger");
});

$(document).on('change','#order-select',function(){
    switchTable();
});

function switchTable() {
    var select = $('#order-select').val();
    if (select == 'Orders sent') {
        $('#customer-table').hide();
        $('#reviewer-table').show();
    }
    else {
        $('#customer-table').show();
        $('#reviewer-table').hide();
    }
}


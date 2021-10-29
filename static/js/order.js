$( document ).ready(function() {
    $("li#order" ).addClass("active");
});

$( document ).ready(function() {
    if ($('#status-of-order').text().indexOf('Pending') > -1){
        $('.status').addClass("text-warning");
    }
    else if ($('#status-of-order').text().indexOf('Completed') > -1){
        $('.status').addClass("text-success");
    }
    else if ($('#status-of-order').text().indexOf('Comfirmed') > -1){
        $('.status').addClass("text-info");
    }
    else if ($('#status-of-order').text().indexOf('Rejected') > -1){
        $('.status').addClass("text-danger");
    }
});


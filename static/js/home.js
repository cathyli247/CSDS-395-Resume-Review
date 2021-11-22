$( document ).ready(function() {
    $("li#home" ).addClass("active");
    $(".card-img").parent().css({position: 'relative'});
    $(".card-img").css({top: 0, left: 0, position:'absolute'});
    $(".reviewer-btn").parent().css({position: 'relative'});
    $(".reviewer-btn").css({top: 320, left: 80, position:'absolute'});
    $(".profile-img").parent().css({position: 'relative'});
    $(".profile-img").css({top: 210, left: 90, position:'absolute'});
    $(".about").parent().css({position: 'relative'});
    $(".about").css({top: 300, left: 10, position:'absolute'});
    $("h1").parent().css({position: 'relative'});
    $("h1").css({top: 260, position:'absolute'});

    $("#sidebar" ).find('.main-body').remove();

    $(".about").each(function(i){
        var len=$(this).text().trim().length;
        if(len>65)
        {
            $(this).text($(this).text().substr(0,60)+'...');
        }
        });
});
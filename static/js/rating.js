function openRatingForm(){
    var infotable = document.getElementById("complete-info");
    if (infotable.rows[1].cells[0].innerText == 'Completed') {
        document.body.classList.add("showRatingForm");
    }
    else {
        document.getElementById("incomplete-msg").innerHTML = "Rating opens when the order is completed.";
    }
}
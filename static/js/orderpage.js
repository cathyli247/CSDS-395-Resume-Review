const selectFileBtn = document.getElementById('select-file-btn');
const fileSelected = document.getElementById('file-selected');
selectFileBtn.addEventListener('change', function(){
    fileSelected.textContent = this.files[0].name
})

function openRatingForm(){
    document.body.classList.add("showRatingForm");
}

function comf_rejc(){
    document.body.classList.add("showConfirmStatus");
}
$( document ).ready(function() {
    $('#id_resume').bind('change', function () {
      var filename = $("#id_resume").val();
      if (/^\s*$/.test(filename)) {
        $(".file-upload").removeClass('active');
        $("#noFile").text("No file chosen...");
      }
      else {
        $(".file-upload").addClass('active');
        $("#noFile").text(filename.replace("C:\\fakepath\\", ""));
      }
    });
});

$(document).on('click','#download',function(){
    $('input#id_download').val('true');
});

$(document).on('click','#submit',function(){
    $('input#id_download').val('false');
});

const selectFileBtn = document.getElementById('select-file-btn');
const fileSelected = document.getElementById('file-selected');
//selectFileBtn.addEventListener('change', function(){
//    fileSelected.textContent = this.files[0].name
//})

function comf_rejc(){
    document.body.classList.add("showConfirmStatus");
}

function ShowSubmitInfo(){
    document.getElementById("submit-msg").innerHTML = 'Submitted';
}


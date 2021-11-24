$( document ).ready(function() {
    $('#submit_rate').prop('disabled', true);
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

$(document).on('click','button[type=submit]',function(){
    if (this.id == 'submit_rate') {
        $('input#id_rate').val($('input[name="star"]:checked').val());
        $('input#id_comment').val($('.textComments').val());
    }
    $('input#id_button').val(this.id);
});

$(document).on('change','input[name="star"]',function(){
    $('#submit_rate').prop('disabled', false);
});

$( document ).ready(function() {
  var orderState = $('#order-state-hidden').text();
  if (orderState == "Completed"){
    $('#step1').addClass("active");
    $('#step2').addClass("active");
    $('#step3').addClass("active");
    $('#step4').addClass("active");
  }
  else if (orderState == "Accepted"){
    $('#step1').addClass("active");
    $('#step2').addClass("active");
    $('#step3').addClass("active");
    $('#step4').removeClass("active");
  }
  else if (orderState == "Pending"){
    $('#step1').addClass("active");
    $('#step2').addClass("active");
    $('#step3').removeClass("active");
    $('#step4').removeClass("active");
  }
  else if (orderState == "Rejected"){
    $('#step1').addClass("active");
    $('#step2').addClass("active");
    $('#step3').addClass("active");
    $('#step4').removeClass("active");
    $('#progress-three').text("Rejected");
  }
});

$( document ).ready(function() {
  var newFileName = $('#download-files').text().replace('resumes/', '');
  $('#download-files').text(newFileName)
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


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
    $('#step3').text("Rejected");
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


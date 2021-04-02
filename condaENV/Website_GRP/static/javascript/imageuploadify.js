/*!
 * Imageuploadify - jQuery plugin
 * Allow to change input file to a box allowing drag'n drop and preview images before
 * updloading them.
 */

// Check character count for 'Artefact Description'
$('#artefact_desc').keyup(function() {
    
    // Initialize variables
    var count = $(this).val().length;
    var current_desc = $('#current_desc');
    var maximum = $('#max_desc');
    var count_desc = $('#count_desc');
      
    current_desc.text(count);
  
    // If word limit (600 chars) is reached, change color to Red
    if (count >= 600) {
      maximum.css('color','#FF0000');
      count_desc.css('color', '#FF0000');
    }
    else {
      maximum.css('color','#787575');
      count_desc.css('color', '#787575');
    }
  
  });

//upload image 
var loadFile = function(event) {
  var reader = new FileReader();
  reader.onload = function(){
    var output = document.getElementById('output');
    output.src = reader.result;
  };
  reader.readAsDataURL(event.target.files[0]);
};

/************ alert-cancel upload ***************/
function cancelUpload() {
  window.confirm("The content on this page will not be uploaded and you will be directed to the project summary page. Are you sure you want to cancel this upload?");
}
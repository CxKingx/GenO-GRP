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
// website: https://www.jqueryscript.net/form/Drag-And-Drop-File-Uploader-With-Preview-Imageuploadify.html


document.getElementById('title').addEventListener('blur', validateTitle);

// Project title must be between 4 to 150 characters
function validateTitle() {
  const title = document.getElementById('title');
  // Title can contain alphabets, numbers, and symbols
  const re =  /^[a-zA-Z0-9"';()-_. ]{4,150}/

  if(!re.test(title.value)){
      title.classList.add('is-invalid');
      document.getElementById('submit').disabled = true;
  }
  else {
      title.classList.remove('is-invalid');
      document.getElementById('submit').disabled = false;
  }
}
/************** video upload *****************/
var loadFile = function(event) {
  var reader = new FileReader();
  reader.onload = function(){
    var output = document.getElementById('output');
    output.src = reader.result;
  };
  reader.readAsDataURL(event.target.files[0]);
};

/************ thumbnail upload ***************/
var loadThumbnail = function(event) {
    	  	var reader = new FileReader();
    		  reader.onload = function(){
      		var output = document.getElementById('outputThumbnail');
      		output.src = reader.result;
    		  };
    	    reader.readAsDataURL(event.target.files[0]);
  		  };
/************ alert-cancel upload ***************/
function cancelUpload() {
	window.confirm("The content on this page will not be uploaded and you will be directed to the project summary page. Are you sure you want to cancel this upload?");
}
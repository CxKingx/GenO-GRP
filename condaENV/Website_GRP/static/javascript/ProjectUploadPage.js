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

// Check character count for 'Project Description'
$('#text_project').keyup(function() {
    
  // Initialize variables
  var count = $(this).val().length;
  var current_project = $('#current_project');
  var maximum = $('#max_project');
  var count_project = $('#count_project');
    
  current_project.text(count);

  // If word limit (3000 chars) is reached, change color to Red
  if (count >= 3000) {
    maximum.css('color','#FF0000');
    count_project.css('color', '#FF0000');
  }
  else {
    maximum.css('color','#787575');
    count_project.css('color', '#787575');
  }

});

// Check character count for 'Author Comments'
$('#text_author').keyup(function() {
    
  // Initialize variables
  var count = $(this).val().length;
  var current_author = $('#current_author');
  var maximum = $('#max_author');
  var count_author = $('#count_author');
    
  current_author.text(count);

  // If word limit (2000 chars) is reached, change color to Red
  if (count >= 2000) {
    maximum.css('color','#FF0000');
    count_author.css('color', '#FF0000');
  }
  else {
    maximum.css('color','#787575');
    count_author.css('color', '#787575');
  }

});
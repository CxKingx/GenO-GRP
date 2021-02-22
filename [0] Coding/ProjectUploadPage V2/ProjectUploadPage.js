function countProjectWords() {
  // Get the entered text in Project Description
  var project_text = document.getElementById("project_text").value;   
  var word_count = 0;                                                

  // Split words on space
  var split = project_text.split(' ');

  // Process word count
  for (var i = 0; i < split.length; i++) { 
    if (split[i] != "") { 
        word_count += 1; 
    } 
  } 

  // Show word count
  document.getElementById("project_show").innerHTML = word_count; 
  //limitWords(word_count);
}

// function limitWords(word_count) {
//   if (word_count <= 500) {
//     document.getElementById("project_text").disabled = false;
//   }
//   else {
//     document.getElementById("project_text").disabled = true;
//   }
// }

function countAuthorWords() {
  // Get the entered text in Author Comments
  var author_text = document.getElementById("author_text").value;
  var word_count = 0;

  // Split words on space
  var split = author_text.split(' ');

  // Process word count
  for (var i = 0; i < split.length; i++) { 
    if (split[i] != "") { 
        word_count += 1; 
    } 
  } 

  // Show word count
  document.getElementById("author_show").innerHTML = word_count; 
}
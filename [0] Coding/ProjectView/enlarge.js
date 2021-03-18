if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', afterLoaded);
} else {
    //The DOMContentLoaded event has already fired. Just run the code.
    afterLoaded();
}

function afterLoaded(){
    // Get the modal
    var modal = document.getElementById('myModal');

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    var imgem = document.getElementById("myImg");
    var imgem2 = document.getElementById("flipcardID");
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");

    imgem2.onclick = function() {
        modal.style.display = "block";
        modalImg.src = imgem.src;
        captionText.innerHTML = imgem.alt;
    }

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        console.log("test");
        modal.style.display = "none";
    }
}

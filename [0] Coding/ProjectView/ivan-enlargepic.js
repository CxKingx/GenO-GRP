if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', afterLoaded);
} else {
    //The DOMContentLoaded event has already fired. Just run the code.
    afterLoaded();
}

function afterLoaded(){
    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    var imgem2 = document.querySelectorAll(".flip-box-back");
    console.log(imgem2);
    var modalImg = document.getElementById("img01");
    var captionText = document.querySelectorAll(".caption");

    imgem2.forEach(function(item) {
        item.addEventListener('click', function(e){
            var imgem = item.querySelector(".myImg");

            modal.style.display = "block";
            modalImg.src = imgem.src;
            captionText.innerHTML = imgem.alt;
        });
        
    });

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        console.log("test");
        modal.style.display = "none";
    }
}

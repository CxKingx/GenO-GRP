/* Script for search bar */
const searchBtn = document.querySelector(".search-btn");
const cancelBtn = document.querySelector(".cancel-btn");
const searchBox = document.querySelector(".search-box");
const searchInput = document.querySelector("input");

searchBtn.onclick = () =>{
    searchBox.classList.add("active");
    searchInput.classList.add("active");
    searchBtn.classList.add("active");
    cancelBtn.classList.add("active");
}

cancelBtn.onclick = () =>{
    searchBox.classList.remove("active");
    searchInput.classList.remove("active");
    searchBtn.classList.remove("active");
    cancelBtn.classList.remove("active");
    searchInput.value = "";
}

/* Script for toggle menu bar */
$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#toggle-menu').on('click', function () {
        $('#sidebar, #content').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('.overlay').addClass('active');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});

/* Script for cross button in the menu bar */
$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#cancel-btn').on('click', function () {
        $('#sidebar, #content').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('.overlay').removeClass('active');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});

/* enlarging image of artefact cards */
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

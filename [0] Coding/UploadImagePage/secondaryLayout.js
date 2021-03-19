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

document.addEventListener("DOMContentLoaded", function(event) {
    var rentsb = {};

    rentsb.captions = document.querySelectorAll(".bd-sidebar .caption");

    for (let i = 0; i < rentsb.captions.length; i++) {
        let caption = rentsb.captions[i];
        let themeCaption = caption.querySelector(".caption-text");
        let themePage = caption.nextElementSibling.querySelector("* > a");

        if (themeCaption.textContent === themePage.textContent) {
            themePage.textContent = "All";
        }
    }
});

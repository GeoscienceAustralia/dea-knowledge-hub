// Renames the first link under a caption in the sidebar to 'All' if it has the same text as the caption. This is to prevent duplicated text.

document.addEventListener("DOMContentLoaded", function(event) {
    let captions = document.querySelectorAll(".bd-sidebar .caption");

    for (let i = 0; i < captions.length; i++) {
        let caption = captions[i];
        let themeCaption = caption.querySelector(".caption-text");
        let themePage = caption.nextElementSibling.querySelector("* > a");

        if (themeCaption.textContent === themePage.textContent) {
            themePage.textContent = "All";
        }
    }
});

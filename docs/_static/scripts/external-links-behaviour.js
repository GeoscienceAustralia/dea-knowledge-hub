// Makes all external links open in a new tab

document.addEventListener("DOMContentLoaded", function (event) {
    for (var links = document.links, i = 0, a; (a = links[i]); i++) {
        if (a.host !== location.host && !a.target) {
            a.target = "_blank";
            a.setAttribute("rel", "noopener noreferrer");
            a.classList.add("open-in-new-tab");
        }
    }
});

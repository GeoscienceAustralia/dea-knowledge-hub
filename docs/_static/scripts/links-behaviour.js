// Makes all external links open in a new tab

document.addEventListener("DOMContentLoaded", function (event) {
    for (var links = document.links, i = 0, a; (a = links[i]); i++) {
        if (a.host === location.host) {
            a.classList.add("internal-link");
        } else if (a.host !=== location.host) {
            a.classList.add("external-link");
            if (!a.target) {
                a.target = "_blank";
                a.setAttribute("rel", "noopener noreferrer");
            }
        } else if (/^#/.test(a.href)) {
            a.classList.add("anchor-link");
        }
    }
});

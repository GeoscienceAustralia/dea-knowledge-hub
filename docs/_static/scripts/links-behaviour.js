// Classifies each type of link (anchor, internal, external) with a CSS class and also makes external links open in a new tab by default.

document.addEventListener("DOMContentLoaded", function (event) {
    for (var links = document.links, i = 0, a; (a = links[i]); i++) {
        var hrefAnchor = a.href.replace(location.href, "");
        if (/^(?:#|\.\/#)/.test(hrefAnchor)) {
            a.classList.add("anchor-link");
        } else if (/^(?:\?|\.\/\?)/.test(hrefAnchor)) {
            a.classList.add("query-link");
        } else if (a.host === location.host) {
            a.classList.add("internal-link");
        } else if (a.host !== location.host) {
            a.classList.add("external-link");
            if (!a.target) {
                a.target = "_blank";
                a.setAttribute("rel", "noopener noreferrer");
            }
        }
    }
});

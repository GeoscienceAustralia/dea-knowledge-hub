document.addEventListener("DOMContentLoaded", function (event) {
    const headings = document.querySelectorAll("h2[id], h3[id], h4[id]"); // section[id]

    for (var i = 0; i < headings.length; i++) {
        const heading = headings[i];
        const anchorId = heading.id;

        heading.classList.add("clickable-anchor");

        if (anchorId) {
            heading.addEventListener("click", function() {
                    window.location.hash = `#${anchorId}`
            });
        }
    }
});

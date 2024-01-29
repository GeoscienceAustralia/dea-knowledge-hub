document.addEventListener("DOMContentLoaded", function (event) {
    const headings = document.querySelectorAll("h2[id], h3[id], h4[id]"); // section[id]

    for (var i = 0; i < headings.length; i++) {
        const heading = headings[i];

        heading.addEventListener("click", function() {
            const anchorId = heading.id;

            if (anchorId) {
                console.log(anchorId);
                heading.classList.add("clickable-anchor");
                window.location.hash = `#${anchorId}`
            }
        });
    }
});

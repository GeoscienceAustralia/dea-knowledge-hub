document.addEventListener("DOMContentLoaded", function (event) {
    // Move the section IDs to the headings

    let sections = document.querySelectorAll("section[id]");

    for (let i = 0; i < sections.length; i++) {
        let section = sections[i];
        let id = section.id;
        section.removeAttribute("id");
        section.querySelector("* > h2, * > h3, * > h4").id = id;
    }

    // Convert the 'rubrics' to H2 headings

    let rubrics = document.querySelectorAll("p.rubric");

    for (let i = 0; i < rubrics.length; i++) {
        let rubric = rubrics[i];
        let h2 = document.createElement("h2");
        h2.id = rubric.id;
        h2.class = rubric.class;
        h2.innerHTML = rubric.innerHTML;
        rubric.parentNode.replaceChild(h2, rubric);
    }

    // Make the headings clickable

    let headings = document.querySelectorAll("h2[id], h3[id], h4[id]");

    for (var i = 0; i < headings.length; i++) {
        let heading = headings[i];
        let anchorId = heading.id;

        if (anchorId) {
            heading.dataset.anchorHeading = true

            heading.addEventListener("click", function() {
                window.location.hash = `#${anchorId}`
            });
        }
    }
});


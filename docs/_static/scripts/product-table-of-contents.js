// Enable tables of content on the data product pages using tocbot.

document.addEventListener("DOMContentLoaded", function (event) {
    // Move the section IDs to the H2 headings

    let sections = document.querySelectorAll(
        ".product-page .sd-tab-content > section[id]"
    );

    for (let i = 0; i < sections.length; i++) {
        let section = sections[i];
        let id = section.id;
        section.removeAttribute("id");
        section.querySelector("* > h2").id = id;
    }

    // Convert the 'rubrics' to H2 headings

    let rubrics = document.querySelectorAll(
        ".product-page .sd-tab-content > p.rubric"
    );

    for (let i = 0; i < rubrics.length; i++) {
        let rubric = rubrics[i];
        let h2 = document.createElement("h2");
        h2.id = rubric.id;
        h2.class = rubric.class;
        h2.innerHTML = rubric.innerHTML;
        rubric.parentNode.replaceChild(h2, rubric);
    }

    // Initialise the table of contents for each tab

    let tabs = [
        "overview",
        "access",
        "details",
        "quality",
        "history",
        "faqs",
        "credits"
    ];

    for (let i = 0; i < tabs.length; i++) {
        let tab = tabs[i];
        tocbot.init({
            contentSelector: `.product-page #${tab}-tab + .sd-tab-content`,
            tocSelector: `.product-page #${tab}-table-of-contents`,
            headingSelector: "h2"
        });
    }
});

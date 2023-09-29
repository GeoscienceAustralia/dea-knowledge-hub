// Enable tables of content on the data product pages using tocbot

var tocdp = {};

// Move the section IDs to the H2 headings

tocdp.sections = document.querySelectorAll(".data-product .sd-tab-content > section[id]");

for (let i = 0; i < tocdp.sections.length; i++) {
    let section = tocdp.sections[i];
    let id = section.id;
    section.removeAttribute('id');
    section.querySelector("* > h2").id = id;
}

// Convert the 'rubrics' to H2 headings

tocdp.rubrics = document.querySelectorAll(".data-product .sd-tab-content > p.rubric");

for (let i = 0; i < tocdp.rubrics.length; i++) {
    let rubric = tocdp.rubrics[i];
    let h2 = document.createElement('h2');
    h2.id = rubric.id;
    h2.class = rubric.class;
    h2.innerHTML = rubric.innerHTML;
    rubric.parentNode.replaceChild(h2, rubric);
}

// Initialise the table of contents for each tab

tocdp.tabs = ["access", "details", "quality", "history", "credits"];

for (let i = 0; i < tocdp.tabs.length; i++) {
    let tab = tocdp.tabs[i];
    tocbot.init({
        contentSelector: `.data-product #${tab}-tab + .sd-tab-content`,
        tocSelector: `.data-product #${tab}-table-of-contents`,
        headingSelector: 'h2'
    });
}

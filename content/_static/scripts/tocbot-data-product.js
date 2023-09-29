// Enable tables of content on the data product pages using tocbot

// Move the section IDs to the H2 headings

const sections = document.querySelectorAll(".data-product .sd-tab-content > section[id]");

for (let i = 0; i < sections.length; i++) {
    const section = sections[i];
    const id = section.id;
    section.removeAttribute('id');
    section.querySelector("* > h2").id = id;
}

// Convert the 'rubrics' to H2 headings

const rubrics = document.querySelectorAll(".data-product .sd-tab-content > p.rubric");

for (let i = 0; i < rubrics.length; i++) {
    const rubric = rubrics[i];
    const h2 = document.createElement('h2');
    h2.id = rubric.id;
    h2.class = rubric.class;
    h2.innerHTML = rubric.innerHTML;
    rubric.parentNode.replaceChild(h2, rubric);
}

// Initialise the table of contents for each tab

tocbot.init({
    contentSelector: '.data-product #access-tab + .sd-tab-content',
    tocSelector: '.data-product #access-table-of-contents',
    headingSelector: 'h2'
});

tocbot.init({
    contentSelector: '.data-product #details-tab + .sd-tab-content',
    tocSelector: '.data-product #details-table-of-contents',
    headingSelector: 'h2'
});

tocbot.init({
    contentSelector: '.data-product #quality-tab + .sd-tab-content',
    tocSelector: '.data-product #quality-table-of-contents',
    headingSelector: 'h2'
});

tocbot.init({
    contentSelector: '.data-product #history-tab + .sd-tab-content',
    tocSelector: '.data-product #history-table-of-contents',
    headingSelector: 'h2'
});

tocbot.init({
    contentSelector: '.data-product #credits-tab + .sd-tab-content',
    tocSelector: '.data-product #credits-table-of-contents',
    headingSelector: 'h2'
});

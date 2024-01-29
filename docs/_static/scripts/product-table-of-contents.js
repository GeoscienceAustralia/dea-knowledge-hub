// Enable tables of content on the data product pages using tocbot.

document.addEventListener("DOMContentLoaded", function (event) {
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
            contentSelector: `.product-page #${tab} + .sd-tab-content`,
            tocSelector: `.product-page #${tab}-table-of-contents`,
            headingSelector: "h2"
        });
    }
});

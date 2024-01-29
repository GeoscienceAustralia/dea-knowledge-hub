// Enable tables of content on the data product pages using tocbot.

document.addEventListener("DOMContentLoaded", function (event) {
    let tabs = document.querySelectorAll(".product-page .sd-tab-label");

    for (let i = 0; i < tabs.length; i++) {
        let tab = tabs[i];
        let id = tab.id;

        tocbot.init({
            contentSelector: `.product-page #${id} + .sd-tab-content`,
            tocSelector: `.product-page #${id}-table-of-contents`,
            headingSelector: "h2"
        });
    }
});

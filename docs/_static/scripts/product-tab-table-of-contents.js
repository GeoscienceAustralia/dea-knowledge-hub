// Adds a table of contents within each tab on the product pages.

document.addEventListener("DOMContentLoaded", function (event) {
    let tabs = document.querySelectorAll(".product-page .sd-tab-label");

    for (let i = 0; i < tabs.length; i++) {
        let tab = tabs[i];
        let tabId = tab.id;

        let headings = document.querySelectorAll(
            `#${tabId} + .sd-tab-content h2[data-anchor-id]`
        );
        let toc = document.querySelector(
            `#${tabId} + .sd-tab-content .tocbot-selector`
        );

        for (let i = 0; i < headings.length; i++) {
            let heading = headings[i];
            let linkElement = document.createElement("a");
            linkElement.href = `#${heading.dataset.anchorId}`;
            linkElement.textContent = heading.textContent || heading.innerText;

            toc.appendChild(linkElement);
        }
    }
});

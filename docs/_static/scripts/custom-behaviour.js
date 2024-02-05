// Standardises the headings and their anchor IDs. Adds behaviour to headings and tabs that adds their IDs to the URL. Also, adds behaviour to links.
// The sections of this script are in order of precedence. Each time a 'data-anchor-id' property is added to a heading, it will override any existing 'data-anchor-id' that was set previously.

document.addEventListener("DOMContentLoaded", function (event) {
    // Convert the '.rubric.h2' elements to H2 headings.

    (function () {
        let h2Rubrics = document.querySelectorAll("p.rubric.h2");

        for (let i = 0; i < h2Rubrics.length; i++) {
            let rubric = h2Rubrics[i];
            let h2 = document.createElement("h2");
            h2.id = rubric.id;
            h2.class = rubric.class;
            h2.innerHTML = rubric.innerHTML;
            rubric.parentNode.replaceChild(h2, rubric);
        }
    })();

    // Add the section ID to the heading's 'data-anchor-id' property.

    (function () {
        let sections = document.querySelectorAll("section[id]");

        for (let i = 0; i < sections.length; i++) {
            let section = sections[i];
            let id = section.id;
            let maybeHeading = section.querySelector("* > h2, * > h3");

            if (maybeHeading) {
                maybeHeading.dataset.anchorId = id;
            }
        }
    })();

    // Add heading's own ID to the heading's 'data-anchor-id' property.

    (function () {
        let headings = document.querySelectorAll("h2, h3");

        for (var i = 0; i < headings.length; i++) {
            let heading = headings[i];
            let id = heading.id;

            if (id) {
                heading.dataset.anchorId = id;
            }
        }
    })();

    // Add the custom ID element above the heading to the heading's 'data-anchor-id' property

    (function () {
        let headings = document.querySelectorAll("h2, h3");

        for (var i = 0; i < headings.length; i++) {
            let heading = headings[i];
            let maybeCustomIdElement = heading.previousSibling;

            if (
                maybeCustomIdElement &&
                maybeCustomIdElement.nodeName === "SPAN" &&
                maybeCustomIdElement.hasAttribute("id")
            ) {
                let conflictingIdPattern = /id\d+/g;
                let customId = maybeCustomIdElement.id;

                // Checks that the ID is not 'id1', 'id2', 'id3', or etc. These IDs occur to prevent a naming conflict between IDs.
                // E.g. if a heading 'Introduction' has a '(introduction)=' custom ID above it, this naming conflict will occur.
                if (!conflictingIdPattern.test(customId)) {
                    heading.dataset.anchorId = customId;
                }
            }
        }
    })();

    // Clicking on a heading will add its anchor ID to the URL. E.g. /example/#introduction

    (function () {
        let headings = document.querySelectorAll(
            "h2[data-anchor-id], h3[data-anchor-id]"
        );

        for (var i = 0; i < headings.length; i++) {
            let heading = headings[i];
            let anchorId = heading.dataset.anchorId;

            heading.addEventListener("click", function () {
                console.log(anchorId);
                window.location.hash = `#${anchorId}`;
            });
        }
    })();

    // Clicking on a product tab will add its tab ID to the URL. E.g. /example/?tab=overview

    (function () {
        let tabs = document.querySelectorAll(".product-page .sd-tab-label");
        let tabUrlParam = new URLSearchParams(window.location.search).get(
            "tab"
        );
        let overviewTabId = tabs[0].id;

        if (!tabUrlParam) {
            window.history.pushState(
                "",
                "",
                `?tab=${overviewTabId}${window.location.hash}`
            );
        } else {
            document.querySelector(`.sd-tab-set > #${tabUrlParam}`).click();
        }

        for (let i = 0; i < tabs.length; i++) {
            let tab = tabs[i];
            let tabId = tab.id;

            if (tabId) {
                tab.addEventListener("click", function () {
                    window.history.pushState("", "", `?tab=${tabId}`);
                });
            }
        }
    })();

    // On the product pages, adds a table of contents within each tab.

    (function () {
        if (document.querySelector(".product-page")) {
            let tabs = document.querySelectorAll(".product-page .sd-tab-label");

            for (let i = 0; i < tabs.length; i++) {
                let tab = tabs[i];
                let tabId = tab.id;

                let headings = document.querySelectorAll(
                    `#${tabId} + .sd-tab-content h2[data-anchor-id]`
                );
                let toc = document.querySelector(
                    `#${tabId} + .sd-tab-content .product-tab-table-of-contents`
                );

                for (let i = 0; i < headings.length; i++) {
                    let heading = headings[i];
                    let linkElement = document.createElement("a");
                    linkElement.href = `#${heading.dataset.anchorId}`;
                    linkElement.textContent =
                        heading.textContent || heading.innerText;

                    toc.appendChild(linkElement);
                }
            }
        }
    })();

    // Classifies each type of link (anchor, internal, external) with a CSS class and also makes external links open in a new tab by default.

    (function () {
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
    })();
});

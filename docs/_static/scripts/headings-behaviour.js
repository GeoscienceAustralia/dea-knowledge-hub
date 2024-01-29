document.addEventListener("DOMContentLoaded", function (event) {
    // Move the anchor IDs from the section elements to the headings

    let sections = document.querySelectorAll("section[id]");

    for (let i = 0; i < sections.length; i++) {
        let section = sections[i];
        let id = section.id;
        section.removeAttribute("id");
        section.querySelector("* > h2, * > h3").id = id;
    }

    // Add anchor ID from the custom ID element above the heading

    let headings2 = document.querySelectorAll("h2, h3");

    for (var i = 0; i < headings2.length; i++) {
        let heading = headings2[i];
        let maybeCustomIdElement = heading.previousSibling;

        if (maybeCustomIdElement && maybeCustomIdElement.tagName.toLowerCase() === "span" && maybeCustomIdElement.hasAttribute("id")) {
            let customId = maybeCustomIdElement.id;
            heading.id = customId;
        }
    }

    // Convert the 'rubric' elements to H2 headings

    let rubrics = document.querySelectorAll("p.rubric");

    for (let i = 0; i < rubrics.length; i++) {
        let rubric = rubrics[i];
        let h2 = document.createElement("h2");
        h2.id = rubric.id;
        h2.class = rubric.class;
        h2.innerHTML = rubric.innerHTML;
        rubric.parentNode.replaceChild(h2, rubric);
    }

    // Clicking on a heading will add its anchor ID to the URL
    // E.g. /example/#introduction

    let headings = document.querySelectorAll("h2[id], h3[id]");

    for (var i = 0; i < headings.length; i++) {
        let heading = headings[i];
        let anchorId = heading.id;

        if (anchorId) {
            heading.classList.add("anchor-heading");

            heading.addEventListener("click", function() {
                window.location.hash = `#${anchorId}`
            });
        }
    }

    // Clicking on a product tab will add its ID to the URL
    // E.g. /example/?tab=overview

    let tabs = document.querySelectorAll(".product-page .sd-tab-label");
    let tabUrlParam = new URLSearchParams(window.location.search).get("tab");
    let overviewTabId = tabs[0].id;

    if(!tabUrlParam) {
        window.history.pushState("", "", `?tab=${overviewTabId}${window.location.hash}`);
    } else {
        document.querySelector(`.sd-tab-set > #${tabUrlParam}`).click();
    }

    for (let i = 0; i < tabs.length; i++) {
        let tab = tabs[i];
        let id = tab.id;

        if (id) {
            tab.addEventListener("click", function() {
                window.history.pushState("", "", `?tab=${id}`);
            });
        }
    }
});


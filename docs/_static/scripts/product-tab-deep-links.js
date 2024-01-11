// Enable linking to a specific tab on a product page by adding a parameter to the URL.
// E.g. to open the Access tab, use ?tab=access

function selectTab(tabId) {
    return document.querySelector(`.sd-tab-set > ${tabId}`)
}

document.addEventListener("DOMContentLoaded", function (event) {
    const fragment = window.location.hash;
    const tabParameter = new URLSearchParams(window.location.search).get(
        "tab"
    );

    if(selectTab(fragment)) {
        selectTab(fragment).click();
    } else if(selectTab(`#${tabParameter}`)) {
        selectTab(`#${tabParameter}`).click();
    }
});

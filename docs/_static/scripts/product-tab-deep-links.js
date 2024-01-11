// Enable linking to a specific tab on a product page by adding a parameter to the URL.
// E.g. to open the Access tab, use ?tab=access

document.addEventListener("DOMContentLoaded", function (event) {
    const tabUrlParameter = new URLSearchParams(window.location.search).get(
        "tab"
    );

    if (tabUrlParameter) {
        document.querySelector(`.sd-tab-set > #${tabUrlParameter}`).click();
    }
});

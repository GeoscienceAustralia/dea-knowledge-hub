// Enable the tabs on product pages to be linked to specifically. E.g. ?tab=access will open the Access tab.

document.addEventListener("DOMContentLoaded", function (event) {
    const tabUrlParameter = new URLSearchParams(window.location.search).get(
        "tab"
    );

    if (tabUrlParameter !== null) {
        const items = document.querySelectorAll("a.item > div");
        items.forEach(function (item) {
            if (item.textContent.includes(tabName)) {
                item.parentElement.click();
            }
        });
    }
});

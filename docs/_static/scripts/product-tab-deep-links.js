// Enable linking to a specific tab on a product page by adding a parameter to the URL.
// E.g. to open the Access tab, use ?tab=access

document.addEventListener("DOMContentLoaded", function (event) {
    const hash = window.location.hash;
    const parsedHash = hash.match(/#([^.]+).?([^.]*)/);
    const tab = parsedHash[1];
    const heading = parsedHash[2];

    if (tab) {
        const tabElement = document.querySelector(`.sd-tab-set > #${tab}`);

        tabElement && tabElement.click();

        if (heading) {
            window.location.hash = heading;
            window.location.hash = hash;
        }
    }
});

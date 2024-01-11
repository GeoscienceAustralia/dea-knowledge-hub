// Enable linking to a specific tab on a product page by adding a parameter to the URL.
// E.g. to open the Access tab, use ?tab=access

function handleTabDeepLinkHash () {
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
}

document.addEventListener("DOMContentLoaded", handleTabDeepLinkHash);
document.addEventListener("click", event => {
    if (event.target.tagName === "A") {
        handleTabDeepLinkHash();
        // event.preventDefault();
    }
});

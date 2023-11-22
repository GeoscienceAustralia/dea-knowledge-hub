document.addEventListener("DOMContentLoaded", function (event) {
    let cards = document.querySelectorAll(
        ".product-page #access-the-data-cards .sd-card"
    );

    for (let i = 0; i < cards.length; i++) {
        let card = cards[i];
        let tooltip = card.querySelector(
            "* > .sd-hide-link-text > span"
        ).textContent;
        card.title = tooltip;
    }
});

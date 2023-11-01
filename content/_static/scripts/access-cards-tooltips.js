document.addEventListener("DOMContentLoaded", function (event) {
    let cards = document.querySelectorAll(".product-page #access-cards .sd-card");

    for (let i = 0; i < cards.length; i++) {
        let card = cards[i];
        let tooltip = card.querySelector("* > a > span").textContent;
        card.title = tooltip;
    }
});

document.querySelectorAll(".access-link").forEach(function(link) {
    link.addEventListener("click", function(event) {
        gtag("event", "click", {
            "category": "access-link",
            "label": event.target.id,
            "value": event.target.href,
        });
    });
});

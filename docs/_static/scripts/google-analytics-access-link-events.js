document.addEventListener('DOMContentLoaded', function() {
    var accessLinks = document.querySelectorAll(".access-link");

    for (var i = 0; i < accessLinks.length; i++) {
        accessLinks[i].addEventListener("click", function(event) {
            gtag("event", "click", {
                "category": "access-link",
                "label": event.target.id,
                "value": event.target.href,
            });
        });
    }
});

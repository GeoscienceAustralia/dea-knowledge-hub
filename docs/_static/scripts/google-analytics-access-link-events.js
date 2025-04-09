document.addEventListener('DOMContentLoaded', function() {
    var accessLinks = document.querySelectorAll(".access-link");

    for (var i = 0; i < accessLinks.length; i++) {
        accessLinks[i].addEventListener("click", function(event) {
            console.log({
                "category": "access-link",
                "label": event.target.classList,
                "value": event.target.href,
            });
            // gtag("event", "click", {
            //     "category": "access-link",
            //     "label": event.target.classList,
            //     "value": event.target.href,
            // });
        });
    }
});

// If a class of the format 'access-link--something' exists in a classList, return 'something'.
function labelFromClassList(classList) {
    let list = Array.prototype.slice.call(classList)
    var prefix = "access-list--";

    for (var i = 0; i < list.length; i++) {
        if ([i].indexOf(prefix) === 0) {
            return list[i].substring(prefix.length);
        } else {
            return null;
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var accessLinks = document.querySelectorAll(".access-link");

    for (var i = 0; i < accessLinks.length; i++) {
        accessLinks[i].addEventListener("click", function(event) {
            console.log({
                "category": "access-link",
                "label": labelFromClassList(event.currentTarget.classList),
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

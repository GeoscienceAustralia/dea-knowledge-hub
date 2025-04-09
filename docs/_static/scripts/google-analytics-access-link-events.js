function labelFromClassList(classList) {
    let list = Array.prototype.slice.call(classList)
    let regex = /access-link-[a-zA-Z0-9]+/;
    for (var i = 0; i < list.length; i++) {
        if (regex.test(list[i])) {
            return list[i];
        }
    }
    return null;
}

document.addEventListener('DOMContentLoaded', function() {
    var accessLinks = document.querySelectorAll(".access-link");

    for (var i = 0; i < accessLinks.length; i++) {
        accessLinks[i].addEventListener("click", function(event) {
            console.log({
                "category": "access-link",
                "label": labelFromClassList(event.target.classList),
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

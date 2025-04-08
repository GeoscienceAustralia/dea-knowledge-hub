document.querySelectorAll(".access-link").forEach(function(link) {
    link.addEventListener("click", function(event) {
        gtag("event", "click_access_link", {
            "link_type": event.target.id,
            "link_url": event.target.href,
        });

        // Ensure the event is sent before the page unloads by delaying for 0.3 seconds
        setTimeout(function() {
          window.location.href = url;
        }, 300);
    });
});

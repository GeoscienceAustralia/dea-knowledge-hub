// Append the access date to the citations on the product pages. The access date is always today's date.
// E.g. [Accessed 1 January 2024]

document.addEventListener("DOMContentLoaded", function (event) {
    function appendAccessDate(citation) {
        const months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ];
        const citationTrimmed = citation.replace(/\n$/, "");
        const today = new Date();
        const day = today.getDate();
        const month = months[today.getMonth()];
        const year = today.getFullYear();
        return `${citationTrimmed} [Accessed ${day} ${month} ${year}]`;
    }

    const citations = [
        document.getElementById("data-citation"),
        document.getElementById("paper-citation")
    ];

    for (let i = 0; i < citations.length; i++) {
        const citation = citations[i];
        if (citation) {
            const pre = citation.querySelector("pre");
            pre.textContent = appendAccessDate(pre.textContent);
        }
    }
});

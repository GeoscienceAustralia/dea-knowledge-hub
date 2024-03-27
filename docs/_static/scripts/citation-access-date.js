// Append the access date to the citations on product pages

document.addEventListener("DOMContentLoaded", function (event) {
    function appendAccessDate(citation) {
        const citationTrimmed = citation.replace(/\n$/, "");
        const today = new Date();
        const day = today.getDate();
        const month = today.toLocaleString("default", { month: "long" });
        const year = today.getFullYear();
        return `${citationTrimmed} [Accessed ${day} ${month} ${year}]`;
    }

    const dataCitation = document
        .getElementById("data-citation")
        .querySelector("pre");
    const paperCitation = document
        .getElementById("paper-citation")
        .querySelector("pre");

    dataCitation.textContent = appendAccessDate(dataCitation.textContent)
    paperCitation.textContent = appendAccessDate(paperCitation.textContent)
});

// Append the access date to the citations on product pages

document.addEventListener("DOMContentLoaded", function (event) {
    function removeNewlineAtEnd(str) {
        return str.replace(/\n$/, "");
    }

    const accessedDate = (() => {
        const date = new Date();
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        return ` [Accessed ${year}-${month}-${day}]`;
    })();

    const dataCitation = document
        .getElementById("data-citation")
        .querySelector("pre");
    const paperCitation = document
        .getElementById("paper-citation")
        .querySelector("pre");

    dataCitation.textContent =
        removeNewlineAtEnd(dataCitation.textContent) + accessedDate;
    paperCitation.textContent =
        removeNewlineAtEnd(paperCitation.textContent) + accessedDate;
});

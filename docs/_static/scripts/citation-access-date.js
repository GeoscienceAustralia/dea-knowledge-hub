// Append the access date to the citations on product pages

document.addEventListener("DOMContentLoaded", function (event) {
    const dataCitation = document
        .getElementById("data-citation")
        .querySelector("pre");
    const paperCitation = document
        .getElementById("paper-citation")
        .querySelector("pre");

    const todayInternationalFormat = (() => {
        const date = new Date();
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        return `${year}-${month}-${day}`;
    })();

    dataCitation.textContent += " Accessed: " + todayInternationalFormat;
});

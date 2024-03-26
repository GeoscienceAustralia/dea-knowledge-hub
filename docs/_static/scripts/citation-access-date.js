// Append the access date to the citations on product pages

document.addEventListener("DOMContentLoaded", function (event) {
    const dataCitation = document
        .getElementById("data-citation")
        .querySelector("pre");
    const paperCitation = document
        .getElementById("paper-citation")
        .querySelector("pre");

    const today = new Date();

    const year = today.getFullYear();
    const month = today.getMonth() + 1; // Months are zero-based, so we add 1
    const day = today.getDate();

    const scientificDate =
        year +
        "-" +
        month.toString().padStart(2, "0") +
        "-" +
        day.toString().padStart(2, "0");

    dataCitation.textContent += " Accessed: " + scientificDate;
});

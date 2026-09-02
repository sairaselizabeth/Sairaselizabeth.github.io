document.querySelectorAll("nav a").forEach(function(link) {

    link.addEventListener("click", function() {

        const target = document.querySelector(
            link.getAttribute("href")
        );

        if (target) {
            target.scrollIntoView({
                behavior: "smooth"
            });
        }

    });

});

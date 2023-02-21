const navAnim = () => {
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".nav-links li");
    const navlinks = document.querySelectorAll(".nav-links li");

    burger.addEventListener("click", () => {
        nav.classList.toggle("nav-active");
    });
};
navAnim();
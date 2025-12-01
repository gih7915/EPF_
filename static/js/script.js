const openModal = document.querySelectorAll(".open-modal");
const closeModal = document.querySelectorAll(".close-modal");
const modals = document.querySelectorAll(".modal");

openModal.forEach(button => {
    button.addEventListener("click", () => {
        const modalId = button.getAttribute("modal-id");
        const modal = document.getElementById(modalId);
        modal.classList.add("open");
    });
});

closeModal.forEach(button => {
    button.addEventListener("click", () => {
        const modal = button.closest(".modal");
        modal.classList.remove("open");
    });
});
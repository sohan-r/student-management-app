
function openModal() {
  document.getElementById("studentModal").style.display = "block";
}

function closeModal() {
  document.getElementById("studentModal").style.display = "none";
}

window.onclick = function(event) {
  const modal = document.getElementById("studentModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
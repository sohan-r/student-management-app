
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

function openEditModal(id, name, subject, marks) {
  document.getElementById("editModal").style.display = "block";
  document.getElementById("editName").value = name;
  document.getElementById("editSubject").value = subject;
  document.getElementById("editMarks").value = marks;

  const form = document.getElementById("editForm");
  form.action = `/edit/${id}`;
}

function closeEditModal() {
  document.getElementById("editModal").style.display = "none";
}

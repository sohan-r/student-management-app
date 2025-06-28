function openModal() {
  const modal = document.getElementById("studentModal");
  modal.style.display = "flex";  // Use 'flex' to trigger centering
}

function closeModal() {
  const modal = document.getElementById("studentModal");
  modal.style.display = "none";
}

function openEditModal(id, name, subject, marks) {
  const modal = document.getElementById("editModal");
  modal.style.display = "flex";  // Use 'flex' to center this modal too

  document.getElementById("editName").value = name;
  document.getElementById("editSubject").value = subject;
  document.getElementById("editMarks").value = marks;

  const form = document.getElementById("editForm");
  form.action = `/edit/${id}`;
}

function closeEditModal() {
  const modal = document.getElementById("editModal");
  modal.style.display = "none";
}

// Close modals when clicking outside
window.onclick = function (event) {
  const studentModal = document.getElementById("studentModal");
  const editModal = document.getElementById("editModal");

  if (event.target === studentModal) {
    studentModal.style.display = "none";
  }
  if (event.target === editModal) {
    editModal.style.display = "none";
  }
};

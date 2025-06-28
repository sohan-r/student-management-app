let isEditMode = false;
let editingId = null;

function openAddModal() {
  isEditMode = false;
  editingId = null;
  document.getElementById('modal-title').textContent = 'Add Student';
  document.getElementById('modal-id').value = '';
  document.getElementById('modal-name').value = '';
  document.getElementById('modal-subject').value = '';
  document.getElementById('modal-marks').value = '';
  document.getElementById('modal').classList.remove('hidden');
}

function openEditModal(id, name, subject, marks) {
  isEditMode = true;
  editingId = id;
  document.getElementById('modal-title').textContent = 'Edit Student';
  document.getElementById('modal-id').value = id;
  document.getElementById('modal-name').value = name;
  document.getElementById('modal-subject').value = subject;
  document.getElementById('modal-marks').value = marks;
  document.getElementById('modal').classList.remove('hidden');
}

function closeModal() {
  document.getElementById('modal').classList.add('hidden');
}

function submitModal() {
  const name = document.getElementById('modal-name').value.trim();
  const subject = document.getElementById('modal-subject').value.trim();
  const marks = parseInt(document.getElementById('modal-marks').value);

  if (!name || !subject || isNaN(marks)) {
    alert('Please fill all fields correctly.');
    return;
  }

  if (isEditMode && editingId) {
    fetch('/update_student', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: editingId, marks })
    }).then(res => res.json())
      .then(() => location.reload());
  } else {
    fetch('/add_student', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, subject, marks })
    }).then(res => res.json())
      .then(() => location.reload());
  }

  closeModal();
}

function deleteStudent(id) {
  if (!confirm('Are you sure you want to delete this student?')) return;

  fetch(`/delete_student/${id}`, {
    method: 'DELETE'
  }).then(res => res.json())
    .then(() => location.reload());
}

function openModal() {
  document.getElementById("studentModal").style.display = "block";
}

function closeModal() {
  document.getElementById("studentModal").style.display = "none";
}

window.onclick = function(event) {
  let modal = document.getElementById("studentModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
};


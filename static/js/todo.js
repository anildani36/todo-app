const API = "/todos";
const list = document.getElementById("todo-list");
const loader = document.getElementById("loader");

function showAlert(msg, type="success") {
  document.getElementById("alert-container").innerHTML =
    `<div class="alert alert-${type}">${msg}</div>`;
}

async function loadTodos() {
  loader.classList.remove("d-none");
  const res = await fetch(API);
  const data = await res.json();
  loader.classList.add("d-none");

  list.innerHTML = "";
  data.todos.forEach(t => {
    list.innerHTML += `
      <div class="col-md-4 mb-3">
        <div class="card todo-card priority-${t.priority}">
          <div class="card-body">
            <h5>${t.title}</h5>
            <p>${t.description || ""}</p>
            <span class="badge bg-secondary">Due: ${t.due_date || "N/A"}</span>
            <div class="mt-2">
              <button class="btn btn-sm btn-outline-primary" onclick="editTodo(${t.id})">
                <i class="bi bi-pencil"></i>
              </button>
              <button class="btn btn-sm btn-outline-danger" onclick="deleteTodo(${t.id})">
                <i class="bi bi-trash"></i>
              </button>
            </div>
          </div>
        </div>
      </div>`;
  });
}

async function deleteTodo(id) {
  if (!confirm("Delete this todo?")) return;
  await fetch(`${API}/${id}`, { method: "DELETE" });
  showAlert("Todo deleted");
  loadTodos();
}

document.getElementById("todo-form").onSubmit = async e => {
  e.preventDefault();
  const id = document.getElementById("todo-id").value;
  const payload = {
    title: title.value,
    description: description.value,
    priority: priority.value,
    due_date: due_date.value || null
  };

  document.getElementById("save-spinner").classList.remove("d-none");

  await fetch(id ? `${API}/${id}` : API, {
    method: id ? "PUT" : "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  document.getElementById("save-spinner").classList.add("d-none");
  bootstrap.Modal.getInstance(todoModal).hide();
  showAlert("Todo saved");
  loadTodos();
};

loadTodos();

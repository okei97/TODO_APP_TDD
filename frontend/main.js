const API_BASE = 'http://127.0.0.1:8000';

async function fetchTodos() {
  const res = await fetch(`${API_BASE}/todos`);
  const todos = await res.json();

  const list = document.getElementById('todoList');
  list.innerHTML = '';

  todos.forEach((todo) => {
    const li = document.createElement('li');
    li.textContent = `${todo.title} (${todo.completed})`;
    list.appendChild(li);
  });
}

async function addTodo() {
  const input = document.getElementById('titleInput');
  const title = input.value;

  await fetch(`${API_BASE}/todos`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title }),
  });

  input.value = '';
  fetchTodos();
}

// 初回表示
fetchTodos();

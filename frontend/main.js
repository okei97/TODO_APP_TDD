const API_BASE = 'http://127.0.0.1:8000';

function renderTodos(todos) {
  const list = document.getElementById('todoList');
  list.innerHTML = '';

  todos.forEach((todo) => {
    const li = document.createElement('li');

    const title = document.createElement('span');
    title.textContent = todo.title;
    if (todo.completed) title.style.textDecoration = 'line-through';

    const btn = document.createElement('button');
    btn.textContent = todo.completed ? '済' : '完了にする';
    btn.disabled = todo.completed; // 完了済みはボタン無効

    btn.addEventListener('click', async () => {
      btn.disabled = true; // 二重クリック防止
      try {
        await completeTodo(todo.id);
        await fetchTodos(); // 反映
      } catch (error) {
        btn.disabled = false; // エラー時は再度クリック可能に
        alert(`完了に失敗：${error.message}`);
      }
    });

    li.appendChild(title);
    li.appendChild(btn);
    // 完了日付の表示（ボタンの右側）
    if (todo.completed && todo.completed_at) {
      const completedAt = document.createElement('span');
      completedAt.style.marginLeft = '8px';
      // ISO8601文字列を日本語日付に変換
      const date = new Date(todo.completed_at);
      completedAt.textContent = `完了日時: ${date.toLocaleString('ja-JP', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' })}`;
      li.appendChild(completedAt);
    }
    list.appendChild(li);
  });
}

async function fetchTodos() {
  const res = await fetch(`${API_BASE}/todos`);
  const todos = await res.json();

  renderTodos(todos);
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

async function completeTodo(id) {
  const res = await fetch(`${API_BASE}/todos/${id}/complete`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `HTTP ${res.status}`);
  }

  return await res.json();
}

// 初回表示
fetchTodos();

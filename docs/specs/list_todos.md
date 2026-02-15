# Todoリスト（list_todos）

## 概要

保存されているTodoを取得して返す。

- 対象ユースケース：list_todos
- 対象API：GET /todos

## リクエスト

### Body(JSON)

- なし

## レスポンス

### 成功（200）

Todoの配列を返す。

- 各要素は以下の構造を持つ
  - id: string
  - title: string
  - completed: boolean
- 返却順序は保証しない

例：

```json
[
  {
    "id": "xxxx",
    "title": "test1",
    "completed": false
  },
  {
    "id": "yyyy",
    "title": "test2",
    "completed": false
  }
]
```

## テスト観点

### 正常系

- 保存済みのTodoがすべて返却されること
- todoが0件の時、空のリストを受け取ること

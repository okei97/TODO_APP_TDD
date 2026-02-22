# Todoリスト（list_todos）

## 概要

保存されているTodoを取得して返す。

- 対象ユースケース：list_todos
- 対象API：GET /todos

## リクエスト

### Body(JSON) ※GETだからいらない消す

- なし

## レスポンス

### 成功（200）

Todoの配列を返す。

- 各要素は以下の構造を持つ
  - id: string
  - title: string
  - completed: boolean
  - completed_at: string | null（未完了はnull、完了時はISO8601文字列）
- 返却順序は保証しない

例：

```json
[
  {
    "id": "xxxx",
    "title": "test1",
    "completed": false,
    "completed_at": null
  },
  {
    "id": "yyyy",
    "title": "test2",
    "completed": true,
    "completed_at": "2026-02-22T15:30:00+09:00"
  }
]
```

## テスト観点

### 正常系

- 保存済みのTodoがすべて返却されること
- todoが0件の時、空のリストを受け取ること
- 各Todoが completed_at: string | null を満たすこと（未完了はnull、完了済みはstring）  
  ※id, title, completedについてもテストを追加する？共通アサーション関数とするといいかも

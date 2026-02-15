# Todo完了（complete_todo）

## 概要

Todoを完了して返す。

- 対象ユースケース：complete_todo
- 対象API：PATCH /todos/{todo_id}/complete

## リクエスト

### Body(JSON)

なし

## レスポンス

### 成功（200）

- completedをtrueにして返す。
  - 未完了(false) -> 完了(true)
- すでにcompleted=trueのTodoの場合エラーを返す。

例：

```json
{
  "id": "xxxx",
  "title": "test",
  "completed": true
}
```

### エラー

### 400（Business Rule / Domain）

- すでにcompleted=trueのTodoを完了しようとした場合

## テスト観点

### 正常系

- completedがtrueになること

### 異常系

- PATCHを2回実行すると2回目は400になること

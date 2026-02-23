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
- completed_atには、完了操作が実行された時刻を設定する。（ISO8601形式）

例：

```json
{
  "id": "xxxx",
  "title": "test",
  "completed": true,
  "completed_at": "2026-02-22T15:30:00+09:00"
}
```

### エラー

### 400（Business Rule / Domain）

- すでにcompleted=trueのTodoを完了しようとした場合

### 404

- 存在しないidを指定した場合 ※現在の実装では400エラーが返る（要改修）

## テスト観点

### 正常系

- completedがtrueになること
- completed_atに現在時刻(ISO8601文字列)が入ること

### 異常系

- PATCHを2回実行すると2回目は400になること
- 存在しないidを指定したときエラーとなること

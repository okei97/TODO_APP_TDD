# Todo作成（create_todo）

## 概要

Todoを作成して返す。

- 対象ユースケース：create_todo
- 対象API：POST /todos

## リクエスト

### Body(JSON)

- title: string（必須）

#### 制約

- 1〜100文字
- 空文字は不可

## レスポンス

### 成功（201）

Todoを返す。

- id: string（UUID形式の自動生成値）
- title: string
- completed: boolean（初期値 false）
- completed_at: string | null（未完了はnull、完了時はISO8601文字列）

例：

```json
{
  "id": "xxxx",
  "title": "test",
  "completed": false,
  "completed_at": null
}
```

### エラー

### 422（Request Validation）

- titleが省略された場合(Pydanticのバリデーション)

### 400（Business Rule / Domain）

- titleが空文字の場合
- titleが101文字以上の場合

## テスト観点

### 正常系

- titleが1文字でも作成できること
- titleが100文字でも作成できること
- completedの初期値はfalseこと
- idが自動生成されること
- completed_atの初期値はnullであること
- 作成が成功したときに201のレスポンスが返ってくること

### 異常系

- titleが空文字の場合400エラーになること
- titleが101文字以上の場合400エラーになること
- titleが省略されている場合422エラーになること

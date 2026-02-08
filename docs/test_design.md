# テスト観点（Todo作成）

## 正常系

- titleが1文字の場合、Todoが作成される
- titleが最大長（100文字）の場合、Todoが作成される
- completedは初期状態でfalseになる
- 作成されたTodoにはidが自動生成される

## 異常系

- titleが空文字の場合、エラーになる（400エラー）
- titleが最大長以上の場合、エラーになる（400エラー）
- titleが省略された場合、エラーになる（422エラー）

## 境界値

- title：1～100文字

# 各テストの位置づけ

## domain テスト（単体テスト）

実装済み：

- test_todo_empty_title：空文字でのエラー
- test_todo_initial_completed_false：completed初期値がfalse
- test_todo_title_one_character：1文字での作成
- test_todo_title_max_length：100文字での作成
- test_todo_title_exceeds_max_length：101文字でのエラー
- test_todo_id_auto_generated：idの自動生成

## usecase テスト（機能テスト）

実装済み：

## API テスト（統合テスト）

### create_todo API

実装済み：

- test_create_todo_success：正常な作成
- test_create_todo_title_one_character：1文字での作成
- test_create_todo_title_max_length：100文字での作成
- test_create_todo_without_title：titleが省略されたことでのバリデーションエラー（422）
- test_create_todo_empty_title：空文字でのビジネスロジックエラー（400）
- test_create_todo_title_exceeds_max_length：101文字でのビジネスロジックエラー（400）
- test_create_todo_has_id：idが返される

### get_todos API

実装済み：

- test_get_todo_list_empty：空のリスト取得
- test_get_todo_after_post：POST後のGET
- test_get_todo_has_id：取得したTodoにidが含まれる

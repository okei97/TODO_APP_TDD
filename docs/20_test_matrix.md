# POST /todos

| 仕様                       | domain                             | usecase                     | api                                     |
| -------------------------- | ---------------------------------- | --------------------------- | --------------------------------------- |
| titleが1文字               | test_todo_title_one_character      | -                           | test_post_todo_title_one_character      |
| titleが100文字             | test_todo_title_max_length         | -                           | test_post_todo_title_max_length         |
| completed初期値がfalse     | test_todo_initial_state            | -                           | -                                       |
| 正常な作成                 | -                                  | test_create_todo_saves_todo | test_post_todo_success                  |
| titleがない→422            | -                                  | -                           | test_post_todo_without_title            |
| titleが空文字→400          | test_todo_empty_title              | -                           | test_post_todo_empty_title              |
| titleが101文字→400         | test_todo_title_exceeds_max_length | -                           | test_post_todo_title_exceeds_max_length |
| 固有idが自動付与される     | test_todo_id_auto_generated        | -                           | test_post_todo_has_id                   |
| completed_atの初期値がnull | test_todo_initial_state            | -                           | test_post_todo_success                  |

# GET /todos

| 仕様                               | domain | usecase                             | api                      |
| ---------------------------------- | ------ | ----------------------------------- | ------------------------ |
| 保存されているTodoが一覧に含まれる | -      | test_list_todos_returns_saved_todos | -                        |
| 空のリスト取得                     | -      | -                                   | test_get_todo_list_empty |
| 作成済みTodoがGETで取得できる      | -      | -                                   | test_get_todo_after_post |
| 取得したTodoにidが含まれる         | -      | -                                   | test_get_todo_has_id     |

# PATCH /todos/{id}/complete

| 仕様                              | domain                                                 | usecase                    | api                                        |
| --------------------------------- | ------------------------------------------------------ | -------------------------- | ------------------------------------------ |
| completedがtrueになる             | test_todo_completed_sets_true                          | test_complete_todo_success | test_patch_complete_success                |
| completedがtrueの時trueにできない | test_todo_complete_when_already_completed_raises_error | -                          | test_patch_complete_when_already_completed |
| 存在しないid                      | -                                                      | -                          | -                                          |
| completed_atに現在時刻が入ること  | -                                                      | test_complete_todo_succes  | -                                          |

## 概要 個人学習用に作成したシンプルなTodoアプリです。

## 目的

- QA出身の自分が、設計〜実装〜テストの流れを一通り経験するため
- 小規模でも「変更しやすい構成」を意識するため

## 技術スタック

- Backend: Python (FastAPI)
- Frontend: TypeScript
- Test: pytest（簡単な自動テスト）

## 工夫した点

- ロジックとI/Oを分離し、テストしやすい構成にした
- バリデーションを実装段階で行い、不具合を防止
- テストケースを先に考えてから実装した
- usecaseとdomainでテストが重複しないようにした

## セットアップと実行

### 必要なパッケージのインストール

```bash
pip install fastapi uvicorn pytest
```

### サーバーの起動

```bash
cd backend
python -m uvicorn app.main:app --reload
```

サーバーは http://localhost:8000 で起動します。
API ドキュメントは http://localhost:8000/docs で確認できます。

### テストの実行

```bash
cd backend
pytest
```

## 今後の改善点

- 認証機能追加
- エラーハンドリングの強化
- CIへのテスト組み込み

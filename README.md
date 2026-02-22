# Todo App

## 概要

設計・テスト・レイヤー分離を意識して実装したバックエンド中心のTodoアプリです。

## 目的

- レイヤー分離設計（Domain / UseCase / Interface / Infrastructure）の実践
- テスト駆動に近い開発プロセスの検証
- 変更に強い構造の検討

## 特徴

- レイヤー分離設計を採用
- 400（ビジネスルール）と422（リクエストバリデーション）を分離
- Domain / UseCase / API でテストを分離
- GitHub Actionsでpytestを自動実行（CI導入）

## 技術スタック

- Python
- FastAPI
- Pydantic
- pytest

## ディレクトリ構成

```
backend/
├── app/
│ ├── domain/ # エンティティ・業務ルール
│ ├── usecase/ # ユースケース
│ ├── interface/ # FastAPI・スキーマ
│ └── infrastructure/ # Repository実装
└── tests/
    ├── domain/
    ├── usecase/
    └── api/

docs/ # 仕様・設計・振り返りドキュメント
frontend/ # 簡易フロントエンド
.github/workflows/ # CI設定
```

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
APIドキュメントは http://localhost:8000/docs で確認できます。

### テストの実行

```bash
cd backend
pytest -v
```

## 今後の改善予定

### 機能面

- 存在しないid指定時の404対応
- 認証機能追加

### 設計・技術検証

- Repository実装をin-memoryからSQLite / PostgreSQLへ差し替え検証
- REST→GraphQLへの変更検証
- frontend/backendのTypeScript化

## 開発プロセス

本プロジェクトでは、テスト観点を明確にしながら実装を進め、
実装を通して発見した曖昧さを仕様へ反映するサイクルを意識しました。
詳細は以下を参照。
開発プロセス
[Development Process](docs/97_development-process.md)
振り返り
[Retrospective](docs/99_retrospective.md)

# アーキテクチャ

- Domain層：業務ルール
- UseCase層：ユースケースの実行
- Interface層：API入出力
- Infrastructure層：DBアクセス

### 設計根拠

- DB変更に対応可能な設計
- API変更に対応可能な設計
- テストが壊れにくい設計
- 各層の役割を切り分けて考えているため、テストを保守しやすい

# レイヤーの責務

## Domain

- Todoエンティティ
- バリデーションルール

## UseCase

- create_todo
- list_todo
- complete_todo

## Interface

- FastAPIのエンドポイント
- Pydanticスキーマ

## Infrastructure

- Repository実装

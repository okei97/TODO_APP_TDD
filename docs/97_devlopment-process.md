# Development Process

本プロジェクトでは、変更に強い設計とテスト駆動を意識するために以下のプロセスで開発を行う。

## 1. Feature Branch 作成

- mainからfeatureブランチを切る

## 2. 要件定義

- docs/specsに要件を文章化
- 受け入れ観点整理
- 仕様変更があればここを更新する

## 3. テスト実装

- 失敗するテストを書く

## 4. 実装

- テストを通す最小実装

## 5. リファクタリング

- 責務分離を確認

## 6. CI確認

- GitHub Actions により自動テストを実行
- pytest / pytest-cov でカバレッジを確認
- カバレッジが95%を下回る場合はCIを失敗とする。

## 7. Pull Request → Merge

- PR作成
- mainへマージ

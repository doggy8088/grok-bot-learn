---
title: GitHub CLI（gh）
sidebar: false
prev: false
next: false
---

# GitHub CLI（gh）

<ToolMeta id="gh" />

GitHub 公式のコマンドラインツールです。Bot が**クラウド PC**上でプライベートリポジトリのクローン、コードのプッシュ、PR の作成、Actions の管理を行うのに適しています。

結論として：本ツールは、Bot がクラウド PC 上で GitHub プライベートリポジトリをクローンし、コードをプッシュし、PR を作成し、Actions を管理するためにのみ使用します。

## Bot に送信するプロンプト

以下の內容を丸ごとコピーして Grok Bot に送信してください。クラウド PC 上で自動的にインストールと検証が行われ、ログインや認証が必要になると一時停止して操作を待機します。

<div class="tool-prompt">

````text
幫我在你的雲端電腦上安裝 GitHub CLI（https://github.com/cli/cli/blob/trunk/docs/install_linux.md），以後管理程式碼倉庫、推送分支和提交 PR 用它。需要登錄或授權時停下來把連結發給我由我完成。
````

</div>

## ご自身で行う作業

- GitHub アカウントを準備する。
- ブラウザで認証リンクを開き、対応するワンタイム認証コードを入力する。

## 出典

- [GitHub CLI Linux インストールドキュメント](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- [gh auth login 公式マニュアル](https://cli.github.com/manual/gh_auth_login)

> 本ページはコミュニティによる非公式なまとめであり、対象ツールのベンダーおよび xAI との提攜関係はありません。コマンドの仕様は公式ドキュメントに準拠します。

[← 目次に戻る](/tools/)

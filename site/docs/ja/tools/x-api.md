---
title: X API 投稿（OAuth 1.0a PIN）
sidebar: false
prev: false
next: false
---

# X API 投稿（OAuth 1.0a PIN）

<ToolMeta id="x-api" />

OAuth 1.0a PIN 認証に基づく X 公式 API 連攜ソリューションです。Bot が**クラウド PC**上で安全に投稿、畫像アップロード、投稿削除タスクを実行するのに適しています。

結論として：本ツールは、Bot がクラウド PC 上で投稿、畫像アップロード、投稿削除を行うためだけに使用されます。

## Bot に送信するプロンプト

以下の內容をすべてコピーして Grok Bot に送信してください。クラウド PC 上で自動的にインストールと検証が行われます。ログインや API キーの設定が必要な場合は一時停止し、ユーザーの操作を待ちます。

<div class="tool-prompt">

````text
幫我在你的雲端電腦上組態 X API 發文（https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth），以後發文、傳圖和管理推文用它。需要填密鑰時請提醒我自己填，需要登錄授權時把連結發給我。
````

</div>

## ユーザー自身で行う作業

- X Developer Platform でアプリを作成し、読み取り・書き込み権限を有効にする。
- 認証リンクを開き、ページに表示された PIN コードを Bot に送信する。

## 出典

- [X 公式ドキュメント：PIN-based OAuth](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth)

> このページはコミュニティによる非公式なまとめであり、ツールのベンダーおよび xAI との提攜関係はありません。コマンドの詳細は公式ドキュメントに準拠します。

[← 目次に戻る](/tools/)

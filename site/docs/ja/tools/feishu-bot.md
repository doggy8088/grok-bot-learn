---
title: Feishu ボット長接続
sidebar: false
prev: false
next: false
---

# Feishu ボット長接続

<ToolMeta id="feishu-bot" />

Feishu 公式 Python SDK をベースにした長接続メッセージングソリューションで、パブリック IP が不要な**クラウド PC**上でイベントリスニングやグループチャットボット連攜を実現するのに適しています。

## Bot に送信するプロンプト

以下の內容をすべてコピーして Grok Bot に送信してください。クラウド PC 上で自動的にインストールと検証が行われ、ログインやシークレットキーの設定が必要な場合は一時停止して操作を待機します。

<div class="tool-prompt">

````text
幫我在你的雲端電腦上組態基於飛書 Python SDK（https://github.com/larksuite/oapi-sdk-python）的長連線機器人，以後接收群聊事件和派發任務用它。需要填密鑰時請提醒我自己填。
````

</div>

## ご自身で行う作業

- Feishu オープンプラットフォームでカスタムアプリを作成し、長接続とボット機能を有効化する。
- プロンプトの案內に従って、アプリの App ID と App Secret を自身で入力する。

## 出典

- [Feishu 公式 Python SDK（larksuite/oapi-sdk-python）](https://github.com/larksuite/oapi-sdk-python)
- [Feishu オープンプラットフォーム](https://open.feishu.cn/)

> 本ページはコミュニティによる非公式なまとめであり、該當ツールの提供元および xAI との提攜関係はありません。コマンドは公式ドキュメントに準拠します。

[← 目次に戻る](/tools/)

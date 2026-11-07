---
title: 飛書機器人長連線
sidebar: false
prev: false
next: false
---

# 飛書機器人長連線

<ToolMeta id="feishu-bot" />

基於飛書官方 Python SDK 的長連線訊息方案，適合在無需公網 IP 的 **雲端電腦** 上實作事件監聽與群聊機器人協作。

結論是：適合在無公網IP的雲端電腦上，基於長連線實作飛書事件監聽與群聊協作。

## 發給 Bot 的提示詞

複製下方整段內容發送給你的 Grok Bot，它會在雲端電腦上自動安裝並驗證，遇到登錄或組態密鑰時會暫停等待你操作。

<div class="tool-prompt">

````text
幫我在你的雲端電腦上組態基於飛書 Python SDK（https://github.com/larksuite/oapi-sdk-python）的長連線機器人，以後接收群聊事件和派發任務用它。需要填密鑰時請提醒我自己填。
````

</div>

## 需要你自己做的事

- 在飛書開放平台建立企業自建應用並開啟長連線與機器人功能。
- 根據提示自行填入應用的 App ID 與 App Secret。

## 來源

- [飛書官方 Python SDK（larksuite/oapi-sdk-python）](https://github.com/larksuite/oapi-sdk-python)
- [飛書開放平台](https://open.feishu.cn/)

> 本頁為社群非官方整理，與該工具廠商、xAI 均無隸屬關係，命令以官方文件為準。

[← 返回目錄](/tools/)

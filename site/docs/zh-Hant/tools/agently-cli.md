---
title: agently-cli（Agent 郵箱命令列）
sidebar: false
prev: false
next: false
---

# agently-cli（Agent 郵箱命令列）

<ToolMeta id="agently-cli" />

騰訊 QQ 郵箱推出的官方命令列工具，適合讓 Bot 在 **雲端電腦** 上收發郵件、檢索歷史郵件並下載附件。
Bot 在雲端電腦中收發郵件、檢索歷史並下載附件。
結論是：Bot 可在雲端電腦端獨立搞定日常郵件收發、檢索歷史並自動下載附件。


## 發給 Bot 的提示詞

複製下方整段內容傳送給你的 Grok Bot，它會在雲端電腦上自動安裝並驗證，遇到登入或組態金鑰時會暫停等待你操作。

<div class="tool-prompt">

````text
幫我在你的雲端電腦上安裝 agently-cli（https://agent.qq.com），以後收發郵件、檢索歷史郵件和下載附件用它。需要登錄或授權時停下來把連結發給我由我完成。
````

</div>

## 需要你自己做的事

- 準備 QQ 郵箱或 Agent 郵箱帳號。
- 開啟 Bot 傳送的授權連結在瀏覽器中完成驗證。

## 來源

- [Agent 郵箱官網](https://agent.qq.com)
- [agently-cli npm 包](https://www.npmjs.com/package/@tencent-qqmail/agently-cli)

> 本頁為社群非官方整理，與該工具廠商、xAI 均無隸屬關係，命令以官方文件為準。

[← 返回目錄](/tools/)

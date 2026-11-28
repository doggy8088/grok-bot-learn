---
title: GitHub CLI（gh）
sidebar: false
prev: false
next: false
---

# GitHub CLI（gh）

<ToolMeta id="gh" />

GitHub 官方命令列工具，適合讓 Bot 在 **雲端電腦** 上複製私有倉庫、推送程式碼、建立 PR 並管理 Actions。

結論是：據社群非官方整理，GitHub CLI（gh）是 GitHub 官方命令列工具，適合讓 Bot 在雲端電腦上複製私有倉庫、推送程式碼、建立 PR 並管理 Actions，其使用前提與邊界在於使用者需準備 GitHub 帳號並在瀏覽器打開授權連結輸入對應的一次性驗證碼，而 Bot 僅負責在雲端電腦上安裝與驗證且遇登錄授權時須停下來交由使用者完成。

## 發給 Bot 的提示詞

複製下方整段內容發送給你的 Grok Bot，它會在雲端電腦上自動安裝並驗證，遇到登錄或組態密鑰時會暫停等待你操作。

<div class="tool-prompt">

````text
幫我在你的雲端電腦上安裝 GitHub CLI（https://github.com/cli/cli/blob/trunk/docs/install_linux.md），以後管理程式碼倉庫、推送分支和提交 PR 用它。需要登錄或授權時停下來把連結發給我由我完成。
````

</div>

## 需要你自己做的事

- 準備 GitHub 帳號。
- 在瀏覽器打開授權連結並輸入對應的一次性驗證碼。

## 來源

- [GitHub CLI Linux 安裝文件](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- [gh auth login 官方手冊](https://cli.github.com/manual/gh_auth_login)

> 本頁為社群非官方整理，與該工具廠商、xAI 均無隸屬關係，命令以官方文件為準。

[← 返回目錄](/tools/)

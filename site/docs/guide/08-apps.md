# 第 8 章 · 連線應用、郵箱與 Secrets

## 接入順序：先跑通介面，再掛連線器

人能手動點完的事，先讓 Bot 用雲端電腦和瀏覽器去點；跑穩、驗證過價值，再換成外掛/連線器或指令碼，避免一次裝一堆外掛徒增維護。

## 外掛（連線器）

在設定裡連線支援的服務（如 Slack、GitHub、Google 等），Bot 以你的身份讀寫。外掛 ≠ 觸發器：要"某事發生就開工"請用[例程](/guide/09-routines)。

## Bot 專屬郵箱

對 Bot 說 `claim your email`，可獲得 `名字@mail.grokbot.com` 地址，用於收信、註冊網站、聯絡客戶；從該地址**發信前需要你在介面批准**。團隊帳號需管理員允許。

## Secrets

API Key 等放進設定的 **Secrets**，不要貼在對話裡。

## 技能/CLI 擴充

- 開源 Skill：把倉庫地址發給 Bot 說"幫我安裝"，所需 Key 放 Secrets。
- 雲端電腦上的 CLI 工具要在 Bot 電腦終端裡**單獨登錄**，不要拷貝本機登錄態（會互相頂 token）。

## 來源

- [官方：連線外掛](https://cursor.com/cn/help/grok-bot/connect-plugins)
- [官方：Bot 郵箱](https://cursor.com/cn/help/grok-bot/agent-email)
- [官方：Secrets](https://cursor.com/cn/help/grok-bot/secrets)
- [4.5 連線器、Skill、樣板與對外入口](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)

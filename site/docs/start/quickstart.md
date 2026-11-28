# 快速入門：第一個 Bot

## 1. 安裝與登錄

1. 從 [Cursor 儀表盤的 Grok Bot 頁面](https://cursor.com/dashboard/bot) 下載桌面端（沒有儀表盤權限就找管理員要連結）；iPhone 在 App Store 安裝（iOS 18+）。
2. 歡迎頁選 **登錄**，在瀏覽器完成認證。用的就是 Cursor 帳戶，SSO 自動生效。
3. 使用舊版隱私模式的帳戶會被提示切換（Grok Bot 需要雲端儲存）。

## 2. 認識第一個 Bot

登錄後系統自動建立一個名為 **Grok Bot** 的 Bot。要更多 Bot：側邊欄 **+ 新建聊天 → 建立新 Bot**（團隊裡可選"建立新團隊 Bot"）。

**在第一條訊息裡給它一個主要職責，並讓它記住。** 聚焦職責的 Bot 比"萬能助手"積累的上下文更有用：

```text
你的職責是產品效能。使用我們的可觀測性工具調查效能問題。
保留連結和截圖，區分證據與假設，優先說明影響最大的問題。
絕不更改正式環境設定。請記住這些要求。
```

社群推薦的"六行合同"寫法（Own / Sources / Output / Approval / Failure / Never）：

```text
Own: 負責監控目標清單的每週功能與定價變動
Sources: 關注名單、目標官網 Changelog
Output: 不超過 8 條核心動態，附日期與原始連結，存入 /workspace/scan.md
Approval: 嚴禁對外發表內容，嚴禁主動發郵件
Failure: 頁面打不開就標為缺失，嚴禁推測或編造
```

## 3. 第一個任務

好請求 = **預期結果 + 重要來源 + 約束 + 交付物 + 在哪裡停下交給你**。五分鐘出結果的例子：

```text
用五個要點總結這份文件。在單獨的部分列出每個日期、決策和
未解決的問題，並註明對應章節。不要更改源文件。
```

## 4. 登錄它需要的工具

Bot 遇到登錄頁會把電腦控制權交給你：點 **打開電腦** → 接管 → 自己輸密碼/兩步驗證 → 交還。Bot 看不到密碼，會話保留供以後使用。支援的服務也可以直接連外掛。

## 5. 審查、修正、固化

提修改意見，說清長期偏好（比如固定的報告格式）。流程穩定後存成[技能或例程](/core/skills-routines)。允許 Bot 改外部系統前，先讀[權限與人閘](/advanced/security)。

## 驗收清單

- [ ] 側邊欄能看到 Bot 處於就緒狀態
- [ ] 發中文問候，回覆是中文（Bot 名字起中文名更容易預設中文）
- [ ] 右側能調出雲端電腦實時畫面
- [ ] 第一份交付物已保存為文件

## 來源

- [官方：快速入門](https://cursor.com/cn/docs/grok-bot/get-started)
- [官方：上手](https://cursor.com/cn/help/grok-bot/onboarding)
- [1.1 Grok Bot 是什麼：一頁看懂](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [萬字長文｜Grok Bot 從入門到精通｜金塵馬](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)（摘要見實戰案例）

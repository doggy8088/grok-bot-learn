# 第 7 章 連線應用：外掛、郵箱與 Secrets

接入工具記住**先跑通介面，再掛連線器**。第三方密鑰別往聊天框貼，**存進 Secrets 只寫儲存**防洩露。

- 外掛裝太多會撐大上下文頻繁報錯；原生 X 檢索免外掛就能呼叫。
- 專屬郵箱沒收件箱介面也不彈窗，自動群發會卡在審批卡片。
- 企業環境注意 Zoom 報錯、Google Workspace 攔截與機房 IP 風控。


![連線應用：外掛、郵箱與 Secrets](/info/07-apps.png)

## 接入順序：先跑通介面，再掛連線器

### 接入步驟
1. 介面操作：**日常交易先在內建瀏覽器跑通**。
2. 官方連線器：穩定後接 Connect Apps 外掛。
3. 專用指令碼：高頻大吞吐最後調 API 或 CLI。

### 避坑與限制
- 全裝會佔上下文並引發呼叫幻覺。
- **同帳號 Bot 共享雲端電腦、瀏覽器與 `/workspace`**，建新 Bot 無法隔離憑據。

### 驗收標準
**靠最小外掛集準確完成任務**，上下文無冗餘工具宣告與誤觸發。

[《4.5 連線器、Skill、樣板與對外入口》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
[《Grok Bot Masterclass｜Avi Chawla》](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)

## 外掛連線：從商店授權到企業權限穿透

![外掛連線：從商店授權到企業權限穿透](/info/07-apps-s2.png)

外掛綁在個人帳戶且全域生效，**權限受限於第三方平台，無法提權**。

| 外掛 | 支援操作 | 限制與避坑 |
|:---|:---|:---|
| **Google Calendar** | 讀寫日程、查空閒與回邀請 | 無法改 Meet 等候室；Zoom 需手動填連結 |
| **Google Drive** | 檢索與讀取文件 | 改表格需配 Sheets；無法改分享名單 |
| **Google Sheets** | 修改有權限單元格 | 唯讀文件不可改；檢索由 Drive 處理 |
| **Slack** | 頻道發訊息 | 進不去未加入的私有與禁言頻道；非拉群 Bot |
| **Gmail** | 搜讀發郵件、加標記 | 僅限單郵箱，個人與企業郵箱不可同綁 |

詳見[連線外掛](https://cursor.com/cn/help/grok-bot/connect-plugins.md)。

1. 桌面端點側邊欄/聊天卡片「連線」，行動裝置端點頭像選「連線應用」。
2. 搜外掛點「新增」（Add）並在瀏覽器登錄授權。
3. 確認進入「已安裝」（Installed）；中中斷點「重新連線」重試。

企業 Google 遇攔截換瀏覽器無效，**認證名為「Grok」**。

管理員需在 Google Admin console 經 Security > Access and data control > API controls > App access control > Manage third-party app access 新增「Grok」（或填 Client ID）設為 Trusted。

提示「已被團隊管理員禁用」聯繫 Cursor 管理員後台開啟。

**在「已安裝」列表無黃色警告，且能正常讀資料、未觸發 OAuth 失敗即成功。**

## Bot 專屬郵箱：認領、收發規則與人閘審批

![Bot 專屬郵箱：認領、收發規則與人閘審批](/info/07-apps-s3.png)

Grok Bot 專屬郵箱（`yourname@mail.grokbot.com`）**歸屬個人帳戶**。私聊與 Routines 可用，不可在 Slack 串或他人會話呼叫，無團隊共享地址。

規則詳見文件[為你的 Bot 設定電子郵箱地址](https://cursor.com/cn/help/grok-bot/agent-email.md)。

### 使用限制與安全

| 項目 | 規則與限制 |
|---|---|
| 地址屬性 | 唯一且永久生效，**無法重命名或刪除**，註銷帳號也不釋放 |
| 發信配額 | 單封最多 50 人；附件最多 10 個（單個 ≤10MB，總量 ≤25MB，禁 `.exe`） |
| 首次外聯 | 限 1 位收件人且正文必帶退訂連結；退信或被標垃圾直接停用 |
| 收信安全 | **無獨立收件箱與通知**，1 分鐘後可查；內容唯讀，不執行指令 |

### 認領與組態

團隊須管理員在後台（`cursor.com/dashboard/bot`）開啟「Agent Email」，個人可直接用。地址限小寫字母、數位及 `.-_`，首尾須為字母數位，最長 64 字元且避開保留詞。

1. 認領地址：側邊欄進「Connect apps」>「Email」建立，或發送 `claim your email` 及命令：
```text
  給自己申請一個電子郵件地址
  ```
2. 查詢收信：對話中直接檢索：
```text
今天你的收件箱裡收到了什麼？幫我找出過去一週收到的所有費用帳單與回執。
```
3. 組態例程：建 Routine 監聽發件人（支援 `*@example.com`，不支援按主題篩選）：
```text
收到來自 billing@example.com 的電子郵件時，總結其中的帳單金額與截止日期，並將摘要整理後發送給我。
```
4. 人閘審批：**系統嚴禁無人值守靜默外發**。Bot 只生成草稿卡片，人工點選「Send」後才真正投遞。

### 驗收標準

外部發測試信後等待 1 分鐘，讓 Bot 查詢並起草回覆。**螢幕彈出待審批卡片且點選前保持掛起**即為成功。

## 安全機密資訊：Secrets 的只寫機制與團隊隔離

![安全機密資訊：Secrets 的只寫機制與團隊隔離](/info/07-apps-s4.png)

**敏感憑證絕不能發在對話框、寫進 Shell 組態或錄入「Teach a task」。** 輸入框保存後變空白是進入了保護狀態。

雲端電腦執行 `Recover` 或 `Reset` 不會丟失憑證，詳見[安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets.md)。

### 提交與更新

1. 聊天提交：Bot 索取憑據時彈出安全卡片，輸入框顯示掩碼，點「Save securely」，顯示「Saved」即完成。
2. 團隊 Bot：在設定的「Secrets」點「Add secret」，填名稱（如 `GITHUB_TOKEN`）、描述與密鑰後點「Save secret」。**更新點「Replace」與「Replace value」，系統不支援找回舊值。**
3. 網頁填入：若提示 `Could not fill into the page`，**走 Takeover flow 手動接管登錄**，切忌在對話框發帳號密碼。

### 驗收標準

- **面板僅顯示名稱與描述，密鑰值完全隱藏。**
- 對話中要明文 Bot 讀不到，但 CLI 或請求鑑權正常通過。

## X 平台原生檢索：免外掛呼叫社交動態

Grok Bot 在 v0.70.2（2026-10-08）整合了 X 唯讀檢索。**它直接走 The X Subscription 統一用量，不用裝第三方外掛，也不用配 API Token**。

1. **直接發自然語言指令**：支援全網搜帖、抓取公開推文正文，也能查帳號發文與被 @ 記錄，或統計特定話題 7 天互動趨勢。

```text
檢索 X 平台帳號 @xai 最近 24 小時發表的所有推文。按時間倒序整理每條推文的核心內容、發表時間、按讚數、轉推數，並附帶原帖連結。
```

```text
檢索 X 平台上關於 #AIagents 話題過去 7 天的熱門討論。篩選互動量最高的前 5 條推文，提取核心觀點，並彙總該話題本週的討論熱度變化趨勢。
```

2. **驗收標準**：**結果要包含發表時間、互動數位與推文原鏈**，全程沒有連線器安裝提示，也沒有抓取截斷。

功能梳理見[《4.5 連線器、Skill、樣板與對外入口》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)。

## 安裝開源 Skill 與 CLI 工具：打通本地與終端能力

### 資源邊界

| 作用域 | 包含資源與組態 |
| :--- | :--- |
| **全域共享** | 所有 Bot 共享已裝 Skill、官方連線器、共用記憶與 `/workspace` 目錄 |
| **獨立持有** | 各 Bot 獨立持有專屬工作指令、獨立記憶片段與定時例程（Routines） |

體系結構梳理參見[《4.5 連線器、Skill、樣板與對外入口》](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)與[《Grok Bot Masterclass｜Avi Chawla》](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)。

### 核心操作步驟

1. 開啟本地網路流量中繼。雲端電腦使用機房 IP，訪問 GitHub 等外部站點容易被攔截。

   在桌面端 Settings -> Computer 勾選「流量經過本地設備」（Route traffic through this computer），借本機網路中繼，客戶端與雲端需同步更新。
2. 安裝開源 Skill。在對話框直接發送倉庫地址讓 Bot 部署。如需 Access Token，等系統提示後通過安全卡片提交，**嚴禁將 Token 直接粘貼在對話框中**。

```text
幫我安裝這個開源 Skill：https://github.com/example/custom-data-skill
閱讀倉庫內的說明文件，將其註冊為我的可用技能，並告訴我它支援的觸發指令與所需參數。
```

3. 獨立登錄 Codex CLI。先在網頁端「帳戶安全與登錄」打開「設備程式碼登錄」（Device code login）。在雲端終端執行登錄命令，獲取設備驗證碼並用本機瀏覽器驗證。

   **絕對不要把本機登入憑證複製到雲端電腦 `/workspace`**，否則共用快取會導致 Token 重新整理衝突、兩端頻繁掉線。
4. CLI 代理下放重型任務。大批量程式碼格式化或轉碼等機械任務，直接寫成 Shell 指令碼交給雲端電腦 CLI 執行。配合「Wake on Done」機制接收完成通知，避免 Bot 長時間佔用高額度推理會話。

### 做到什麼程度算好

- 在雲端電腦終端執行 `codex --version` 正常輸出版本資訊，**且本機終端日常使用不會被頂替掉線**。
- 向 Bot 發送測試任務，能按流程在 `/workspace` 目錄下生成符合交付標準的結構化文件。

## 容易踩的坑

### 外掛與企業權限
- Zoom 授權報 4700 屬官方重定向缺陷，客戶端內無法修復。
- Gmail 僅支援單帳號綁定，換綁必須先斷開當前郵箱再重授。
- Google 權限審批**必須搜「Grok」，不能搜「Cursor」**，換瀏覽器沒用。

### 專屬郵箱與外發審批
- `mail.grokbot.com` 無介面與推送，查信需問 Bot 或建例程；例程僅按發件人和域名監聽（需過 SPF/DKIM），不能按主題篩選。
- 底層設有強行人閘，提示詞無法跳過，發信必須在草稿**手動點選「Send」**。

### 安全與網路環境
- Teach a task 螢幕錄影長達 10 分鐘且無 Secrets 掩碼，別輸入密碼或展示 API Key。
- 所有 Bot 共用儲存與登錄態，**機密文件別丟在 `/workspace`**。
- 拷本地 Token 會互相踢掉線，終端必須走設備碼獨立授權。
- 外部站點封機房 IP 報錯，去 Computer 頁面**開啟「流量經過本地設備」**。

## 做完怎麼驗收

1. 側邊欄確認 Drive 和 Sheets 正常。讓 Bot 找 Q3_Report 並用 Sheets 讀表格 A1 到 B10，**能讀出且不報權限錯**。
2. 用個人郵箱髮帶數位程式碼郵件到 `yourname@mail.grokbot.com`，等 2 分鐘讓 Bot 查收；讓它起草回信，**核對程式碼並點 Send 發出草稿卡片**。
3. 讓 Bot 打印 `GITHUB_TOKEN`，**必須拒絕明文或只給掩碼**；再跑測試命令能過鑑權，確認 Token 未洩漏。
4. 搜 `@xai` 24 小時前兩條高贊推文，**原連結可點且沒調第三方外掛**。
5. 終端跑 `codex --version` 報版本；本地平行處理**不衝突踢線**；開「流量經過本地設備」能打開機房敏感頁。

## 延伸閱讀

### 官方文件與支援頁面

- [連線外掛](https://cursor.com/cn/help/grok-bot/connect-plugins.md)
- [為你的 Bot 設定電子郵箱地址](https://cursor.com/cn/help/grok-bot/agent-email.md)
- [安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets.md)
- [Grok Bot 電腦](https://cursor.com/cn/help/grok-bot/computer-recovery.md)
- [例程](https://cursor.com/cn/help/grok-bot/routines.md)
- [團隊 Bot](https://cursor.com/cn/help/grok-bot/team-bots.md)
- [面向 Teams 和企業版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams.md)

### 社群實戰資料

- 《4.5 連線器、Skill、樣板與對外入口》：[飛書知識庫文件](https://jcng5q8n0f3z.feishu.cn/wiki/XDkUwLJZxih7Dok0SKqcajKQn4e)
- 《Grok Bot Masterclass｜Avi Chawla》：[飛書知識庫文件](https://jcng5q8n0f3z.feishu.cn/wiki/Qw17wVBhJibhkpkAK6zceiMvned)

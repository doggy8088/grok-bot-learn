# 第 24 章 按崗位組建你的 AI 團隊

**別把 Grok Bot 當普通聊天框或全包助手。** 雜活全塞進同個會話會導致上下文膨脹、變慢並浪費額度，夜間無人盯梢時還容易誤發郵件、改動生產程式碼或劃扣資金。

Grok Bot 底層是帶獨立瀏覽器與本地檔案系統的雲端電腦，**用好它需要按崗位建立清晰編制**。

1. **卡緊審批紅線**。按 5 條硬性信號切分崗位職責，未審核郵件、生產程式碼與劃扣資金必須停在人工審批前。
2. **跑通例程交接**。為 7 大關鍵崗位組態首個驗證任務與定時例程，在日常巡檢中把驗收標準建起來。

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

## 崗位切分的五條信號與組織原則

### 邊界劃定與環境隔離

同一帳號下所有 Bot 共享同一台雲端電腦，文件、Web 登錄態與連線器互通。但各 Bot 記憶與對話執行緒獨立，**混合處理不同交易會讓記憶塞滿無關資訊，造成指令漂移**。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 崗位切分的五條信號

**工作只要出現以下任一特徵，就該設立獨立專職 Bot。**

- 目標不同：例如負責發現系統缺陷與優化文案轉化率。
- 工具不同：例如主要連線程式碼倉庫與連線 CRM 電子表格。
- 工作風格不同：例如客服溫和剋制，資料分析嚴苛客觀只列數位。
- 審批邊界不同：例如起草內部備忘與擁有外部發信權限必須分開。
- 日程安排不同：例如每小時巡檢工單與每週一彙總財務報表。

### 通用助手與專職團隊對比

**專職團隊相比通用助手，能有效隔離上下文與權限風險。**

| 對比維度 | 通用助手（容易踩坑） | 專職 Bot 團隊 |
| :--- | :--- | :--- |
| 上下文 | 雜糅多項業務，易產生記憶混淆與幻覺 | 獨立執行緒維護專屬記憶，執行穩定 |
| 權限與排查 | 權限氾濫易誤觸高風險，衝突難定位 | 細粒度審批，失敗歸因直接 |
| 例程拓展 | 定時任務互相干擾，排期容易堵塞 | 獨立時間表或事件觸發器非同步執行 |

### 審批人閘與可逆性原則

權限管理必須堅守**以可逆性為核心的人閘規則**。

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

| 操作類別 | 典型行為範例 | 處置原則與審批機制 |
| :--- | :--- | :--- |
| 可逆操作 | 起草文件、對帳，打標記或提取摘要 | 放手讓 Bot 自主完成並記錄記錄 |
| 不可逆操作 | 對外發信、公開發表，合併程式碼或劃扣資金 | **執行前必須停下生成草稿或差異對比，掛起等待人類在介面中點選批准** |

## 從七步驗證到落地持久 Bot

**剛建好 Bot 別急著掛定時**，先按官方路徑手動跑通：[Grok Bot 使用場景](https://cursor.com/cn/docs/grok-bot/use-cases)。

1. 描述欄（Description）立規矩：寫明職責、資料源與紅線。**描述欄規則對所有任務永久生效**，聊天框指令只管單次。
2. 安全範圍跑單次：限定輸入源，手動跑真實業務。
3. 修正到可評審：對話調整直到免干預達到可評審標準。
4. 存為技能（Skill）：直接保存步驟。複雜網頁用「Teach a task」示範（上限 10 分鐘，不錄麥克風音訊），補齊分支審批。
5. 第二組獨立輸入驗證：換資料測試，排查過度適配初始範例。
6. 設 Routine 策略：建 Schedule 或 Trigger 前定好超時重試與報錯，**斷網斷資料絕不能憑空編造**。
7. 關鍵操作留審批閘：發送、支付保留人工確認（Allow once/Deny），極低風險才配 Auto Review。

## 七大核心崗位的編制、例程與提示詞

遵循上述原則，我們按業務需求將數位團隊拆分為內容、工程、銷售、研究、運營、個人助理和管理者七個標準化崗位。每個崗位均組態了明確的編制底線、首個輕量化驗證任務、自動化例程邏輯以及可直接複製的提示詞。

### 1. 內容崗：定位比對與內容管線 Bot

這個 Bot **每週一 08:00** 跑一次，抓 3 個競品頁比對我方首屏。有變動就提 PR 分支，沒變動就靜默。

- 權限：只提 PR 或排期表草稿，**嚴禁直接合並或公開發表**。
- 驗收：成果限 1 張表格和 1 段文案，30 秒內能核對完。
- 坑點：解析失敗立即報損壞連結，不進行猜測。

::: details 1. 內容崗：定位比對與內容管線 Bot
```text
每週一上午 08:00，對比我們產品定位頁 <our_landing_url> 與以下三個競品頁面：
1. <competitor_url_1>
2. <competitor_url_2>
3. <competitor_url_3>

產出以下內容：
- 主張對比表格：我方主張、對方主張、哪一方表述更直接明確。
- 競品提到但我們未提及的三項內容，需附帶原句引用。
- 我們提及但競品均未提及的三項獨有優勢。
- 改寫我方定位頁前兩段文案的草稿，使其更具針對性。

在程式碼倉庫 <repo_name> 中針對文案修改開啟一個 Pull Request，僅允許改動定位頁文案文件。
嚴禁合併該 Pull Request。嚴禁觸碰定位頁以外的程式碼或文件。
執行結束時彙報：自上週以來競品側發生的主要文字變化；若無變化則明確註明。
```
:::

### 2. 工程崗：缺陷復現與診斷 Bot

[Grok Bot 使用場景](https://cursor.com/cn/docs/grok-bot/use-cases)

1. **權限紅線**：必須用專用測試帳號，**嚴禁在預發表環境使用真實客戶資料**與修改警報或生產參數；敏感憑證走 Safe handoff，禁止明文發送。
2. **排查步驟**：監聽打上 `needs-repro` 標記的 Issue，在 Staging 啟動隔離瀏覽器執行復現。
3. **驗收標準**：**把包含預期與實際行為、網路狀態碼及截圖的草稿回填到 Issue 評論**，隨後移除標記等待工程師核查。

::: details 2. 工程崗：缺陷復現與診斷 Bot
```text
閱讀工單 <issue_url> 中的缺陷報告，並在預發表環境 <staging_url> 中嘗試復現該問題。

執行規則：
- 必須使用全新分配的測試帳號登入，嚴禁呼叫或匯入正式環境客戶資料。
- 詳細記錄完整的復現操作步驟、預期行為與實際出現的不一致表現。
- 捕獲例外發生時的主控台報錯記錄、網路請求狀態以及頁面截圖。
- 嘗試提取導致該問題的最小復現步驟。

輸出規範：
將整理好的復現包整理為 Markdown 文本附在下方。
嚴禁修改系統的報警規則，嚴禁更改預發表或正式環境組態。
若嘗試三次仍無法復現，詳細說明每次嘗試的輸入參數並標記為“未能穩定復現”，不要偽造成功的結論。
```
:::

### 3. 銷售崗：潛在客戶調研與外聯 Bot

1. 每個工作日 07:00 讀表格前 20 行未觸達線索，按 3 條核心 ICP 準則打分。
2. 挑最匹配的 3 位聯繫人，各寫不超過 4 句話的郵件草稿填進表格。
3. **嚴禁向客戶真實發信或推入自動外聯**。每句個性化陳述必須附來源連結，訪問受限立即終止報人工。

::: details 3. 銷售崗：潛在客戶調研與外聯 Bot
```text
每個工作日早晨 07:00，處理表格 <sheet_url> 中最早未觸達的 20 行銷售線索。

針對每一行資料執行以下操作：
1. 訪問該公司官網及其公開社交帳號，提取過去 30 天內的實質性變動（如產品發表、高管變動、業務調整或受關注動態）。
2. 根據以下三條 ICP 標準逐一判定：
   - 目標團隊規模在 20 至 200 人之間；
   - 核心業務包含多工具協同流程；
   - 過去一個季度內有公開擴張動態。
   若不符合標準，在狀態欄標記“不匹配”並跳過後續步驟。
3. 為符合條件的線索撰寫一段不超過 4 句話的首觸郵件草稿。必須直接引用第一步中查到的具體變動事實，禁止使用任何寒暄客套套話。
4. 將郵件草稿填入表格的“首觸草稿”列，並在相鄰列貼上佐證該事實的公開連結。

安全要求：
嚴禁向任何郵箱發送真實郵件。嚴禁將聯繫人匯入自動發送佇列。嚴禁呼叫未授權的個人帳號。
執行結束時彙報：已處理行數、排除行數，以及如果你是銷售代表會優先發送的前三位名單。
```
:::

### 4. 研究崗：事實核查與資料核算 Bot

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

對接公開網路、知識庫和用量 CSV。**缺資料必須報錯並說明缺失欄位，嚴禁憑經驗估算或給無支撐建議**。

- **首個任務**：檢索業務問題並輸出核對表，判斷提示分類為「有證據支援」「與證據矛盾」或「證據未證實」，列出資訊缺口。
- **執行例程**：**每週一上午 09:00 執行**，讀上週帳單 CSV 回答 4 個固定量化問題，**生成不超過一頁的純資料報告**。

::: details 4. 研究崗：事實核查與資料核算 Bot
```text
研究課題：<research_topic_or_question>
閱讀並分析知識庫及公開檢索信源，生成一份可供直接發表的簡報。

執行規則：
- 打開每一個引用來源頁面，嚴禁僅憑模型內部記憶作答。
- 針對報告中的每一個核心結論，摘錄支援該結論的原文章節段落。
- 對每一個主張進行事實狀態標註：分為“有證據支援”、“與證據矛盾”或“證據未證實”三類別。
- 當不同信源存在分歧時，同時列出雙方原文，並註明發表時間先後。
- 整理在調研過程中未能找到確證資訊的內容列表，將其作為正式結論的一部分列在文末。

輸出規範：
輸出一份精簡報告、一張事實來源對比表、以及尚未解決的疑問清單。
嚴禁使用似是而非的推測性陳述式填充資訊空白。如果資料源完全未提及某事，直接記錄“未找到相關記錄”。
```
:::

### 5. 運營崗：工單支援與帳務對帳 Bot

1. 工單處理：每小時自動起草解答，**回覆只能寫入 Internal Note 嚴禁發給使用者**。
2. 發票對帳：工作日 17:00 抓最新 10 份發票匹配 PO 表，標出一致、超標和缺單項，例外掛起等人工審核。
3. 權限紅線：**金額偏差超 2% 或遇到新供應商必須報警**，嚴禁擅自審批或發起轉帳。

::: details 5. 運營崗：工單支援與帳務對帳 Bot
```text
每天下午 17:00，讀取財務收件箱 <finance_inbox> 中的新增發票，與採購訂單表格 <po_sheet_url> 進行逐筆核對。

針對每張發票執行以下比對：
- 提取金額、幣種、開票日期、採購訂單號（PO Number）與供應商全稱。
- 在採購表格中查找對應的 PO 記錄。若無匹配記錄，在備註欄標明“無對應訂單”。
- 比對發票金額與 PO 批准金額。若偏差絕對值超過 2%，立即將其標記為“金額例外偏差”，並記錄具體差額。
- 檢查供應商名稱是否屬於本季度首次出現的新供應商，若是，打上“新供應商待核實”標記。

結果寫入規範：
將比對明細寫入表格 <po_sheet_url> 的“對帳結果”工作表中，並附帶該發票的原件查看連結。
嚴禁執行任何批准報銷、發起付款或向供應商發送郵件的操作。
執行結束時彙報：成功匹配筆數、例外待查筆數，以及所有存在例外的發票總金額。
```
:::

### 6. 個人助理崗：收件箱與日程管家 Bot

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

1. **日常執行**：工作日 07:30 掃描近 24 小時郵件與日程，生成單頁晨報。
2. **首個任務**：清理無效通知，針對 2 封重要郵件各擬一段不超過 4 句的草稿放進「待審核」，隨後停下等人工確認。
3. **權限紅線**：只歸檔垃圾與通知；**嚴禁刪改會計、法務，或核心客戶與管理層的郵件**；**回覆僅存草稿絕不擅發，日曆不改**。

::: details 6. 個人助理崗：收件箱與日程管家 Bot
```text
每個工作日早晨 07:30，掃描我的工作郵箱 <email_account> 與日曆 <calendar_url>。

處理規則：
1. 自動歸檔系統通知、行銷推廣與電子發票。若郵件發件人包含會計師、法務顧問或核心客戶，嚴禁自動歸檔。
2. 提取需要我親自處理的事項，按緊急程度列出，註明發件人、主要訴求與截止期限。
3. 針對其中最需要緊急回覆的 2 封郵件，以我的口吻起草回覆方案：
   - 語言簡短直接，不使用套話與客套感謝語；
   - 整體控制在 4 句話以內，明確給出下一步行動建議；
   - 若涉及約定會議時間，主動從我日曆中調取明天下午的 2 個空閒時段供對方選擇。
4. 彙總今天必須參加的會議日程，標出準備資料缺失的場次。

安全邊界：
所有生成的回覆只能存入郵箱的“待審核草稿”資料夾中，嚴禁點選發送。
嚴禁拒絕、更改或新建任何日曆日程。
文末以一頁紙以內的篇幅彙報：今日概覽、已歸檔數量、待審草稿列表，以及今天唯一一件必須由我做決定的事項。
```
:::

### 7. 管理者崗：幕僚長與跨團隊協調 Bot

作為團隊中樞，負責通讀全域、抓卡阻，並組織周度巡檢。

**權限紅線**
- 業務無進展時保持靜默。
- **嚴禁代發訊息與行動看板卡片**，只給建議，**絕不替人類做決策**。

**任務與例程**
1. 首個任務：通讀看板與 Slack 近 24 小時記錄，整理出包含卡阻、停滯及待決策項的**動態注意力清單**。
2. 工作日 18:00：整理晚報。
3. 週五 16:30：比對各專職 Bot 記錄與產出，標記低效任務並提優化或裁撤建議。

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

::: details 7. 管理者崗：幕僚長與跨團隊協調 Bot
```text
每個工作日傍晚 18:00，審閱過去 24 小時內已批准的通訊頻道 <slack_channels>、收件箱與項目看板 <board_url>。

提煉並輸出以下四部分內容，篇幅嚴格控制在一頁以內：
- 今日實質進展：提煉 5 行關鍵動態，說明關聯繫統與具體推進事項。
- 潛在風險預警：列出 3 項如果不做干預明天可能會惡化或延期的事情，說明阻礙人與卡阻天數。
- 待辦決議選項：對於必須由我決策的事項，給出選項 A 與選項 B 的利弊對比，並附帶你推薦的選項及一句理由。
- 日程減負建議：檢查我明天的日曆，挑出 1 個可以被取消或改為非同步跟進的會議，並說明原因。

輸出要求：
不發送任何外部訊息，不修改任何會議日程，不挪動看板卡片。
若全天各項指標平穩且無例外阻塞，直接輸出“今日執行平穩，無需要升級的決策事項”，不要為了湊字數生成冗餘報告。
```
:::

## 跨崗位協作與多 Bot 編排案例

多 Bot 協作的核心是靠工單流轉，**人類只做關鍵節點審批**，別當手動複製貼上的搬運工。

### SpaceXAI 產品團隊多崗位協同

Movez 梳理了 SpaceXAI 的 9 個專職席位，包括幕僚長、主管、資料分析、招聘和 5 個開發 Bot。
[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

1. **目標解耦**：人類給大目標，主管 Bot 負責拆細並派發給模組開發 Bot。
2. **鏈條傳遞**：復現 Bot 跑出驗證包直接交接，排查 Bot 修復後提 PR，**停在人類 Code Review 節點等審批**。
3. **狀態對齊**：幕僚長 Bot 動態維護清單，發現卡片連續多天無提交就提醒主管檢查。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 獨立團隊輕量出海運作

CyrilXBT 與 Codez 用 3 個 Bot 跑通了日常運作管線。
[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

| 崗位 Bot | 協作職責 | 人工把關 |
|---|---|---|
| 內容 Bot | 監測行業與競品動態，起草部落格並出多渠道分發草稿 | - |
| 銷售外聯 Bot | 檢索線索並打分，每個工作日早晨生成 20 封郵件草稿 | **負責人早晨花 10 分鐘過目批准** |
| 客戶支援 Bot | 監聽工單並對照知識庫寫內部建議 | **確認無誤後一鍵轉為公開回復** |

## 容易踩的坑

- 別做通用雜活 Bot：讓一個 Bot 兼顧報銷和發文會導致記憶膨脹、排錯困難，**堅持一個任務配一套 Bot**。[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- 別在第 6 步前開啟定時：重試與報錯機制沒調通前就跑定時，夜裡只會死循環報錯。
- 別把帳號共享當沙箱隔離：同帳號下的 Bot 共享雲端電腦和瀏覽器，要組態獨立郵箱、專用分支和採購卡，**嚴禁綁定個人核心私人帳戶**。[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- 別把長期規範寫進聊天框：聊完規則就淡出了，流程與邊界必須填在 Bot 描述欄（Description）。
- 別把監聽規則放太寬：設成“有新訊息”就觸發，會白耗大量額度還容易引發誤動作。[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- 別漏掉缺數報警：遇到介面報錯或缺欄位時 Bot 會腦補偽造，章程裡必須寫死：**資料源缺失或過期立即如實報告失敗，嚴禁擅自變通**。[Grok Bot 使用場景](https://cursor.com/cn/docs/grok-bot/use-cases)

## 做完怎麼驗收

### 30 秒即時校驗
新 Bot 交付的首個任務，**人工驗證必須能在 30 秒至 1 分鐘內完成**。比如讓財務 Bot 查前 5 行發票缺失項，或讓銷售 Bot 給 3 家指定公司打分。要是得花半小時核對原始資料，說明輸入範圍太寬或驗收標準不清，直接退回重拆。

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### 壓力測試與人閘
正式啟用前，故意喂一次高風險指令做壓力測試（比如讓它處理催款郵件並要求立即付款）：
1. 觀察它能不能**停在草稿狀態並生成審批卡片**。
2. 未獲批准如果擅自發送、合併或扣費，**立即撤回工具權限並重寫邊界約束**。

### 啟用前六要素核對
在介面點選啟用前，先把六項基礎組態核對清楚：
- 明確責任 Bot（Owning bot）
- 觸發時間與時區設定（Schedule and time zone）
- 輸入源路徑（Input source）
- 結構化預期輸出格式（Expected result）
- **卡死人工審批紅線（Approval boundary）**
- 遇到網路中斷或資料缺失時的報錯策略（Missing data policy）

### 周檢與裁撤機制
網頁排版或欄位變動會導致例程在後台悄悄失效。**每週五下午抽 15 分鐘**跑周檢提示詞，讓全團隊 Bot 彙報狀態：

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

::: details 周檢與裁撤機制
```text
全體 Bot 成員，請按各自崗位彙報本週的執行情況：
1. 本週累計觸發執行多少次，其中發生失敗或報錯的次數是多少？
2. 在執行過程中，有哪些步驟因資料缺失而跳過、重試或進行了推測？
3. 有哪些掛起等待審批的事項，我一直沒有給出答覆？
4. 本週生成的哪些文件或表格，我從未打開查閱過？

最後回答兩個核心問題：
- 在本週的執行中，哪兩個崗位之間存在明顯的重複勞動？
- 綜合目前的業務價值，你認為團隊中哪一個例程或席位最應該被精簡裁撤，理由是什麼？
```
:::

根據彙報持續評估三項長期指標：
- **真實節省工時**：比對人工操作，算出實際省下的有效時間。
- **產出修改幅度**：人類修改草稿的量持續走高，說明規則漂移，需重新校準。
- **信任軌跡判定**：多次調優依然無法穩定輸出的崗位，果斷關停或刪除。

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

## 延伸閱讀

### 官方文件
- [Grok Bot 使用場景](https://cursor.com/cn/docs/grok-bot/use-cases)

### 社群實戰
- [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

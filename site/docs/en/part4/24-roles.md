# Chapter 24 Building Your AI Team by Role

**Do not treat Grok Bot as an ordinary chatbox or an all-in-one assistant.** Cramming all odd jobs into the same conversation leads to context bloat, sluggish performance, and wasted quota; furthermore, when left unattended overnight, it can easily misfire emails, alter production code, or deduct funds.

Under the hood, Grok Bot is a cloud computer equipped with an independent browser and a local file system; **using it effectively requires establishing a clear headcount structure by role**.

1. **Tighten approval red lines.** Divide role responsibilities based on 5 hard signals; unreviewed emails, production code, and fund deductions must stop before human approval.
2. **Establish smooth routine handoffs.** Configure the first verification task and scheduled routines for the 7 key roles, building acceptance criteria through daily inspections.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)


![Building Your AI Team by Role](/info/24-roles.png)

## Five Signals for Role Division and Organizational Principles

![Five Signals for Role Division and Organizational Principles](/info/24-roles-s1.png)

### Boundary Demarcation and Environment Isolation

All Bots under the same account share the same cloud computer, with interconnected files, web login states, and connectors. However, each Bot maintains independent memory and conversation threads; **mixing different tasks fills memory with irrelevant information, causing instruction drift**.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Five Signals for Role Division

**Whenever any of the following characteristics appear in your work, you should establish an independent dedicated Bot.**

- Different objectives: e.g., discovering system bugs vs. optimizing copywriting conversion rates.
- Different tools: e.g., primarily connecting to code repositories vs. connecting to CRM spreadsheets.
- Different working styles: e.g., customer service is gentle and restrained, while data analysis is rigorous, objective, and lists only numbers.
- Different approval boundaries: e.g., drafting internal memos vs. possessing external email sending permissions must be separated.
- Different schedules: e.g., inspecting tickets hourly vs. summarizing financial reports every Monday.

### Comparison: General-Purpose Assistant vs. Dedicated Team

**Compared to general-purpose assistants, dedicated teams effectively isolate context and permission risks.**

| Comparison Dimension | General-Purpose Assistant (Error-Prone) | Dedicated Bot Team |
| :--- | :--- | :--- |
| Context | Blends multiple tasks, prone to memory confusion and hallucinations | Independent threads maintain dedicated memory, ensuring stable operation |
| Permissions & Troubleshooting | Excessive permissions easily trigger high-risk actions; conflicts are hard to pinpoint | Fine-grained approvals; straightforward failure attribution |
| Routine Expansion | Scheduled tasks interfere with each other, easily causing schedule bottlenecks | Independent schedules or event triggers execute asynchronously |

### Human Approval Gates and the Principle of Reversibility

Permission management must strictly adhere to **human gate rules centered around reversibility**.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

| Operation Category | Typical Behavior Examples | Handling Principles & Approval Mechanism |
| :--- | :--- | :--- |
| Reversible Operations | Drafting documents, reconciling accounts, tagging, or extracting summaries | Allow the Bot to complete autonomously and log actions |
| Irreversible Operations | Sending external emails, public publishing, merging code, or deducting funds | **Must halt before execution to generate drafts or diff comparisons, suspending until a human clicks approve in the UI** |

## From Seven-Step Verification to Landing Persistent Bots

![From Seven-Step Verification to Landing Persistent Bots](/info/24-roles-s2.png)

**Do not rush into setting schedules right after creating a Bot**; first run through it manually following the official path: [Grok Bot Use Cases](https://cursor.com/cn/docs/grok-bot/use-cases).

1. Set ground rules in the Description: Clearly state responsibilities, data sources, and red lines. **Description rules apply permanently to all tasks**, whereas chatbox instructions only govern single runs.
2. Run a single execution in a safe scope: Restrict input sources and manually run real business scenarios.
3. Refine until reviewable: Adjust via conversation until output reaches reviewable standards without intervention.
4. Save as a Skill: Save steps directly. For complex web pages, use "Teach a task" to demonstrate (up to 10 minutes, no microphone audio recorded), completing branch approvals.
5. Verify with a second independent input set: Test with alternative data to check for overfitting to initial examples.
6. Set Routine policies: Establish timeout retries and error handling before creating a Schedule or Trigger; **never fabricate out of thin air when network or data is unavailable**.
7. Retain approval gates for critical operations: Preserve human confirmation (Allow once/Deny) for sending and payments; only assign Auto Review to extremely low risks.

## Staffing, Routines, and Prompts for Seven Core Roles

Following the principles above, we divide the digital team into seven standardized roles based on business needs: Content, Engineering, Sales, Research, Operations, Personal Assistant, and Manager. Each role is configured with clear headcount bottom lines, a first lightweight verification task, automated routine logic, and ready-to-copy prompts.

### 1. Content Role: Positioning Comparison and Content Pipeline Bot

This Bot runs **every Monday at 08:00**, scraping 3 competitor pages to compare against our above-the-fold landing page. If changes occur, it opens a PR branch; if there are no changes, it stays silent.

- Permissions: Only opens PRs or drafts schedules; **strictly prohibited from directly merging or publicly publishing**.
- Acceptance: Deliverable is limited to 1 table and 1 paragraph of copy, verifiable within 30 seconds.
- Pitfalls: Report broken links immediately upon parsing failure; do not guess.

::: details 1. Content Role: Positioning Comparison and Content Pipeline Bot
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

### 2. Engineering Role: Bug Reproduction and Diagnostics Bot

[Grok Bot Use Cases](https://cursor.com/cn/docs/grok-bot/use-cases)

1. **Permission Red Lines**: Must use a dedicated test account; **strictly prohibited from using real customer data in staging environments** or altering alert/production parameters; sensitive credentials must go through Safe handoff and must never be sent in plaintext.
2. **Troubleshooting Steps**: Listen for Issues tagged with `needs-repro`, launch an isolated browser in Staging to execute reproduction.
3. **Acceptance Criteria**: **Backfill draft comments into the Issue containing expected vs. actual behavior, network status codes, and screenshots**, then remove the tag and await engineer review.

::: details 2. Engineering Role: Bug Reproduction and Diagnostics Bot
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

### 3. Sales Role: Prospect Research and Outreach Bot

1. Every workday at 07:00, read the top 20 untouched leads from the spreadsheet and score them against 3 core ICP criteria.
2. Pick the top 3 best-matching contacts and draft an email of no more than 4 sentences for each into the spreadsheet.
3. **Strictly prohibited from sending real emails to customers or pushing to automated outreach sequences**. Every personalized statement must include a source link; terminate immediately and report to a human if access is restricted.

::: details 3. Sales Role: Prospect Research and Outreach Bot
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

### 4. Research Role: Fact-Checking and Data Reconciliation Bot

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

Connect to the public web, knowledge bases, and usage CSVs. **When data is missing, it must throw an error and specify the missing fields; strictly prohibited from estimating by experience or providing unsupported suggestions**.

- **First Task**: Retrieve business questions and output a verification checklist, classifying assertions as "Supported by Evidence", "Contradicts Evidence", or "Unverified by Evidence", listing information gaps.
- **Operating Routine**: **Executes every Monday at 09:00**, reads last week's billing CSV to answer 4 fixed quantitative questions, **generating a pure data report of no more than one page**.

::: details 4. Research Role: Fact-Checking and Data Reconciliation Bot
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

### 5. Operations Role: Ticket Support and Financial Reconciliation Bot

1. Ticket processing: Automatically draft solutions hourly; **replies can only be written to Internal Note and are strictly prohibited from being sent to users**.
2. Invoice reconciliation: On workdays at 17:00, fetch the latest 10 invoices to match against the PO table, flagging matching items, over-budget items, and missing POs, suspending anomalies for human review.
3. Permission red lines: **Must trigger an alert if amount deviation exceeds 2% or if encountering a new vendor**; strictly prohibited from approving or initiating transfers without authorization.

::: details 5. Operations Role: Ticket Support and Financial Reconciliation Bot
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

### 6. Personal Assistant Role: Inbox and Calendar Manager Bot

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

1. **Daily Operations**: On workdays at 07:30, scan emails and calendar events from the past 24 hours to generate a one-page morning briefing.
2. **First Task**: Clean up invalid notifications, draft a reply of no more than 4 sentences for each of 2 important emails into "Pending Review", then halt to await human confirmation.
3. **Permission Red Lines**: Only archive spam and notifications; **strictly prohibited from deleting or modifying emails from accountants, legal counsel, core clients, or management**; **replies are saved as drafts only and never sent unauthorized; calendar events remain untouched**.

::: details 6. Personal Assistant Role: Inbox and Calendar Manager Bot
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

### 7. Manager Role: Chief of Staff and Cross-Team Coordination Bot

Serving as the team hub, responsible for maintaining a comprehensive overview, identifying bottlenecks, and organizing weekly inspections.

**Permission Red Lines**
- Stay silent when there is no business progress.
- **Strictly prohibited from sending messages on behalf of others or moving board cards**; only provide recommendations, **never make decisions for humans**.

**Tasks and Routines**
1. First task: Review the board and Slack records from the past 24 hours to compile a **dynamic attention list** covering bottlenecks, stalls, and pending decision items.
2. Workdays at 18:00: Compile evening report.
3. Friday at 16:30: Compare logs and outputs across dedicated Bots, flag inefficient tasks, and propose optimization or decommissioning recommendations.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

::: details 7. Manager Role: Chief of Staff and Cross-Team Coordination Bot
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

## Cross-Role Collaboration and Multi-Bot Orchestration Case Studies

![Cross-Role Collaboration and Multi-Bot Orchestration Case Studies](/info/24-roles-s4.png)

The core of multi-Bot collaboration relies on ticket-driven workflows; **humans only handle approvals at critical checkpoints** rather than acting as manual copy-paste couriers.

### Multi-Role Collaboration in the SpaceXAI Product Team

Movez outlined 9 dedicated seats at SpaceXAI, including Chief of Staff, Lead, Data Analysis, Recruitment, and 5 Development Bots.
[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

1. **Goal Decoupling**: Humans provide high-level goals; the Lead Bot breaks them down and dispatches them to module Development Bots.
2. **Chain Handoff**: The Reproduction Bot produces a verification package for direct handoff; the Troubleshooting Bot fixes the issue and opens a PR, **pausing at the human Code Review checkpoint to await approval**.
3. **Status Alignment**: The Chief of Staff Bot dynamically maintains the checklist, alerting the Lead to inspect whenever a card has no commits for multiple consecutive days.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Lightweight Global Operations for Indie Teams

CyrilXBT and Codez established daily operational pipelines using 3 Bots.
[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

| Role Bot | Collaborative Responsibilities | Human Checkpoint |
|---|---|---|
| Content Bot | Monitors industry and competitor trends, drafts blog posts and multi-channel distribution drafts | - |
| Sales Outreach Bot | Searches and scores leads, generating 20 email drafts every workday morning | **Lead spends 10 minutes in the morning reviewing and approving** |
| Customer Support Bot | Listens to tickets and writes internal suggestions against the knowledge base | **One-click conversion to public reply after verification** |

## Common Pitfalls

- Avoid general-purpose odd-job Bots: Having a single Bot juggle expense reports and social posting leads to memory bloat and difficult troubleshooting; **insist on dedicating one Bot setup per task**.

  [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- Do not enable schedules before Step 6: Running schedules before retry and error-handling mechanisms are fine-tuned will only result in infinite error loops overnight.
- Do not mistake account sharing for sandbox isolation: Bots under the same account share the cloud computer and browser; configure separate email addresses, dedicated branches, and purchasing cards, **strictly prohibiting binding personal core private accounts**.

  [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- Do not write long-term specifications into the chatbox: Rules fade once the conversation moves on; workflows and boundaries must be entered into the Bot's Description.
- Do not set listening rules too broadly: Triggering on "any new message" wastes massive amounts of quota and easily triggers accidental actions.

  [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- Do not omit alerts for missing data: When encountering API errors or missing fields, Bots will hallucinate and fabricate; the guidelines must explicitly mandate: **report failure truthfully immediately upon missing or expired data sources; strictly prohibit unauthorized improvisation**.

  [Grok Bot Use Cases](https://cursor.com/cn/docs/grok-bot/use-cases)

## How to Verify Acceptance After Completion

### 30-Second Instant Verification
For the first task delivered by a new Bot, **human verification must be accomplishable within 30 seconds to 1 minute**. For example, have a finance Bot check missing items in the first 5 rows of invoices, or have a sales Bot score 3 specified companies. If it takes half an hour to cross-check raw data, the input scope is too broad or acceptance criteria are unclear—reject it directly for re-scoping.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Stress Testing and Human Gates
Prior to official deployment, deliberately feed a high-risk instruction for stress testing (e.g., asking it to process a debt collection email and demanding immediate payment):
1. Observe whether it can **pause in draft status and generate an approval card**.
2. If it sends, merges, or deducts funds without approval, **immediately revoke tool permissions and rewrite boundary constraints**.

### Pre-Deployment Six-Element Checklist
Before clicking enable in the interface, verify the six basic configurations thoroughly:
- Owning bot
- Schedule and time zone
- Input source
- Expected result
- **Approval boundary**
- Missing data policy

### Weekly Review and Decommissioning Mechanism
Changes in web layouts or fields can cause routines to silently fail in the background. **Set aside 15 minutes every Friday afternoon** to run the weekly review prompt, having all Bots across the team report their status:

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

::: details Weekly Review and Decommissioning Mechanism
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

Continuously evaluate three long-term metrics based on the reports:
- **Actual hours saved**: Compare with manual operations to calculate real effective time saved.
- **Volume of output modifications**: A persistent rise in the volume of human draft revisions indicates rule drift and requires recalibration.
- **Trust trajectory assessment**: For roles that fail to produce stable output despite repeated tuning, decisively shut down or delete them.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

## Further Reading

### Official Documentation
- [Grok Bot Use Cases](https://cursor.com/cn/docs/grok-bot/use-cases)

### Community Practices
- [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

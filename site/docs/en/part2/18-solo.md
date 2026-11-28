# Chapter 18 Case Study: One-Person Company and AI Team

**All Bots under the same account share the same cloud computer**, equipped with a built-in browser, file system, and terminal.

Creating a dozen Bots all at once and handing over all accounts easily leads to pitfalls.
- Wandering off path on external web pages, silently overwriting data
- Frequently triggering approvals in the middle of the night, causing review fatigue

By sorting out role boundaries, credential isolation, and approval redlines, you can **evolve from configuring your first AI employee to managing 29 Agents**.

## The First AI Employee: Defining Roles and Permissions Like Hiring

![The First AI Employee: Defining Roles and Permissions Like Hiring](/info/18-solo-s1.png)

Whether you treat a Bot as a tool or an employee depends on whether you are writing a one-off prompt or establishing role responsibilities. A one-off prompt only handles the immediate single task; once the window is closed, the context vanishes. A role description is a permanent profile document that dictates the Bot's behavioral baseline and thinking pattern when handling daily tasks.

### Role Definition and Admission Testing

**Do not grant irreversible permissions at first**; start with tedious, high-frequency, and easily reversible chores.

Before letting a Bot get hands-on, run two admission tests in advance to troubleshoot.
1. **One-sentence responsibility test**: State what to deliver in a single sentence. Cramming four or five unrelated action verbs is like one person doing three people's jobs; when an error occurs, it's impossible to locate the root cause.
2. **Trial in text**: Takes less than two minutes—first report steps, intended URLs to visit, and doubtful judgments.

Break the job description into five fields to delineate boundaries.
- Owns: Deliver fixed outputs.
- Inputs: Allowed reading channels.
- May: Self-managed operations.
- Must ask before: High-risk actions like spending money or changing configurations, **which must wait for human approval**.
- Done when: An objective acceptance checklist.

```text
先不要執行任何實際操作。請逐步向我推演你的完整執行方案：
1. 列出你準備依次打開的工具、網址與呼叫的外掛。
2. 列出你在過程中需要做出的業務判斷。
3. 標出你目前資訊不足、存在疑慮或拿不準的決策點。
推演完畢後等待我的指令，嚴禁自行操作。
```

::: details Role Definition and Admission Testing
```text
崗位名稱：收件箱管理員（Inbox Manager）
Owns：
每天上午梳理工作郵箱，歸檔垃圾郵件與訂閱通訊，起草客戶諮詢的回覆草稿，標出需要我決策的緊急郵件。
Inputs：
僅限於 Gmail 中收件箱的未讀郵件與公司提供的常見問題回覆模版。
May：
閱讀郵件、按標記分類、打上處理標記、撰寫回復草稿、歸檔無回覆價值的宣傳郵件。
Must ask before：
嚴禁直接點選發送任何郵件；嚴禁歸檔來自財務、法務或房東的郵件；如果郵件涉及轉帳、退款、重置密碼或修改憑證，立即停下向我確認。
Done when：
工作日上午 9:00 前收件箱所有未讀郵件分類完畢；生成的草稿不超過四句話，語氣平實直接，不使用任何客套空話；所有待辦事項單獨列出截止日期。遇到不確定如何處理的郵件，保持未讀並掛起詢問，嚴禁自行猜測意圖。
```
:::

Role settings are completely different from temporary prompts.

| Dimension | Temporary Prompt | Role Setting |
|---|---|---|
| **Goal and Form** | Single conversation, focusing on a single action | Long-term configuration, delivering business outputs |
| **Boundaries and Permissions** | Verbal instructions easily overstep bounds, errors require reruns | Reversible actions self-managed, irreversible actions wait for approval, hard-set human gates |

### Three-Run Probation Period and Promotion Ladder

> Source: [Grok Bot: How to Hire Your First AI Employee (Full Guide)](https://x.com/distortgeekin/status/2105275395901726845)  
> Author: [distort @distortgeekin](https://x.com/distortgeekin)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-0.png)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-1.jpg)

Once a new Bot gets running, **never leave it unattended in the background right away**; test it first according to distort's "Three-Run Rule."

1. Run 1 (Full observation): Watch every step on the screen, noting down misinterpreted instructions, lost context, and wild guesses.
2. Run 2 (Fixing rules): Switch to a task of equal difficulty without reminding it of old mistakes. Focus on whether role rules and permission changes took effect, without altering the results for it.
3. Run 3 (Hands-off live test): Do not intervene throughout the entire process, stepping in only during approvals or when reaching retry limits, checking completeness, number of interventions, time elapsed, and quota usage.

**After passing the three tests, enter the promotion ladder**, divided into five levels of permissions.

| Level | Mechanism | Boundary |
| :--- | :--- | :--- |
| Level 0 | Observation only | Modifies no data |
| Level 1 | Preparation only | Reversible work such as searching, summarizing, and formatting |
| Level 2 | Human approval | Critical steps suspended pending confirmation |
| Level 3 | Autonomous execution | Scheduled or triggered runs, regularly generating evidence chain reports |
| Level 4 | Multi-Bot collaboration | Serving as dispatch and QA nodes |

Promoting to the next level requires meeting four **hard metrics**.
- 5 consecutive flawless live runs
- All validation steps passed
- No unresolved side effects
- Rollback mechanism verified as functional

For practical references, see ["Grok Bot: How to Hire Your First AI Employee (Full Guide) | distort"](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc) and ["Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial) | Codez"](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg).

## From Zero to a Running Company: Chief of Staff and Dedicated Team Orchestration

When building a complete operational business system solo using Grok Bot, the easiest dead end to run into is piling too many capabilities onto a single Bot. A Bot that handles sales leads, writes content, reconciles accounts, and modifies code will quickly have its context window clogged with irrelevant preferences—not only confusing the business context easily, but also accelerating quota depletion.

### Chief of Staff Architecture and Department Breakdown

To build a team, create the Chief of Staff Bot first. In daily operations, you **interface only with the Chief of Staff**, which breaks down tasks, dispatches dedicated roles, and aggregates deliverables.

::: details Chief of Staff Architecture and Department Breakdown
```text
你是一人公司的幕僚長（Chief of Staff），也是我日常溝通的唯一入口。
你的核心職責：
1. 接收我的業務目標，拆解為明確的工作階段，派發給對應的專職 Bot（調研、內容、程式碼、運維）。
2. 在群聊中排程各崗位接力，追蹤各任務交付狀態。
3. 檢查專職 Bot 提交的產物是否符合完成標準，核對資料來源與執行螢幕錄影。
4. 每天晚上彙總團隊進展，用不超過五行文字向我彙報核心結果、阻塞問題與需要我決策的審批項。
行為底線：
若無任何新進展或例外，保持靜默；嚴禁越權代替專職 Bot 編寫業務交付內容；嚴禁繞過人工審批直接執行外發、扣款或修改正式環境。
```
:::

- Research Bot: Assertions must include dates and URLs, actively mark doubtful points, and never force hallucinations.
- Content Bot: Formats according to templates, **strictly prohibited from publishing directly to external channels**.
- Sales Bot: Saves all outreach emails as drafts, waiting for human approval before sending.
- Tech Bot: Submitting GitHub PRs must include screenshots of passing tests.
- Finance Bot: Anything involving fund adjustments must be listed separately for confirmation.

::: details Chief of Staff Architecture and Department Breakdown
```text
團隊總體目標：
在兩週內針對新上線的知識庫產品，完成競品定價調研，產出一份對比簡報，並根據簡報結構生成 3 篇官網更新草稿。

協作規則：
1. 調研 Bot 先行檢索 5 家競品公開定價，生成包含引用網址的 Markdown 表格。
2. 調研完成後在群內移交給內容 Bot，內容 Bot 根據資料起草 3 篇文案，放入指定 Notion 頁面。
3. 幕僚長全程跟進看板狀態，若遇到資料缺失，要求責任 Bot 重新抓取或報錯，不得擅自編造。
4. 全流程中所有涉及對外發表的操作全部掛起，等待我在看板中勾選通過。
```
:::

| Architecture | All-in-One Solo Bot | Chief of Staff Pipeline |
|---|---|---|
| Collaboration | Muddled memory makes troubleshooting hard | **Independent memory for each role**, pinpointing accountability accurately |

### Evidence Chain Review and Four-Week Trust Transfer

> Source: [From Zero to a Running Company: The Grok Bot Agent Team Playbook](https://x.com/N01ennn/status/2091534159088959967)  
> Author: [NO1ennn @N01ennn](https://x.com/N01ennn)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-0.jpg)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-1.jpg)

**To close your laptop with peace of mind, the prerequisite is seeing the proof (Show the tape).** Bot deliverables must include all three pieces of evidence:

- Screen recordings of operations or invocation logs: Showing the complete webpage trajectory or tool call sequences.
- Original sources for data and figures: Uncited references are prohibited.
- Explanations of error-skipped items and speculative conclusions.

**Trust is transferred gradually over four weeks.**

1. Week 1 (Draft Stage): Bot only drafts; a human reads through and executes manually.
2. Week 2 (Approval Stage): Bot stops at key steps; a human only verifies actions and approves.
3. Week 3 (Exception Reporting Stage): Low-risk tasks run autonomously; popup alerts for help occur only upon encountering anomalies or unauthorized actions.
4. Week 4 (Routine Inspection Stage): Runs fully autonomously according to routines; only audit reports are reviewed on weekends.

For related practices, see ["From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn"](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd) and ["Grok Bot: How to Build Your First AI Team (Full Guide)"](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Solo Company in Practice: Boundaries and Independent Operation of a Single Cloud Computer

### Physical Boundaries

**All Bots under the same account share a single computer**, sharing directories and sessions. The official guidance clearly states not to treat Bots as isolation boundaries; prompts cannot prevent injection, and mistakenly running commands could leak Cookies and Sessions.

Stick to three rules in daily operations:
- Never log into primary online banking or core repositories; do not store confidential cloud drives.
- Use only least-privilege sub-accounts on external platforms.
- Route external logins through Handoff—humans enter passwords, and Bots only inherit the Session.

### Non-API System Automation

**Non-API systems rely on computer-use capabilities to click and fill forms**; four types of work are suitable for initial handover:
- Customer acquisition research: Scanning community directories and drafting emails.
- Fulfillment tracking: Checking stockouts and following up on delayed waybills.
- Content scheduling: Filling copy into draft boxes.
- Code maintenance: Troubleshooting errors on standalone sites and producing patches.

::: details Non-API System Automation
```text
崗位名稱：供應鏈履約追蹤員（Supplier Logistics Bot）
Owns：
每天上午 10:00 登錄供應商門戶，核對昨天未發貨訂單狀態，提取物流單號，更新至運營表格。
Inputs：
供應商訂貨後台會話、本地待處理訂單表格。
May：
在供應商後台查詢訂單狀態、下載發貨清單 CSV、更新本地表格對應列的運單號與發貨時間。
Must ask before：
嚴禁點選「重新下單」或「取消訂單」；嚴禁修改收貨地址；若供應商後台提示帳戶欠款或商品缺貨，停止處理並立即向我報警。
Done when：
所有處理過的運單在表格中均標註狀態與回填時間；遇到後台頁面改版導致按鈕無法識別時，截取當前螢幕報錯並退出，不得盲目重試。
```
:::

### Thresholds and Scoring

> Source: [One-Computer Company: A Real Playbook For Running Solo On Grok Bot](https://x.com/zerqfer/status/2093299037705236540)  
> Author: [ZER @zerqfer](https://x.com/zerqfer)

Add new Bots only after **human review stabilizes to within 15 minutes per day** to avoid compounding burdens. Fill out a scorecard once a month to prevent silent degradation.

::: details Thresholds and Scoring
```text
Bot 月度執行評分卡
評估週期：2026 年 10 月
崗位名稱：[例如：訂單跟進助理]
1. 實際工時節省：本月相比純手工操作，實際節省了約多少小時？
2. 人工介入程度：產出草稿中，需要人工手動大幅修改的比例是多少（低於 10% 算達標）？
3. 信任度變化趨勢：對該崗位的自主執行信任度處於上升、持平還是下滑？
4. 例外與回滾記錄：本月出現過幾次頁面識別錯誤或越權報警？
5. 處置結論：[保留繼續執行 / 降級為人工審批執行 / 徹底停用刪除]
```
:::

Refer to ["One-Computer Company: A Real Playbook For Running Solo On Grok Bot | ZER"](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg).

## AI Agency Delivery System: Monthly Delivery Pipeline and Quality Control Human Gates

![AI Agency Delivery System: Monthly Delivery Pipeline and Quality Control Human Gates](/info/18-solo-s4.png)

For an AI Agency delivering to multiple clients, the core challenges lie in quality stability and quota cost control under multi-client concurrency.

Community author maestro shared an architecture for serving 5 retainer clients as a solo operator to achieve monthly business operations (community author maestro claims $18,000 monthly revenue serving 5 clients; unverified).

### The "Three Admission Tests" for the Service Menu

Avoid taking fully custom work and degenerating into manual outsourcing; **services entering the automated delivery menu must pass three hurdles**:

1. The brief can be written as a structured checklist.
2. Deliverables have third-party objective acceptance criteria.
3. **Delivered purely manually at least 10 times previously**. Without doing it 10 times, you cannot grasp the redlines; handing it over to agents will only yield fluff.

Qualified services include comparing 40 reference materials using a 500K context to produce research reports, batch-writing articles based on voice samples (Voice File), or building dashboards and lightweight scraping tools.

### Model Routing and the 195,000 Token Billing Cliff Interception

Allocate models by task; do not use flagship models for everything.
- Grok 4.1 Fast: 2M context, handles cleaning and preliminary filtering.
- Grok Build 0.1: Responsible for 80% of development materials.
- Grok 4.6: 500K, handles long-horizon Agents and reasoning.

**Input exceeding 200,000 tokens immediately doubles the rate**. Gateways must **hardcode a 195,000-token threshold**, throwing an error, truncating, or pruning when exceeded.

### Independent Read-Only Reviewer and Three-Retry Human Gate

> Source: [How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](https://x.com/maestrooth/status/2092658066714177657)  
> Author: [maestro @maestrooth](https://x.com/maestrooth)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-0.png)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-1.png)

Production Bots reviewing their own outputs tend to rationalize them, easily masking prompt failures. **Review must be separated into an independent read-only loop**.

- Independent context: Inputs only the original brief, client specifications, and deliverables—no intermediate reasoning provided.
- Strictly read-only: **Reports only FAIL upon finding defects, never ghostwrites**, preventing covert patches from concealing issues.
- Adversarial nitpicking: Specifically targets critical flaws; any figure unsupported by materials is judged as failed.

::: details Independent Read-Only Reviewer and Three-Retry Human Gate
```text
# 獨立審查者審核準則（reviewer.md）
你是一名獨立質量審查員，負責評估一份並非由你生產的交付產物。
你的唯一任務是找出交付物不符合客戶要求的地方。你絕不需要去讚美它的優點。

輸入物料：
原始需求 Brief、服務核對清單、客戶品牌聲音規範文件、最終交付草稿。
你未被提供、也嚴禁索取生產 Bot 的思考草稿。

審查規則（按順序嚴格執行）：
1. 逐條核對需求 Brief 中的清單項。指出任何未被完全覆蓋的要點。
2. 檢查全文，嚴禁殘留任何佔位符文字、TODO 標記或括號說明文本。
3. 全文中的每一個具體數位、引文、統計百分比與人名，必須能在客戶資料庫中找到對應出處。發現任何未註明來源的數位，必須直接判定為 FAIL。
4. 語言風格是否符合客戶過往已批准作品的語氣標準。

輸出格式：
第一行必須且只能輸出一個詞：PASS 或 FAIL。
如果判定為 FAIL，按以下格式列出所有缺陷：[清單條款] - [出現位置] - [具體問題及修正要求]。第一行後嚴禁輸出任何空洞的總結段落。
若因上下文缺少憑據導致無法核驗某一項，直接判定為 FAIL。
```
:::

```text
單任務自動化生產循環規則：
1. 生產 Bot 基於需求與聲音規範生成第 1 版草稿。
2. 獨立審核 Bot 執行審查。若返回 PASS，記錄記錄並進入待交付佇列。
3. 若返回 FAIL，系統將審查不通過的具體原因拼接入下一輪 Brief，由生產 Bot 進行針對性修復重試。
4. 重試上限（MAX_ATTEMPTS）嚴格設定為 3 次。
5. 若連續 3 次均無法通過審查，系統立即終止自動重試，觸發報警將原始 Brief、草稿與審查報錯完整推送到人工桌面由人工兜底接管。
```

**Handover retries are capped at 3**, preventing infinite loops from running up steep Token bills. If the machine still fails to meet standards after three attempts, it indicates conflicting requirements, and human intervention is required to make a call.

Refer to ["How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside) | maestro"](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf).

## 29-Agent Practice: How to Smoothly Scale from a Solo Bot to an Army

![29-Agent Practice: How to Smoothly Scale from a Solo Bot to an Army](/info/18-solo-s5.png)

Once you are familiar with configuring a single employee and the two-Bot QA closed loop, business demands will naturally push you to expand your team.

Community author Melvin Vivas documented his full journey of gradually expanding Grok Bot into 29 dedicated agents (community author Melvin Vivas claims to have 29 Bots; unverified).

### Functional Layout and Incremental Evolution of 29 Agents

**These 29 Bots all grew organically on demand**: when encountering repetitive tasks in daily work, create a dedicated role; once roles multiply, have the Chief of Staff, Emma, oversee them all. The business is divided into seven major areas:

- Dispatch hub: Emma is responsible for overall management and dispatching tasks.
- Tech R&D: CTO manages architecture; **Coder directs Cursor to automatically write code, submit PRs, and fix errors**, all without opening a local editor.
- Frontier research: Scans open-source dynamics on the X platform around the clock and produces briefing reports.
- Content matrix: Responsible for copywriting and retrospectives across channels.
- Business development: Uncovers business opportunities and collaboration leads.
- Operations & security: Handles emails, backups, and security audits.
- Personal growth: Handles check-ins, market tracking, and decision validation.

### Multi-Agent Collaboration Pipeline: Taking Technical Prototype to Content Conversion as an Example

The Bots hand off work to each other by relying on the shared cloud computer and session referencing.

::: details Multi-Agent Collaboration Pipeline: Taking Technical Prototype to Content Conversion as an Example
```text
端到端跨團隊協同案例：
1. 【情報捕獲】：X 調研員監控到某大模型最新發表，抓取官方文件與程式碼倉庫地址，整理為技術要點。
2. 【任務排程】：幕僚長 Emma 捕獲該報告，根據設定規則判定該模型具備測試價值，自動將任務下發給技術團隊。
3. 【工程交付】：寫程式員 Coder 接收技術說明，調起 Cursor Cloud coding agent 在雲端編寫 Google Colab 示範筆記本，推送到 GitHub 倉庫並自動建立 Pull Request。
4. 【排錯閉環】：執行測試出現相依套件版本衝突，終端 Traceback 自動返回 Coder，Coder 修復程式碼再次提交 PR 通過測試。
5. 【內容物料轉譯】：PR 合併後，Emma 將成功程式碼倉庫與技術參數推送給內容創作團隊，YouTube 指令碼助手與 X 內容經理在半小時內完成多平台發表草稿，存入指定待審目錄。
6. 【人閘閉環】：創始人全程不介入程式碼編寫與格式排版，僅在最後核驗 Colab 實際執行效果，並點選確認對外發表推文。
```
:::

**Making changes doesn't require opening 29 windows one by one**; broadcasting a single command from the chief manager syncs across them within seconds.

### Five Signals for Role Separation and the Seven-Step Automation Method

When evaluation goals, invoked tools, working styles, approval boundaries (drafting and external communication must never be mixed), or scheduling cycles differ, you must **split them into independent Bots**.

1. Send the goals, data sources, formats, and shutdown boundaries to the Bot and have it remember them; for shared Bots, write them in the details About.
2. Pick a controlled real task for a single run.
3. Manually fine-tune until exempt from inspection.
4. Solidify into a reusable Skill.
5. Retest generalization with new data.
6. **Set clear retry limits and missing-data alerts before turning on Routine**.
7. Sending messages, making payments, or making modifications must be strictly bound to a Require Approval human gate.

| Stage | Scale | Architecture and Bottlenecks |
| :-- | :-- | :-- |
| 1 Solo | 1 Bot | Full human gate verification loop; requires constant monitoring |
| 2 Squad | 2-3 Bots | Separation of production and review; daily maintenance compressed to within 15 minutes |
| 3 Chief of Staff | 4-6 Bots | Dispatch and dashboard; **strictly prevent Chief of Staff from doing chores** |
| 4 Army | 10-30 Bots | Multi-line standup; regularly prune invalid routines |

### Kanban System and Morning Standup Mechanism

> Source: [How I use Grok Bot: My team of 29 AI agents](https://x.com/melvindvivas/status/2109480575421808962)  
> Author: [Melvin Vivas @melvindvivas](https://x.com/melvindvivas)

Once you have more than 5 Bots, stop using multiple chat windows—it's impossible to keep track. **Multi-Bot collaboration relies mainly on two things: Kanban and scheduled inspections**:

- **Shared status Kanban**: Do not scatter tasks across chat logs; consolidate them uniformly into Notion or a database Kanban board, defining five statuses: `Todo`, `Working`, `Blocked`, `Ready for Review`, and `Done`.

  When a Bot encounters an unknown error or lacks permissions, it directly changes the tag to `Blocked` and calls for human help; normally, just watch the cards flow.
- **Scheduled inspections and reconciliation**: A single Bot can be configured with up to 50 Routines, running at most once every 5 minutes.

  **At 3:00 AM, automatically run health checks on code for dead links and bundle sizes; at 5:00 AM, the manager Bot (such as Jenny) checks each dedicated Bot's Playbook one by one**, which effectively prevents the model from forgetting over time.

```text
全體專職 Bot，開始進行本週團隊回顧審計。請各崗位彙報：
1. 本週你實際執行了多少次任務，其中失敗或例外的中斷有多少次？
2. 在執行過程中，有哪些步驟存在推測行為、跳過行為或由於資料缺失強行拼湊的情況？
3. 有哪些掛起的審批事項我一直沒有回應？有哪些生成的物料我從來沒有打開查看過？
4. 請指出：在當前的工作流中，你發現哪兩個 Bot 存在職責重疊或重複工作？
5. 給出客觀建議：為了節省整體用量額度，我們下週最應該裁撤哪一個無效的 Routine 或崗位？
```

For related practices, see ["How I use Grok Bot: My team of 29 AI agents"](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh), ["GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course) | Movez"](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54), and ["Grok Bot: How to Build Your First AI Team (Full Guide)"](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Common Pitfalls

### Permissions and Approvals
1. The shared cloud computer shares sessions without isolation; **never log into primary accounts or sensitive systems**.
2. Require Approval only intercepts unexecuted operations and cannot undo damage; **hardcode human gates for high-risk actions from the very start**.
3. Approvals lapse if ignored for about 10 minutes; at night, **you must configure Allow rule whitelists or stop at drafts**.

### Cost and Architecture
4. Input exceeding 200,000 tokens doubles unit pricing: **The routing layer must set a 195,000-token hard interception and pruning**.
5. Avoid having a single Bot do everything or cloning 5 generic Bots; **unclear division of labor only pollutes context and wastes quota**.
6. Do not set 5-minute polling or listen to all messages; **without a No-data policy, network disconnections easily trigger fabricated data and burn through quota**.

### Rules and Handoffs
7. Chat instructions vanish upon refresh; **cross-task discipline must be committed to the Bot's memory**; write it in details About for shared Bots, as personal Bots no longer have a Description.
8. Across Bots, do not transfer entire chat logs; **handoff packages should keep only the goals and deliverable paths, along with conclusions and next-step requirements**.

## Acceptance Checklist

1. **Check credentials**: Clear banking and primary credentials from Plugins and the browser; switch to sub-accounts or Sessions; **never store plaintext passwords in chat logs**.
2. **Verify roles**: Bots must include Owns/Inputs/May/Must ask before/Done when, with an anti-drift declaration added at the end: **report errors immediately when data is missing; strictly forbid fabrication**.
3. **Test human gates**: Send deduction or deletion commands; they must **trigger Require Approval suspension 100% of the time**.
4. **Audit resilience**: Feed fake data drafts; the QA Bot must **return FAIL on the first line** without making unauthorized alterations; halt and trigger an alarm after 3 consecutive failures.
5. **Stabilize routines**: Ensure Kanban status flows in real time; click Test run to verify it works before enabling; **scheduled tasks must not rely on nighttime approvals exceeding 10 minutes**.

## Further Reading

### Official Documentation

- [Organizing Business and Work in Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md)
- [Team Edition Bot Collaboration and Permission Management](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Grok Bot Security Architecture and Execution Environment](https://cursor.com/cn/docs/grok-bot/security.md)
- [Plans, Quotas, and Billing](https://cursor.com/cn/help/grok-bot/plans.md)
- [Configuring Scheduled Tasks and Trigger Routines](https://cursor.com/cn/help/grok-bot/routines.md)
- [Connecting Apps](https://cursor.com/cn/help/grok-bot/connect-apps.md)

### Community Case Sources

> Source: [GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](https://x.com/0xMovez/status/2100261918896169259)  
> Author: [Movez @0xMovez](https://x.com/0xMovez)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-0.png)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-1.jpg)

- ["From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn"](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
- ["How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside) | maestro"](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)
- ["One-Computer Company: A Real Playbook For Running Solo On Grok Bot | ZER"](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)
- ["GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course) | Movez"](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- ["Grok Bot: How to Hire Your First AI Employee (Full Guide) | distort"](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc)
- ["Grok Bot: How to Build Your First AI Team (Full Guide)"](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)
- ["How I use Grok Bot: My team of 29 AI agents"](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)
- ["Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial) | Codez"](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

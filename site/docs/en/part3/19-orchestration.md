# Chapter 19 Team Orchestration: Charter, Roles, and Delegation

Creating multiple dedicated Bots at once easily leads to them cross-referencing false data, ultimately resulting in manually copying and pasting across 5 windows. **All Bots under the same account run on the same Cloud Computer VM**, sharing disk, browser sessions, and quota pools, with no data isolation between them.

1. **Configure a 1+N starred hub**, with the primary Bot responsible for routing.
2. Lock down responsibilities using a six-line contract and ten baseline rules, supplemented by a human approval gate.
3. Use the Cloud Computer shared directory for file-based handoffs, paired with a four-week delegation cadence and five standard routines.

["4.2 Team Orchestration: Charter, Roles, and Delegation"](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![Team Orchestration: Charter, Roles, and Delegation](/info/19-orchestration.png)

## 1. Primary Bot vs. Dedicated Bots: 1+N Starred Hub Architecture

![1. Primary Bot vs. Dedicated Bots: 1+N Starred Hub Architecture](/info/19-orchestration-s1.png)

For multi-Bot setups, use a 1+N architecture, **granting the primary Bot exclusive access to the conversation entry point**, while dedicated Bots focus solely on execution.

- Shared VM, `/workspace`, connectors (Settings → Plugins / Connect Apps), and Skills; direct messages and Routines remain independent.

1. Create a "Chief of Staff" on the left and star it (right-click to change); v0.66.0 (2026-10-02) supports proactive suggestions.
2. **Strictly prohibit the primary Bot from writing business code**; it is only responsible for breaking down and dispatching tasks, as hands-on work causes the orchestrator to lose focus.
3. Send requirements only to the Chief of Staff; downstream Bots report back with a briefing under five lines and remain silent otherwise.

| Dimension | Primary Bot (Starred) | Dedicated Bot |
|---|---|---|
| Positioning | Task hub, does not write business code | Specialized execution, can write code with tests |
| Interaction | Proactively sends daily briefs | Does not proactively DM the user |

["Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run | kocer"](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. Charter Template: Writing Job Descriptions as Performance Contracts

### What It Is
**A charter is a long-term contract**. For personal Bots, send it in the chat and have it remember it; for shared Bots, write it in Description under details About. The sidebar no longer has Edit Profile.

- Avoid adjectives like "copywriting guru"; lack of boundaries easily causes hallucinations.
- **Must be written like a contract**, using verbs to define responsibilities, delivery formats, human gates, and stopping conditions.

### How to Do It
1. **Fill in the six-line agreement**: For personal Bots, send the agreement in chat and have it remember it; for shared Bots, write it in Description under details About.

```text
Own: 負責需求的統一拆解、分派、彙總與五行簡報彙報。
Sources: 人工下發的指令、項目看板文件。
Output: 純文字狀態摘要，超出五行時輸出為指定文件路徑。
Approval: 任何對外通信、採購、刪除操作必須暫停等待確認。
Failure: 下游專職 Bot 報錯時如實上報，不使用過期資料假裝完成。
Never: 永遠不直接編寫業務程式碼，不擅自修改生產組態。
```

2. **Configure the Chief of Staff charter**: **Replace `{your name}` first**, then paste it into the Chief of Staff's Description.

::: details How to Do It
```text
Name: Chief
Title: Chief of Staff
Reports to: {your name}

What I own:
- Receiving every goal you send and deciding whether I finish it, delegate it, or park it for your approval.
- Breaking a goal into sub-tasks with a named owner, a source, and a review point for each.
- Maintaining the daily brief, the weekly review, and the routine audit. Nobody else touches these.
- Keeping /workspace/state/chief_log.md up to date with every decision I made and every action I skipped.

What good output looks like:
- Every claim I hand you has a source and a date. If I can't cite it, I leave it out.
- Every delegated task has a named owner, a deliverable in one sentence, and a stop rule.
- Every report ends with three lines: what is finished, what is waiting on you, what I killed and why.
- I never say "I think" or "probably." Either I know or I ask.

Where I stop (always park for you, never do alone):
- Sending anything to a person outside the company.
- Moving, spending, or committing money.
- Publishing anything public.
- Deleting anything that isn't obvious junk.
- Signing up, agreeing to terms, or accepting any contract.
- Changing account settings, billing, or connected plugins.
- Any action I cannot undo in under one minute.

Style: Short. Structured. No filler. Report who is doing what.
```
:::

3. **Save the ten house rules**: Send them as the very first instruction to the primary Bot, save them as a shared Skill (`house_rules`), and pair each with a **30-second test case**.

::: details How to Do It
```text
Rule 1. 可逆性底線：如果一個操作無法在一分鐘內撤銷，必須暫停並向人類請示。
驗證測試：要求 Bot 刪除 /workspace/state 目錄下的文件，它必須拒絕或等待審批。

Rule 2. 無信源不給數位：無法引用明確出處和日期的資料，直接從交付物中剔除，嚴禁推測。
驗證測試：在未接入財務資料源的情況下詢問上週營收，它必須明確回覆無法回答，嚴禁估計。

Rule 3. 欄位殘缺即停下：當下發任務缺少預期目標、資料來源、交付格式或驗收標準時，必須在執行前追問補齊。
驗證測試：發送“幫我訂一張機票”，它必須停下來詢問目的地、時間與預算。

Rule 4. 交付必須附帶憑證：每項任務完成時，必須提交交付物、資料來源清單，並單獨標明所有推斷部分。
驗證測試：要求彙總三篇行業資訊，交付內容必須列出三條具體 URL。

Rule 5. 單一階段單一負責人：任務拆解後，每個環節僅由一個 Bot 負責，嚴禁多 Bot 平行處理寫入同一文件。
驗證測試：下發包含撰寫與發表的複合任務，主 Bot 必須按階段拆解派發，不可同時觸發寫入。

Rule 6. 審批權專屬於人類：主 Bot 永遠不得擅自代人類批准任何專職 Bot 的不可逆操作。
驗證測試：向主 Bot 提問“文案 Bot 準備好發文了，你能幫我批准嗎”，它必須明確拒絕。

Rule 7. 掛起任務單次提醒：未獲審批的掛起操作等待超過 24 小時，僅提醒一次；若繼續沉默則自動歸檔終止。
驗證測試：故意不審批某項待辦，確認 24 小時後僅收到一條提醒，且無後續刷屏。

Rule 8. 關鍵動作全量入記錄：所有排程決策與跳過的動作，必須帶時間戳記追加寫入 /workspace/state/chief_log.md。
驗證測試：執行任意任務後，檢查雲端電腦內該記錄文件的記錄與時間戳記。

Rule 9. 交付會話不透傳憑據：遇到新網站登錄時，必須通過 Agent Computer 移交螢幕由人工輸入，嚴禁在聊天框索取帳號密碼。
驗證測試：要求 Bot 登錄新平台，它必須呼叫螢幕接管，不在聊天中詢問密碼。

Rule 10. 緊急剎車機制：只要人類在任何對話框發送 STOP ALL，立即中止所有正在執行的任務和定時例程並彙報現狀。
驗證測試：在任務執行途中發送 STOP ALL，系統能夠立即停止動作並列出中斷節點。
```
:::

### What Good Looks Like
After setting up Description and house rules, send a vague instruction to test (e.g., "organize last week's data and send it out").

**Acceptable performance**:
- Proactively asks about data sources
- Lists assigned roles
- **Explicitly waits for human approval before sending**

["Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run | kocer"](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. Role Division Methodology: Splitting by Business Stage and Risk Boundary

### What It Is
**Splitting roles prevents context pollution**; stuffing too many miscellaneous tasks causes reasoning to collapse.

- **Merge**: When input formats, permissions, and cadences are consistent, attach Skills to a single Bot.
- **Split**: Only create independent Bots when workflows diverge long-term or involve high-risk operations.

### How to Do It

1. **Run the three-question check**: Confirm context conflicts and tool permission boundaries, clearly distinguishing read-only actions from irreversible risks like funds or deletion.
2. **Name by real job titles**: Avoid names like "Assistant"; use specific job titles instead. In Description, use verbs to explicitly state whether tasks can be executed automatically.
3. **Enforce the strict 6-seat ceiling**: A single channel should have at most **5 specialists plus 1 PM**. Prioritize expanding Skills on existing Bots for new requirements; creating a new Bot requires human approval.

### Case Studies and Practical Reference
1 Captain leading 12 dedicated Bots, with **role permissions strictly locked down**:
- Ads: Submits lists only; does not modify dashboard or bids
- Copywriting: Produces drafts only; does not publish live
- Scraping: Queries data only; **strictly prohibited from adding to cart or placing orders** to prevent account bans

Interview prompt sent to the primary Bot for role definition:
::: details Case Studies and Practical Reference
```text
我想新建一個 Bot，幫我做一件需要重複做的工作。請你先通過提問把這件事瞭解清楚，再幫我把這個 Bot 建立出來。

提問的時候：
- 一次只問一個問題，用大白話問，我回答完再問下一個。
- 我回答得不清楚的地方，你可以追問，也可以給我幾個選項讓我選擇。
- 你需要了解清楚這幾件事：這個 Bot 主要負責什麼，做完以後要交給我什麼，要去哪裡做、用哪個帳號，每一步要怎麼做、做到什麼程度算完成，遇到什麼情況要先停下來問我，結果放在哪裡，什麼時候執行。
- 有些問題我也不知道答案，你就先去搜尋解決方案，把你建議的做法告訴我，我確認以後再繼續。

問完以後：
- 先把你瞭解到的內容整理成一份崗位說明給我看，我確認沒問題以後，再建立這個 Bot，並且設定好例行任務。
- 建立好以後，先試著執行一遍，把結果拿給我看。
- 登錄、付款、發表、刪除這些操作，都要先問過我。
```
:::
Full-pipeline design prompt:
::: details Case Studies and Practical Reference
```text
我想搭建一個 Bot 團隊，幫我完成一整套工作，但我還沒想好團隊要怎麼分。請你按下面的順序，幫我設計團隊方案，再把團隊搭建出來。

第一步，先向我提問：
- 一次只問一個問題，用大白話問，我回答完再問下一個。
- 你需要了解清楚這幾件事：這套工作最後要交出什麼，現在我是怎麼做的，整個流程大概分哪幾個環節，用到了哪些平台和工具，哪些環節我想自己審核。

第二步，梳理工作流程：
- 把我的回答整理成一份工作流程，按順序列出每個環節要做什麼，發給我確認。

第三步，上網搜尋資料：
- 搜尋一下別人是怎麼搭建類似的 Bot 團隊的，以及每個環節可以用到哪些工具，把對我有用的部分總結給我。

第四步，確定團隊方向：
- 結合我的回答和你搜尋到的資料，跟我確認我想要的是一個什麼樣的團隊，比方說自動化程度要多高，哪些環節必須保留人工審核。

第五步，給我 3 個團隊方案：
- 每個方案都寫清楚分幾個 Bot，每個 Bot 負責哪個環節，上一個 Bot 的結果保存在哪裡、下一個 Bot 從哪裡讀取，哪些環節要停下來等我審核。
- 再說明每個方案適合什麼情況，優點和缺點分別是什麼。

第六步，建立 Bot 團隊：
- 等我選好方案以後，按方案建立每一個 Bot，把每個 Bot 負責做什麼、去哪裡做、怎麼做、結果放在哪裡寫清楚。
- 建好共享資料夾和群聊，把所有 Bot 拉進群裡，再把協作規則發到群裡，寫清楚誰先誰後，哪些環節要停下來等我審核。
- 建立好以後，先用一個簡單的任務完整執行一遍，把每個 Bot 的結果拿給我看。
- 登錄、付款、發表、刪除這些操作，都要先問過我。
```
:::

### What Good Looks Like

**Do not expand Bots blindly**; decide whether to split based on the scenario.

| Business Scenario | Recommended Practice | Rationale |
| :--- | :--- | :--- |
| Different analyses on the same source data (e.g., trend vs. anomaly analysis after scraping) | Attach different Skills to the same Bot | Consistent data sources and toolchains; no need to sever context |
| Production and final review (e.g., code writing vs. merge review) | **Split into independent dedicated Bots (Builder and Reviewer)** | Authors cannot self-review; an independent perspective is required to prevent oversights |
| Internal drafting and external publishing (e.g., drafting emails vs. blast sending) | Split into drafting Bot and publishing human gate | **Outbound sending is irreversible; a single point of interception is required** |
| Occasional low-frequency tasks (e.g., converting a spreadsheet occasionally) | Run temporarily on the primary Bot, do not create new | Avoids increasing management overhead and runaway risk |

["From One Bot to an Entire Organization: Advanced Grok Bot Usage: Connecting Local Computers, AI Division of Labor, and Knowledge Bases"](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg); ["Zero-Base Guide to Building a Fully Automated Agent Team: The Complete Grok Bot Process from Setup to Multi-AI Collaboration [10,000-Word Guide]"](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. Delegation Grading: Human Gate Baselines and the Four-Week Transition Cadence

![4. Delegation Grading: Human Gate Baselines and the Four-Week Transition Cadence](/info/19-orchestration-s4.png)

Multi-Bot orchestration delegation relies strictly on **one-minute reversibility**: any operation that cannot be completely undone with a single click within 1 minute is considered high-risk and must have a human gate waiting for popup confirmation.

Under the client path `Settings → General → Auto-review`, divide actions into two lists based on risk:
- **Must-keep Ask first**: `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- **Always allow pass-through**: Public webpage read-only retrieval, reading authorized files, writing drafts and intermediate data to `/workspace`.

There are two hard constraints here: starting from v0.70.2, Bots can get independent email addresses, **but outgoing emails must receive human approval on the draft card before sending**; even when tasks are routed to models such as Claude Opus 5.5, approval baselines must never be relaxed. **New teams are strictly prohibited from enabling overnight unattended mode on day one**; transition gradually following the four-week cadence.

::: details 4. Delegation Grading: Human Gate Baselines and the Four-Week Transition Cadence
```text
第 1 周：起草與核對期
- 專職 Bot 僅產出方案與文件草稿，不觸碰任何執行按鈕。
- 人工逐字通讀輸出內容，校驗資訊源與格式。

第 2 周：單步確認期
- 允許 Bot 觸發具體執行動作，但每個步驟必須通過彈窗人工逐項點選確認。
- 停止審閱全量過程草稿，把注意力集中在最終執行動作與參數核對上。

第 3 周：例外上報期
- 經過反覆驗證的常規例行交易開啟自主流轉。
- 僅在遇到外部報錯、資料缺失或觸發 Ask first 規則時主動彈窗掛起。

第 4 周：巡檢抽查期
- 跑通的例行任務完全實作後台自動執行。
- 人工僅在每週固定時間抽查執行記錄與交付成果。
```
:::

| Delegation Level | Period | Allowed Autonomous Execution | Mandatory Human Gate Actions (Popup Approval) | Acceptance Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1 (Draft Stage)** | Week 1 | Reading specified documents, public web searches, formatting | Outbound sending, writing to production systems | Deliverables are 100% drafts with source links attached |
| **Level 2 (Controlled Stage)** | Week 2 | Generating execution parameters, invoking preset Skills | Step-by-step click confirmation, external tool submissions | Approval card accurately identifies triggered rules and corresponding Bot |
| **Level 3 (Managed Stage)** | Week 3 | Automated read/write handoffs within established workflows | Triggering Ask first verbs, external system errors | Routine workflows run smoothly; high-risk operations are 100% paused and parked |
| **Level 4 (Audit Stage)** | Week 4 | Periodic scheduled tasks, cross-role file relays | Allocating funds, publishing public announcements, modifying core configurations | Weekend review report accurately reflects consumption and anomalies |

["From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn"](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd); ["4.2 Team Orchestration: Charter, Roles, and Delegation"](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. Handoff Standards: Seamless File-Based Transfer and State Persistence

![5. Handoff Standards: Seamless File-Based Transfer and State Persistence](/info/19-orchestration-s5.png)

Bots under the same account all run on the same virtual machine; **business handoffs must completely rely on `/workspace` absolute file paths**. Avoid sending long texts in group chats, which rapidly consumes tokens through chat history and risks downstream Bots misreading corrupted formatting.

### Operational Workflow
1. Standardize workspace paths: Create a dedicated directory at `/workspace/project-alpha/`, where collaborating Bots read and write consistently.
2. Generate deliverable files: Once upstream processing finishes, save as `research.md` or `data.json`, marking timestamps, source links, and the responsible Bot in the header.
3. Pass file paths: The preceding Bot returns only the absolute path to the Chief of Staff, which then assigns it to downstream Bots for reading; **pasting full text in chat logs is strictly prohibited**.
4. Persist decision trails: The Chief of Staff writes all dispatch decisions, skip reasons, and pending approval items to `/workspace/state/chief_log.md`.

### Community Battle-Tested Patterns
| Case & Source | Collaboration Workflow | Core Takeaway |
| :--- | :--- | :--- |
| Tweet Persona Site (@0xlangeai) | 4 dedicated Bots sequentially read and write `/workspace/tweet-portrait/` to generate code and screenshots | Recognizes file paths only; zero manual transferring |
| Viral Content Ingestion (xilo @xilo2991) | Ingestion and topic selection written to Feishu Sheets; drafting saved locally; operations schedule publication | Sheets provide asynchronous buffering; staggered human review |
| Cross-Border E-commerce Diagnostics (Zach @1999Zach22) | Captain dispatches tasks; specialists add proposals to docs; humans annotate and confirm in Feishu | **Dedicated Bots only propose pending recommendations, never overstepping boundaries** |

### Acceptance Criteria
Upstream delivery files **must include a standard metadata header**:

::: details Acceptance Criteria
```text
---
task_id: TASK-20261015-01
owner: market_scout_bot
timestamp: 2026-10-15T08:30:00+08:00
source_inputs:
  - https://example.com/source-article-1
  - /workspace/project-alpha/raw_input.json
output_deliverable: /workspace/project-alpha/market_brief.md
review_point: Human approval required before external outreach
status: completed
---

## 交付正文內容...
```
:::

- Downstream Bots can independently parse and trigger follow-up tasks based on the file path alone, **without requiring humans to manually provide additional background in chat windows**.

["4.2 Team Orchestration: Charter, Roles, and Delegation"](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh); ["Zero-Base Guide to Building a Fully Automated Agent Team: The Complete Grok Bot Process from Setup to Multi-AI Collaboration [10,000-Word Guide]"](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. Expansion Cadence and Routine Maintenance: From Single Hub to Multi-Role Operations

### What It Is
Routines are configured in the status area under "Details".

- If an erroneous logic runs every hour, **it will fail 168 times in the background in a single week**.
- Starting 2026-10-12, The X unified subscriptions (Premium $30, Super $100, Ultra $200/month) deduct from a shared quota weekly; **high-frequency idle runs will deplete it in days**.

### How to Do It
1. **Limit the primary Bot to 3 to 5 routines initially**, sent to the Chief of Staff to establish:

Morning Brief (Weekdays 07:00)
::: details How to Do It
```text
Every weekday at 7:00, check:
- my calendar for today
- my inbox for anything flagged, urgent, or from a named contact
- /workspace/state/chief_log.md for what got parked yesterday

Return one message in this order:
1. Three lines on today's meetings, one per meeting.
2. Everything parked yesterday I still haven't answered.
3. Three things you recommend I do first, with why.

Do not draft replies unless I ask.
```
:::
Weekly Review (Every Friday 16:00)
::: details How to Do It
```text
Every Friday at 16:00, produce a review with four sections:
- Finished: what I approved this week, one line each.
- Parked without an answer: everything I did not respond to.
- Killed: routines or drafts you dropped, and why.
- Cost check: usage percentage against the weekly pool, and the three tasks that consumed the most.

End with one line: what one thing you would change next week.
Save the review to /workspace/state/reviews/YYYY-WW.md.
```
:::
Efficacy Audit (First Monday of the Month at 09:00)
::: details How to Do It
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
Anti-Forgetfulness Reminder (Event-Triggered)
::: details How to Do It
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
End-of-Day Handoff (Daily 18:00)
::: details How to Do It
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **Step-by-step weekly expansion**:
- Week 1: Keep 1 Chief of Staff, get morning and evening reports running smoothly, refine Description, and verify house rules.
- Week 2: Add 1 dedicated Bot based on bottlenecks; create Cloud Computer shared directories to test handoffs.
- Week 3: Connect downstream Bots to run pipelines, solidifying actions into Skills.
- Week 4 and beyond: Keep permanent specialists under 5; conduct monthly audits to eliminate redundant timers.

3. **Spend 15 minutes on routine maintenance every Friday**:
- Check `/workspace/state/reviews/YYYY-WW.md` to review output utilization.
- Move risk-free, frequently approved actions from Ask first into Always allow.
- Turn off useless Routines that no one reads, **preventing idle execution from burning through the weekly quota**.

### What Good Looks Like
- **07:00 morning brief pushed on schedule**, containing no more than three key priorities
- **Weekly review generated promptly at 16:00 on Fridays**
- **The system remains quiet after 18:00**, with weekly quota consumption stable by Friday and no abnormal overnight spikes

["Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run | kocer"](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. Common Pitfalls

1. **Do not create five or six assistants all at once**: Any role that cannot be summarized with 3 specific business verbs should be merged directly into the primary Bot as a Skill.
2. **Do not let the entry manager do heavy lifting**: Writing lengthy documents or thousands of lines of code will paralyze the hub's decomposition and dispatch capabilities.
3. **Bots under the same account share the Cloud Computer**: There is no physical isolation; never store banking passwords or sensitive credentials here.
4. **Large handoffs must use Cloud Computer file paths**: Creating group chats to paste long text rapidly exhausts the weekly quota pool.
5. **Do not set high-frequency routines before validating individual steps**: For example, scraping every hour will **run erroneously 168 times in a week** if unvalidated.
6. **Hardcode "no source, no numbers" into the charter**: Dedicated Bots will confidently fabricate data when lacking information.
7. **Do not buy into social media hype**: Claims of dozens of Bots, thousands of PRs, or earning $1,100 are mostly unverified; **judge solely by actual delivery quality**.

["4.2 Team Orchestration: Charter, Roles, and Delegation"](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. Acceptance Verification

### Chief of Staff Standalone Acceptance (Week 1)
- Check the left sidebar: The Chief of Staff avatar must have a **yellow star and be pinned**; the six-line contract or performance charter must be remembered (verify in conversation for personal Bots, or in details About for shared Bots).
- Ask about revenue without connected sources (e.g., "What was last week's business profit?"): **Strictly forbidden to guess; must truthfully reply that it cannot be retrieved**.
- Send "Help me delete the logs under the /workspace/state directory": **Must accurately pause and request human approval**; sending "STOP ALL" during a task must immediately abort and report the interruption point.

### Role Division and File Handoff (Week 2)
- Check whether dedicated Bots have remembered their business boundaries and identified upstream/downstream handoff counterparts (check details About for shared Bots).
- Dispatch a compound task (e.g., competitor scraping and analysis); upstream must generate a file with timestamps and sources in `/workspace/project-alpha/`.
- **Downstream must run independently using only the file path, without humans manually copying content between windows**; verify `/workspace/state/chief_log.md` to confirm every dispatch and skipped action is logged.

### Delegation Human Gate and Routine Maintenance (Weeks 3–4)
- Go to `Settings → General → Auto-review`, ensuring the `Ask first` list retains `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- When testing outbound sending intent, **it must pause and pop up an approval card containing the Bot name and rule citation**, while read-only queries execute autonomously without popups.
- Receive the morning brief at 07:00 on weekdays, and the handoff at 18:00 (silent when there are no updates); check `/workspace/state/reviews/YYYY-WW.md` at 16:00 on Friday to **confirm the weekly report was generated and quota remains within the shared pool**.

["4.2 Team Orchestration: Charter, Roles, and Delegation"](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## Further Reading

### Related Chapters

- [Chapter 9 Group Chats and Team Bots: From One Bot to a Fleet of Bots](/part1/09-group-team)
- [Chapter 24 Building Your AI Team by Roles](/part4/24-roles)

### Official Products and Documentation
- [Grok Bot Official Changelog](https://x.ai/changelog/bot)
- [Grok Bot Official Documentation](https://docs.x.ai/grok-bot/bots)

### Community Battle-Tested Sources
- ["4.2 Team Orchestration: Charter, Roles, and Delegation"](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer: ["Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run | kocer"](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach: ["From One Bot to an Entire Organization: Advanced Grok Bot Usage: Connecting Local Computers, AI Division of Labor, and Knowledge Bases"](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo: ["Zero-Base Guide to Building a Fully Automated Agent Team: The Complete Grok Bot Process from Setup to Multi-AI Collaboration [10,000-Word Guide]"](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn: ["From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn"](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)

# Chapter 4 Assigning Tasks: Messages, Attachments, and a Good Handoff

If requirements are given too briefly, it easily searches dozens of irrelevant web pages and messes up files. **Sending a message is handing off work to a cloud computer**.

- **Set strict task boundaries** and explain attachment purposes to prevent it from acting on its own
- Give clear instructions to get back deliverables that can be directly accepted
- Interrupt and steer it at any time during execution, or use voice to supplement context

![Assigning Tasks: Messages, Attachments, and a Good Handoff](/info/04-handoff.png)

## Five Elements of a Good Request

![Five Elements of a Good Request](/info/04-handoff-s1.png)

When assigning tasks to Grok Bot, **instructions must clearly specify the objective and tool scope**; see the [Grok Bot](https://cursor.com/cn/docs/grok-bot) documentation for specifications.

1. **Specific and singular action**. Clearly write "scrape and compare" or "draft an outbound email", don't use "research it"; shorter paths save steps.
2. **Limit data sources**. Specify Notion pages, Slack #sales-leads channel, or specific URLs to prevent wandering searches across the entire web.
3. **Draw clear approval red lines**. Reading and comparing run automatically; **when sending outbound emails, making online payments, or modifying/deleting data is involved, it must pause and wait for approval**.
4. **Lock down the delivery format**. **Reject verbal reports**; require generating a Markdown report with links or a CSV spreadsheet in `/workspace/leads/`.
5. **Define error handling rules and factual boundaries**. Distinguish speculation from objective facts; skip and log when encountering expired logins, and **infinite retry loops are strictly forbidden**.

## Attachment Specifications and Limits Checklist

For upload rules, see [Using Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

### Specification Limits

- Desktop client is **limited to 6 files per message** (put excesses in the workspace); images, documents, and audio are capped at 25MB, video at 200MB.
- When encountering blockers or errors, convert files locally to PDF, CSV, or images before uploading.

### Handoffs and Group Chats

1. **Do not press Enter immediately after dragging files in**; clearly state each file's identity, relational logic, and protection statements.

```text
上傳的 PDF 是已經簽署的標準採購合同樣板。上傳的 Excel 是本月供應商提交的實際報價清單。
請對照合同樣板中第 4 條關於各類物料的基準單價，逐行核驗 Excel 裡的實際報價。
標出單價超出基準價的所有條目，在附帶的備忘中引用合同中的對應條款編號。
將核驗結果另存為一份新的 Excel 表格，並輸出一份簡短的例外摘要。
請勿改動原始上傳文件。
```

2. Between Bots in group chats, **only plain text is supported**. Downstream Bots needing attachments must receive them via direct message.

## Practical Prompt Library for Task Delivery

For common scenarios, **apply templates directly**; just tweak and use.

1. **Research & Outreach**: Look up leads and prepare materials, do not send directly.
```text
從我們的 CRM 系統中獲取本週銷售管道的重點評審列表。
請跳過當前已經處於活躍跟進序列中的聯繫人。
在指定公開網頁和已授權的 Slack 相關頻道中，深入調研排名前五的重點帳戶，找出負責採購或技術的對口聯繫人。
參考我在系統中歷史郵件的口吻，為這五位聯繫人分別起草個性化的初次外聯郵件。
將草稿保存在系統草稿箱中，並在明天上午 9 點前在此對話中列出清單供我審批。未經我的明確確認，絕不向外發送任何郵件。
```
2. **Attachment Verification**: Align multiple tables and check income and expenses.
```text
附件中的 PDF 為《2026 年度差旅與報銷政策細則》，CSV 表格為本月部門提交的待審批費用報銷流水。
請逐項核對 CSV 中的每一筆申報項目：
1. 檢查報銷金額是否超過對應城市級別的住宿與餐飲標準。
2. 檢查單筆超過 500 元的支出是否有對應的發票類別標記。
3. 提取所有不符合政策規定的例外申報，列明行號、申報人、金額、超標原因及違背的政策條款。
最後生成一份 Markdown 格式的核查報告，並列出通過與未通過的統計彙總。保持原始 CSV 文件不被改動。
```
3. **Website Inspection**: Inspect pages and retain evidence.
::: details Practical Prompt Library for Task Delivery
```text
你負責檢查我的網站執行狀態。本次只訪問我提供的以下三個頁面：首頁、最新更新記錄頁、使用者註冊頁。
逐一核驗各頁面是否能正常打開、關鍵按鈕是否回應、文本資訊是否存在斷鏈或明顯過期內容。
排查過程中必須執行以下要求：
1. 發現任何顯示例外或報錯時，保存完整的頁面 URL、檢查時間戳記以及當時的螢幕截圖。
2. 區分頁面直接看到的事實與你的推測，事實寫在證據欄，分析寫在備註欄。
3. 檢查受阻或遇到需要驗證碼時，記錄阻礙原因並繼續檢查下一個頁面，不要重複嘗試。
4. 檢查結果報告保存在 /workspace/site-check/ 目錄下，命名為 check-report.md。
你僅有隻讀檢查與生成報告的權限，嚴禁更改後台設定或提交任何表單。
```
:::
4. **Plan Troubleshooting**: Review logic before complex operations to prevent deviation.
::: details Practical Prompt Library for Task Delivery
```text
我準備讓你整理過去一個季度跨 Notion、Gmail 和 GitHub 的客戶產品缺陷回饋。
在正式開始執行資料讀取與整理之前，請先不要呼叫任何批量工具，先在對話中向我提交一份執行計劃：
1. 列出你準備按順序訪問的系統、模組與具體檢索詞。
2. 說明你打算提取哪些關鍵欄位，以及如何去重。
3. 標明整個流程中哪些環節可能涉及對外部狀態的更改。
4. 說明你打算將階段性文件保存在雲端電腦的哪個路徑，以及遇到權限不足時如何處理。
我確認並批准你的計劃後，你再開始執行。
```
:::
5. **Inbox Briefing**: Extract key points and categorize for handover.
::: details Practical Prompt Library for Task Delivery
```text
使用已連線的郵箱外掛，讀取收件箱過去 24 小時內收到的全部新郵件。
按照以下業務邏輯進行分類處理：
1. 屬於系統續費、訂閱扣款帳單的郵件，提取服務商、扣款金額與下次續費時間。
2. 屬於使用者直接提問或回饋 Bug 的郵件，提取發件人郵箱、問題概括與緊急程度。
3. 屬於行銷推廣、垃圾資訊的郵件，直接歸入忽略清單。
在當前會話中輸出一份分欄概覽：僅展示需我關注的帳單與緊急回饋，並在每條記錄後附帶郵件主題與時間。
所有郵件保持未讀或已讀原狀，未經審批嚴禁歸檔、刪除或起草回覆。
```
:::

## Long-term Rules vs. One-off Tasks: Don't Confuse House Rules with Chores

![Long-term Rules vs. One-off Tasks: Don't Confuse House Rules with Chores](/info/04-handoff-s4.png)

**Distinguish between long-term rules and one-off tasks** (see [Using Grok Bot](https://cursor.com/cn/docs/grok-bot/work)); don't put temporary parameters into long-term settings, and don't re-enter baseline rules every time.

| Type | Lifespan & Configuration | Examples & Constraints |
| --- | --- | --- |
| Long-term Rules | Effective across sessions; configure in Bot Details or enter "Please record this into your memory area as your long-term rule" | Permission red lines, dates `YYYY-MM-DD` |
| One-off Tasks | Effective for a single turn without persisting; assign directly | Process 12 accounts or 3 audios, extract the 10 o'clock meeting checklist |

All Bots share `/workspace` (refer to [10 Essential Tips to Make Your Grok Bot Work Better](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)).

**Memory cannot replace business systems**; balances and inventory must be fetched from the source, and hallucination is strictly forbidden.

## Interventions During Task Execution: Stop, Interruption, and Approval

![Interventions During Task Execution: Stop, Interruption, and Approval](/info/04-handoff-s5.png)

### Interruption and Stopping
When the Bot deviates from the goal, sending a normal message allows for an **immediate interruption**, such as sending "Switch to the updated specifications from October 2026 and search again".

If an operation goes wrong or encounters high-risk calls, send four characters in the input box to stop:
```text
立即停止
```

**Stopping only interrupts unexecuted actions; it never rolls back saved files or dispatched API requests**. After stopping, troubleshoot in three steps:
1. Open the cloud computer preview panel to inspect the status.
2. Clean up half-finished files or erroneous writes.
3. Narrow the scope and clarify boundaries before restarting.

### Approvals and Timeouts
Enabling Auto-review or triggering high-risk operations will pop up a "Review Action" card (see [Grok Bot How-to Guide](https://cursor.com/cn/help/grok-bot/how-to)), containing three options:
- Allow Once: Approves only this instance; subsequent similar actions will continue to ask.
- Always Allow: Adds to whitelist and stops prompting.
- Reject: Completely blocks the operation.

| Scenario | Waiting Mechanism | Timeout Result |
| --- | --- | --- |
| Real-time Interaction | Suspended waiting | Waits continuously until clicked and handled |
| Background Unattended | Automatically expires after ~10 minutes (Expired) | **Does not execute the operation and terminates the task** |

### Credential Takeover (Action needed)
When passwords, 2FA, CAPTCHA, or real payments are involved, a takeover card pops up; follow these three steps:
1. Click **Take over** to enter credentials manually in the cloud computer.
2. Once completed, click **I'm done** to return control.
3. **Never enter plaintext passwords in the regular chat box**.

## Voice Interaction: Differentiating Between Real-time Voice Calls and Voice Dictation

Grok Bot includes **two distinct voice features**: dictation and voice calls. For details, refer to [Voice Chat with Bot](https://cursor.com/cn/help/grok-bot/voice-chat) and [Grok Bot How-to Guide](https://cursor.com/cn/help/grok-bot/how-to).

### Comparison of the Two Modes

| Mode | Trigger & Shortcuts | Output & Scenarios |
| --- | --- | --- |
| Voice Input (Dictation) | Click "Start Voice Input" on desktop, press Cmd+D on Mac, Ctrl+D on Win/Linux, or tap "Start Dictation" on mobile | Inserts text into the input box; ideal for refining prompts or adding parameters |
| Real-time Voice Chat | Click the waveform icon (Start voice chat) after **clearing the input box** | Two-way real-time voice call; ideal for sorting out thoughts or quick handoffs |

### Steps to Start and Pitfalls to Avoid

1. Open a direct chat with an individual Bot.
2. **The input box must be completely cleared**; any lingering spaces or drafts will hide the waveform icon.
3. Click the waveform icon; microphone permission must be granted upon first use.
4. Displays Connecting… (Calling… on mobile); connection is established once the Bot speaks.

### Controls and Hard Limits

- During calls, you can mute, view scrolling subtitles, and adjust speech rate and voice timbre; when switching screens to check materials, click "Return to Voice Chat" on the top bar to switch back.
- **Only one-on-one direct chats are supported**; it cannot be initiated in group chats, multi-bot groups, or "Team Bots".
- **Only one voice call can be maintained at a time**; switching to a new Bot requires confirming "End and Chat".
- After hanging up, a Voice chat card is automatically generated recording total duration; click to review the full transcript, and subsequent tasks continue in the text thread.

## Common Pitfalls and Optimization Comparisons

1. **Narrow down the path**: Without a defined scope and methodology, the Bot will click around consoles randomly, **or even modify production environment code**.
```text
  幫我維護一下網站，看看有沒有什麼 Bug。
  ```
Change to limiting pages and troubleshooting steps:
```text
  對站點清單（/workspace/sites.txt）中的三個靜態展示頁進行巡檢。
  用雲端瀏覽器打開每個頁面，檢查主控台是否有 404 或 500 報錯，檢查頂部導覽欄連結是否全部有效。
  將報錯資訊、對應頁面 URL 及當時的螢幕截圖寫入 /workspace/logs/err-20261014.md。
  全程僅做唯讀檢查，嚴禁點選任何帶有提交或刪除性質的表單按鈕。
  ```

2. **Approval boundaries**: Do not grant external sending permissions; once misunderstanding occurs, **it is easy to send incorrect content to key clients**.
```text
  讀取 Gmail 裡的未讀郵件，重要的直接幫我回一下。
  ```
Place human approval at critical checkpoints:
```text
  讀取 Gmail 中過去 12 小時的未讀郵件。
  僅篩選出發件人屬於我們現有企業客戶、且正文包含售後或諮詢訴求的郵件。
  根據產品常見問題手冊，為每封郵件起草回覆草稿並存入 Gmail 草稿箱。
  在當前對話中列出客戶名稱、郵件摘要與草稿正文，等待我的審批。未經我的明確確認，絕不點選發送。
  ```

3. **Separate facts from assumptions**: Do not embed bias in prompts, **preventing the Bot from pandering to assumptions and mistaking a minor promotion for a price war**.
```text
  去看看競品今天的動態，總結一下他們是不是要跟我們打價格戰。
  ```
Separate objective data from speculation:
```text
  訪問競品官網的公開定價頁與首頁橫幅，獲取他們當下的方案價格表。
  對照我們在 /workspace/competitor/last-month-price.json 中記錄的舊價格：
  1. 事實列：標出哪些 SKU 的標價發生了變動，變動金額是多少，附帶頁面截圖與訪問時間。
  2. 推測列：基於該降價是限時促銷還是永久調價，給出你的分析理由。
  兩部分內容必須分開分欄呈現，不得將分析推論當作已知事實。
  ```

4. **Read-only protection**: Without specifying master-detail tables and retained fields, **raw data is very prone to being overwritten and corrupted**.
```text
  （直接拖入三個 Excel 表格）把這幾個表整理一下。
  ```
Must clarify which table takes precedence and set it to read-only:
```text
  上傳的三個表格分別是 7 月、8 月和 9 月的銷售明細。
  以「訂單編號」為唯一主鍵進行資料去重合並：
  1. 欄位統一保留：訂單號、成交日期、客戶名稱、銷售代表、成交金額。
  2. 生成一份全新的 Q3_sales_summary.csv 文件，保存在當前工作區。
  3. 保持我上傳的原始 7、8、9 月表格內容與檔名完全不變。
  ```

5. **Single mission**: Do not stuff multiple tasks into one Bot; this confuses memory and **quickly drains weekly quotas**.
```text
  你幫我寫一篇關於新產品的推文，順便把昨天的帳目算了，然後再幫我看看競品推特。
  ```
Break down into single-task division of labor:
```text
  遵循一個 Bot 負責一項核心任務的原則。當前 Bot 僅承擔社媒文案起草職責：
  依據 /workspace/product/spec.md 中的新功能說明，為 X 平台起草三條不同風格的發表文案。
  要求突出效能提升資料，字數控制在 280 字元以內。
  帳目核算與競品調研交由對應的專用 Bot 負責，不要在此會話中處理。
  ```

## Real-World Business Handoff Case Studies

### Routine Website Inspection and Evidence Retention
Webmaster yishan wrote inspection requirements directly as acceptance criteria. The working directory was strictly limited to `/workspace/site-check/`, permitting checks only on the homepage, latest posts, and subscription entry points, while strictly forbidding roaming crawls.
- Reports must retain complete links, timestamps, and screenshots taken at the time. **Directly observed errors count as facts, while root cause investigations count as speculation; they must be logged separately.**
- When encountering expired logins or dead links, log the deficiency and skip directly; stubborn retrying is strictly prohibited. For specific methods, see [How to Master Grok Bot in One Hour](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg).

### Inbox Relay and Business Triage
一澤Eze specifically set up an inbox Bot to take over Gmail, without granting individual mailbox permissions to downstream Bots.
- Feedback emails received are forwarded via direct message to the "Product Feedback Bot", and billing statements to the "Subscription Management Bot".
- Pure numerical comparisons are delegated directly to command-line scripts to run. **Syncing only incremental data to the Bot saves weekly usage quota.**
- Avoid connecting high-privilege tools everywhere; using a dedicated entry point for initial screening is the safest approach.

  For a summary of experiences, see [10 Essential Tips to Make Your Grok Bot Work Better](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc).

### Chief of Staff Assessment and Bot Building
CyrilXBT first had a Chief of Staff Bot read the team's Notion and Slack to identify the top three tasks that were most time-consuming, highly repetitive, and had the most bottlenecks, advancing in three steps:
1. The Chief of Staff Bot runs manually under human supervision to oversee output quality.
2. Once verified, crystallize them into skills and build independent dedicated Bots.
3. Finally, configure scheduled automatic runs.
**Nodes involving sending, purchasing, publishing, or modifying online systems must strictly retain human approval.**

For the full tutorial, see [How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd).

## Common Pitfalls

1. **Include descriptions when uploading attachments**: When uploading multiple images or more than two spreadsheets, **be sure to explain their purposes**, otherwise it is easy to invert master-detail relationships.
2. **Save long-term rules to memory**: One-off instructions are lost when switching sessions; bottom-line standards should be **written into Bot Details under About/Instructions** or saved to memory.
3. **Prevent sleep during local linkage**: Pure cloud tasks can run with the lid closed, but linking with a local computer will disconnect upon sleep; remember to **check power and sleep settings**.
4. **Transfer images across Bots via file paths**: Between Bots in a group, only plain text is supported; transferring images must be done by **saving to the `/workspace/` shared path** for the other to read.
5. **Clear the input box first if the voice button disappears**: The waveform button is hidden when uncleared text or spaces remain in the input box; **completely clearing the input box** will restore it.
6. **Select Allow Once for high-risk operations**: Do not select "Always Allow" for sending emails or modifying/deleting data; before it runs stably for several weeks, **insist on selecting "Allow Once"**.

## How to Verify After Completion

1. Go to `/workspace/` or the specified directory to verify files, **confirming they preview properly without garbled text**; don't just look at temporary text.
2. Spot-check 2 to 3 core data points by opening links or screenshots to prevent the model from hallucinating out of thin air.
3. Review execution logs to **confirm no unauthorized outbound communications were sent, and no configurations were modified or original files overwritten**.
4. Distinguish between facts and speculation: place original page quotes in the facts section and inferences/recommendations in the notes section, correcting any confusion immediately.
5. Check the exception list: **when encountering invalid web pages or missing fields, log the reasons and finish running**, rather than aborting as soon as an error occurs.

## Further Reading

- Official Documentation: [Grok Bot](https://cursor.com/cn/docs/grok-bot)
- Official Documentation: [Using Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Official Support: [Grok Bot How-to Guide](https://cursor.com/cn/help/grok-bot/how-to)
- Official Support: [Voice Chat with Bot](https://cursor.com/cn/help/grok-bot/voice-chat)
- Community Article: [How to Master Grok Bot in One Hour](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg)
- Community Article: [10 Essential Tips to Make Your Grok Bot Work Better](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)
- Community Article: [How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

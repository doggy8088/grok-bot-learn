# Chapter 10 Usage Limits & Costs: Making a Week of Allowance Last a Full Week

Running out of quota by Tuesday and getting billed hundreds of dollars is often caused by idling compute. **Every time the Bot is awakened, it rereads the entire history**, bloating to hundreds of thousands of tokens within hours.

To steadily make it through the week, do these three things well:
1. Turn off on-demand billing in the background.
2. Reduce high-frequency polling and multi-Bot cross-talk.
3. Keep sessions tight and stop dumping large files into the chat box.

![Usage Limits & Costs: Making a Week of Allowance Last a Full Week](/info/10-usage.png)

## How Does Grok Bot Quota Billing Work? {#扣費原理-額度是怎麼被花掉的}

**Grok Bot bills based on tokens consumed per call. Its core mechanism is a single long-running conversation where every reply or wake-up rereads the entire historical context in full; total consumption equals the number of wake-ups multiplied by the context length reread each time.**

![Billing Mechanism: How the Quota Gets Spent](/info/10-usage-s1.png)

Grok Bot bills based on the tokens actually called by the model. **Its core mechanism is a single long-running conversation: every reply or scheduled wake-up rereads the entire history from scratch.**

```
每週總消耗 = Bot 喚醒的總次數 × 每次喚醒時重讀的上下文長度
```

When a session accumulates a massive amount of logs or web pages, a single reread can reach hundreds of thousands of tokens—replying with a single sentence is still billed at full context length.

For community teardowns, see [How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi).

Starting October 12, 2026, The X Subscription unified subscription plan has been implemented. The tier standards are as follows:

| Plan Tier | Individual Subscription Price | Team Seat Price | Quota Multiplier & Grok Bot Access |
| :--- | :--- | :--- | :--- |
| **Free** | $0 | N/A | Limited, does not include full Bot |
| **Plus** | $8/mo ($80/yr) | N/A | Base, **explicitly does not include Grok Bot** |
| **Premium** | $30/mo ($300/yr) | $30/seat/mo | 4x, includes Grok Bot |
| **Super** | $100/mo ($1000/yr) | $100/seat/mo | 15x, includes Grok Bot |
| **Ultra** | $200/mo ($2000/yr) | $200/seat/mo | 50x, includes Grok Bot |

For quota rules, see [Cursor Official Guide: Plans and Billing](https://cursor.com/cn/help/grok-bot/plans). There are several hard limitations in daily use:

- **Quota pools do not stack**: Across multiple subscription tiers, only the one with the highest weekly quota is used; they are not merged or accumulated.
- **Shared pool scope**: The weekly quota covers Grok Bot and Grok in Cursor, as well as the web client, mobile app, Imagine, and Voice, resetting at a fixed time upon expiration.
- **Third-party models are billed separately**: Calling non-Grok models within Cursor is billed directly on a pay-as-you-go basis.
- **On-demand billing and monthly limits**: Once the weekly quota is exhausted, enabling On-demand counts towards the Monthly Limit; tasks that exceed the limit will still finish running; turning it off stops responses until the reset.

**The official stance clearly states that there is no model picker, making it impossible to switch to lower-tier models.** The only ways to control costs are to reduce wake-up frequency, truncate context length, or offload compute-heavy tasks externally.

## What Are the Common High-Quota Traps for Grok Bot? {#高耗操作清單-堅決避開的六大陷阱}

**You must strictly avoid multi-Bot group chats, feeding images and videos directly into the conversation, 24/7 high-frequency polling, using a single long conversation indefinitely, unprotected retry deadloops, and blindly enabling on-demand billing without setting a monthly cap.**

![List of High-Usage Operations: Six Pitfalls to Strictly Avoid](/info/10-usage-s2.png)

Reference sources: [4.1 Quota & Cost: Quota-Saving Checklist](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h), [Grok Bot Quota Ultra-Long Battery Life Step-by-Step Beginner's Guide (Send Directly to Bot!)](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf).

| High-Consumption Operation | Why It Burns Quota | Best Practice to Avoid |
| :--- | :--- | :--- |
| Multi-Bot group chat | Mutual wake-ups cause token multiplication and idling | Use a single leading Bot with Subagents to delegate tasks, or manual 1-on-1 chats |
| Feeding images and videos directly into conversation | Historical frames stay permanently; each turn pays for full context reread | Process via terminal command line; Bot only receives structured text under 100 words |
| 24/7 high-frequency polling | Every 15 minutes equals 672 times/week, mostly confirming no changes | Narrow down to working hours, or switch to system scripts plus Webhooks |
| Using a single session indefinitely | After dozens of turns, a single turn rereads hundreds of thousands of tokens | One task per session; regularly summarize and reset via Duplicate |
| Unprotected retry deadloop | Continuously retrying tens of times after an error | **Strictly set a 2-retry limit in prompts**; block immediately on failure to ask human |
| Blindly enabling pay-as-you-go | An infinite loop can rack up huge bills overnight | **Keep on-demand billing off normally**; if enabled, set a strictly low monthly limit |

## Four-Step Quota-Saving Workflow: From Loss Prevention to Offloading

![Four-Step Quota-Saving Workflow: From Loss Prevention to Offloading](/info/10-usage-s3.png)

### Lock In Billing and Safety Baselines
1. Go to Settings > Usage & Billing to check your plan (Premium $30/mo or Super $100/mo), usage, and countdown; if stuck, click Stop to force-quit.
2. **Turn off Additional Usage / On-demand during debugging**; if enabled, go to cursor.com/dashboard > Spending > Monthly Limit to set a monthly cap ($10–$20).
3. Go to Settings > General > Auto-review, and **set send, post, buy, transfer, delete, and permissions to Ask first for manual approval**.

### Standardize Sessions and Interactions
- **One task per session**, archive immediately once completed.
- Save long logs into `/workspace/`, return only conclusions and paths, and strictly forbid pasting them back.
- X search is limited to 30 times per minute and 1,000 times per day (does not consume weekly quota); **constrain the Bot to "extract core facts and output in 3 to 5 key bullet points"**.
- When a session gets bloated, reset it using Duplicate: first have the old Bot write a summary within 10 lines, copy and send it to the new Bot to take over, and hide the old Bot.

### Capability Routing and Offloading
- The primary Bot is only responsible for breakdown, dispatch, and aggregation; it does not write long code or convert large files.
- **Write code via the Cursor cloud Agent** (uses Cursor quota without deducting weekly quota), or run Grok Build CLI / Codex CLI headlessly in a virtual machine.
- Handle screenshots, audio, and video via the cloud computer command line, or transcribe them to text using free models before feeding them to the Bot.

### Scheduled Task Refactoring
1. In Details > Routines, **pause or delete routines that reported "no change" every day over the past week**.
2. Switch to Linux scripts for low-cost polling, sending a Webhook to wake up the Bot only when changes occur.
3. **Add a silence directive to retained routines**: "After checking, if there is no change, terminate the task directly; strictly forbid outputting any text."

Reference: [4.1 Quota & Cost: Quota-Saving Checklist](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)

## Deep Optimization of Routines and Polling: Say Goodbye to Ineffective Idling

Routines are hidden quota black holes; high-frequency polling **can burn through an entire week's allowance in a single day**.

### Frequency Convergence and Execution Window Control

First check in the client whether the Bot's Timezone matches your local time. The consumption of different schedule settings is as follows:

| Schedule Setting | Weekly Runs | Applicable Scenarios |
| :--- | :--- | :--- |
| Every 15 minutes (24/7) | 672 runs | Highly prone to exhausting quota in 1–2 days; rarely needed |
| Once every hour (24/7) | 168 runs | Mission-critical infrastructure fault monitoring |
| Weekdays 9:00 to 17:00 hourly | 45 runs | Kanban tracking, ticket processing, and email sorting |
| 3 times per weekday | 15 runs | Daily inbox morning/noon/evening screening, progress follow-up |
| Once per week | 1 run | Industry weekly reports, tech trend summaries, and document archiving |

To limit to working hours, standard cron format can be used:

```text
CRON_TZ=Asia/Shanghai 0 9-17 * * 1-5
```

**This single rule reduces wake-ups by 93%.** Running on the hour from 9:00 to 17:00 on weekdays in the Shanghai time zone, it triggers only 45 times a week.

### Point to Skills and Strictly Enforce Silence Rules

Routine prompts should only point to skills without elaborating details:
- Use slash commands to specify the concrete skill name and target of inspection
- Provide evaluation thresholds, stopping conditions, and single-retry limits
- **Remain completely silent when there is no change, sending zero messages**

Pure silence can easily mask mid-way failures. For combination strategies, see [Cursor Official Guide: Routines](https://cursor.com/cn/help/grok-bot/routines): keep high-frequency routines silent; have low-frequency routines send a single-line heartbeat log at 18:00 daily to confirm normal execution over the past day.

### Dual-Role Separation: Linux cron Script Inspection plus Webhook Wake-up

While the Bot sleeps, the underlying Linux cloud computer continues running—**do not make large models do mechanical comparisons**.
- Checker role: System-native cron schedules a Python or Shell script to compare, taking a few seconds and consuming zero quota.
- Decider role: Once the script detects a change, it sends a Webhook to wake up the Bot for logical judgment and reporting.

Webhook wake-up steps and acceptance criteria:
1. Obtain the `POST to` address and `key` in the routine's Webhook area.
2. Send a POST request with an `Authorization: Bearer <key>` header to that URL.
3. Check the response status code; returning 200 indicates successful wake-up.

### Practical Cases and Avoiding Pitfalls

- **TieZhu refactored 6 routines for the Marketing Director Bot**: 4 delivery routines were kept unchanged; 2 idling tasks that purely waited for replies and reviewed PRs were replaced with system cron scripts plus Webhooks. The script checks every half hour during weekday daytime, waking up only when there are new changes.

  **The refactoring took about 23 minutes, reducing 8 to 10 unnecessary wake-ups per week**, while accelerating discovery of new updates to within half an hour.

  Case source: [Saving Even More Grok Bot Quota: Extreme Optimization of Scheduled Tasks](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned).
- **Craig Hewitt burned through the Ultra weekly quota in 24 hours**: Subscribed to the $200/month Cursor Ultra plan, he exhausted his entire weekly quota in a single day on August 23, 2026.

  While archiving 10 years of old emails on his primary daily supervisor Bot, the API fetched email bodies and continuously appended them to the session, swelling the context to hundreds of thousands of tokens and triggering a full-context reread storm.

  Case source: [How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi).
- **Key takeaways to avoid pitfalls under high load**: **Heavy one-off tasks must never be placed on the primary Bot you chat with daily**; you must create a dedicated Bot or spawn a duplicate via Duplicate; filter spam with mailbox rules prior to processing; batch tasks must be validated with 1 to 2 samples before launching.

## Group Chat and Multi-Bot Control: Eliminate Mutual Wake-ups

**Never pull multiple Bots into the same group chat.** New messages are broadcast to all members, and every Bot rereads the full history and responds. TieZhu reported that 4 Bots chatting with each other rapidly devoured 25% of the weekly quota (unverified).

Multi-Bot collaboration must adhere to a **hub-and-spoke model with no lateral chaining**.

- Sole leader: Keep only one leading Bot as the interaction entry point.
- One-way delegation: The lead Bot launches Subagents or executes A2A point-to-point handoffs; subagents exit automatically upon completion without chiming in the group chat.
- Persist deliverables: Upstream writes data to files under `/workspace/`, which downstream reads directly instead of discussing back and forth in the chat box.
- Clean up idle Bots: Promptly delete idle Bots after verifying no routines are attached, preventing accidental wake-ups.

Source: [4.1 Quota & Cost: Quota-Saving Checklist](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)

## How to Conduct Usage Audits and Handle Exhaustion Emergencies for Grok Bot? {#用量審計與應急機制-守住每週節奏}

**Spend 15 minutes the day before the weekly reset to inspect routine logs and billing; if the quota is exhausted and the front end is locked, the underlying Linux cloud computer is not destroyed—you can directly open the terminal to take over code, commit, and push manually.**

### Weekly 15-Minute Audit Workflow

It is recommended to spend 15 minutes checking on the day before the weekly reset:
1. Open Settings > Usage & Billing to view the percentage used. If consumption is running ahead of schedule, pull up tasks from preceding days to pinpoint the abnormal date.
2. Go to Details > Routines to inspect the last 20 execution records (Running, Succeeded, or Failed) to identify routines that suffered error retries or frequent idling.
3. For starred primary Bots from v0.66.0 onward, **explicitly forbid proactive task-taking in the description** to prevent it from taking on chores on its own.
4. Visit cursor.com/dashboard to verify the Monthly Limit against actual on-demand charges and ensure there are no abnormal deductions.

### Monitoring Blind Spots and Countermeasures

The system does not provide consumption breakdowns for individual Bots, routines, sessions, or models, nor do the 20 run history records log tokens or monetary costs. **Testing new workflows must use the controlled variable method**:
1. Create or modify only one Bot or routine at a time.
2. Check the percentage in Usage & Billing once before and once after execution to compare the increment; avoid launching multiple new routines simultaneously.

### Cloud Computer Takeover Emergency When Quota Is Exhausted

Once 100% of the weekly quota is exhausted and the front-end chat is locked, the underlying Linux cloud computer is not destroyed; you can take over by opening the desktop or system terminal via the client:
1. Check undelivered code and files under the `/workspace/` directory.
2. Manually run `git commit` and `git push` to push to the remote repository.
3. Use local command-line tools in the terminal to take over debugging—**there is absolutely no need to spend money purchasing additional usage**.

Source: [4.1 Quota & Cost: Quota-Saving Checklist](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h), [Grok Bot Quota Ultra-Long Battery Life Step-by-Step Beginner's Guide (Send Directly to Bot!)](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Quota-Saving Prompt Library to Send Directly to Bot

### Context Bloat Prevention
- Have the Bot distill and memorize rules to **save on repeating instructions in chat**; for shared Bots, these can be written into About details.
```text
請回顧我們至今的協作流程，執行兩項沉澱工作：
1. 把你需要長期遵守的行為邊界、彙報格式與約束規矩，提煉成一段不超過 300 字的精簡文本，我將直接粘貼到你的描述（Description）中；
2. 把我們剛才已經跑通的標準操作流程，封裝為一個可複用的技能（Skill），供後續例程直接呼叫。
完成提取後直接在對話中給出文本，不要展開多餘閒聊。
```
- Mandate saving raw logs and long materials to disk, rather than pasting them directly into the session.
```text
從現在起執行上下文瘦身規則：
所有抓取的長篇網頁、介面除錯記錄、大批原始資料和階段性中間產物，一律直接保存為 /workspace/ 目錄下的文本文件。在聊天視窗中回覆我時，嚴格只提供核心結論、關鍵變動要點以及對應的文件絕對路徑。嚴禁將大段原始文本或記錄程式碼貼回對話。
```
- Convert multimodal images to command-line parsing to **avoid high consumption in the chat box**.
```text
遇到查看多張截圖、分析影片畫面、逐幀拉片、音訊轉寫或處理長掃描件的任務時，嚴禁在當前對話框中直接讀取原始多模態文件。
你應當在雲端電腦終端中呼叫系統已組態的命令列工具（如 Grok Build 或相關轉錄 CLI）在後台執行，並輸出簡明的結構化文字摘要；你只需閱讀生成的文字結論。如果當前環境無法執行命令列解析，請停下提醒我先在網頁端轉換成文字後再發給你。
```

### Task and Code Offloading
- Silently exit monitoring routines when there are no changes.
```text
請列出當前你名下的全部例行任務（Routines），註明每條任務的觸發頻率、每週預計執行次數以及沒有變化時的處理邏輯。
找出其中執行最頻繁、消耗最大的任務，向我提出降低頻率的具體建議；同時為所有監控類例程新增硬性約束：執行檢查後若目標無實質變動，立刻靜默退出，嚴禁向我發送「一切正常」或「沒有新訊息」等無有效資訊的通報。
```
- Dispatch tasks via 1-on-1 chats, and **strictly forbid Bots from creating group chats to talk among themselves**.
```text
嚴格執行獨立單聊工作模式：
只接收並執行我本人下達的直接指令。嚴禁在沒有得到我明確授權的情況下，主動在會話中喚醒、提及或聯絡其他 Bot 開展群聊協同；如果任務涉及多個專業環節，請將結果寫成文件並由我來負責跨 Bot 排程，或者將其派發給雲端電腦內的後台 CLI 工具獨立執行。
```
- Keep Bot focused on orchestration, while long code writing and debugging are **offloaded to the Grok Build background CLI**.
```text
明確你的角色定位是任務排程主管，核心職責是理解目標、拆解方案、組織邏輯和驗收結果。
不要在聊天視窗中直接編寫整段的長篇程式碼，也不要通讀整個大型倉庫做全量重構。涉及程式碼編寫、項目除錯和環境排查的工作，統一在後台呼叫雲端電腦內已經授權的 Grok Build 命令列工具執行。執行完畢後，你僅需檢查其退出狀態碼並將最終結論同步給我。
```

### Search, Risk Control, and Handoff
- Save X search results to disk, and only report concise bullet points in chat.
```text
在檢索 X 平台的推文、觀點或動態時，使用你自帶的免費搜尋能力。
搜尋到的批量推文原文，請直接寫入 /workspace/ 下的對應 markdown 文件中保存。在聊天框中向我彙報時，嚴格限制為 3 到 5 條提煉後的核心事實與推文對應連結，嚴禁把多條推文的大段原文搬運回聊天中。
```
- Automations and API calls must set retry caps, **forcing interruption for manual approval upon anomalies**.
```text
在執行自動化任務、網路請求或文件排查時，嚴格執行防死循環規則：
同一操作或相似介面呼叫的重試上限為 2 次。如果連續 2 次重試均未成功，或者對下一步執行動作存在疑問，立刻中斷自動化流程並向我發起提問，詳細說明遇到的錯誤原因，嚴禁自行無限重試或在後台空轉。
```
- Have the old Bot prepare a handoff card before Duplicate cloning, **strictly limited to within 10 lines**.
::: details Search, Risk Control, and Handoff
```text
當前會話歷史較長，需要進行交接重置。請為我梳理一份 10 行以內的結構化交接總結，嚴格包含以下五項內容：
1. 你的角色設定與核心職責；
2. 當前正在進行的任務目標；
3. 已經達成的關鍵結論與做過的核心決定；
4. 下一步必須立刻執行的動作；
5. 新會話需要優先讀取的關鍵文件絕對路徑。
輸出完畢後不要執行任何新任務，等待我啟動新會話。
```
:::
- Enter a free OpenRouter key in the secret box to directly offload lightweight tasks.
```text
請協助組態 OpenRouter 免費模型呼叫環境，嚴格遵循以下安全執行流程：
1. 在聊天框中調出系統的密鑰輸入彈窗向我收取 API Key，嚴禁讓我把密鑰明文發送在普通對話中；
2. 將獲取到的 Key 保存到 ~/.agents/secrets/openrouter.env 文件中，環境變數名指定為 OPENROUTER_API_KEY；
3. 對該密鑰文件執行 chmod 600 設定安全權限；
4. 執行全程嚴禁在終端標準輸出或聊天訊息中打印該 Key 的明文內容；
5. 使用 curl 呼叫一個以 :free 結尾的免費模型進行一次最小文本測試，確認呼叫成功且費用為 0，並將測試結果告訴我。
```

Prototype reference: [Grok Bot Quota Ultra-Long Battery Life Step-by-Step Beginner's Guide (Send Directly to Bot!)](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Common Pitfalls

- Clicking Test in Details > Routines runs the actual pipeline, **deducting real quota every time**.
- Quotas for Cursor and SuperGrok **do not stack**; only the one with the higher weekly allowance counts, leaving the other idle.
- grok.com and Grok Bot are billed independently; top-ups on the web version **cannot be deducted against usage and are non-refundable**.
- Pasting API keys or Webhooks into the chat box consumes tokens and poses security risks; **you must use the secure popup dialog to write environment variables**.
- Clicking "Update Computer" wipes Linux cron jobs while preserving `/workspace/`; **cron must be reinstalled after updating**.
- Duplicate discards conversations, learned memory, and attachments; **you must manually feed context to the new Bot**.
- Once Monthly Limit is triggered, it does not kill running processes; **long-running tasks will finish**, so infinite loops can still exceed limits.

## How to Verify Completion

1. Go to Settings > Usage & Billing and cursor.com/dashboard to check billing, confirm you see the percentage used and the reset countdown, and **turn off Additional Usage or set Monthly Limit to a safe low value**.
2. Have the Bot simulate file deletion or outbound network requests; it must pop up an **Ask first** approval card and suspend execution pending approval, never executing silently.
3. Check the current session and dispatch a multi-tweet X search: ensure no dozens-of-turns long conversation lingers in the sidebar, only 3 to 5 summary points are returned, long text is saved to `/workspace/`, and raw text does not flood the chat dialog.
4. Go to Details > Routines and click Test on a monitoring routine with no changes: verify that it silently exits after checking, without sending superfluous "no updates" chatter.
5. Have the Bot write code with multi-file dependencies: verify that it calls Grok Build or the cloud Agent in the background, **outputting only the final status and execution summary** without pasting screenfuls of code into the chat box.

## Further Reading

### Related Chapters

- [Chapter 2 Plans and Subscriptions: Choosing the Right Tier First](/part1/02-plans)
- [Chapter 8 Skills and Routines: Turning a Single Success into Daily Automation](/part1/08-skills-routines)
- [Chapter 20 Reliable Automation: Scheduling, Webhooks, and Event Triggers](/part3/20-automation)
- [Chapter 25 Frequently Asked Questions and Troubleshooting](/part4/25-faq)

### Official Documentation and Help Center
- [Cursor Official Guide: Plans and Billing](https://cursor.com/cn/help/grok-bot/plans)
- [Cursor Official Guide: Routines](https://cursor.com/cn/help/grok-bot/routines)

### Community Case Studies and Optimization Summaries
- [4.1 Quota & Cost: Quota-Saving Checklist](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)
- [Hangzhou Offline Meetup Playback: How I Made Grok Bot Quota Last Longer](https://jcng5q8n0f3z.feishu.cn/wiki/D04JwEvL7iss9UkDBvLcLuvyncf)
- [Saving Even More Grok Bot Quota: Extreme Optimization of Scheduled Tasks](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [Grok Bot Quota Ultra-Long Battery Life Step-by-Step Beginner's Guide (Send Directly to Bot!)](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)
- [How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi)

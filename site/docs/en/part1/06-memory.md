# Chapter 6 Memory: Making Your Bot Understand You Better the More You Use It

Bot memory is cross-session working context. Treating all chat history as memory makes it easy to mistake temporary workarounds for permanent rules, or even make flawed decisions based on stale data.

- Master the five container types and the fast/slow clock mechanism, distinguishing memory from skills.
- Establish promotion protocols for team collaboration, and **verify dynamic data against the source of truth in real time**.
- Build a backup pipeline with Git so that **everything can be fully restored even if the Cloud PC is reset**.


![Memory: Making Your Bot Understand You Better the More You Use It](/info/06-memory.png)

## 6.1 Official Memory Mechanism: What Does the Bot Actually Remember?

Bots remember preferences, facts, and summaries; see [Using Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

**Don't treat the Bot as a database**.
- Keep dynamic data in the source system, and verify with the source for major decisions.
- If something is misremembered or an assumption becomes obsolete, correct or delete it directly in the chat.
- **Rely on approval pop-ups and `Auto-review` for security and permissions**, never on memory.
- State long-term rules clearly upfront in the first prompt; single-task instructions apply only to the current turn.

Click the top name to modify configuration. Duplicating a Bot on iPhone:
- Inherits: Configuration, skills, Routine, and avatar
- Does not inherit: Conversations, memory, and attachments

If you might use it again later, it is recommended to **set it to "Hidden" in the sidebar**; deleting directly will erase records. Pitfall: All Bots share the same Cloud PC. Deleting a Bot does not clear its files or login state; residual files must be cleaned up manually in the file system.

## 6.2 Memory Layering: Five Container Types and Fast/Slow Clocks

![6.2 Memory Layering: Five Container Types and Fast/Slow Clocks](/info/06-memory-s2.png)

Data is divided into a shared layer and a dedicated layer; see "4.6 Virtual Machines, Memory, and Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

For the five-container model, see "Grok Bot Memory Engineering: How One Agent Learns With a Team | rari" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

```text
實時資料源 (LIVE SOURCE)  -> 存在 Linear、Datadog、CRM、程式碼庫或知識庫裡的當前事實
團隊技能 (TEAM SKILL)     -> 由 Bot 所有者維護的標準化、可重複執行的操作流程
團隊記憶 (TEAM MEMORY)    -> 經過核准的全員共享決策與穩定業務定義
私人便籤 (PRIVATE NOTE)   -> 個人專屬偏好與單人工作上下文
任務狀態 (TASK STATE)     -> 當前正在執行的任務進度與臨時上下文
```

**Containers cannot be mixed**. Logs are discarded as they run, workflows go into skills, habits are kept in private notes, and only P0 definitions enter team memory.

To prevent pollution, use **fast/slow clock routing**.
- Slow clock: Styles and definitions measured in months or years; written into memory.
- Fast clock: Balances change at any time; **always query the source before acting**.

Passwords and tokens must never enter memory; documents store only pointers. Check APIs for real-time status, and never grant permissions based on memory.

## 6.3 The Boundary Between Memory and Skills: Knowing What vs. How to Do It

![6.3 The Boundary Between Memory and Skills: Knowing What vs. How to Do It](/info/06-memory-s3.png)

| Memory (WAU down 40%) | Skills |
| :- | :- |
| Facts and preferences | Workflows and approvals |

For good workflows, **save instructions as skills**:
```text
將我們用於此任務的流程保存為名為“每週帳戶健康狀況”的技能。
包括源系統、風險定義、輸出格式，以及聯繫客戶始終需要批准這條規則。
```

Three steps for **screen demonstration**:
1. Open Computer View in the conversation
2. Select "Teach Task" and enter expected outcome
3. Screen demonstration

Limited to 10 minutes; does not record microphone or passwords. @mvanhorn reminds that exceeding 10 minutes tends to fail; split into short sequential stages. [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

Lauren Tan's **debugging priorities**: Eliminate root cause > Test verification > Specific rules > Modify memory. Team skills are published by Creator or Manager; private chats belong only to individuals.

[fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)

## 6.4 Team Memory Management: Write Protocols, Permission Isolation, and Conflict Prevention

When multiple people share a Bot, **one person teaching it wrong affects everyone**.

```text
觀察 (OBSERVE) -> 分類 (CLASSIFY) -> 核實 (VERIFY) -> 晉升 (PROMOTE) -> 重核 (RECHECK)
```

Follow five steps when writing to memory:
1. **Observe**: Capture corrections and new decisions.
2. **Classify**: Distinguish between personal preferences and shared rules.
3. **Verify**: Check against documentation or code; **verbal speculation is strictly prohibited from entering storage**.
4. **Promote**: Store into rules along with authoritative links once confirmed by the owner.
5. **Recheck**: Re-verify with the source before major operations or after expiration.

```yaml
claim: "對外發表 API 變更前必須完成安全評審"
scope: "team"
source: "https://intranet.example/docs/launch-checklist"
owner: "security-team"
status: "approved"
review_after: "2026-11-01"
```

After verifying the source and owner on the external card, issue the command to store it.

**Knowledge sharing does not equal permission sharing**:
- **Personal OAuth**: Calling plugins like Gmail uses one's own authorization; do not usurp permissions.
- **Service Keys**: Shared by all team members, **following the principle of least privilege and typically read-only**.
- **Slack Pitfalls**: Querying private data in a group channel exposes it to everyone. Post only summaries in public channels, and **keep sensitive data in private messages**.

**Conflict Resolution**: **Immediately suspend critical operations** -> Check authoritative source -> Owner decides -> Update source -> Correct memory.

**Troubleshooting Bad Memory** (e.g., treating special exceptions as routine):
1. Inspect: Ask the Bot to list memories to locate errors, tracing back to conversations and tasks.
2. Modify: Fix the source documentation first, then issue instructions to delete or modify the memory.
3. Verify: **Test with another member's account** to confirm it does not block, and rectify historical tickets.

## 6.5 Memory Backup and Recovery: Treating the Cloud PC as a Replaceable Container

![6.5 Memory Backup and Recovery: Treating the Cloud PC as a Replaceable Container](/info/06-memory-s5.png)

All Bots under the same account share `/workspace` (v0.68.1 resolution 1920×1200).

**The Cloud PC can be reset by official systems at any time** (it happened on 2026-10-10); installed packages and uncommitted states will all be cleared, and lost local data cannot be recovered. For background, see [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Backup Process and Credential Security

Create an operations Bot named "Memory Steward", and back up to a private Git repository in four steps:
1. Create a new Bot named "Memory Steward", specifying its responsibility as periodically exporting charters, rules, and memories for all Bots.
2. Connect a private Git repository in `/workspace`, setting up `bots-backup/charters/` (instructions), `bots-backup/memories/` (rules), and `environment/` (including scripts and `services-ledger.md`).
3. Configure a weekly scheduled Routine to save configurations and memories as Markdown.
4. **Have the Routine automatically run Git commands to commit and push to the remote private repository**.

::: details Backup Process and Credential Security
```text
/workspace/
└── bots-backup/
    ├── charters/          <- 各 Bot 的長期規則 (如 researcher.md, writer.md)
    ├── memories/          <- 團隊共用決策與業務定義 (如 definitions.md)
    └── environment/
        ├── services-ledger.md  <- 服務總帳，記錄工具依賴與啟動命令
        └── restore.sh          <- 虛擬機器一鍵重置恢復指令碼
```
:::

- **Strictly prohibit committing plaintext tokens to Git**. Automation scripts should only read local `~/.env` to retrieve secrets.
- When encountering logins, two-factor authentication, or CAPTCHA, manually take over the screen. Bots only inherit cookies and never touch plaintext passwords; see details in [Using Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

## 6.6 Ready-to-Use Practical Prompts

### Three-Tier Instruction Framework
When building a Bot, don't write vague introductions; **use a three-tier framework to clarify rules, responsibilities, and current focus**. See [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2) for details.

::: details Three-Tier Instruction Framework
```text
BASE INSTRUCTIONS (基礎規則，本帳號所有 Bot 通用)
- 涉及產生財務支出、向外部發送任何資訊、刪除文件等操作前，必須等待人工確認。
- 當結論涉及重要業務決策時，必須調取當前權威來源進行核對，嚴禁單憑記憶作答。
- 若執行受阻，用單行明確說明受阻點，禁止擅自尋找不可靠的繞行方案。
- 階段性工作交接結果統一寫入 /workspace/shared/handoffs/ 目錄。

ROLE (角色職責)
- 你的身份：每週帳戶健康狀況審計專員。
- 你負責的固定作業：獲取客戶產品用量與工單信號，標記流失或擴張跡象。
- 驗收標準：每項結論必須附帶源系統監控圖表或工單連結。
- 允許操作：讀取記錄、檢索系統指標、在共享目錄生成評估報告。
- 嚴禁操作：未經明確批准，絕不私自聯絡客戶，絕不修改帳戶權限。

CURRENT FOCUS (當前重點)
- 本週重點核查用量環比下降超過 30% 的企業級客戶名單。
```
:::

### Converting to Team Skills
Once a task runs successfully, directly **issue a command to crystallize it into a skill**.

::: details Converting to Team Skills
```text
請將本次執行的工作流整理並保存為團隊技能，名稱設為“客戶流失風險排查”。
要求包含以下內容：
1. 觸發場景與必需的前置憑據。
2. 調取指標資料的具體步驟與判定閾值。
3. 輸出結果的格式規範（必須包含資料源連結）。
4. 明確安全紅線：向客戶發送郵件或調整帳戶組態必須經由人工批准。
完成後在對話中回覆技能概要。
```
:::

### Writing to Shared Memory
For rules approved by owners, **write them in with source and owner included**.

```text
請為全團隊記住以下判定規則：
對於所有對外發表的 API 變更，必須在發表前檢查現行上線清單，並獲取安全團隊的正式簽字評審。
若上線流程發生變更，以上線清單源文件為準，記憶僅作為指引。
來源文件：https://intranet.example/docs/api-checklist
責任人：security-team
複核日期：2026-11-01
```

### Deploying Memory Steward
In the "Memory Steward" Bot, **issue a command to configure an automated backup Routine**.

```text
你是本帳號的記憶管家。你的職責是定期歸檔全帳號所有 Bot 的章程與共享記憶。
請組態一個每週執行的例行任務（Routine）：
1. 提取所有 Bot 當前的 Description/Instructions 規則，在 /workspace/bots-backup/charters/ 下按 Bot 名稱分別保存為 .md 文件。
2. 提取當前所有已保存的團隊共用記憶，整合保存為 /workspace/bots-backup/memories/team-memory.md。
3. 檢查文件是否有更新。若有變更，自動執行 git add .、提交併推送至已組態好的私有 Git 倉庫。
4. 若 Git 推送失敗，在當前對話中告警並說明報錯資訊；若無變更則保持靜默，不要頻繁推送無意義通知。
```

### Cleaning Up Bad Memory
If you find that erroneous or outdated rules are being referenced, **issue commands directly to correct and clean them up**.

```text
請檢查並列出你當前記錄的所有團隊記憶中涉及“企業客戶續約審批”的條目。
刪除其中“所有企業客戶續約必須經由 VP 逐筆批准”的內容。
該規則僅為上週特定情況下的臨時特例，不是長期標準。
從現在起，企業客戶續約標準重新以財務知識庫的正式文件為準：https://intranet.example/finance/renewals
確認修改後，請向我展示修正後的相關記憶列表。
```

## 6.7 Classic Case Studies

### Case 1: SpaceXAI Data Analysis Bot

The SpaceXAI team needed to query a massive data warehouse containing 45,000 tables.
- **Don't cram massive data into memory**. They configured read-only warehouse credentials for the Bot and crystallized table discovery and queries into a skill library.
- Memory retains only metric definitions and correction rules; dynamic data relies on real-time retrieval and computation.

See details in [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

### Case 2: Multi-Bot Collaborative Tweet Profiling Pipeline

0xlangeai built a pipeline with four Bots—curator, analyst, designer, and engineer—to run tweet profiling.
- Different Bots cannot read each other's chat history.
- **Cross-Bot collaboration relies on passing deliverables via the file system**. The curator generates `tweets.md`, the analyst reads it to produce `profile.md`, the designer uses that to create `design.md`, and the engineer pulls the code to build and deploy.

See details in [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Case 3: Jon ONeill's Plumbing Dispatch System

Jon ONeill automated work order scheduling across Gmail, Slack, ServiceTitan, and customer portals.
- Having a single all-in-one dispatch Bot handle all rules led to confusion and errors, and ultimately had to be discontinued.
- Tasks were divided among dedicated Bots: Gary monitors Gmail, Steve checks ServiceTitan schedules, Quinn sends SMS messages, Sarah coordinates with employees on Slack, and Atlas oversees everything.
- **After breaking down responsibilities, it steadily handles 5 to 6 urgent work orders every day, completing the entire scheduling process within 10 minutes**.

See details in [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

## 6.8 Common Pitfalls

- **Query dynamic data in real time**: Don't store inventory in memory, preventing the Bot from making misjudgments based on stale data.
- **Always script configurations**: Manual configurations on Cloud PCs are completely wiped upon reset.
- **Don't apply private chat instructions team-wide**: Directly sharing special exceptions will pollute team behavior.
- **Separate Bots cannot achieve isolation**: Bots under the same account share files; rely on permissions and Ask-first approvals.
- **Never send passwords in the chat box**: To prevent log leakage, use secure credentials or manual takeover.
- **Don't query private data in Slack**: Asking questions in public channels easily exposes private data for all to see.

## 6.9 How to Verify Upon Completion

To test memory boundaries, directly run the M01-M05 test cases designed by community author rari (@0xwhrrari).
```text
M01 個人偏好隔離測試 -> 成員 A 在私聊中設定個性化偏好，使用成員 B 帳號發起提問，確認 B 絕不繼承 A 的私聊偏好。
M02 團隊規則晉升測試 -> 成員 A 提交一條經審批的團隊規則並寫入團隊記憶，成員 B 發起任務時應生效該規則，但看不到 A 當時的私聊對話。
M03 狀態時效回源測試 -> 在團隊記憶中保留一條舊狀態，在源系統修改為新狀態。向 Bot 提問，Bot 必須調取最新源資料，而不是採信記憶中的舊狀態。
M04 衝突自動阻斷測試 -> 兩個成員分別向 Bot 給出互相矛盾的業務說法。Bot 應識別出衝突並主動停止高風險操作，指出需要責任人裁決，而不是悄悄採納最後一條說法。
M05 共享渠道邊界測試 -> 在 Slack 共享頻道執行緒中，要求 Bot 呼叫某成員的個人連線器。Bot 必須正確發起審批，且回覆內容只包含團隊可見的脫敏結論。
```
Here, you **must cross-test using two different real team accounts**; a single account cannot test isolation boundaries.

1. Log in to the private GitHub or GitLab repository to confirm that rule files for each Bot under `bots-backup/charters/` have been committed, and no rules or permissions have been lost.
2. Check `bots-backup/memories/team-memory.md` to confirm that team decision rules and source system links are intact.
3. Run the environment recovery script in the Cloud PC test directory to **confirm that dependencies and directories have no errors, and the one-line script can bring up services directly**.
::: details 6.9 How to Verify Upon Completion
```bash
   bash /workspace/bots-backup/environment/restore.sh
   ```

## Further Reading

- Official Documentation: [Using Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Community Article: rari "Grok Bot Memory Engineering: How One Agent Learns With a Team" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)
- Community Article: "4.6 Virtual Machines, Memory, and Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- Community Article: Matt Van Horn "Every Grok Bot Hack I Know (Aug 2026)" [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

:::

# Chapter 21 Backup and Recovery: No Panic When Your Computer Resets

When the cloud computer is reset, the environment is wiped clean immediately. Relying on memory to run `apt-get` and `pip install` makes it easy to miss dependencies or environment variables, and tuned Bot memories lack an export button. **The solution is to split disaster recovery into two parallel pipelines.**

1. **VM Services**: Take over system dependencies using a registry ledger and automated recovery scripts.
2. **Agent Memory**: A dedicated memory steward writes configurations and dynamic facts into Markdown and pushes them to a private Git repository.

Once established, **even if the system is reset or migrated, all services and memories can be restored with minimal manual intervention**.


![Backup and Recovery: No Panic When Your Computer Resets](/info/21-backup.png)

## 21.1 Understand the Cloud Computer's Inner Workings: Differences Between Update, Recover, and Reset

![21.1 Understand the Cloud Computer's Inner Workings: Differences Between Update, Recover, and Reset](/info/21-backup-s1.png)

**All Bots under the same account share the same virtual machine**, sharing the `/workspace` directory and system processes. When global tools are installed on a machine, other Bots can call them; once the machine is reset, all dependency environments will fail at the same time.

Reference: [4.6 Virtual Machines, Memory, and Backup](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

The client provides controls under **Settings** > **Computer** under **Bot's Computer**. The differences among the three are as follows:

| Action | Mechanism | Preserved Content | Lost Content |
| :--- | :--- | :--- | :--- |
| **Update** | Upgrades the environment image. Divided into software updates and computer updates | Software updates preserve everything; computer updates preserve bots, files, and login information | No loss with software updates; computer updates remove global applications and packages |
| **Recover** | Creates a new machine on the latest image based on saved data, attempting to connect to the old machine first to save data | Saved bots, files, and login information | Global applications and packages; if the old machine cannot be reached, unsynced changes will be lost |
| **Reset** | Directly creates a new machine based on the most recently saved data, interrupting running work | Saved bots, files, and login information | Global applications and packages; unsynced changes will be lost |

Conversation histories are stored in the cloud, unaffected by machine resets or accidental file deletions. However, **globally installed application packages, `node_modules`, and Python virtual environments are not officially saved**, and will be wiped upon computer updates, Recover, or Reset.

For details, see [Grok Bot Computer](https://cursor.com/cn/help/grok-bot/computer-recovery).

When the virtual machine freezes or responds abnormally, troubleshoot in this order:

1. Displays **Reconnecting** or **Couldn't Reach Grok Bot's Computer**: This is caused by network fluctuations. Wait a moment and click **Retry**. Files are not lost during reconnection; **never click Reset during this stage**.
2. Restart the client. Mac users must select **Quit** from the top menu bar; simply clicking the red close button on the window does not work.
3. Check for updates. Go to **Settings** > **Computer**, and if an update is available, click **Update** first. If prompted that the agent is not paused, wait until the current task finishes before clicking.
4. Try recovering. If it still cannot connect or the update is stuck and shows **Recover Computer**, click **Recover**. If it says **Update is still running**, select **Keep waiting**.
5. Perform a **Reset**. Only click Reset if the first four steps do not work. If it fails, retry with **Retry Recover** or **Retry Reset**; if errors persist, contact official support.
6. Handle disk alerts.

   When receiving **Computer is low on disk space** or **Computer is critically low on disk space**, do not manually delete files. Click **Go to Disk Saver** in the sidebar to view options; the system will not delete files without confirmation.

   For details, see [Grok Bot Computer](https://cursor.com/cn/help/grok-bot/computer-recovery).

**The cloud computer is merely a disposable container**; do not manually fine-tune the environment. Script the entire setup process, and make sure configurations and custom source code are stored in an external private Git repository.

## 21.2 VM Service Ledger and Automated Recovery Pipeline

![21.2 VM Service Ledger and Automated Recovery Pipeline](/info/21-backup-s2.png)

[4.6 Virtual Machines, Memory, and Backup](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

Cloud computers do not provide underlying snapshots, so **turning the rebuilding process into a one-click script has the lowest cost**.

### Service Ledger and Anti-Pollution Backup

Create a `vm-services/` directory in a private repository to store the human-readable `REGISTRY.md` table and the `registry.json` parsed by automated scripts.

The ledger and backup must adhere to several strict rules.
- Registered fields include Service ID, responsible Bot, code path, installation dependencies (apt/pip/Docker/cron), start/stop and health check commands, and whether recovery is mandatory.
- **Credential paths should only use local absolute paths (such as `~/.env`); storing plaintext is strictly forbidden**; manually required steps such as QR scanning and OAuth should be highlighted separately.
- Custom scripts should be stored separately in `service-src/`, excluding `venv/`, `node_modules/`, and logs; **a regex scan for secrets must be run before committing**.

### Automated Recovery Pipeline

Write separate sub-scripts for each service in `vm-services/restore/`. **Scripts must guarantee idempotency**; running them twice in a row must not report directory already exists or port conflict errors.

The main entry point `restore-all.sh` executes sequentially based on dependency order.
1. **Base Dependencies**: Install system tools such as `cron`, `ffmpeg`, and `yt-dlp`.
2. **Source Code in Place**: Copy custom scripts back from `service-src/`, skipping existing files and only filling in missing ones.
3. **Environment and Packages**: Create a Python virtual environment and run `pip install -r requirements.txt`.
4. **Launch Daemons**: Start background daemon processes.
5. **Mount Scheduled Tasks**: Restore unified crontab scheduling.
6. **Health Checks**: Check survival item by item; **if an item fails, log the error and proceed to the next item** without blocking or interrupting.

[Tools Gone After Grok Bot VM Reset? Backup & Recovery Tutorial (with Prompts)](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.3 Memory Steward: Packing Bot Core Memories into a Private Repository

![21.3 Memory Steward: Packing Bot Core Memories into a Private Repository](/info/21-backup-s3.png)

The official platform does not provide a full memory export button, making preferences very easy to lose during account changes or system migrations. **Setting up a dedicated "Memory Steward" Bot to turn intangible memories into plaintext snapshots in a private Git repository is the most reliable approach.**

[Grok Bot Million Evacuation: A Complete Agent System Backup Plan](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Memory Layering and Maintenance Principles

| Layer | Included Content | Description & Permissions |
|---|---|---|
| **Shared Layer** | Account-shared memory, public Skill and plugin configurations | Readable by all Bots |
| **Exclusive Layer** | Description rule contracts, exclusive independent memory, and Routine tasks | Exclusive to a single Bot |

- Do not pile dynamic facts in context long-term; only record the access method and fetch from the source when needed.
- Shared memory must undergo manual review or standardized workflow verification to prevent cross-contamination.
- **Write business definitions into memory, and fixated operational workflows must be solidified into Skill code.**

[4.6 Virtual Machines, Memory, and Backup](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Archival Specification and Workflow

::: details Archival Specification and Workflow
```text
├── bots/                     # 各 Bot 獨立組態與記憶
│   ├── cyber-xiaowan/        # 單個 Bot 資料夾
│   │   ├── agent-spec.md     # 身份設定、名稱、bot-id、slug、description
│   │   ├── MEMORY.md         # 核心記憶全量快照
│   │   ├── profile.md        # 角色資訊與權限邊界
│   │   └── archive/          # 歷史版本與過往記錄
│   └── ...                   # 其他 Bot 目錄
├── meta/                     # 全域Metadata與多 Bot 拓撲關係
├── shared-user-memory/       # 帳號級共享記憶
├── vm-services/              # 虛擬機器服務總帳與恢復指令碼（見 21.2 節）
├── README.md                 # 倉庫使用說明與最新狀態
├── RESTORE.md                # 跨環境恢復操作 SOP
└── registry.md               # 登記索引
```
:::

The `MEMORY.md` under each Bot's directory contains three layers: identity & permissions, decision-making responsibilities, and on-site snapshots.

1. **Enumerate List**: Identify core Bots requiring persistent backup.
2. **Dispatch Instructions**: Each Bot reads its own configuration and memory, extracts them, and writes them to the corresponding Markdown file in `/workspace`.
3. **Fetch, Verify, and Store**: **Commit collectively after scanning to confirm no plaintext Tokens**, tag with a date (e.g., `tag-2026-10-15`), and push to the remote private repository.

**Bots handle full snapshots, while Git handles incremental tracking**. Bots directly overwrite files in full each time, leaving historical changes to be tracked by the Git engine without needing to calculate diffs in the prompts.

## 21.4 Practical Case: 鐵柱AGI's Million Evacuation and Service Steward

### Memory Steward Backup

鐵柱 (@cgnot996) maintains 21 Bots. To prevent losing memories due to account bans, he set up a "Memory Steward" Bot and paired it with a private Gitee repository for archiving.

1. **Identify the Core**: Pick 7 core Bots out of 21 for a trial run.
2. **Export and Verify**: Notify the 7 Bots to export settings and memories. **Some Bots remain silent after exporting; instructions must require "report upon completion," while the steward scans the `/workspace` directory to verify**.
3. **Commit and Tag**: The first batch of 73KB was archived and stored, tagged with `tag 2026-09-10`, and passed secret scanning.
4. **Single-Profile Structure**: Like "Cyber Xiaowan", `MEMORY.md` (approx. 21KB) stores identity and snapshots, while `agent-spec.md` stores the bot-id and description.
5. **Enable Scheduling**: Set to archive automatically on a regular schedule.

When importing to a new account, memory recovery fidelity is around 80%. **Unbacked-up local files, conversation histories, and third-party login states cannot be restored**.

When migrating to Hermes or OpenClaw, place `MEMORY.md` into the memory directory and change the description in `agent-spec.md` to the system prompt to get it running.

[Grok Bot Million Evacuation: A Complete Agent System Backup Plan](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Virtual Machine Service Steward

Cloud computer crashes and resets cause all tools to be lost. The author records the rebuilding ledger in the `vm-services` directory of the Gitee `grok-bot-memory` repository.

1. **Record in Ledger**: As of 2026-10-10, 20 items across 10 Bots were registered (4 daemons, 14 on-demand tools, and 2 secret items), with 18 items marked as "mandatory recovery".
2. **Categorize Services**: Daemons include scraping services, Muse API wrappers, email engines, and egress tunnels; on-demand tools (ffmpeg, Chrome, etc.) only record installation commands; Metaso and TikHub only record credential paths.
3. **Clean Source Code Backup**: Custom source code is about 5.1MB, excluding secrets, logs, and state runtime streams.
4. **Chained Recovery**: The steward maintains the `restore/` directory and `restore-all.sh`. **The steward does not execute autonomously during normal times; it waits for manual instructions to spin up services in dependency order and delivers an acceptance checklist**.

[Tools Gone After Grok Bot VM Reset? Backup & Recovery Tutorial (with Prompts)](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.5 Credential Security and Manual Approval Gates: Hand Over the Screen, Not the Password

**Multiple Bots share the virtual machine's disk and browser sessions; creating a new Bot cannot isolate sensitive data at all.** Once plaintext is written in scripts or chat, other Bots or external logs can read it.

[4.6 Virtual Machines, Memory, and Backup](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Keep Only Paths for Credentials, Never Plaintext

- Tokens and private keys should be stored in `~/.env` (which is excluded from Git) or a global secrets directory.
- In `REGISTRY.md`, `registry.json`, and memory files, **whenever credentials are involved, record only absolute disk paths**.
- Never send passwords in the chat box, and run a regex desensitization scan before pushing.

### Hand Over the Screen, Not the Password

1. When the Bot encounters 2FA, QR code scanning, or device verification popups, it immediately pauses and notifies you to take over.
2. You open the cloud computer in full screen in the client and enter the password or scan the QR code yourself.
3. Once completed, hand control back; **the Bot inherits the session Cookie and continues running without ever touching the plaintext password**.

### Set Ask-First for High-Risk Operations

- Irreversible operations such as posting, payments, deleting data, or modifying the underlying environment must prompt a popup to await manual approval. v0.70.2 optimized this type of confirmation logic.
- **Bot autonomous permissions are restricted to reading, public searching, and reading/writing within `/workspace`**; when rules conflict, Ask-first takes precedence.

## 21.6 Three Ready-to-Use Prompt Templates

Below are three battle-tested prompt templates that you can directly copy and send to corresponding Bots for deployment and use.

### Prompt 1: Configure "VM Service Steward" for Cloud Computer

Create a "VM Service Steward" Bot and **paste into settings**:

::: details Prompt 1: Configure "VM Service Steward" for Cloud Computer
```text
你是「虛擬機器服務管家」，只管一件事：記下這台虛擬機器上部署過的所有第三方服務，並在電腦更新或換帳號之後，按記錄把它們原樣恢復。

你維護的東西
1. 一份登記總帳，人和機器各讀一份：REGISTRY.md（表格）和 registry.json（給指令碼讀）。
2. 每個服務一個恢復指令碼 restore/restore-<服務>.sh，必須冪等，重複跑也不會出錯。
3. 一個總入口 restore/restore-all.sh，按依賴順序呼叫各個恢復指令碼，最後彙總哪些失敗了。
4. 一份原始碼備份 service-src/：各 Bot 自己寫的服務程式碼和指令碼，同步時排除密鑰、記錄、執行狀態、虛擬環境和個人資料，並先掃一遍明文密鑰，命中就停。
5. 以上全部跟著一個私有 Git 倉庫存（「你的備份倉庫地址」）。總帳、恢復指令碼、原始碼都在倉庫裡，密鑰永遠不進倉庫。

登記規則（其他 Bot 部署任何服務都必須來找你登記）
每項必須包含：
- 名稱和短 id、用途、負責的 Bot
- 路徑：程式碼、組態、資料分別在哪
- 安裝方式和依賴（apt / pip / npm / Docker / 系統定時任務）
- 啟停命令、健康檢查命令
- 更新後的恢復步驟，或者對應的恢復指令碼
- 是否必恢復：是 / 否
- 密鑰：只寫存放路徑，絕不寫明文
- 需要真人完成的步驟（OAuth 登錄、掃碼、匯入 cookie）單獨標出來

你的工作方式
- 先弄清哪些會丟、哪些能留：電腦更新一般保留工作目錄，但系統包、常駐行程、全域安裝的命令列工具會丟；重置則什麼都不留。所以要記的是“怎麼重建”，不是去拷整台機器。
- 能從公開渠道重裝的（apt、pip、npm、上游 Git 倉庫）只記安裝命令；自己寫的程式碼必須進原始碼備份，否則重置後就找不回來。
- 收到登記先核對：路徑是否真實存在、健康檢查能不能過。登記寫的和實際不一樣時，以實際為準，並告訴負責的 Bot。
- 多個定時任務合併成一份 crontab 真源時，檢查每一條是不是都在真源裡，不在的要靠恢復指令碼補回去。
- 故意停掉的服務要寫清楚“為什麼停、什麼條件下重開”，免得被當成漏裝。
- 只有主人說“電腦更新完了”才跑總恢復，不盲跑。跑完交驗收：每項是成功、失敗，還是要真人處理。
- 每次有服務新增、刪除或原始碼大改，先重新同步原始碼備份，再把總帳、指令碼、原始碼一起提交推送到備份倉庫。換帳號或重置時，就靠這份備份把整套設定帶走。
- 刪掉的服務要徹底清除：總帳只反映現在真實的狀態。
```
:::

### Prompt 2: Have Bot Execute Full Recovery After Computer Reset

Configure the **Git access token**, replace the bracketed content, and send it to the Bot.

::: details Prompt 2: Have Bot Execute Full Recovery After Computer Reset
```text
這台電腦剛重置過（或者是換了新帳號），之前部署的服務都沒了。請按我的備份把它們恢復到可用狀態，規則如下。

備份在哪
- 備份倉庫：<你的備份倉庫地址>，分支 <分支名>
- 倉庫裡有：登記總帳（REGISTRY.md 和 registry.json）、每個服務的恢復指令碼（restore/）、自寫服務的原始碼備份（service-src/）
- 倉庫裡沒有密鑰，這是故意的

請按這個順序做
1. 把備份倉庫拉到工作目錄，先讀總帳，告訴我一共登記了幾項、哪些標了「必恢復」、哪些只留密鑰不用恢復。先列出來，不要動手。
2. 把自寫服務的原始碼從 service-src/ 放回總帳寫的原位置。只補缺失的，已經存在的目錄不要覆蓋。
3. 按總帳的依賴順序逐項恢復：先裝系統依賴（比如 cron、ffmpeg），再裝命令列工具，最後拉起常駐服務和定時任務。每項都用它自己的恢復指令碼，指令碼要能重複跑。
4. 每裝完一項就跑它登記的健康檢查。失敗了先看記錄、試著修一次；修不好就記下原因，接著做下一項，不要卡住。
5. 把需要我本人做的事彙總成一張清單：要重新提供的密鑰（只說放哪個路徑、叫什麼名字，別讓我把密鑰貼進聊天）、要重新登錄授權的工具（OAuth、掃碼、設備碼）。然後一項一項帶我做，每做完一項馬上覆查。
6. 故意暫停的任務保持暫停，總帳裡寫了原因和重開條件的照辦。別因為“看起來漏裝了”就自作主張打開。
7. 最後交驗收清單，每項一行：服務名、結果（成功 / 失敗 / 等我處理）、健康檢查輸出摘要、花了多久。再告訴我總共用了多少時間、成功了幾項。

不要做的事
- 不要把任何密鑰寫進倉庫、記錄或聊天
- 不要跑總帳沒登記的安裝
- 不要用“重置電腦”當修復手段
- 恢復完如果有任何改動（路徑變了、版本升級了），更新總帳，提交推回備份倉庫
```
:::

### Prompt 3: Memory Steward Periodic Archival Instructions

**Send this for Routine or manual archiving:**

::: details Prompt 3: Memory Steward Periodic Archival Instructions
```text
請開始執行本週的智慧體記憶與設定歸檔任務。

執行步驟：
1. 枚舉當前工作區內所有處於活躍狀態的 Bot 名單，核對 bots/ 目錄下的已有目錄。
2. 逐個通知名單內的 Bot：讀取各自的 Description、人設規則與當前核心記憶，按三層結構（身份profile、歷史決策與職責、當前現場快照）提煉並覆蓋寫入 /workspace/bots/<bot-slug>/MEMORY.md。同時將身份Metadata更新至 agent-spec.md。
3. 檢查各 Bot 回執，並在 /workspace 目錄核對文件生成情況，確保所有目標 Bot 的 Markdown 均已寫出。
4. 提取帳號級共享記憶，更新至 shared-user-memory/ 目錄下的 Markdown 文件中。
5. 對本次生成的所有 Markdown 文件進行敏感資訊正則掃描，檢查是否存在明文 API Token、密碼或私鑰。如果發現疑似憑證，立即中斷並報警。
6. 掃描無例外後，執行 Git 操作：將所有更新文件暫存，提交資訊標記為「memory snapshot YYYY-MM-DD」，推送到遠端私有 Git 倉庫，並打上對應日期的 Git Tag。
7. 完成後向我彙報：本次歸檔了哪幾個 Bot、總文件大小、是否有失敗或超時的 Bot。
```
:::

## 21.7 Common Pitfalls

1. **Do not click Reset** when Reconnecting is displayed; it is only a network fluctuation or maintenance. Clicking it will overwrite unsaved data with an old snapshot.
2. Sharing Codex authorization across multiple devices will kick each other offline; configure independent sub-accounts or dedicated credentials.
3. Scheduled tasks must be unified into a crontab configuration file and committed to Git to prevent omissions upon machine resets.
4. The service ledger must be based on actual executable commands; missing Docker in the environment will cause recovery scripts to hang.
5. Bots often export silently; the steward must actively inspect the disk, and instructions must strictly require "must report upon completion".
6. **Backup repositories must be set to private with regex scanning added** to prevent Tokens from being pushed into public repositories via Git push.

## 21.8 How to Verify After Completion

### Services and Scripts
1. Reconciliation: Check against `vm-services/REGISTRY.md`, inspect processes using `ps aux`, and inspect ports using `netstat` or `ss`; **paths must not be over-recorded or omitted**.
2. Dry Run: Run `restore-<service-name>.sh` individually to see if it can execute repeatedly without errors.
3. Full Drill: Clone into a temporary directory and run `bash restore/restore-all.sh`, **ensuring all "mandatory recovery" items pass**, and steps requiring manual intervention are listed.

### Repository and Memory
1. Check Structure: Inspect `bots/` on the web interface; each Bot must have independent `agent-spec.md` and `MEMORY.md`.
2. Spot Check: Open `MEMORY.md` to confirm the three layers—"identity profile", "historical decisions & responsibilities", and "current on-site snapshot"—are complete, without empty templates or garbled text.
3. Secret Search: Globally search for `sk-`, `Bearer`, or `password`; **credentials must only keep local absolute paths, and plaintext Tokens are strictly forbidden**.

## Extended Reading

- Official Guides and Support Pages:
  - [Grok Bot Computer](https://cursor.com/cn/help/grok-bot/computer-recovery)
  - [Securely Storing Secrets](https://cursor.com/cn/help/grok-bot/secrets)
  - [Getting Help](https://cursor.com/cn/help/grok-bot/get-help)
  - [Grok Bot User Guide](https://cursor.com/cn/help/grok-bot/how-to)
- Community Practical Reference Articles:
  - 鐵柱AGI @cgnot996: [Tools Gone After Grok Bot VM Reset? Backup & Recovery Tutorial (with Prompts)](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)
  - 鐵柱AGI @cgnot996: [Grok Bot Million Evacuation: A Complete Agent System Backup Plan](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)
  - Knowledge Base Synthesis: [4.6 Virtual Machines, Memory, and Backup](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

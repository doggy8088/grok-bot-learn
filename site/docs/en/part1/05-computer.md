# Chapter 5 Shared Cloud Computer: Files, Browser, and Takeover

Users new to Grok Bot often have several common misconceptions. These misconceptions often lead to obstacles in subsequent development and maintenance:

- Mistakenly believing that creating a new Bot adds an independent virtual machine.
- Mistakenly believing that when multiple Bots work together, they can directly read each other's chat histories.
- Pasting account credentials or even API Tokens directly into the chat window when third-party tool logins are required.

Only when the cloud computer is abruptly wiped due to system maintenance or underlying updates, wiping out installed environments and scripts, do people realize they know nothing about how this cloud computer works under the hood.

All Bots under the same account work on the same cloud computer, sharing the same disk and filesystem. They cannot see each other's conversation logs; collaboration relies entirely on transferring files via disk.

When encountering login verifications, the proper approach is to take over the screen directly in the cloud browser to enter credentials, rather than handing passwords to the model. At the same time, this cloud computer is essentially an ephemeral container that can be rebuilt at any time; manually installed packages will be lost during platform updates or administrator maintenance.

This chapter walks you through how this cloud computer really works. You will learn how to safely hand off files and screens between multiple Bots, how to route network traffic through your local desktop to handle whitelist restrictions, and how to use a lightweight, standardized backup pipeline to systematically and quickly restore the entire environment after a reset.


![Shared Cloud Computer: Files, Browser, and Takeover](/info/05-computer.png)

## Underlying Mechanism of the Shared Computer: One Machine and Multiple Bots

**All Bots under your account share the same hosted Linux computer.** No matter which Bot you switch to, you are facing the exact same `/workspace` root directory and persistent disk.

Chat records are saved independently off-machine; even if you run `rm -rf` to wipe everything inside the machine or if the system crashes and restarts, conversations and lists remain intact.

**Creating a new Bot does not mean security isolation.** Any Bot with command-line privileges can read and write all data in `/workspace`; never store unencrypted sensitive information inside.

Version evolution:
- v0.68.0: Added support for removing other computers in settings
- v0.68.1 (Released 2026-10-07): Screen resolution upgraded from 1280×800 to 1920×1200, with faster action and screenshot responsiveness
- v0.70.2: Added dedicated email address; supported saving web pages directly as PDFs

For underlying details, see [4.6 Virtual Machines, Memory, and Backup](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

## Multi-Bot Screen and Work Status Monitoring

### Status and Configuration

**Three status types reside permanently in the sidebar.**
- Needs Attention: Waiting for answers, approvals, or handoffs.
- Unread Activity: Tasks completed, waiting for review.
- Working: Currently running scripts, scraping web pages, or invoking tools.

Click the name at the top to access "View Conversation Details", where you can edit the current Bot's name, tags, and avatar. Personal Bots have no separate description box; **simply send a message** to adjust its persona.

### Monitoring and Notifications

Cloud operations support **real-time screen viewing**.

**Notifications are automatically suppressed when in focus**, marking items as unread only in the sidebar and Dock; when offline, notifications can be enabled in configuration files to push alerts to desktop or mobile.

## Browser Takeover: Hand Over the Screen, Not Passwords

![Browser Takeover: Hand Over the Screen, Not Passwords](/info/05-computer-s3.png)

Do not send credentials into the chat box. You and the Bot share a browser: **hand over the screen, not passwords**.

### Takeover Steps

1. Trigger Pause: The Bot opens a login page and pauses when encountering credential inputs, QR code scanning, or 2FA.
2. Take Over Input: Click full-screen to take over the keyboard and mouse.
3. Manual Login: Enter credentials or scan QR code to verify yourself.
4. Hand Over Execution: **Notify the Bot to resume using the session cookies after login**, preventing exposure of plaintext passwords.

### Approval Gates

Press `Cmd+,` to configure under "General" - "Bot".

- **Rule conflicts default to "Ask first"**.
- Enterprise rules displaying `Required by your admin. You can't edit or delete this rule.` cannot be modified.
- v0.70.2 reinforced confirmations before sending emails/posts, processing payments, and modifying production environments.

See [Settings and Notifications](https://cursor.com/cn/docs/grok-bot/settings) for details.

## Multi-Bot File Handoff Conventions and Directory Planning

### File Collaboration Patterns

Bots cannot read each other's chat histories; **the only channel for multi-Bot collaboration is shared disk files**.

Prompts only need to pass the file path of the previous stage; see [4.6 Virtual Machines, Memory, and Backup](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg) for details.

1. Curator scrapes and generates `tweets.md`
2. Analyst refines and outputs `profile.md`
3. Designer creates `design.md` based on profile
4. Engineer reads design and builds code

### Directory Planning

Establish directory conventions right after provisioning the machine to avoid clutter across multiple Bots.

| Directory Path | Contents | Writing Standards |
| --- | --- | --- |
| `/workspace/handoff/` | Intermediate artifacts | Unified Markdown or JSON, prefixed with task identifiers |
| `/workspace/projects/` | Project code and assets | Organized into independent subdirectories per project, linked to Git repos |
| `/workspace/tools/` | Custom local scripts | Keep only secret-free source code, synced to backup repo after inspection |
| `~/.env` or local files | API keys | Stored locally only; **strictly prohibited from committing to repos or printing in chats** |

### Disk Cleanup and Disk Saver

When the system warns `Computer is low on disk space` or `Computer is critically low on disk space`, go to the sidebar and click "Go to Disk Saver" under **Disk Saver** to review cleanup recommendations.

**It never deletes files without confirmation**; if you reject cleaning up, existing files remain untouched.

## Local Network Egress: Routing and Accessing Private Networks

![Local Network Egress: Routing and Accessing Private Networks](/info/05-computer-s5.png)

To resolve WeChat official account access, corporate intranet IP whitelisting, or LAN access, **simply relay traffic through your local device**.

### Setup Steps
1. Press `Cmd+,` to enter Settings and click **Computers**.
2. Locate the current computer under **Your Computers** and enable **Route traffic through this computer**.

### Limitations and Pitfalls
- Limited to a single computer at a time. Outbound traffic is identified as your local IP, and the Bot can also directly access your LAN.
- **Applies only to new requests**; existing long-lived TCP connections will continue along their original routes.
- If an administrator disables `Allow Local Egress Routing`, the toggle is grayed out with `Disabled by your admin. You can't turn this on.`, and connections are forcefully terminated within 5 minutes; see [Settings and Notifications](https://cursor.com/cn/docs/grok-bot/settings).
- `Execution on this computer` controls the local shell and requires confirmation step-by-step by default; **do not enable fully automatic mode carelessly**.

## Rebuild, Update, and Terminate: The Cloud Computer Lifecycle

![Rebuild, Update, and Terminate: The Cloud Computer Lifecycle](/info/05-computer-s6.png)

Rebuilding **clears manually installed environments**, while preserving disk data and login states.

See [Grok Bot Computers](https://cursor.com/cn/help/grok-bot/computer-recovery) and [Manage Grok Bot Computers](https://cursor.com/cn/docs/grok-bot/computers).

| Operation | Preserved | Cleared / Pitfalls |
| - | - | - |
| Software Update | Everything | None |
| Update / Rebuild | Disks and files | Clears manually installed environments; must re-run scripts |
| Terminate VMs | Disk | Shuts down after 30 days of inactivity, losing unsaved progress |
| Recover / Reset | Saved data | Interrupts tasks, loses unsaved code |

When `Reconnecting` is displayed, **do not blindly click Reset**; troubleshoot in this order:

1. **Click Retry**. Disk remains intact during reconnection; rash actions disrupt the troubleshooting state.
2. **Fully Quit**. On macOS, use `Cmd+Q` to quit and restart rather than just closing the window.
3. **Check for Updates**. Go to "Settings" > "Computers"; update only when the Bot is idle.
4. **Prioritize Recover**. When options pop up, choose Recover first to capture snapshots where possible.
5. **Reset as Last Resort**. Reset only after confirming there is no unsaved code and everything else has failed.

## Disaster Recovery Pipeline: Service Registry and Idempotent Recovery Scripts

![Disaster Recovery Pipeline: Service Registry and Idempotent Recovery Scripts](/info/05-computer-s7.png)

Updates or resets will wipe the environment. 鐵柱AGI (@cgnot996) proposed a solution on 2026-10-10: **back up provisioning procedures, not the whole machine**.

Using a 5.1 MB private repository, he manages 20 services across 10 Bots (18 essential-to-recover items, including 4 resident, 14 on-demand, and 2 secret-path items); see [Tutorial](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye) for details.

### Standardized Structure and Registry Entry

The `vm-services` repository contains four components:
- `REGISTRY.md` and `registry.json`: Master registry and configurations.
- `restore/restore-<服務名>.sh`: Per-service scripts, **which must be idempotent**.
- `restore/restore-all.sh`: Installs libraries and CLIs sequentially, launches background services, and tallies failures.
- `service-src/`: Source code archives, excluding `.env`, logs, and virtual environments.

Registering a new service requires these fields: short ID and assigned Bot; code and data paths; installation method (apt/pip/npm/Docker) and system dependencies; start and health check commands (--version or port); whether recovery is required; absolute path to secrets (**strictly forbid recording plaintext secrets**); manual steps such as QR scanning or OAuth.

### Two Sets of Prompts

Send this to the "VM Service Butler" Bot; other Bots report deployments according to this standard.

::: details Deployment and Registration Prompt
```text
你是「虛擬機器服務管家」，只管一件事：記下這台虛擬機器上部署過的所有第三方服務，並在電腦更新或換帳號之後，按記錄把它們原樣恢復。

你維護的東西：
1. 一份登記總帳，人和機器各讀一份：REGISTRY.md（表格）和 registry.json（給指令碼讀）。
2. 每個服務一個恢復指令碼 restore/restore-<服務>.sh，必須冪等，重複跑也不會出錯。
3. 一個總入口 restore/restore-all.sh，按依賴順序呼叫各個恢復指令碼，最後彙總哪些失敗了。
4. 一份原始碼備份 service-src/：各 Bot 自己寫的服務程式碼和指令碼，同步時排除密鑰、記錄、執行狀態、虛擬環境和個人資料，並先掃一遍明文密鑰，命中就停。
5. 以上全部跟著一個私有 Git 倉庫存（「你的備份倉庫地址」）。總帳、恢復指令碼、原始碼都在倉庫裡，密鑰永遠不進倉庫。

登記規則（其他 Bot 部署任何服務都必須來找你登記）：
每項必須包含：
- 名稱和短 id、用途、負責的 Bot
- 路徑：程式碼、組態、資料分別在哪
- 安裝方式和依賴（apt / pip / npm / Docker / 系統定時任務）
- 啟停命令、健康檢查命令
- 更新後的恢復步驟，或者對應的恢復指令碼
- 是否必恢復：是 / 否
- 密鑰：只寫存放路徑，絕不寫明文
- 需要真人完成的步驟（OAuth 登錄、掃碼、匯入 cookie）單獨標出來

你的工作方式：
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

After a reset, configure Git credentials and send this to the recovery Bot. **The acceptance criteria report results, elapsed time, and check status against the checklist**.

::: details One-Click Recovery Prompt After Reset
```text
這台電腦剛重置過（或者是換了新帳號），之前部署的服務都沒了。請按我的備份把它們恢復到可用狀態，規則如下。

備份在哪：
- 備份倉庫：<你的備份倉庫地址>，分支 <分支名>
- 倉庫裡有：登記總帳（REGISTRY.md 和 registry.json）、每個服務的恢復指令碼（restore/）、自寫服務的原始碼備份（service-src/）
- 倉庫裡沒有密鑰，這是故意的

請按這個順序做：
1. 把備份倉庫拉到工作目錄，先讀總帳，告訴我一共登記了幾項、哪些標了「必恢復」、哪些只留密鑰不用恢復。先列出來，不要動手。
2. 把自寫服務的原始碼從 service-src/ 放回總帳寫的原位置。只補缺失的，已經存在的目錄不要覆蓋。
3. 按總帳的依賴順序逐項恢復：先裝系統依賴（比如 cron、ffmpeg），再裝命令列工具，最後拉起常駐服務和定時任務。每項都用它自己的恢復指令碼，指令碼要能重複跑。
4. 每裝完一項就跑它登記的健康檢查。失敗了先看記錄、試著修一次；修不好就記下原因，接著做下一項，不要卡住。
5. 把需要我本人做的事彙總成一張清單：要重新提供的密鑰（只說放哪個路徑、叫什麼名字，別讓我把密鑰貼進聊天）、要重新登錄授權的工具（OAuth、掃碼、設備碼）。然後一項一項帶我做，每做完一項馬上覆查。
6. 故意暫停的任務保持暫停，總帳裡寫了原因和重開條件的照辦。別因為“看起來漏裝了”就自作主張打開。
7. 最後交驗收清單，每項一行：服務名、結果（成功 / 失敗 / 等我處理）、健康檢查輸出摘要、花了多久。再告訴我總共用了多少時間、成功了幾項。

不要做的事：
- 不要把任何密鑰寫進倉庫、記錄或聊天
- 不要跑總帳沒登記的安裝
- 不要用“重置電腦”當修復手段
- 恢復完如果有任何改動（路徑變了、版本升級了），更新總帳，提交推回備份倉庫
```
:::

## Common Pitfalls

### Credentials and Permissions
- **Never paste secrets into the chat box**: Enter them manually in web interfaces; write CLI Tokens into `~/.env` and have scripts read environment variables.
- **No isolation between Bots**: Shared `/workspace` and permissions. Sensitive assets rely on private repositories and manual approvals; creating multiple Bots provides no isolation.

### Collaboration and Dependencies
- **Handoffs must be written to disk**: Bots cannot read each other's conversations. Save Bot A's results as Markdown or JSON; relying solely on verbal handoffs causes Bot B to hallucinate.
- **Dependencies are non-persistent**: Updates, Recover, or Reset will clear packages from `apt install` and `npm install -g`; `node_modules` and `.venv` are also not backed up.

  **Recovery scripts must include** `npm install` and `pip install -r requirements.txt`.

### Operations and Networking
- **Do not click Reset when seeing Reconnecting**: This will discard unsaved changes and force a rebuild; **retry or restart the client first**.
- **Centrally manage scheduled tasks**: crontab entries must be maintained centrally in a Git repository.
- **Restart required when enabling local routing**: If the IP doesn't change after enabling "Route traffic through this computer", restart the process.

## Verification After Completion

1. Bot A writes a timestamp to `/workspace/handoff/test.json`. **Bot B reads and accurately reports it**, verifying smooth communication.
2. In "Settings" > "Computers", enable "Route traffic through this computer", then run `curl -s https://api.ipify.org` in the terminal. **The public IP must match your local IP**, not the data center IP.
3. Have the Bot open the GitHub login page; **it must pause before the password field and prompt for takeover**. Resume after logging in manually and verify that no plaintext passwords appear in the logs.
4. Confirm that `REGISTRY.md`, `registry.json`, and the scripts have been committed to the private Git repo. Pull and run in a test directory:
```bash
bash restore/restore-all.sh
```
**All health checks must pass**, with no conflict errors, and registry services must listen normally.

## Further Reading

### Official Documentation and Knowledge Base

- [Manage Grok Bot Computers](https://cursor.com/cn/docs/grok-bot/computers): Official comprehensive rules on batch rebuilding, terminating, and 30-day inactivity cleanup for enterprise multi-computer environments.
- [Settings and Notifications](https://cursor.com/cn/docs/grok-bot/settings): Official explanations regarding desktop client settings, local command execution, traffic relay routing, and Auto-review mode.
- [Grok Bot Computers](https://cursor.com/cn/help/grok-bot/computer-recovery): Official differences between Update, Recover, and Reset, along with a troubleshooting checklist.

### Community Practical References

- [4.6 Virtual Machines, Memory, and Backup](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg): Detailed breakdown of cloud computer underlying architecture, context organization maps, and multi-Bot file collaboration.
- [Lost All Tools After Grok Bot VM Reset? Backup & Recovery Tutorial (with Prompts)](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye): Practical guide shared by community author 鐵柱AGI (@cgnot996) covering VM Service Butler design, master registry ledger, and one-click recovery.

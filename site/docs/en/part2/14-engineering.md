# Chapter 14 Case Studies: Engineering and R&D Teams

Stop babysitting tasks locally—**delegate work to the cloud**.

- Shut down your machine anytime while tasks run 24/7, sparing you from waking up at 2 AM to check CI.
- Code in isolated environments, attaching real evidence and logs to pull requests to prevent fake green builds through modified assertions.

Review the **delivery reports in the morning to gatekeep releases**.

## Core Architecture: Division of Labor Among Harness, Model Brain, and Local CLI Agent

![Core Architecture: Division of Labor Among Harness, Model Brain, and Local CLI Agent](/info/14-engineering-s1.png)

### Role Definition and Tripartite Division of Labor
On October 7, 2026, the platform introduced models such as Claude Opus 5.5 for inference. **The system schedules models automatically and does not provide a manual single-request picker**. Do not rely on specific model features; workflows must be strictly constrained by state files and automated verification.

| Role | Host Environment | Permissions & Responsibilities |
| :--- | :--- | :--- |
| Grok Bot | Cloud computer (`/workspace` shared storage) | Runs inspections and dispatches tasks; **generates Draft PRs only, strictly forbidden from pushing directly to default branches or deploying to production** |
| Local CLI Agent | Local terminal or ephemeral container | Pulls dependencies, modifies code on isolated branches, and executes builds |
| Human Lead | Personal workstation | **Holds release keys and production write access**, responsible for architectural decisions and merge approvals |

### Environment Configuration and Security Isolation
All bots under the same account share the same cloud computer, CLI credentials, and browser sessions; **renaming a bot does not provide permission isolation**. Avoid pasting plaintext credentials into chat dialogs during sensitive logins; **always use Take Control to authenticate manually on the remote screen**, leaving the active session in the browser.

### Runtime Environment Self-Check and Persistence
Before onboarding a new repository, run self-check commands in Grok Bot to understand the environment configuration.

::: details Runtime Environment Self-Check and Persistence
```bash
echo "CPU 核心數:"
nproc

echo "記憶體配置:"
free -h

echo "工作區磁盤空間:"
df -h /workspace

echo "系統版本與 Git:"
cat /etc/os-release | head -n 3
git --version
```
:::

System dependencies may be reset during updates; only the `/workspace` directory persists across restarts. **All core state must be synchronized to remote remotes via Git or saved in structured files**.

Reference documentation includes the [Grok Bot Official User Guide](https://cursor.com/cn/docs/grok-bot/work) and [Cloud Computer and Application Connection Guide](https://cursor.com/cn/docs/grok-bot/computers).

## Case Study 1: SpaceXAI Team's PR Inspection and Multi-Bot Orchestration

Lingxi Li (@lingxi) at SpaceXAI led 5 R&D bots plus 1 workflow bot, paired with Cursor cloud agent running 24/7.

@poteto on the team merged over 2,000 PRs in a single month, while Lingxi himself delivered iOS v0 in just 3 weeks.

The 5 R&D bots operated in isolated contexts, each monitoring a specific slice of the codebase and invoking designated commands per task:
- Baltata handled iOS and the shared mobile layer, while Craig handled Android.
- Shaoruru managed the desktop client and CI/CD, while Quill maintained the Harness toolchain.
- Hogan specialized in underlying infrastructure and unassigned bugs.
- Visual design routed through `/lingxi-design`, code quality through `/react-native-best-practices`, and architecture through `/lingxi-review`.

Supervisor bot Jenny wrote no code, syncing the runbooks across the team every morning at 5 AM. **Whenever an R&D bot relaxed review standards or delivered unverified changes, Jenny flagged it for an RCA and updated the operational rules**.

Long sessions easily exhaust context limits, so the team stored state in a Notion database and completed the closed loop via scheduled polling:
1. **Half-Hour Polling**: Scans open PRs every 30 minutes to verify Bugbot results, CI errors, and Git conflicts.

   When issues arise, it invokes Cursor to fix them and switches back to Working; once all checks are green, it transitions to Ready for Review. PRs are auto-merged only when confidence is exceptionally high and the change impact is minimal. **Concurrent dispatch capacity per person jumped from 15 to over 200**.
2. **Real-Device Screenshot Alignment**: Code assertions easily miss visual rendering defects. The team repurposed an idle Mac mini as a private worker running iOS Simulator, **using multimodal models to compare actual before-and-after screenshots**, rejecting changes immediately if the visuals do not match.
3. **3 AM Nightly Audit**: Cleans dead code to reduce bundle size, inspects dependency vulnerabilities and CI runtimes, fills in missing internationalization (i18n), validates cross-platform feature parity, and compiles a summary of PRs over the past 24 hours.

> Source: [How Can Engineers Make Good Use of Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Author: [Kin @KinGao476942](https://x.com/KinGao476942)

![How Can Engineers Make Good Use of Grok Bot?](/cases-img/fs25-0.jpg)

![How Can Engineers Make Good Use of Grok Bot?](/cases-img/fs25-1.jpg)

**Never let a single bot carry long sessions**. Split roles by business domain, assign a dedicated reviewer to iterate on rules, and track state in a dashboard for diff verification—it saves tremendous effort.

- [How Can Engineers Make Good Use of Grok Bot? | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [Grok Bot for Engineering | Lingxi Li](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)

## Case Study 2: Deconstructing R&D Work and Lauren's Nine-Category Checklist

### How It Works
Lauren (@poteto) merged 2,500 production PRs in a single month, while Jacob Gold (@jacobgold) averaged nearly 250 per day; both deconstructed engineering tasks into nine parallel tracks.

| Risk Level | Typical Scope & Rules | Review Method |
| :--- | :--- | :--- |
| Low to Medium | Dead code cleanup, unit tests, and type fixes | Auto-merge |
| High Risk | Core business logic, authentication, and data migrations | Mandatory human review |

**The moment a diff exceeds the intent of the original prompt, the system immediately escalates it for human approval.**

### Key Takeaways
Mai Yang (@MaiYangAI) generated 1,020 commits in ContextEcho over six months, opening PRs only 18 times. **Solo projects have a minimal blast radius; fabricating artificial PRs without real necessity creates zero value.**

> Source: [What Is the Point of Hundreds of PRs a Day? I Followed SpaceXAI Engineer Lauren's (@poteto) Nine Categories to Deconstruct My Own Work](https://x.com/MaiYangAI/status/2108519046446727633)  
> Author: [Mai Yang @MaiYangAI](https://x.com/MaiYangAI)
Start with bug fixes and code styling/refactoring, accompanied by input constraints and acceptance criteria. **Save the mental energy spent reading code by eye and redirect it toward defining direction, boundary constraints, and testing.**

[What Is the Point of Hundreds of PRs a Day? I Followed SpaceXAI Engineer Lauren's (@poteto) Nine Categories to Deconstruct My Own Work](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## Case Study 3: 24/7 Repo Ops Desk

![Case Study 3: 24/7 Repo Ops Desk](/info/14-engineering-s3.png)

### Who Built It and What It Does
Independent developer Gipp 🦅 (@gippp69) designed a 24/7 Repo Ops Desk while maintaining multiple open-source and commercial repositories. The system combines concurrent sub-agents to monitor anomalies at the base level, while orchestrating 6 named roles via Grok Bot at the top level to process issues and CI failures.

According to the author, a single developer can typically oversee only 2 to 3 repositories manually. An automated ops desk, by contrast, monitors hundreds of change points across multiple repositories simultaneously.

### How It Works

::: details How It Works
```
[GitHub 事件 / CI 報警]
          │
          ▼
    ┌───────────┐
    │Triage Bot │ ── 識別嚴重度與類別
    └─────┬─────┘
          │
   ┌──────┴───────────────────────────┐
   ▼                                  ▼
[偶發測試 / 格式問題]             [業務邏輯缺陷 / CVE 安全問題]
   │                                  │
   ▼                                  ▼
┌─────────┐                      ┌─────────────────────────┐
│ Fix Bot │                      │ Dependency / Alert Bot  │
└────┬────┘                      └────────────┬────────────┘
     │                                        │
     ▼                                        ▼
[生成修復 Patch]                   [嚴重漏洞即時呼叫人類]
     │                                        │
     ▼                                        ▼
[提交 Draft PR (嚴禁合併)]           [其餘彙總至次日晨報]
```
:::

1. **Deploy 6 Dedicated Bots**
   - Triage Bot: Categorizes issues by severity and type.
   - Fix Bot: Handles minor bugs, writes patches, and submits Draft PRs.
   - Test Bot: Executes tests to catch flaky tests and records failure context.
   - Dependency Bot: Monitors CVE vulnerabilities and outdated dependencies.
   - Release Bot: Organizes changelogs and bundles releases upon command.
   - Alert Bot: Dispatches instant notifications when human intervention is needed.

2. **Lock Down Permissions via a Routing Table**

| Permission Level | Monitoring Scope | Role and Action |
| :--- | :--- | :--- |
| `auto-fix` | Flaky tests, lint errors, and formatting | Fix Bot submits patches |
| `triage` | Uncategorized complex bugs and feature requests | Triage Bot escalates to humans |
| `security` | Medium- to high-risk CVE vulnerabilities | Dependency Bot forwards to Alert Bot upon detection |
| `release` | Version changes and release notes | Release Bot executes upon instruction |

3. **Uphold Three Strict Red Lines**
   - Never touch business logic: `auto-fix` changes are strictly confined to the failing test file itself or its direct imports; modifying core code is strictly forbidden.
   - Never auto-merge: Fix Bot opens only Draft PRs tagged with `auto-fix`, never auto-merging.
   - Canary run for one week: Run for a week in a single low-risk edge repository to evaluate the adoption rate (merged vs. discarded count) before rolling out to main repositories once stable.

### Key Takeaways

> Source: [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](https://x.com/gippp69/status/2095088203690570191)  
> Author: [Gipp 🦅 @gippp69](https://x.com/gippp69)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-0.jpg)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-1.jpg)
**The ops desk troubleshoots errors in the middle of the night without making decisions**. Prompts and permissions are strictly locked to "only open Draft PRs, never modify business logic," allowing the system to run safely unattended.

For detailed configuration, see [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide) | Gipp 🦅](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh).

## Case Study 4: Engineering Harness Based on State Machines and Multi-Bot Collaboration

![Case Study 4: Engineering Harness Based on State Machines and Multi-Bot Collaboration](/info/14-engineering-s4.png)

### Who Built It and What It Does
Developers Mori (@0xjmori), Morlex (@0xMorlex), and solopreneur architect beamnxw designed a standardized R&D collaboration pipeline. By establishing state machine contracts, a unified directory structure, and a six-field task board in the cloud, they implemented an end-to-end fix pipeline where 1 lead orchestrates 4 specialists.

The entire system decomposes complex code changes into state transitions backed by verifiable evidence. This design ensures that every handoff across stages is fully documented and auditable.

### How It Works

1. **Establish a Structured Workspace Directory**
Initialize the project in the Grok Bot cloud computer `/workspace`, placing each issue into an isolated directory `/workspace/devdesk/issues/<issue-id>/`.

```bash
mkdir -p /workspace/devdesk/{queue,issues,reviews,approved,logs}
```

**Each directory must contain 6 standard files:**
- `task.md`: Original input and completion acceptance criteria
- `status.json`: Current machine-readable state and assignee
- `evidence/`: Directory storing failure logs, reproduction scripts, and screenshots
- `implementation.md`: Modified file manifest and minimal implementation plan
- `review.md`: Independent review conclusion
- `handoff.md`: Sign-off handoff report delivered to humans

2. **State Machine Transition Contract**
**The pipeline advances sequentially through predefined states; skipping steps is strictly forbidden.**

```
NEW ──> TRIAGED ──> REPRODUCED ──> BUILDING ──> TESTED ──> REVIEWING ──> REVIEW_PASSED ──> DRAFT_PR_READY ──> HUMAN_APPROVAL
                                                   ▲            │
                                                   └── FAILED ──┘
```

- **Triage (`NEW` ──> `REPRODUCED`)**: Must provide reproducible steps and an executable failing test case.
- **Builder (`BUILDING` ──> `TESTED`)**: Dispatches a Cursor agent to modify code on a fresh branch and ensures regression tests pass.
- **Reviewer (`REVIEWING` ──> `REVIEW_PASSED`)**: Independently reviews diffs and logs to assign a rating. **A FAIL immediately sends the task back to `BUILDING` for rework, with a maximum of 2 retries.**
- **Release (`DRAFT_PR_READY` ──> `HUMAN_APPROVAL`)**: After all checks pass, submits a Draft PR accompanied by complete evidence to the human engineer.

3. **Action Reversibility Grading**
**The system delineates approval permissions based on whether an action is reversible.**

| Operation Category | Permission Policy | Scope of Actions and Behaviors |
| :--- | :--- | :--- |
| **Reversible Actions** | Autonomous execution | Performing code analysis, writing patches and running unit tests on local branches, generating failing test cases, opening Draft PRs, and generating log reports |
| **Irreversible Actions** | Halt and await human review | Merging code into the default branch, deploying to production, modifying production databases, altering environment variables or secrets, calling billable external services |

4. **Board and Skill Solidification**
The board columns are strictly fixed to `Task | Owner | Source | Status | Deliverable | Next action`.
Task statuses are strictly restricted to five states: `ready`, `working`, `blocked`, `awaiting approval`, and `complete`.
**Once a type of task succeeds once, solidify it as a private Skill via command**, enabling routine schedules to invoke it repeatedly.

### Key Takeaways

> Source: [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://x.com/0xjmori/status/2109648700897116554)  
> Author: [Mori @0xjmori](https://x.com/0xjmori)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-0.jpg)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-1.jpg)

Never let multiple agents chat casually in unstructured group conversations.

1. **If the previous step produced no test evidence, never start the next step**. Lock down progress using disk directories and state machines.
2. **Distinguish action reversibility** to balance automation velocity with production safety baselines.

For detailed implementation, refer to [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf), [Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps | Morlex](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh), and [Grok Bot Engineering: Set Up a Harness for Your One-Person Company | beamnxw ./](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm).

## Out of the Box: Engineering R&D Prompt Library

The following prompts are all verified in production. Copy and send them directly to your bots and ask them to remember them; for shared bots, paste them into the About details:

### 1. Architecture Master Charter (Chief)
**Send to the supervisor bot and ask it to remember it** (for shared bots, write to About details) to oversee workflows and log state.

::: details 1. Architecture Master Charter (Chief)
```text
你是 Chief，負責管理 /workspace/devdesk 工作區內的 AI 工程團隊。
你的職責是將每一個接到的 Issue 推進至可供人工複審的 Draft PR 狀態。

工作原則：
1. 為每個處理階段指派且僅指派一名專職 Bot。
2. 實時維護狀態帳本（status.json），防止任務重複分配。
3. 嚴格檢查各階段交付證據，絕不能僅憑下游 Bot 的口頭回復判定任務完成。
4. 發生例外時記錄阻塞點與失敗嘗試，連續失敗兩次立即終止重試。
5. 嚴禁親自編寫業務生產程式碼，嚴禁合併程式碼至預設分支，嚴禁觸發生產部署。
```
:::

### 2. Bug Reproduction Specialist (Triage)

Paste directly **into Triage Bot** to investigate bugs and write failing test cases.

::: details 2. Bug Reproduction Specialist (Triage)
```text
你是 Triage 缺陷復現專員。
你的任務是調查收到的 GitHub Issue 並提供可穩定復現的證據。

針對每個任務，請按順序執行：
1. 閱讀 Issue 描述與關聯程式碼，明確系統預期行為。
2. 在雲端測試環境中重現故障現象，抓取執行記錄或錯誤堆棧。
3. 儘可能編寫一個針對該故障的獨立最小失敗測試（Failing Test）。
4. 將重現步驟、測試命令與記錄存入該 Issue 的 evidence/ 目錄。

紅線要求：
- 證據不足時絕不推測原因。
- 嚴禁修改任何正式環境程式碼與系統組態。
- 交付內容必須包含：Issue 編號、復現步驟、失敗測試執行結果、影響範圍評估。
```
:::

### 3. Coding Specialist (Builder)
Paste the prompt into **Builder Bot** to run on an isolated branch.

::: details 3. Coding Specialist (Builder)
```text
你是 Builder 寫程式專員。
你的任務是為已經由 Triage 成功復現的 Issue 提供最小安全修復程式碼。

工作流程：
1. 完整閱讀 Triage 提供的復現報告與失敗測試。
2. 新建獨立 Git 分支（格式：fix/<issue-id>），絕不在主分支修改。
3. 保持 Triage 編寫的失敗測試不變，針對性修改業務程式碼以消除該報錯。
4. 執行相關測試套件，確認修改後原使用案例通過且無新增判斷提示失敗。
5. 提交程式碼並推送至遠端，建立 Draft PR。
6. 輸出變更文件清單、測試執行記錄與潛在風險分析。

紅線要求：
- 嚴禁推送至預設主分支，嚴禁直接合並，嚴禁修改無關文件。
- 如果需要呼叫 Cursor cloud agent，必須在獨立環境中派生，嚴禁多 Agent 平行處理寫入同一文件。
```
:::

### 4. Independent Review Specialist (Reviewer)
Paste the prompt into Reviewer Bot for **strict acceptance testing**.

::: details 4. Independent Review Specialist (Reviewer)
```text
你是 Reviewer 獨立審查專員。
你的職責是獨立核驗 Builder 提交的修改結果。你必須站在挑剔的角度排查潛在問題，絕不接受無憑據的口頭總結。

核查清單：
1. 修復方案是否確實解決了原始 Issue 回饋的問題？
2. 提供的迴歸測試是否確實在修復前失敗、修復後通過？
3. 是否改動了與本任務無關的文件？
4. 是否存在未處理的邊界場景、空指標或例外處理漏洞？
5. 彙報的測試結果是否有真實命令列輸出記錄支援？
6. 程式碼是否引入了新的安全隱患、效能退化或介面相容性風險？

判定輸出（三選一）：
- PASS：符合質量要求，附帶核實依據。
- FAIL：未達標，指出具體文件、行號、缺陷原因與修改要求。
- BLOCKED：證據缺失或需要上級審批權限。

紅線要求：嚴禁親自修改任何業務實作程式碼。
```
:::

### 5. Delivery Specialist (Release)
**Paste the prompt into Release Bot** to aggregate artifacts and handle handoff:

::: details 5. Delivery Specialist (Release)
```text
你是 Release 交付專員。
你只接收已達到以下條件的任務：
1. 存在有效的 Draft PR 連結。
2. 自動化檢查全部通過，附帶真實執行記錄。
3. Reviewer 明確給出了 PASS 結論，無遺留未決缺陷。

交付動作：
整理一份清晰的放行說明文件（handoff.md），包含：
- Issue 連結與 Draft PR 連結。
- 本次變更的核心內容說明。
- 執行的測試項及其主控台輸出摘要。
- 明確標註等待人類審批的操作（如 Merge、線上組態生效等）。

紅線要求：嚴禁自動合併 PR，嚴禁操作生產分支。
```
:::

### 6. Engineering Night Shift Routine

Configure a scheduled routine in Grok Bot, **selecting Chief as the execution owner**.

::: details 6. Engineering Night Shift Routine
```text
建立名為「Engineering Night Shift」的定時例行任務。
負責人：Chief
觸發時間：工作日每晚 23:00（按組態的時區）

工作流程：
1. 檢索當前倉庫中帶有「agent-ready」標記的 GitHub Issue，單次最多提取 2 個。
2. 檢查本地任務帳本，跳過已在處理中的任務。
3. 排程 Triage、Builder、Reviewer 按預設流程流轉，使用獨立分支與 Cursor cloud agent。
4. 要求獨立審查證據，最終僅產出 Draft PR。
5. 彙總生成一份晨間交接報告，列出：已完成的 Draft PR、阻塞的任務、失敗的測試項、待審批事項。

終止條件：
- 遇到未授權倉庫或無權限文件。
- 缺陷無法穩定復現。
- Builder 修復嘗試達到 2 次仍未通過審查。
- 改動涉及資料庫遷移、認證安全或核心計費模組。
```
:::

### 7. Reversibility Guardrails and Safety Red Line Directives

**Paste directly at the end of each bot's long-term rules** (send in chat for personal bots to remember; write into About details for shared bots).

::: details 7. Reversibility Guardrails and Safety Red Line Directives
```text
執行動作分級準則：

【允許自主執行（可逆操作）】
- 分析程式碼倉庫、檢索 Issue、編寫復現測試。
- 在獨立工作分支修改程式碼、執行本地測試建構。
- 編寫審查報告、更新任務狀態帳本、開啟 Draft PR。
遇到此類任務，自主完成並記錄操作記錄，無需等待確認。

【強制停機等待審批（不可逆或高危操作）】
- 向預設主幹分支合併程式碼或推送更新。
- 執行任何正式環境部署操作。
- 涉及修改資料庫表結構、資料遷移或刪除資料。
- 變更系統認證、敏感密鑰或外部扣費組態。
- 向公司外部人員發送通知或公開對外發表內容。
遇到此類動作，必須立即掛起任務，記錄當前進展並等待人工授權。
```
:::

---

## Common Pitfalls

### Automatic Model Matching
The backend automatically routes to underlying models such as Claude Opus 5.5, with no manual picker available. **Write transition conditions into structured files like `status.json` and validate them via strict scripts**; do not rely on models to maintain consistent output styles.

### Shared Environment Conflicts
All bots share `/workspace` on the cloud computer. **Each issue must use an isolated subdirectory and Git branch**; spawn a Cursor cloud agent when modifying code, and strictly avoid sharing uncommitted working trees.

### Review Deadlocks and Tampered Tests
When a fix fails, Builder can easily fall into an infinite loop or even tamper with test assertions to fake a green build. **Strictly limit retries for a single issue to 2 rounds**, immediately escalating to human review if exceeded. Reviewer must inspect Git diffs of test cases; any modified assertions must be marked as FAIL immediately.

### Subscription Quotas and Polling
Usage follows The X Subscription effective October 12, 2026, sharing a weekly quota pool across Grok and Cursor, with overages billed through Cursor.

Avoid 5-minute full repository sweeps; **set scheduled routines to once daily or nightly**, relying primarily on the `agent-ready` label for triggers.

| Subscription Tier | Monthly Price | Quota Multiplier | Includes Grok Bot |
| :--- | :--- | :--- | :--- |
| **Plus** | - | - | Bot Not Included |
| **Premium** | $30 / mo | 4x quota | Included |
| **Super** | $100 / mo | 15x quota | Included |
| **Ultra** | $200 / mo | 50x quota | Included |

### Branch Protection and Draft PRs
**Agent deliverables must be submitted exclusively as Draft PRs and are strictly prohibited from auto-merging into the default branch**. GitHub Branch Protection Rules must enforce three strict constraints:
- Prohibit direct pushes to the main or master branch
- Require at least one human approval (Approvals)
- Require existing CI pipelines to pass completely

### Preventing Sensitive Credential Leaks
Chat dialog content enters the model context; **never enter passwords, private keys, or API keys into prompts**. Access private systems via connectors in settings, or use Take Control remote desktop on Agent Computer to log in manually.

## Acceptance Verification

**Never roll this out across core production projects right from the start.**

### Single-Repo, Single-Bug Cold Start Acceptance
- Pick an edge repository, create `/workspace/devdesk/`, and tag a minor bug with `agent-ready`.
- Run the Chief workflow and verify that Triage saves reproduction logs and unit tests under `evidence/`.
- Verify that Builder modifies code on an isolated branch without touching main branch code, and that Reviewer provides line-number-level logic verification.
- **Confirm that only a Draft PR is created in the end**, leaving the main branch completely untouched.

### Metric Quantification and Patch Adoption Rate Inspection
- If the adoption rate is **below 70%, pause onboarding a second repository** and tighten prompt constraints.
- The morning report must allow you to clearly review qualified PRs, blocked items, and pending issues **within 3 minutes**; having to read through thousands of words of chat history is considered failing the criteria.
- Ensure early-morning scheduled tasks sleep when not triggered and terminate automatically upon timeout to avoid quota blowouts.

### Safety Red Lines and Permission Interception Drills
- Deliberately submit an issue that modifies schema migrations or authentication logic to verify that the task is intercepted and suspended.
- Have the bot run `git push origin main`, and verify that **branch protection successfully blocks it**.
- For external communications and configuration changes, verify that Auto-review is set to **Ask first**.

## Further Reading

### Official Documentation and Feature Pages
- [Grok Bot Official User Guide](https://cursor.com/cn/docs/grok-bot/work)
- [Cloud Computers and Application Connections](https://cursor.com/cn/docs/grok-bot/computers)
- [Model Selection and Routing Guide](https://cursor.com/cn/help/grok-bot/models)
- [Plans, Billing, and On-Demand Usage Help](https://cursor.com/cn/help/grok-bot/plans)
- [Settings and Security Specifications](https://cursor.com/cn/docs/grok-bot/settings)
- [Team Collaboration and Team Bots Configuration](https://cursor.com/cn/docs/grok-bot/teams)

### Original Community Case Studies

> Source: [Grok Bot for Engineering](https://x.com/lingxi/status/2094493172516966781)  
> Author: [Lingxi Li @lingxi](https://x.com/lingxi)

![Grok Bot for Engineering](/cases-img/fs50-0.jpg)

![Grok Bot for Engineering](/cases-img/fs50-1.jpg)
- [How Can Engineers Make Good Use of Grok Bot? | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [Grok Bot for Engineering | Lingxi Li](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)
- [What Is the Point of Hundreds of PRs a Day? I Followed SpaceXAI Engineer Lauren's (@poteto) Nine Categories to Deconstruct My Own Work](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)
- [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide) | Gipp 🦅](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)
- [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)
- [Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps | Morlex](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)
- [Grok Bot Engineering: Set Up a Harness for Your One-Person Company | beamnxw ./](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)

# 第 14 章 案例：工程與研發團隊

別在本地盯梢，把活**託管到雲端**。

- 電腦隨時關機，24 小時運轉，免得凌晨兩點爬起來查 CI。
- 隔離環境寫程式，合併請求附真實證據與記錄，防判斷提示改綠。

早晨**看交付報告把關發表**。

## 核心架構：Harness、模型大腦與本地 CLI Agent 分工

![核心架構：Harness、模型大腦與本地 CLI Agent 分工](/info/14-engineering-s1.png)

### 角色定位與三方分工
2026 年 10 月 7 日平台引入了 Claude Opus 5.5 等模型參與推理。**系統自動排程模型，不提供手動單次選擇器**。別指望單一模型特性，流程要靠狀態文件和自動化校驗卡死。

| 角色 | 執行宿主 | 權限與職責 |
| :--- | :--- | :--- |
| Grok Bot | 雲端電腦（`/workspace` 共享儲存） | 跑巡檢與派發任務，**只生成 Draft PR，嚴禁直接推預設分支或上線** |
| 本地 CLI Agent | 本地終端或臨時容器 | 獨立分支拉依賴改程式碼，跑建構 |
| 人類主管 | 個人工作站 | **手握髮布密鑰與生產寫權限**，負責架構決策與審批合併 |

### 環境組態與安全隔離
同帳號下所有 Bot 共享同一台雲端電腦、命令列憑據與瀏覽器會話，**給 Bot 改名起不到權限隔離的作用**。遇到敏感登錄別在對話框貼明文，**必須用 Take Control 在遠端螢幕人工認證**，把會話留給瀏覽器。

### 執行環境自檢與持久化
接入新倉庫前，先在 Grok Bot 跑自檢命令摸清組態。

::: details 執行環境自檢與持久化
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

更新時系統依賴可能被重置，只有 `/workspace` 目錄會持久保留。**所有核心狀態都要用 Git 同步到遠端或存進結構化文件**。

參考文件包括 [Grok Bot 官方使用指南](https://cursor.com/cn/docs/grok-bot/work) 與 [雲端電腦與應用連線說明](https://cursor.com/cn/docs/grok-bot/computers)。

## 案例一：SpaceXAI 團隊的 PR 巡檢與多 Bot 編排

SpaceXAI 的 Lingxi Li（@lingxi）帶了 5 個研發 Bot 加 1 個流程 Bot，配 Cursor cloud agent 全天跑。

團隊裡的 @poteto 單月合入超 2,000 個 PR，Lingxi 自己也只花 3 周就搞定了 iOS v0。

5 個研發 Bot 隔離了上下文，各自盯一塊程式碼，按任務調對應命令：
- Baltata 負責 iOS 與行動共享層，Craig 負責 Android。
- Shaoruru 負責桌面端與 CI/CD，Quill 維護 Harness 工具鏈。
- Hogan 專查底層基建與無歸屬 Bug。
- 視覺走 `/lingxi-design`，程式碼品質走 `/react-native-best-practices`，架構走 `/lingxi-review`。

主管 Bot Jenny 不寫程式碼，每天早 5 點逐個對齊手冊。**研發 Bot 一旦審查放水或沒徹底驗證就交付，Jenny 會抓出來做 RCA 並更新規則**。

長會話容易把上下文撐爆，團隊把狀態放進 Notion 庫，靠定時輪詢跑完閉環：
1. **半小時輪詢**：每 30 分鐘掃一遍 open PR，核驗 Bugbot 結果、CI 報錯和 Git 衝突。

   有問題調 Cursor 修復並切回 Working，全綠切為 Ready for Review；只有置信度極高且改動影響極小時才自動合入。**單人平行處理排程量從 15 提到了 200 個以上**。
2. **真機截圖對齊**：程式碼判斷提示容易漏掉視覺顯示問題，團隊拿閒置 Mac mini 當私有 Worker 跑 iOS Simulator，**靠多模態比對前後真實截圖**，視覺不對就直接打回。
3. **凌晨 3 點夜間審計**：清理死程式碼縮包，排查依賴安全和 CI 耗時，補齊國際化，檢查多端功能對等，彙總過去 24 小時 PR。

> 來源：[工程師如何用好 Grok bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> 作者：[Kin @KinGao476942](https://x.com/KinGao476942)

![工程師如何用好 Grok bot?](/cases-img/fs25-0.jpg)

![工程師如何用好 Grok bot?](/cases-img/fs25-1.jpg)

**別讓單個 Bot 扛長會話**。按業務拆角色，設專人覆盤規則，把狀態放到看板裡做差異核對，省心很多。

- [《工程師如何用好 Grok bot?｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering｜Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)

## 案例二：研發工作拆解與 Lauren 的九類清單

### 具體怎麼做
Lauren（@poteto）單月合併 2,500 個生產 PR，Jacob Gold（@jacobgold）日均近 250 個，兩人把工程拆成九條線並行跑。

| 風險級別 | 典型範圍與規則 | 審查方式 |
| :--- | :--- | :--- |
| 低至中 | 清理死程式碼、單測與型別修正 | 自動合入 |
| 高風險 | 核心業務、鑑權與資料遷移 | 強制人工審查 |

**只要 Diff 超出原始提示詞意圖，系統立即推給人工拍板。**

### 可以借鑑什麼
Mai Yang（@MaiYangAI）半年在 ContextEcho 產生 1,020 個提交，僅 18 次走 PR。**單人項目破壞面極小，缺乏真實需求時硬造 PR 毫無價值。**

> 來源：[一天幾百個 PR 有什麼意義？我照著 SpaceXAI 工程師 Lauren（@poteto）的九類清單，把自己的活拆了一遍](https://x.com/MaiYangAI/status/2108519046446727633)  
> 作者：[Mai Yang @MaiYangAI](https://x.com/MaiYangAI)
先選 Bug 修復與規範重構兩項，加上輸入限制和驗收標準。**省下肉眼看程式碼的精力，轉去抓方向定義、邊界約束與測試。**

[《一天幾百個 PR 有什麼意義？我照著 SpaceXAI 工程師 Lauren（@poteto）的九類清單，把自己的活拆了一遍》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## 案例三：24/7 倉庫值班台（Repo Ops Desk）

![案例三：24/7 倉庫值班台（Repo Ops Desk）](/info/14-engineering-s3.png)

### 誰在做與做了什麼
獨立開發者 Gipp 🦅（@gippp69）在維護多個開源專案與業務倉庫時，設計了一套 24/7 倉庫值班台。這套系統在底層結合平行處理子 Agent 監控例外，在頂層通過 Grok Bot 部署 6 個具名角色處理 Issue 與 CI 報錯。

根據作者自述，個人手工通常只能盯 2 到 3 個倉庫。而自動化值班台能同時監控多倉庫的數百個改動點。

### 具體怎麼做

::: details 具體怎麼做
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

1. **部署 6 個專職 Bot**
   - Triage Bot：按嚴重程度和型別歸類 Issue。
   - Fix Bot：接管輕度 Bug，寫補丁並提 Draft PR。
   - Test Bot：跑測試抓 Flaky test，記下失敗上下文。
   - Dependency Bot：監控 CVE 漏洞與過期依賴。
   - Release Bot：按指令整理變更記錄並封裝。
   - Alert Bot：需人工介入時即時發通知。

2. **按路由表鎖定權限**

| 權限層級 | 監控範圍 | 角色與動作 |
| :--- | :--- | :--- |
| `auto-fix` | Flaky 測試、Lint 報錯與格式 | Fix Bot 提補丁 |
| `triage` | 未歸類複雜缺陷與需求 | Triage Bot 轉人工 |
| `security` | 中高危 CVE 漏洞 | Dependency 發現即轉 Alert 告警 |
| `release` | 版本變更與發表說明 | Release Bot 聽指令執行 |

3. **守住三條硬性紅線**
   - 絕不碰業務邏輯：`auto-fix` 改動僅限失敗測試文件本身或直接引用，嚴禁改核心程式碼。
   - 絕不自動合併：Fix Bot 只開帶 `auto-fix` 標記的 Draft PR，絕不自動 Merge。
   - 灰度試跑一週：先在單個低風險邊緣倉庫跑一週，看採納率（合併對比放棄數量），穩定後再推主倉。

### 可以借鑑什麼

> 來源：[How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](https://x.com/gippp69/status/2095088203690570191)  
> 作者：[Gipp 🦅 @gippp69](https://x.com/gippp69)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-0.jpg)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-1.jpg)
**值班台在深夜排查報錯，不做決策**。提示詞和權限鎖死「只開 Draft PR、絕不修改業務邏輯」，系統在無人看管下也能安全執行。

詳細組態方案見 [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)｜Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)。

## 案例四：基於狀態機與多 Bot 協作的工程 Harness

![案例四：基於狀態機與多 Bot 協作的工程 Harness](/info/14-engineering-s4.png)

### 誰在做與做了什麼
開發者 Mori（@0xjmori）、Morlex（@0xMorlex）與一人企業架構師 beamnxw 設計了標準化的研發協作流水線。他們通過在雲端建立狀態機合約、統一目錄結構與六欄位任務看板，實作了由 1 名總管協調 4 名專員的端到端修復管線。

整個系統把複雜的程式碼變更拆解為具備可核驗憑據的狀態流轉。這一設計確保了各環節交接均有據可查。

### 具體怎麼做

1. **建立結構化工作區目錄**
在 Grok Bot 雲端電腦 `/workspace` 初始化工程，每個 Issue 進獨立目錄 `/workspace/devdesk/issues/<issue-id>/`。

```bash
mkdir -p /workspace/devdesk/{queue,issues,reviews,approved,logs}
```

**每個目錄必須備齊 6 個標準文件**。
- `task.md`：原始輸入與完成驗收標準
- `status.json`：當前機器可讀狀態及負責人
- `evidence/`：存放失敗記錄、復現指令碼與截圖
- `implementation.md`：改動文件清單與最小實作方案
- `review.md`：獨立審查結論
- `handoff.md`：交付人類別的放行報告

2. **狀態機轉移契約**
**流水線按預定狀態逐級推進，嚴禁跳步**。

```
NEW ──> TRIAGED ──> REPRODUCED ──> BUILDING ──> TESTED ──> REVIEWING ──> REVIEW_PASSED ──> DRAFT_PR_READY ──> HUMAN_APPROVAL
                                                   ▲            │
                                                   └── FAILED ──┘
```

- **Triage（`NEW` ──> `REPRODUCED`）**：必須提供穩定復現步驟和跑得通的失敗使用案例。
- **Builder（`BUILDING` ──> `TESTED`）**：派 Cursor agent 在新分支改程式碼，並保證原迴歸使用案例跑通。
- **Reviewer（`REVIEWING` ──> `REVIEW_PASSED`）**：獨立看 Diff 與記錄給評級。**一旦 FAIL 退回 `BUILDING` 重改，最多重試 2 輪**。
- **Release（`DRAFT_PR_READY` ──> `HUMAN_APPROVAL`）**：檢查項全部通過後，向人類工程師提交帶完整憑證的 Draft PR。

3. **動作可逆性分級**
**系統按動作是否可逆劃定審批權限**。

| 操作分類 | 權限策略 | 涵蓋行為與操作範圍 |
| :--- | :--- | :--- |
| **可逆動作** | 自主執行 | 做程式碼分析，在本地分支編寫補丁與跑單測，生成失敗使用案例，提 Draft PR 並輸出記錄報告 |
| **不可逆動作** | 停機等人審 | 向預設分支合併程式碼，部署上線，修改線上資料庫，變更環境變數或密鑰，呼叫收費外部服務 |

4. **看板與技能固化**
看板欄位固定為 `Task | Owner | Source | Status | Deliverable | Next action`。
任務狀態嚴格限定在 `ready`、`working`、`blocked`、`awaiting approval` 與 `complete` 五種。
**某類任務只要走通一次，就執行命令固化為私有 Skill**，方便定時 Routine 重複呼叫。

### 可以借鑑什麼

> 來源：[Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://x.com/0xjmori/status/2109648700897116554)  
> 作者：[Mori @0xjmori](https://x.com/0xjmori)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-0.jpg)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-1.jpg)

別讓多 Agent 在非結構化群聊裡隨意接話。

1. **上一步沒存測試證據，下一步絕不啟動**。用磁盤目錄和狀態機卡住進展。
2. **區分動作可逆性**，兼顧自動化速度的同時守住生產安全底線。

具體實踐參考 [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)、[《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps｜Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh) 與 [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company｜beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)。

## 開箱即用：工程研發提示詞庫

以下提示詞均經過生產實踐驗證。直接複製發給 Bot 並讓它記住；共享 Bot 寫入詳情 About：

### 1. 架構總控章程（Chief）
**發給主管 Bot 並讓它記住**（共享 Bot 寫入詳情 About），用來把控流程和記錄狀態。

::: details 1. 架構總控章程（Chief）
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

### 2. 缺陷復現專員（Triage）

直接**貼進 Triage Bot**，用來挖缺陷、寫失敗使用案例。

::: details 2. 缺陷復現專員（Triage）
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

### 3. 寫程式專員（Builder）
把提示詞貼進 **Builder Bot**，在隔離分支跑。

::: details 3. 寫程式專員（Builder）
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

### 4. 獨立審查專員（Reviewer）
提示詞粘進 Reviewer Bot，**嚴格驗收**。

::: details 4. 獨立審查專員（Reviewer）
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

### 5. 交付專員（Release）
**把提示詞貼進 Release Bot**，用來彙總產物並交付：

::: details 5. 交付專員（Release）
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

### 6. 夜間值守例行任務（Engineering Night Shift Routine）

在 Grok Bot 裡配定時任務，**執行主體選 Chief**。

::: details 6. 夜間值守例行任務（Engineering Night Shift Routine）
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

### 7. 可逆性人閘與安全紅線指令

**直接貼到各 Bot 的長期規則末尾**（個人 Bot 發在對話裡讓它記住，共享 Bot 寫在詳情 About）。

::: details 7. 可逆性人閘與安全紅線指令
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

## 容易踩的坑

### 模型自動匹配
後台會自動匹配 Claude Opus 5.5 等底層模型，無法手動挑。**把流轉條件寫進 `status.json` 等結構化文件，靠硬指令碼校驗**，別指望模型輸出風格一直穩定。

### 共享環境衝突
所有 Bot 共用雲端電腦的 `/workspace`。**每個 Issue 必須用獨立子目錄與 Git 分支**，改程式碼派生 Cursor cloud agent，嚴禁混用未提交的工作樹。

### 審查死循環與篡改測試
Builder 修復失敗容易死循環，甚至會改測試判斷提示騙綠燈。**單個 Issue 重試嚴格限制在 2 輪以內**，超限立刻轉人工。Reviewer 必須比對測試案例的 Git Diff，改動判斷提示直接判 FAIL。

### 訂閱額度與輪詢
用量按 2026 年 10 月 12 日生效的 The X Subscription 執行，和 Grok、Cursor 共享周用量池，超額走 Cursor 計費。

別搞 5 分鐘全量掃描，**定時任務設成每天或夜間 1 次**，觸發儘量靠 `agent-ready` 標記。

| 訂閱方案 | 月費價格 | 額度倍數 | 是否包含 Grok Bot |
| :--- | :--- | :--- | :--- |
| **Plus** | - | - | 不含 Bot |
| **Premium** | $30 / 月 | 4x 額度 | 包含 |
| **Super** | $100 / 月 | 15x 額度 | 包含 |
| **Ultra** | $200 / 月 | 50x 額度 | 包含 |

### 分支保護與 Draft PR
**Agent 產物只做 Draft PR，嚴禁自動合入主分支**。GitHub 的 Branch Protection Rules 必須卡死三條硬性約束：
- 禁止直接 Push 到 main 或 master 分支
- 至少一人人工審批（Approvals）
- 必須跑通原有 CI 流水線

### 敏感憑據防洩漏
對話內容會進模型上下文，**嚴禁在提示詞裡輸入密碼、私鑰或 API 密鑰**。訪問私有系統走設定裡的連線器，或者用 Agent Computer 的 Take Control 遠端桌面手工登錄。

## 做完怎麼驗收

**切忌一上來就在生產核心項目全面鋪開**。

### 單倉庫單 Bug 冷啟動驗收
- 挑邊緣庫建 `/workspace/devdesk/`，選小 Bug 打上 `agent-ready`。
- 跑 Chief 流程，核驗 Triage 在 `evidence/` 下存好復現記錄與單測。
- Builder 在獨立分支改且不碰主幹程式碼，Reviewer 給出行號與邏輯核對。
- **確認最終只提 Draft PR**，主分支無任何變更。

### 指標量化與補丁採納率檢驗
- 採納率**低於 70% 暫停接入第二倉庫**，收緊提示詞約束。
- 晨報須在 **3 分鐘內**看清合格 PR、攔截與待定項，翻看幾千字對話算未達標。
- 凌晨定時任務無觸發休眠，超時自動中斷，避免額度暴擊。

### 安全紅線與權限攔截實操演練
- 故意提修改表結構（Migration）或認證邏輯的 Issue，確認任務被攔截掛起。
- 讓 Bot 執行 `git push origin main`，**分支保護必須成功攔截**。
- 涉及外部通信與組態變更，確認 Auto-review 開啟 **Ask first**。

## 延伸閱讀

### 官方文件與功能頁面
- [Grok Bot 官方使用指南](https://cursor.com/cn/docs/grok-bot/work)
- [雲端電腦與應用連線](https://cursor.com/cn/docs/grok-bot/computers)
- [模型選擇與路由說明](https://cursor.com/cn/help/grok-bot/models)
- [方案、計費與按需用量幫助](https://cursor.com/cn/help/grok-bot/plans)
- [設定與安全規範](https://cursor.com/cn/docs/grok-bot/settings)
- [團隊協作與 Team Bots 組態](https://cursor.com/cn/docs/grok-bot/teams)

### 社群實戰案例原文

> 來源：[Grok Bot for Engineering](https://x.com/lingxi/status/2094493172516966781)  
> 作者：[Lingxi Li @lingxi](https://x.com/lingxi)

![Grok Bot for Engineering](/cases-img/fs50-0.jpg)

![Grok Bot for Engineering](/cases-img/fs50-1.jpg)
- [《工程師如何用好 Grok bot?｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering｜Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)
- [《一天幾百個 PR 有什麼意義？我照著 SpaceXAI 工程師 Lauren（@poteto）的九類清單，把自己的活拆了一遍》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)
- [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)｜Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)
- [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)
- [《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps｜Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)
- [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company｜beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)

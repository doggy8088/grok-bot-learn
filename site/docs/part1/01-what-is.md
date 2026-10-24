# 第 1 章 Grok Bot 是什麼：一個自帶電腦的 AI 同事

傳統網頁對話無法積累資產，**合上電腦任務直接中斷**。面對跨軟體呼叫與持續巡檢，人依然被拴在電腦前機械點選。

本章包含四項核心內容。
- 它的執行機制與共享雲端電腦的物理邊界；
- 適合與不適合承接的任務型別；
- 它與市面上其他常駐 Agent 的選型差異；
- **寫出符合規範的崗位說明，並設立防止越權的人工審批閘門**。


![Grok Bot 是什麼：一個自帶電腦的 AI 同事](/info/01-what-is.png)

## Grok Bot 的底層執行機制是什麼？ {#產品機制-環境底座與思考模型拆分}

**Grok Bot 核心是將常駐雲端的 Linux 底座與按需排程的思考模型拆分，配有終端、瀏覽器和持久文件，即便電腦關機合蓋，後台任務照樣能在雲端電腦中繼續執行。**

![產品機制：環境底座與思考模型拆分](/info/01-what-is-s1.png)

xAI 與 Cursor 在 2026 年 8 月 11 日推出 Grok Bot，**核心是把環境底座與思考模型拆分**。

- **底座（Harness）**：常駐雲端，配有 Linux 終端、瀏覽器和持久文件。關機合蓋，後台任務照常跑。
- **模型（Brain）**：按需排程。2026 年 10 月 7 日預設切為 Claude Opus 5.5，可派生 Cursor Agent 協同寫程式。

| 工具 | 執行環境 | 離線與協作 |
| --- | --- | --- |
| 聊天助手 | 臨時網頁 | 關網頁即斷，單次對話 |
| 命令列 Agent | 本地終端 | 退出即停，限本地倉庫 |
| Grok Bot | 持久雲端電腦 | **關機仍執行**，跨任務文件交接 |

機制參考 [《1.1 Grok Bot 是什麼：一頁看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)。

## Grok Bot 共享雲端電腦如何隔離與接管？ {#共享雲端電腦的物理邊界與接管機制}

**同帳號所有 Bot 共用雲端電腦且無法隔離路徑與 Cookie，跨任務交接需在 /workspace 存文件，遇輸密碼或付款等操作可點選 Take over 手動接管。**

![共享雲端電腦的物理邊界與接管機制](/info/01-what-is-s2.png)

同帳號所有 Bot 共用雲端電腦。Heavy 檔實測至強 8 核 8 執行緒、16GB 記憶體、128GB 硬碟（未核，官方為準），v0.68.1 分辨率升到 1920×1200。

規範見 [Grok Bot 電腦和應用文件](https://cursor.com/cn/docs/grok-bot/work#the-computer-and-apps)。

- 新建 Bot **無法隔離權限**。共用路徑和登錄態，都能讀 Cookie。
- 跨 Bot 協同依賴文件落盤。私聊天然隔離，交接要在 `/workspace` 存文件。
- 輸密碼、兩步驗證或付款點 Take over 處理，**切勿在聊天框發明文密碼**。
- 控制本地須單獨授權。與本地隔離，去 Settings → General → Agent → Execution on Local Computer 開啟，執行時彈窗確認。

## Grok Bot 適合與不適合做哪些任務？ {#適合與不適合的任務型別}

**Grok Bot 適合流程固定、高頻重複且需跨工具呼叫的任務，例如情報巡檢與缺陷復現，但不適合即時問答、本地寫碼及無人工閘門的高危操作。**

![適合與不適合的任務型別](/info/01-what-is-s3.png)

### 任務過濾標準
**任務該不該交給 Grok Bot，直接看三條過濾標準。**
- 能在網頁端、終端或通過 API 完整跑通；
- 中間文件或最終報告能由人工直接核驗；
- 高危敏感動作能停下來等人工彈窗批准。

### 適合的任務
**適合流程固定、高頻重複且需跨工具呼叫的活。**
- 情報巡檢：定期訪問固定官網出摘要表。
- 線索清洗：CRM 撈目標帳戶，結合公開資訊起草外聯信供審核。
- 財務對帳：每週核對發票，標記缺票並催收。
- 缺陷復現：讀 Issue 在預發表環境復現，提取記錄與截圖。
- 經營晨報：每天彙總庫存指標，揪出例外點。

### 不適合的任務
**別硬塞不匹配的活，容易白耗每週額度甚至失控。**
- 即時問答：查報錯用普通網頁模型幾秒搞定，不用雲端電腦。
- 本地寫碼：中斷點除錯與 Git 衝突放本地 Codex CLI 或 Claude Code。
- 生活瑣事：管日曆缺乏企業級資料源，硬搬很彆扭。
- 無增量輪詢：每 5 分鐘無條件重新整理會空耗推理額度。
- 高危操作：群發郵件與刪庫必須留人工閘門。

規劃方法參考 [《1.2 Grok Bot 和 Muse、Hermes、dots、Cue 怎麼選》](https://jcng5q8n0f3z.feishu.cn/wiki/BnH9wLTmyiQZ03kJhsecOrffnAd)。

## 選型對照：Grok Bot 與主流常駐 Agent 橫向對比

### 整機與組裝機形態

選常駐 Agent 主要看圖省心還是愛折騰。**開箱即用的整機**（Grok Bot、Muse）免去部署煩惱，但受平台額度限制；組裝機（Hermes）接開源模型無額度約束，但環境報錯得自己修。

### 主流常駐 Agent 特性與選型對照

| 產品 | 底座與門檻 | 特點與適用場景 |
| --- | --- | --- |
| Grok Bot | 共享 Linux 雲端電腦。2026-10-12 起執行 The X Subscription 統一方案（Premium $30/月、Super $100/月、Ultra $200/月），**Plus 檔不含 Bot**；客戶端 v0.70.2 支援獨立郵箱與連線卡片 | 7×24 小時常駐，支援例程與技能，多 Bot 非同步交接文件並調 X 平台檢索。適合免運維、多崗位協同與巡檢對帳 |
| OpenAI dots | 個人常駐雲端電腦，ChatGPT Pro 檔包含 | 基於 GPT-6 Astra（2026-09-30 發表），常駐後台連 4000 多個外掛，主打日常伴隨與輕量代辦 |
| Manus Cue | 獨立雲端電腦，處於早期體驗階段 | 2026-09-29 鐵柱上手體驗；原生配獨立協同郵箱、電話與錢包，自主跑腿註冊與採購，自主權極高且伴隨操作風險 |
| Meta Muse | Meta 託管雲端代理，諾鴨船長評測偏家庭生態 | 深度綁定 Meta 社交網路與硬體，適合家庭日常與社交輔助 |
| Hermes | 本地或私有伺服器，開源自建 | 自由更換開源模型，無商業額度限制。適合本地敏感資料流水線，**需自己動手配環境與排錯** |

詳細推文對比參考 [《鐵柱推文合集④：社群、生態與競品對照》](https://jcng5q8n0f3z.feishu.cn/wiki/RMRTwk3MqiUqEwk0TzTchA4LnDg)。

## 典型實戰案例拆解

### 金塵馬的情報總監（個人調研崗位）

金塵馬（@jinchenma_ai）在 Edit Profile 的 Description 寫明長期崗位規則，定性為情報調研員。派單落實結果與來源、限制與格式及確認點五要素，檢索 X 平台長文並區分影片帖，標明曝光資料，**無一手資料嚴禁編造**。

首次糾偏格式後，指令 Bot 把流程沉澱為 Skill「AI 課程情報蒐集」。

換第二組輸入測通後組態 Routine，定在每個工作日早上 8:10 自動執行彙報；新建「內容總監」評審選題，初稿存入 `/workspace/grokbot-demo/`。

**崗位說明沉澱長期規則，臨時需求走訊息**，多 Bot 經 `/workspace` 落盤解耦。

細節見[《萬字長文｜Grok Bot 從入門到精通｜金塵馬》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)。

### 金塵馬的電商運營團隊（多角色分工流水線）

團隊由 4 個 Bot 協同。先建「店鋪經營值班員」讀商品表、庫存表與訂單表發晨報，**卡死唯讀紅線，嚴禁改價改庫存，也不得發信或退款**。

原值班員升級為「電商運營主管」，拆出內容增長專員、商品庫存分析員與訂單售後助理，資料存入 `/workspace/ecommerce-ops/日期/`。遇爆款僅剩 3 天庫存，內容專員暫停推廣，售後助理備好延期話術，主管彙總決策清單。

不要起手搭建龐大團隊，**涉及資金、庫存與外部發信的操作全部鎖定人工審批**。

### 鐵柱的開源倉庫管理員 Bot（自動化運維巡檢）

鐵柱AGI（@cgnot996）建常駐 Bot 維護 awesome-grok-bot 知識庫。系統定期巡檢 X 平台推文、官方更新記錄與技術社群，將新玩法、課程、官方文件和活動分類收錄。

宣發前已自動收錄相關資料，**2026 年 8 月突破 130+ Star（作者自述，未核）**，並獲官方人員申請表單邀請。

## 新手上路：從開通到第一個專職 Bot

![新手上路：從開通到第一個專職 Bot](/info/01-what-is-s6.png)

### 確認訂閱檔位與安裝客戶端

按 2026 年 10 月 12 日起執行的 The X Subscription 統一方案選檔：
- **Premium 檔**：$30/月（年付 $300），4x 額度池，個人日常起步選這檔。
- **Super 檔**：$100/月（年付 $1000），15x 額度池，適合重度研究與多例程。
- **Ultra 檔**：$200/月（年付 $2000），50x 額度池，適合高頻團隊主力。
- **$8/月（年付 $80）的 Plus 檔不含 Bot 功能**，千萬別選錯。已有 Cursor 付費個人版或團隊版、SuperGrok 訂閱或 Grok Business 席位也能直接用。

  桌面端支援 macOS、Windows、Linux，行動裝置端支援 iPhone，裝好後登入帳號。

### 建立 Bot 並派發測試任務

1. 側邊欄點 New → Create new agent，起名「競品情報員」。打開 Edit Profile，在 Description 填入標準六行工作合同。
```text
Own: 負責監控目標清單的每週功能更新與定價變動
Sources: Notion 中的關注名單、目標官網 Changelog 頁面
Output: 不超過 8 條核心動態，附帶日期與原始連結，存入 /workspace/scan.md
Approval: 嚴禁對外發表任何內容，嚴禁主動發送任何郵件
Failure: 若目標頁面無法打開，在報告中明確標為資料缺失，嚴禁推測或編造內容
Never: 在源系統可訪問時，嚴禁依賴自身記憶給出概括
```
2. 在對話框下發測試指令，寫明目標、來源、限制、格式及確認點五要素。
```text
調研所附競品清單中的前 3 個產品官網。
比對它們過去兩週內的功能更新與價格調整。
跳過無任何變動的模組。
提取核心變動點，整理成 Markdown 表格，並直接保存到 /workspace/scan.md。
在對話框中僅回覆處理狀態與保存路徑；不要對外發送任何通知，不要擅自更改系統設定。
```
3. **觀察右側雲端電腦窗口**。Bot 會自動喚起雲端瀏覽器提取頁面，並把內容寫入指定文件。

### 組態安全審批與定時例程

1. 進 Settings → General → Auto-review，**高危操作必須全部開啟 Ask first**。

   卡死發信（`send`）、發文（`post`）、扣費（`buy`）、刪文件（`delete`，含 `/workspace` 或本地文件）與改權限（`permissions`），觸發後會彈卡片暫停，等你人工點批准。
2. 抓取任務連續兩次執行穩定後，在對話框發送沉澱指令。
```text
把剛才已經跑通的競品頁面抓取與格式整理流程保存為一個 Skill，名稱叫「競品動態巡檢」。
寫清呼叫條件、所需權限、抓取步驟、例外報錯邏輯與產出文件格式。
```
3. 換個競品網址，輸入 `/` 調這個 Skill 測試。確認無誤後**組態 Routine 定時**，設在每週一早晨 9:00 自動執行，結果彙報發在當前對話，詳細報告存入 `/workspace`。

## 容易踩的坑

### 架構與安全

- 看到社群 29 個 Bot 架構（Melvin Vivas 自述，未核）別跟風，同質化 Bot 易亂且費額度。**一個崗位沒跑順前，不要建第二個**。
- 所有 Bot 共享雲端電腦與檔案系統，爬蟲能讀 `/workspace` 和 Cookie。**安全控制只能靠 Ask first 人工審批閘門**。
- 別在聊天框發帳號密碼。遇到登錄介面，**調出右側螢幕點 Take over 按鈕由人工登錄**。

### 資源與預期

- 每月 $8 的 Plus 檔沒有 Bot 入口，**必須認準每月 $30 起步的 Premium 檔**。
- Routine 設 5 或 10 分鐘輪詢會掏空每週額度池。**要拉長定時任務間隔，並加未更新即退出邏輯**。
- 別輕信 Alex Finn 盈利或 0xkvro 降本神話（自述，未核），**業務以實際跑通的指標為準**。

## 做完怎麼驗收

1. 側邊欄點 Bot 進聊天，發訊息展開 **1920×1200 實時桌面**；去 Usage & Billing 確認方案是 Premium、Super 或 Ultra，進度條正常。
2. Edit Profile 的 Description 須寫齊職責、資料源、產出物、審批紅線與缺數兜底（**六行硬約束**）。發死鏈測它，**必須如實報缺**，不瞎編資料。
3. Settings → General → Auto-review 裡，把 `send`、`post`、`buy`、`delete`、`permissions` 設為 Ask first。測發信或刪文件，**必須彈審批卡片等人工確認**。
4. Routine 右鍵 Test run 跑通後合蓋關軟體。到點重開看提醒，進雲端電腦 `/workspace`，**確認 Markdown 或 CSV 按最新時間戳記更新**。

## 延伸閱讀

### 相關章節

- [第 5 章 共享雲端電腦：文件、瀏覽器與接管](/part1/05-computer)
- [第 6 章 記憶：讓 Bot 越用越懂你](/part1/06-memory)
- [第 7 章 連線應用：外掛、郵箱與 Secrets](/part1/07-apps)
- [第 11 章 權限、安全與人閘](/part1/11-safety)
- [Grok 和 Grok Bot 有什麼區別](/part1/grok-vs-grok-bot)
- [第 2 章 方案與訂閱：先選對檔位](/part1/02-plans)

### 官方頁面與文件

- [Grok Bot 快速入門指南](https://cursor.com/cn/docs/grok-bot/get-started)
- [使用 Grok Bot：電腦、應用與任務](https://cursor.com/cn/docs/grok-bot/work)
- [Grok Bot 使用場景與典型角色](https://cursor.com/cn/docs/grok-bot/use-cases)
- [面向團隊版和企業版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)
- [Grok Bot 方案與計費說明](https://cursor.com/cn/help/grok-bot/plans)
- [團隊 Bot 使用規範](https://cursor.com/cn/help/grok-bot/team-bots)
- [Grok Bot 安全架構與 Auto-review 規則](https://cursor.com/cn/docs/grok-bot/security)

### 社群實戰與橫向對比

- [《1.1 Grok Bot 是什麼：一頁看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [《1.2 Grok Bot 和 Muse、Hermes、dots、Cue 怎麼選》](https://jcng5q8n0f3z.feishu.cn/wiki/BnH9wLTmyiQZ03kJhsecOrffnAd)
- [《鐵柱推文合集④：社群、生態與競品對照》](https://jcng5q8n0f3z.feishu.cn/wiki/RMRTwk3MqiUqEwk0TzTchA4LnDg)
- [《萬字長文｜Grok Bot 從入門到精通｜金塵馬》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)

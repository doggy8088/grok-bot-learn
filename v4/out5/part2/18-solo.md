# 第 18 章 案例：一人公司與 AI 團隊

**同一帳號下的所有 Bot 共享同一台雲端電腦**，自帶瀏覽器、檔案系統與終端。

一口氣新建十幾個 Bot 並交出全部帳號，容易踩坑。
- 外部網頁走錯路徑、靜默覆蓋資料
- 半夜頻繁觸發審批，讓人疲於審核

理順崗位邊界、憑據隔離與審批紅線，就能**從組態首個 AI 員工演進到管理 29 個 Agent**。

## 第一個 AI 員工：像招聘一樣定義崗位與權限

把 Bot 當作工具還是員工，取決於你是在寫單次提示詞，還是在確立崗位職責。單次提示詞只管眼前的一項交易，窗口一關上下文就消失。崗位職責是一份固定的檔案文件，它決定了這個 Bot 每天處理交易時的行為底線與思考模式。

### 崗位定義與准入測試

**先別給不可逆權限**，從枯燥、高頻且易撤銷的雜事切入。

讓 Bot 上手前，先跑兩項准入測試提前排錯。
1. **一句話職責測試**：一句講清交付什麼。塞入四五個無關動詞等於一人幹三人活，出錯沒法定位根因。
2. **純文字推演（Trial in text）**：耗時不到兩分鐘，先彙報步驟、預訪網址與存疑判斷。

崗位描述拆成五個欄位劃清邊界。
- Owns：交付固定產物。
- Inputs：允許讀取的渠道。
- May：可自理的操作。
- Must ask before：花錢或改組態等高危動作，**必須等人工審批**。
- Done when：客觀核對的驗收清單。

```text
先不要執行任何實際操作。請逐步向我推演你的完整執行方案：
1. 列出你準備依次打開的工具、網址與呼叫的外掛。
2. 列出你在過程中需要做出的業務判斷。
3. 標出你目前資訊不足、存在疑慮或拿不準的決策點。
推演完畢後等待我的指令，嚴禁自行操作。
```

::: details 崗位定義與准入測試
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

崗位設定與臨時提示詞完全不同。

| 維度 | 臨時提示詞 | 崗位設定 |
|---|---|---|
| **目標與形態** | 單次對話，關注單次動作 | 長期組態，交付業務產物 |
| **邊界與權限** | 口頭交代易越權，出錯重跑 | 可逆自理，不可逆等審批，硬設人閘 |

### 三次執行試用期與晉升階梯

> 來源：[Grok Bot: How to Hire Your First AI Employee (Full Guide)](https://x.com/distortgeekin/status/2105275395901726845)  
> 作者：[distort @distortgeekin](https://x.com/distortgeekin)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-0.png)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-1.jpg)

新 Bot 剛跑通，**千萬別直接放後台無人值守**，先按 distort 的「三次執行法則」測試。

1. 第 1 次（全程旁觀）：盯著螢幕看每步操作，記下誤讀指令、丟上下文和瞎猜的地方。
2. 第 2 次（修復規則）：換同難度任務，不提醒舊錯。重點看崗位規則與權限改動是否生效，不替它改結果。
3. 第 3 次（放手實測）：全程不插手，只在審批或達到重試上限時介入，核驗完成度、干預次數、耗時與額度。

**通過三次測試後進入晉升階梯**，分五級權限。

| 級別 | 機制 | 邊界 |
| :--- | :--- | :--- |
| Level 0 | 僅觀察 | 不改任何資料 |
| Level 1 | 僅準備 | 搜尋、摘要與排版等可逆工作 |
| Level 2 | 人工審批 | 關鍵步驟掛起等待確認 |
| Level 3 | 獨立執行 | 定時或觸發執行，定期產出證據鏈彙報 |
| Level 4 | 多 Bot 協同 | 擔任分發與質檢節點 |

升到下一級必須滿足四項**硬性指標**。
- 連續 5 次實跑無瑕疵
- 驗證步驟全通過
- 無未解決的副作用
- 回滾機制驗證可用

實踐參考 [《Grok Bot: How to Hire Your First AI Employee (Full Guide)｜distort》](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc) 與 [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)。

## 從零到運轉的公司：幕僚長與專職團隊編排

一個人使用 Grok Bot 搭建完整業務運轉體系時，最容易走入的死衚衕就是給單個 Bot 堆積太多能力。一個既管銷售線索、又管內容寫作、還管對帳和改程式碼的 Bot，其上下文窗口很快會被大量不相干的偏好填滿，不僅容易混淆業務語境，還會加速額度損耗。

### 幕僚長架構與部門拆分

搭團隊先建幕僚長 Bot。你日常**只跟幕僚長對接**，由它拆解任務、排程專職崗位並彙總交付。

::: details 幕僚長架構與部門拆分
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

- 調研 Bot：論斷須注日期與網址，存疑主動標出，不強行編造。
- 內容 Bot：按模版排版，**嚴禁直接對外發表**。
- 銷售 Bot：拜訪郵件全存草稿箱，等人工核准再發。
- 技術 Bot：提 GitHub PR 必附測試通過截圖。
- 財務 Bot：涉及資金調整必須單獨列出待確認。

::: details 幕僚長架構與部門拆分
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

| 架構 | 單兵全能 | 幕僚長流水線 |
|---|---|---|
| 協作 | 記憶混雜難定位 | **各崗獨立記憶**，精準定責 |

### 證據鏈審查與四周信任轉移

> 來源：[From Zero to a Running Company: The Grok Bot Agent Team Playbook](https://x.com/N01ennn/status/2091534159088959967)  
> 作者：[NO1ennn @N01ennn](https://x.com/N01ennn)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-0.jpg)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-1.jpg)

**想放心合上電腦，前提是看到憑證（Show the tape）。** Bot 交付必須帶齊三項憑據。

- 操作螢幕錄影或呼叫記錄：展示完整網頁軌跡或工具呼叫序列。
- 資料與數位的原始出處：禁止無來源引用。
- 報錯跳過項與推測結論說明。

**信任分四周逐步轉移。**

1. 第 1 周（草稿階段）：Bot 僅起草，人工通讀並手動執行。
2. 第 2 周（審批階段）：Bot 跑到關鍵步停下，人工僅核對動作並審批。
3. 第 3 周（例外上報階段）：低風險交易自主跑，遇例外或越權才彈窗求助。
4. 第 4 周（例程巡檢階段）：按例程完全自主執行，週末只看審計報告。

相關實踐參考 [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd) 與 [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)。

## 一人公司實戰：單台雲端電腦的邊界與獨立運營

### 物理邊界

**同帳戶所有 Bot 共享單台電腦**，共用目錄與會話。官方明確別把 Bot 當隔離邊界，Prompt 防不住注入，誤跑命令會洩露 Cookie 與 Session。

平時守住三條。
- 不登主網銀和核心倉庫，不存機密網盤。
- 外部平台只用最小權限子帳號。
- 外部登錄走 Handoff，人工輸密碼，Bot 只繼承 Session。

### 無 API 系統自動化

**無 API 系統靠電腦能力點選填表**，四類工作適合先交接。
- 獲客調研：掃社群目錄並起草郵件。
- 履約跟進：核對缺貨並跟進延誤運單。
- 內容排期：文案填進草稿箱。
- 程式碼維護：排查獨立站報錯並出補丁。

::: details 無 API 系統自動化
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

### 門檻與評分

> 來源：[One-Computer Company: A Real Playbook For Running Solo On Grok Bot](https://x.com/zerqfer/status/2093299037705236540)  
> 作者：[ZER @zerqfer](https://x.com/zerqfer)

**人工審查穩定降至每天 15 分鐘內**才能加新 Bot，避免放大負擔。每月填一次評分卡防靜默衰退。

::: details 門檻與評分
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

參考 [《One-Computer Company: A Real Playbook For Running Solo On Grok Bot｜ZER》](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)。

## AI Agency 交付體系：月交付流水線與質檢人閘

對於面向多客戶交付的 AI 代理機構（AI Agency），核心難點在於多客戶平行處理時的質量穩定與額度成本控制。

社群作者 maestro 分享了單人服務 5 家 Retainer 客戶、實作月度業務運轉的體系架構（社群作者 maestro 自述月營 1.8 萬美元、服務 5 家客戶，未核）。

### 業務選單的「三項准入測試」

別接全客製化淪為手工外包，**業務進自動交付選單得過三關**。

1. Brief 能寫成結構化清單。
2. 交付物有第三方客觀驗收標準。
3. **此前純手工交付至少 10 次**。沒做滿 10 次摸不清紅線，交給智慧體只會產出廢話。

達標業務包含 500K 上下文比對 40 篇資料做研報、按聲音樣本（Voice File）批量寫稿，或搭建看板與輕量抓取工具。

### 模型路由與 19.5 萬 Token 計費懸崖攔截

模型按活分配，別全上旗艦。
- Grok 4.1 Fast：2M 上下文，跑清洗初篩。
- Grok Build 0.1：負責 80% 開發物料。
- Grok 4.6：500K，跑長程 Agent 與推理。

**輸入超 200,000 Token 費率直接翻倍**。網關要**硬寫程式 195,000 Token 閾值**，超限報錯截斷或剪枝。

### 獨立唯讀審核者與三次重試人閘

> 來源：[How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](https://x.com/maestrooth/status/2092658066714177657)  
> 作者：[maestro @maestrooth](https://x.com/maestrooth)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-0.png)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-1.png)

生產 Bot 審自己的產物會有自洽傾向，容易掩蓋提示詞失效。**審核必須切成獨立的唯讀迴路**。

- 獨立上下文：只輸入原始 Brief、客戶規範和產物，不給中間推理。
- 嚴格唯讀：**發現缺陷只報 FAIL 絕不代筆**，防止私自修補掩蓋問題。
- 對抗挑刺：專抓罩門，沒有資料支援的數位一律判掛。

::: details 獨立唯讀審核者與三次重試人閘
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

**交接重試最多 3 次**，防止死循環刷出高額 Token 帳單。機器試了三次仍不達標，說明需求衝突，必須由人工介入判定。

參考 [《How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)。

## 29 個 Agent 的實戰：如何從單兵平滑擴編到軍團

當你熟悉了單個員工的組態與雙 Bot 的質檢閉環，業務需求自然會推動你擴建團隊。

社群作者 Melvin Vivas 記錄了自己如何一步步將 Grok Bot 擴充至 29 個專職智慧體的完整實踐（社群作者 Melvin Vivas 自述擁有 29 個 Bot，未核）。

### 29 個 Agent 的職能佈局與漸進演進

**這 29 個 Bot 全是按需長出來的**：平時遇到重複交易就建專職角色，角色多了再由幕僚長 Emma 統管。業務分為七大板塊：

- 排程中樞：Emma 負責統管全域與分發任務。
- 技術研發：CTO 管架構；**Coder 調動 Cursor 自動編寫程式碼提 PR 並修復報錯**，全程不用開本地編輯器。
- 前沿調研：全天掃描 X 平台開源動態並出簡報。
- 內容矩陣：負責各渠道文案創作與覆盤。
- 商務拓展：挖掘商機與合作線索。
- 運營安全：負責郵件、備份與安全審查。
- 個人成長：處理打卡、行情追蹤與決策論證。

### 多 Agent 協同流水線：以技術原型到內容轉換為例

各 Bot 靠共享雲端電腦和會話引用接力。

::: details 多 Agent 協同流水線：以技術原型到內容轉換為例
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

**改動不用挨個點開 29 個窗口**，總管廣播一條指令幾秒就能同步。

### 角色拆分的五大信號與自動化七步法

考核目標、呼叫工具、工作風格、審批邊界（草稿與對外溝通絕不能混）或排程週期不同時，必須**拆分獨立 Bot**。

1. Bot Description 寫清目標、資料源、格式與停機邊界。
2. 挑受控真實任務單次執行。
3. 人工調優到免檢。
4. 沉澱為複用 Skill。
5. 換新資料複測泛化。
6. **定好重試上限與缺失報警，才開 Routine**。
7. 發信、付款或改動，強綁 Require Approval 人閘。

| 階段 | 規模 | 架構與瓶頸 |
| :-- | :-- | :-- |
| 1 單兵 | 1 Bot | 全量人閘驗證閉環；需時刻盯盤 |
| 2 小組 | 2-3 Bot | 生產與審核分離；日維護壓進 15 分鐘 |
| 3 幕僚長 | 4-6 Bot | 分發與看板；**杜絕幕僚長幹雜活** |
| 4 軍團 | 10-30 Bot | 多線 standup；定期修剪無效例程 |

### 看板系統與晨會機制

> 來源：[How I use Grok Bot: My team of 29 AI agents](https://x.com/melvindvivas/status/2109480575421808962)  
> 作者：[Melvin Vivas @melvindvivas](https://x.com/melvindvivas)

Bot 超過 5 個就別用多聊天視窗了，根本看不過來。**多 Bot 協同主要靠看板和定時巡檢兩件事**：

- **共享狀態看板**：任務別散在聊天記錄裡，統一收攏到 Notion 或資料庫看板，定好五種狀態：`Todo`、`Working`、`Blocked`、`Ready for Review`、`Done`。Bot 遇到未知報錯或缺權限直接改標 `Blocked` 並呼叫人工，平時看卡片流轉就行。
- **定時巡檢與對帳**：單 Bot 最多配 50 個 Routine，最高每 5 分鐘跑一次。**凌晨 3:00 自動體檢程式碼死鏈與包體積，5:00 由總管 Bot（如 Jenny）逐個核對專職 Bot 的 Playbook**，能有效防止模型久了遺忘。

```text
全體專職 Bot，開始進行本週團隊回顧審計。請各崗位彙報：
1. 本週你實際執行了多少次任務，其中失敗或例外的中斷有多少次？
2. 在執行過程中，有哪些步驟存在推測行為、跳過行為或由於資料缺失強行拼湊的情況？
3. 有哪些掛起的審批事項我一直沒有回應？有哪些生成的物料我從來沒有打開查看過？
4. 請指出：在當前的工作流中，你發現哪兩個 Bot 存在職責重疊或重複工作？
5. 給出客觀建議：為了節省整體用量額度，我們下週最應該裁撤哪一個無效的 Routine 或崗位？
```

相關實踐參考 [《How I use Grok Bot: My team of 29 AI agents》](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)、[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54) 與 [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)。

## 容易踩的坑

### 權限與審批
1. 共享雲端電腦共用 Session 無隔離，**絕不要登錄主帳戶和敏感系統**。
2. Require Approval 只能攔未執行操作，無法撤銷破壞，**高危動作首次就設死人閘**。
3. 審批約 10 分鐘不理會失效（Lapse），夜間**必須配 Allow rule 白名單或停在草稿**。

### 成本與架構
4. 輸入超 20 萬（200,000）Token 單價翻倍：**路由層要設 195,000 Token 硬攔截與剪枝**。
5. 別搞單 Bot 攬全活或複製 5 個通用 Bot，**分工不清只會汙染上下文並浪費額度**。
6. 別設 5 分鐘輪詢或監聽全訊息，**缺 No-data policy 時斷網容易瞎編資料耗盡額度**。

### 規則與交接
7. 聊天框叮囑重新整理就失效，**跨任務紀律必須寫在設定介面的 Description**。
8. 跨 Bot 別搬運全部記錄，**交接包只留目標與交付物路徑，加上結論和下一步要求**。

## 做完怎麼驗收

1. **查憑據**：清掉 Plugins 和瀏覽器的銀行與主憑據，改用子帳號或 Session，**聊天記錄絕不存明文密碼**。
2. **驗崗位**：Bot 須包含 Owns/Inputs/May/Must ask before/Done when，末尾加反漂移宣告，**缺資料立即報錯、嚴禁編造**。
3. **測人閘**：發扣款或刪除指令，必須 **100% 觸發 Require Approval 掛起**。
4. **抗審核**：喂假資料草稿，質檢 Bot 須 **第一行返回 FAIL** 且不擅改；連續失敗 3 次停機報警。
5. **穩例程**：看板狀態實時流轉，開啟前點 Test run 跑通，**定時任務不依賴超 10 分鐘夜間審批**。

## 延伸閱讀

### 官方文件

- [在 Grok Bot 中組織業務與工作（docs_grok-bot_work.md）](https://cursor.com/cn/docs/grok-bot/work.md)
- [團隊版 Bot 協作與權限管理（docs_grok-bot_teams.md）](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Grok Bot 安全架構與執行環境（docs_grok-bot_security.md）](https://cursor.com/cn/docs/grok-bot/security.md)
- [方案、額度與計費說明（help_grok-bot_plans.md）](https://cursor.com/cn/help/grok-bot/plans.md)
- [組態定時任務與觸發例程（help_grok-bot_routines.md）](https://cursor.com/cn/help/grok-bot/routines.md)
- [連線外部應用與官方外掛（help_grok-bot_connect-plugins.md）](https://cursor.com/cn/help/grok-bot/connect-plugins.md)

### 社群實戰來源

> 來源：[GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](https://x.com/0xMovez/status/2100261918896169259)  
> 作者：[Movez @0xMovez](https://x.com/0xMovez)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-0.png)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-1.jpg)

- [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
- [《How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)
- [《One-Computer Company: A Real Playbook For Running Solo On Grok Bot｜ZER》](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- [《Grok Bot: How to Hire Your First AI Employee (Full Guide)｜distort》](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc)
- [《Grok Bot: How to Build Your First AI Team (Full Guide)》](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)
- [《How I use Grok Bot: My team of 29 AI agents》](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

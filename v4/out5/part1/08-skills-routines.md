# 第 8 章 技能與例程：把一次成功變成每天自動跑

別直接設定時。**脫離人工盯梢易卡死，還會半夜三點誤跑，空轉耗盡整週額度。**

把操作沉澱為技能（Skill），組裝成例程（Routine）：
1. 校準時區，規範 Webhook。
2. 限制 Slack 觸發範圍。
3. 加上虛擬機器兩段式檢測。

**設好邊界，合上電腦後台也能穩定交付。**

## 技能的沉澱與引用：固定你的標準作業程式

技能是保存在帳號裡的操作指令，**名下所有 Bot 都能直接呼叫**。

### 怎麼沉澱技能

**方式一：對話後文本總結**
任務跑通後先別關會話，直接讓當前 Bot 提煉保存。提示詞要明確輸入源、例外處理與越界限制，直接發送這段樣板。

::: details 怎麼沉澱技能
```text
請把我們剛剛完成的這套流程保存為名為“每日工單例外審查”的技能。
技能內容必須包含以下要素：
1. 適用場景：工作日審查支援渠道中滯留超過 4 小時的工單。
2. 輸入資料：從已連線的工單外掛中讀取狀態為 Open 且優先級為 High 的列表。
3. 決策規則：若工單包含退款申請且金額大於 500 元，標記為一級風險；其餘標記為二級跟進。
4. 交付格式：生成 Markdown 表格，列出工單編號、客戶標識、滯留時長、風險等級與跟進建議。
5. 例外處理：若工單系統介面無回應或無符合條件的資料，輸出明確說明，嚴禁使用歷史快取或偽造資料。
6. 安全邊界：未經人工明確批准，嚴禁直接呼叫介面回覆客戶或變更工單狀態。
```
:::

**方式二：示範教會（Teach task）**
介面操作複雜時，直接示範更省事。
1. 聊天視窗右側打開電腦預覽，選擇“教會任務”（Teach task）。
2. 簡述目標後在雲端電腦上操作。**系統最多錄 10 分鐘螢幕且不錄麥克風音訊，切勿輸入密碼等機密，敏感憑據走安全卡片**。
3. 自動生成草稿後，**必須補齊決策規則、報錯與審批邊界，切勿直接上線**。沒看到入口說明還在灰度，改用方式一。

### 如何引用與管理技能

- **輸入框引用**：輸入框輸入斜槓 `/` 即可選擇技能載入。
- **開啟權限**：列表中找不到時，去桌面側邊欄“連線應用”（Connected Apps）點已連數量，在“私有技能”裡打開開關。

### 做到什麼程度算合格

| 檢查項 | 不合格寫法 | 合格寫法 |
| :--- | :--- | :--- |
| 輸入來源 | “分析一下最近的資料” | 明確指定外掛、API 端點、文件路徑或資料庫檢視 |
| 邊界控制 | “遇到問題看著辦” | 資料缺失立即中斷報錯，嚴禁編造資料 |
| 動作權限 | “幫我把報表發給客戶” | 生成草稿並在聊天停留，**等人工允許後再發送** |
| 輸出結構 | 自由發揮的大段文本 | 固定欄位列表、Markdown 表格或落盤路徑 |

出處：[《使用 Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)

## 例程的核心機制：設定、查看與測試

例程是掛在 Bot 名下的工作流觸發器，跑在雲端 Linux 的 `/workspace` 目錄。**就算合上電腦或退出客戶端，雲端任務也會按計劃推進。**

### 規格與限制

- 每個 Bot 最多建立 50 個例程，系統保留最近 20 次執行記錄。
- 定時例程最短觸發間隔為 5 分鐘，不支援秒級排程。
- **刪除例程不可逆**，後續執行會永久終止；刪除 Bot 會連帶清空全部例程。

出處：[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 建立與管理例程

桌面端在聊天框發指令直接建立：

```text
每個工作日上午 8:30，呼叫“每日工單例外審查”技能，在此對話中輸出審查清單。如果未檢索到高風險工單，只發一行“今日無高風險工單”即可，不要刷屏。
```

桌面端管理：
1. 點選聊天視窗頂部的 Bot 名稱進入 Details，在例程（Routines）列表能看執行時期間或 Paused，右側開關隨時暫停（Pause）或恢復（Resume）。
2. 點選具體例程可查三項屬性：Instruction（執行提示詞）、When to run（計劃描述）與 Webhook（專屬 URL、密鑰與請求頭）。
3. 底部工具欄提供 Test、Edit 與紅色垃圾桶（Delete routine）。**點選 Edit 會在對話框預填 "Edit your routine: [例程名]"**，補上修改要求發送即可更新。

手機端管理：
1. 打開 Bot 資料頁找到例程，點選 Add routine 會預填 "Set up a routine to "，補齊指令發送即可建立。
2. 點選已有例程能查 Schedule、Next run 與 Instruction，也能看 Active 開關和執行歷史（Run history）。
3. **關閉 Active 開關即可暫停，向左滑動所在行可直接刪除。** 狀態與桌面端雙向實時同步。

出處：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)。

### 計劃排程與時區組態

時區檢查路徑：Settings -> Bot -> Timezone。

| 模式 | 執行機制 | 注意事項 |
| :--- | :--- | :--- |
| Auto-detect | 自動跟隨當前電腦時區 | 適合固定地點；跨國差旅容易導致執行時期間變動 |
| 手動指定時區 | 手動下拉選擇對應時區 | 面向特定區域（如北京時間 UTC+8 或美東 EST）建議手動指定 |

- **新建定時例程不會立刻首跑**，必須等待下一個計劃時間點。例如早上 8:05 設每天 8:00 執行，首次執行是在明早 8:00。
- **週末若需連續巡檢，指令中必須明確強調“包括週末在內每天執行”。** 未作特殊宣告時，Bot 預設按週一至週五執行。

出處：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)，[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 測試例程

在桌面端詳情頁點選底部的 Test 按鈕即可手動觸發，按鈕狀態會變為 Running…，執行回饋直接打在聊天視窗中。

**測試執行的是真實操作**，會啟動雲端電腦瀏覽器、改寫工作區文件並正常扣除額度，涉及刪改先用沙箱資料測試。**若提示 Couldn't start a test run，需要檢查雲端電腦連線狀態或是否有前序任務阻塞。**

出處：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)。

## Webhook 與 Slack 觸發器：從輪詢走向被動喚醒

定時輪詢外部網頁極費額度，高頻空轉會迅速耗盡整週算力。**改用事件驅動喚醒 Bot**，平時徹底休眠，外部有變化時再被動觸發。

2026-10-12 起，Grok Bot 納入 The X Subscription 體系，與 Grok、Cursor 共享額度池：

| 訂閱檔位 | 價格 | 用量倍數 | Bot 支援情況 |
| :--- | :--- | :--- | :--- |
| Premium | 每月 $30 或每年 $300 | 4 倍基礎用量 | 包含 Bot |
| Super | 每月 $100 或每年 $1000 | 15 倍用量 | 包含 Bot |
| Ultra | 每月 $200 或每年 $2000 | 50 倍用量 | 包含 Bot |
| Plus | - | - | 不包含 Bot |

### Webhook 組態與非同步驗收

在聊天視窗發送指令，可讓 Bot 建立 Webhook 觸發器。

```text
為當前 Bot 建立一個 Webhook 觸發的例程，命名為“外部知識接收端”。
指令內容：讀取請求體中的 JSON 資料，提取 url 和 note 欄位，將其抓取整理為 Markdown 存入 /workspace/notes 目錄。
```

在桌面端打開例程詳情，展開 Webhook 查看核心欄位：
1. POST to：接收外部請求的公網唯一 URL。
2. key：鑑權私鑰，呼叫時需在請求頭攜帶 `Authorization: Bearer <key>`。
3. header：拼接完整的請求頭文本，點選可直接複製。

**組態必須點選 Save 保存後才會在網關生效並生成密鑰。** 詳情頁若卡住點不開，讓 Bot 發送直達連結。[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)

外部系統通過 POST 請求推送資料，直接帶上 JSON 請求體。

```json
{
  "url": "https://example.com/article/1024",
  "source": "ios_share",
  "note": "精讀核心論點並歸檔"
}
```

Bot 會把 JSON 作為上下文變數，連同預設 Instruction 一同送入模型。[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

- **HTTP 200 僅代表網關成功接收請求並啟動執行，不代表任務執行成功。** 業務成敗需在聊天視窗或工作區落盤文件查看。
- 返回非 200 說明任務未建立，通常因例程處於暫停（Paused）狀態或密鑰失效。[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

### Slack 觸發器與防爆額度

Slack 外掛是隨對話實時呼叫的讀寫工具；Slack 觸發器是例程啟動條件，使用前必須在 Cursor 帳號整合中完成授權。

用自然語言發指令，即可建立監聽。

```text
建立一個 Slack 觸發例程：當 #incident-response 頻道中有人發訊息提及 @bot 且包含短語 "needs repro" 時，在雲端電腦上拉取報錯記錄並嘗試復現。不要監聽其他頻道，也不要在沒有該短語時回應。
```

監聽型別支援四種：Bot 被提及、匹配特定詞句、新增表情回應，或是接收任意訊息。

- **嚴禁在公共頻道監聽任意訊息**，閒聊打卡會觸發全量匹配，整週額度一天就會燒光。
- 必須綁定單一專屬頻道，不能選“整個工作區”。
- 過濾條件儘量收緊，比如限定特定前綴或工單連結。
- 觸發器只對建立後的新訊息生效，歷史訊息不追溯。[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

## 自動化實戰案例：三種典型流水線

### 案例 1：手機一鍵入庫知識庫（iOS 快捷指令 + Webhook）

社群作者鐵柱（@cgnot996）搭了一套歸檔流。在手機上刷到技術文章或影片時點系統分享，Grok Bot 會自動抓全文、提要點，整理成 Markdown 格式寫進 `/workspace/knowledge/inbox.md`。

按這幾步組態。
1. **新建雲端例程**：在 Grok Bot 端新建“手機知識歸檔”例程，觸發條件選 Webhook，拿到專屬的 POST URL 和 Authorization 標頭。
2. **編寫處理指令**：指令設為接收傳入的 URL，在雲端電腦用瀏覽器打開；要是影片就提取文稿；解析完後按格式提取標題與標記，並整理核心要點與關聯連結，追加寫入 `/workspace/knowledge/inbox.md`。
3. **建立手機快捷指令**：在 iPhone 打開“快捷指令”App 新建一條，打開“在共享表單中顯示”，接收型別勾選“網頁和文本”。
4. **新增請求節點**：新增“獲取 URL 內容”節點，方法選 `POST`，URL 填 Webhook 目標地址，頭部加 `Authorization` 值為 `Bearer [你的私鑰]`，請求體選 `JSON` 並將 `url` 綁定到“快捷指令輸入”。
5. **解決分享限制**：微信公眾號等應用無法直接喚起帶快捷指令的分享面板。**額外建一條“輸入框中轉”快捷指令綁到操作按鈕（Action Button）**，點開彈窗貼連結，再轉發給 Webhook。

**手機端只做輕量參數捕獲與 HTTP 發送，繁重的內容抓取和排版全交給雲端非同步跑。** 這樣手機不耗電也不用等，幾秒就能退出來。

出處：[《Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)，[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

### 案例 2：虛擬機器兩段式巡檢與額度極限優化

社群作者鐵柱（@cgnot996）優化了“行銷總監”Bot 的 6 條例行任務。他把盯 xAI 回覆和每日審 PR 這兩項純等變動的巡檢改成輕量比對，有實質進展才叫醒模型，每週省下 8 至 10 次無效空轉。

任務分為兩類別。

| 任務型別 | 典型代表 | 排程策略與執行特徵 |
| :--- | :--- | :--- |
| 到點必須交付產物 | SEO 日報、權重月報 | 到點產出完整報告讓人查閱，保留原生定時排程 |
| 到點單純等待變動 | 監控頁面更新、新 PR 檢查 | 定時空轉會扣額度，需要改成輕量檢測 |

落地分四步走。
1. **部署本地哨兵**：在 Grok Bot 跑著的 Linux 虛擬機器本地寫一個極簡指令碼，用 Python 或 Bash 都行，完全不調大模型。
2. **組態定時比對**：用 Linux 自帶的 `cron` 定時器跑指令碼，工作日每半小時查一次。指令碼只比對網頁哈希值或查 GitHub 介面看 PR 數，耗時幾秒且不消耗 Grok 訂閱額度。
3. **實施差異喚醒**：**比對發現實質變動後，指令碼才執行 `curl` 向 Webhook 發起 POST 呼叫。**
4. **模型介入處置**：Bot 醒來後開始讀 PR 程式碼或回覆內容，梳理決策建議並推送通知。

機械判斷交給本地指令碼，需要動腦才叫醒大模型。這樣不用為了一句“今日無事發生”白白消耗大模型上下文。

出處：[《Grok Bot 額度再省一點：定時任務極限優化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)。

### 案例 3：每日客戶流失風險監測

官方團隊與運營 29 個 Bot 的作者 melvindvivas 採用這套方案監控客戶異動。每天早晨自動拉取用量與工單指標，生成預警觀察清單，全程嚴格受控。

落地分四步走。
1. **確立崗位章程合同**：建專職 Account Risk Bot，在 Profile 的 Description 寫明規則合同，定好風險閾值。比如 API 呼叫量連續三天跌幅超 40%，且伴隨沒解決的 P1 工單。
2. **設定定時拉取任務**：配好工作日早晨 8:00 跑的例程，定時拉取源系統指標。
3. **組態故障熔斷機制**：**資料倉庫連線超時或資料未就緒，直接報告缺失失敗原因，嚴禁拿昨天快照推測，嚴禁輸出未證實資料。**
4. **設定安全審批人閘**：在 Settings 的 Custom Rules 裡把發郵件、修改 CRM 欄位和分發清單全部設為“先詢問”（Ask first）。Bot 整理出的清單隻在聊天視窗靜默展示，等客戶經理核實後手動點選批准卡片。

**高價值自動化不能只給模型放權，賦予執行能力的同時必須加上邊界合同與人工閘門。**

出處：[《使用 Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)，[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

## 例程排錯指南

### 計劃時間到了，Bot 完全沒有反應
- 桌面端 Details 確認未被 Paused，手機端確認 Active 開啟。**久未登錄超時未回 Bot 確認，任務會自動暫停**。
- 核對 When to run 時區與週末設定。新建計劃只等下個自然週期，先點 Test 測鏈路。
- 手機端查“執行歷史”，**顯示 No runs yet 說明信號沒進網關**，顯示 Failed 可點開看具體報錯。

出處：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

### 外部 Webhook 推送了，但例程未啟動
- 調介面先看返回值，**非 200 說明請求被網關攔截**。
- 核對請求頭 `Authorization` 的 Bearer 密鑰，重新生成後舊密鑰立刻作廢。
- 新建觸發器後**必須點右下角 Save**，端點和密鑰才會在網關生效。

出處：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

### Slack 觸發器不觸發
- 觸發器**只對上線後的新增訊息生效**，編輯歷史訊息不會觸發。
- 確認沒發錯頻道，帳號在目標頻道需有讀取權限，**關鍵詞要精確匹配**。

出處：[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)

### 任務跑了一半突然卡死中斷
- 後台無人值守的審批卡片**只等待約 10 分鐘**，超時變 Expired 就會中斷失敗。
- 開啟通知，或在 Settings > Bot > Auto-review 模式的“自訂規則”中放行信任動作自動執行。
- 遇報錯右鍵氣泡點 **Copy request ID**，帶上報錯文本找官方調記錄排查。

出處：[《Grok Bot 操作指南》](https://cursor.com/cn/help/grok-bot/how-to.md)

### 雲端電腦更新後，本地指令碼與定時器丟失
| 更新型別 | 環境保留情況 |
| :--- | :--- |
| 軟體更新 | 雲端電腦環境與文件不受影響 |
| 電腦更新（“設定”>“電腦”>“更新 Bot 的電腦”） | 重構鏡像；保留 `/workspace` 與瀏覽器登錄態，**清空 apt 全域包（如 cron）** |

出處：[《Grok Bot 操作指南》](https://cursor.com/cn/help/grok-bot/how-to.md)，[《Grok Bot 額度再省一點：定時任務極限優化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)

## 容易踩的坑

1. **點 Test 會真執行**：會呼叫工具刪文件，**測試前在指令留審批中斷點**。[《例程》](https://cursor.com/cn/help/grok-bot/routines.md)。
2. **輪詢與定時機制**：每 5 分鐘輪詢耗盡整週額度，**用輕量指令碼比對，有變動再喚醒模型**。“每天 9 點”預設工作日跑，**註明“包括週末在內”，在 Settings 固定時區**。[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。
3. **聊天框勿貼 Webhook 密鑰**：會記入雲端歷史。**憑證須在安全機密資訊請求卡片輸入**，誤貼立刻刪除。[《Grok Bot 額度再省一點：定時任務極限優化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)。
4. **防審批攔截靜默失敗**：設攔截須開行動裝置端通知。**審批彈出後 10 分鐘無人應答超時報廢**。[《Grok Bot 操作指南》](https://cursor.com/cn/help/grok-bot/how-to.md)。
5. **Bot 共享環境**：在 `/workspace/temp` 刪文件影響其他 Bot，**寫文件須為各項目指定獨立子目錄**。[《使用 Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)。

## 做完怎麼驗收

按順序過完這四步，**全通過才能放手讓它無人值守**：

1. 核對時間：在詳情頁確認 **Next run** 時間戳記和本地時區完全對得上。
2. 測缺資料：斷網或傳空文件點 Test，例程必須報錯終止，不能瞎編內容。
3. 測審批攔截：故意發刪除或外發指令，要是沒彈卡直接執行，說明有漏洞，得去 Settings 補。
4. 查記錄落盤：正常跑一次，去 `/workspace` 確認文件已寫入，且聊天視窗沒有刷屏。

出處：[《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)。

## 延伸閱讀

### 官方文件

- [《使用 Grok Bot》](https://cursor.com/cn/docs/grok-bot/work.md)
- [《例程》](https://cursor.com/cn/help/grok-bot/routines.md)
- [《Grok Bot 操作指南》](https://cursor.com/cn/help/grok-bot/how-to.md)

### 社群實戰

- [《4.3 觸發器與自動化：定時、Webhook、在 X 上派活》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [《Grok Bot 額度再省一點：定時任務極限優化》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [《Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建》](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)

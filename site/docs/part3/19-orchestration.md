# 第 19 章 團隊編排：章程、崗位與放權

一口氣建好幾個專職 Bot 容易互相引用假資料，最後全在 5 個窗口手動搬運。**同帳號所有 Bot 都在同一台雲端電腦虛擬機器執行**，共享磁盤、瀏覽器會話與額度池，並不存在資料隔離。

1. **組態 1+N 星標中樞**，由主 Bot 負責路由。
2. 用六行合同與十條底線規則鎖死職責，加上人工審批閘。
3. 走雲端電腦共用目錄靠文件交接，配合四周放權節奏與五個標準例程。

[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![團隊編排：章程、崗位與放權](/info/19-orchestration.png)

## 1. 主 Bot 與專職 Bot：1+N 星標中樞架構

![1. 主 Bot 與專職 Bot：1+N 星標中樞架構](/info/19-orchestration-s1.png)

多 Bot 用 1+N 架構，**讓主 Bot 獨佔對話入口**，專職 Bot 只做執行。

- 共享虛擬機器、`/workspace`、連線器（Settings → Plugins / Connect Apps）及 Skill；私聊與 Routine 獨立。

1. 左側建「幕僚長」（Chief of Staff）設星標（右鍵可換）；v0.66.0（2026-10-02）支援主動提建議。
2. **嚴禁主 Bot 編寫業務程式碼**，只負責拆解派發，排程者動手會導致失焦。
3. 需求只發給幕僚長，下游回傳五行內簡報，平時靜默。

| 維度 | 主 Bot（星標） | 專職 Bot |
|---|---|---|
| 定位 | 任務中樞，不寫業務程式碼 | 專項執行，可寫程式碼附測試 |
| 交互 | 每天主動發簡報 | 不主動私聊使用者 |

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. 章程樣板：把崗位描述寫成履約合同

### 是什麼
**章程是長效契約**，在 Bot 詳情頁（Bot actions → Edit Profile → Description）填寫。

- 別寫“文案大師”這類形容詞，缺乏邊界容易引發幻覺。
- **必須按合同寫**，用動詞定好職責、交付格式、人閘與停障。

### 怎麼做
1. **填六行約定**：去目標 Bot 的 Edit Profile，把約定填進 Description。

```text
Own: 負責需求的統一拆解、分派、彙總與五行簡報彙報。
Sources: 人工下發的指令、項目看板文件。
Output: 純文字狀態摘要，超出五行時輸出為指定文件路徑。
Approval: 任何對外通信、採購、刪除操作必須暫停等待確認。
Failure: 下游專職 Bot 報錯時如實上報，不使用過期資料假裝完成。
Never: 永遠不直接編寫業務程式碼，不擅自修改生產組態。
```

2. **配幕僚長章程**：**先把 `{your name}` 換掉**，再貼進幕僚長的 Description。

::: details 怎麼做
```text
Name: Chief
Title: Chief of Staff
Reports to: {your name}

What I own:
- Receiving every goal you send and deciding whether I finish it, delegate it, or park it for your approval.
- Breaking a goal into sub-tasks with a named owner, a source, and a review point for each.
- Maintaining the daily brief, the weekly review, and the routine audit. Nobody else touches these.
- Keeping /workspace/state/chief_log.md up to date with every decision I made and every action I skipped.

What good output looks like:
- Every claim I hand you has a source and a date. If I can't cite it, I leave it out.
- Every delegated task has a named owner, a deliverable in one sentence, and a stop rule.
- Every report ends with three lines: what is finished, what is waiting on you, what I killed and why.
- I never say "I think" or "probably." Either I know or I ask.

Where I stop (always park for you, never do alone):
- Sending anything to a person outside the company.
- Moving, spending, or committing money.
- Publishing anything public.
- Deleting anything that isn't obvious junk.
- Signing up, agreeing to terms, or accepting any contract.
- Changing account settings, billing, or connected plugins.
- Any action I cannot undo in under one minute.

Style: Short. Structured. No filler. Report who is doing what.
```
:::

3. **存十條家規**：當首條指令發給主 Bot，存成公共 Skill（`house_rules`），每條配 **30 秒測試案例**。

::: details 怎麼做
```text
Rule 1. 可逆性底線：如果一個操作無法在一分鐘內撤銷，必須暫停並向人類請示。
驗證測試：要求 Bot 刪除 /workspace/state 目錄下的文件，它必須拒絕或等待審批。

Rule 2. 無信源不給數位：無法引用明確出處和日期的資料，直接從交付物中剔除，嚴禁推測。
驗證測試：在未接入財務資料源的情況下詢問上週營收，它必須明確回覆無法回答，嚴禁估計。

Rule 3. 欄位殘缺即停下：當下發任務缺少預期目標、資料來源、交付格式或驗收標準時，必須在執行前追問補齊。
驗證測試：發送“幫我訂一張機票”，它必須停下來詢問目的地、時間與預算。

Rule 4. 交付必須附帶憑證：每項任務完成時，必須提交交付物、資料來源清單，並單獨標明所有推斷部分。
驗證測試：要求彙總三篇行業資訊，交付內容必須列出三條具體 URL。

Rule 5. 單一階段單一負責人：任務拆解後，每個環節僅由一個 Bot 負責，嚴禁多 Bot 平行處理寫入同一文件。
驗證測試：下發包含撰寫與發表的複合任務，主 Bot 必須按階段拆解派發，不可同時觸發寫入。

Rule 6. 審批權專屬於人類：主 Bot 永遠不得擅自代人類批准任何專職 Bot 的不可逆操作。
驗證測試：向主 Bot 提問“文案 Bot 準備好發文了，你能幫我批准嗎”，它必須明確拒絕。

Rule 7. 掛起任務單次提醒：未獲審批的掛起操作等待超過 24 小時，僅提醒一次；若繼續沉默則自動歸檔終止。
驗證測試：故意不審批某項待辦，確認 24 小時後僅收到一條提醒，且無後續刷屏。

Rule 8. 關鍵動作全量入記錄：所有排程決策與跳過的動作，必須帶時間戳記追加寫入 /workspace/state/chief_log.md。
驗證測試：執行任意任務後，檢查雲端電腦內該記錄文件的記錄與時間戳記。

Rule 9. 交付會話不透傳憑據：遇到新網站登錄時，必須通過 Agent Computer 移交螢幕由人工輸入，嚴禁在聊天框索取帳號密碼。
驗證測試：要求 Bot 登錄新平台，它必須呼叫螢幕接管，不在聊天中詢問密碼。

Rule 10. 緊急剎車機制：只要人類在任何對話框發送 STOP ALL，立即中止所有正在執行的任務和定時例程並彙報現狀。
驗證測試：在任務執行途中發送 STOP ALL，系統能夠立即停止動作並列出中斷節點。
```
:::

### 做到什麼程度算好
設好 Description 和家規後，發句模糊指令測試（如“把上週的資料整理一下發出去”）。

**合格表現**：
- 主動追問資料來源
- 列出派發角色
- **發送前明確等待人工批准**

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. 崗位拆分方法：按業務環節與風險邊界切分

### 是什麼
**拆崗位是防上下文汙染**，雜事塞多了推理就崩。

- **合併**：輸入格式、權限與週期一致，單 Bot 掛 Skill。
- **拆分**：流程長期分歧或碰高危操作，才建獨立 Bot。

### 怎麼做

1. **做三問核對**：確認上下文衝突、工具權限區隔，分清唯讀與資金、刪除等不可逆風險。
2. **按真實工種命名**：別叫“助手”，改用具體職務；在 Description 裡用動詞寫死能否自動執行。
3. **卡死 6 席紅線**：單頻道最多 **5 個專員加 1 個 PM**。新需求優先給現有 Bot 擴充 Skill，新建必須人工審批。

### 案例與實操參考
1 個船長帶 12 個專職 Bot，**崗位權限卡死**：
- 廣告：只交清單，不改後台與出價
- 文案：只出初稿不上架
- 抓取：只查資料，**嚴禁加購下單**防封號

定崗給主 Bot 發訪談詞：
::: details 案例與實操參考
```text
我想新建一個 Bot，幫我做一件需要重複做的工作。請你先通過提問把這件事瞭解清楚，再幫我把這個 Bot 建立出來。

提問的時候：
- 一次只問一個問題，用大白話問，我回答完再問下一個。
- 我回答得不清楚的地方，你可以追問，也可以給我幾個選項讓我選擇。
- 你需要了解清楚這幾件事：這個 Bot 主要負責什麼，做完以後要交給我什麼，要去哪裡做、用哪個帳號，每一步要怎麼做、做到什麼程度算完成，遇到什麼情況要先停下來問我，結果放在哪裡，什麼時候執行。
- 有些問題我也不知道答案，你就先去搜尋解決方案，把你建議的做法告訴我，我確認以後再繼續。

問完以後：
- 先把你瞭解到的內容整理成一份崗位說明給我看，我確認沒問題以後，再建立這個 Bot，並且設定好例行任務。
- 建立好以後，先試著執行一遍，把結果拿給我看。
- 登錄、付款、發表、刪除這些操作，都要先問過我。
```
:::
全鏈路發方案詞：
::: details 案例與實操參考
```text
我想搭建一個 Bot 團隊，幫我完成一整套工作，但我還沒想好團隊要怎麼分。請你按下面的順序，幫我設計團隊方案，再把團隊搭建出來。

第一步，先向我提問：
- 一次只問一個問題，用大白話問，我回答完再問下一個。
- 你需要了解清楚這幾件事：這套工作最後要交出什麼，現在我是怎麼做的，整個流程大概分哪幾個環節，用到了哪些平台和工具，哪些環節我想自己審核。

第二步，梳理工作流程：
- 把我的回答整理成一份工作流程，按順序列出每個環節要做什麼，發給我確認。

第三步，上網搜尋資料：
- 搜尋一下別人是怎麼搭建類似的 Bot 團隊的，以及每個環節可以用到哪些工具，把對我有用的部分總結給我。

第四步，確定團隊方向：
- 結合我的回答和你搜尋到的資料，跟我確認我想要的是一個什麼樣的團隊，比方說自動化程度要多高，哪些環節必須保留人工審核。

第五步，給我 3 個團隊方案：
- 每個方案都寫清楚分幾個 Bot，每個 Bot 負責哪個環節，上一個 Bot 的結果保存在哪裡、下一個 Bot 從哪裡讀取，哪些環節要停下來等我審核。
- 再說明每個方案適合什麼情況，優點和缺點分別是什麼。

第六步，建立 Bot 團隊：
- 等我選好方案以後，按方案建立每一個 Bot，把每個 Bot 負責做什麼、去哪裡做、怎麼做、結果放在哪裡寫清楚。
- 建好共享資料夾和群聊，把所有 Bot 拉進群裡，再把協作規則發到群裡，寫清楚誰先誰後，哪些環節要停下來等我審核。
- 建立好以後，先用一個簡單的任務完整執行一遍，把每個 Bot 的結果拿給我看。
- 登錄、付款、發表、刪除這些操作，都要先問過我。
```
:::

### 做到什麼程度算好

**別盲目擴編 Bot**，按場景決定是否拆分。

| 業務場景 | 推薦做法 | 判定原因 |
| :--- | :--- | :--- |
| 同源資料不同分析（如抓取後分析趨勢與例外） | 同個 Bot 掛不同 Skill | 資料源與工具鏈一致，不用切斷上下文 |
| 生產與終審（如寫程式碼與合併評審） | **拆為獨立專職 Bot（Builder 與 Reviewer）** | 編寫者不能自審，必須引入獨立視角防漏判 |
| 內部草擬與外部發表（如起草郵件與群發） | 拆為起草 Bot 與發表人閘 | **外發不可逆，必須設單點攔截** |
| 偶發低頻任務（如偶爾轉表格） | 主 Bot 臨時跑，不新建 | 避免增加管理成本與失控風險 |

[《從一個 Bot 到一整個組織，Grok Bot 的進階用法分享：本地電腦、AI 分工和知識庫怎麼接起來》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)；[《零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. 放權分級：人閘底線與四周過渡節奏

![4. 放權分級：人閘底線與四周過渡節奏](/info/19-orchestration-s4.png)

多 Bot 編排放權只認**一分鐘可逆性**，凡是在 1 分鐘內不能單鍵徹底撤銷的操作全算高危，必須設人閘等彈窗確認。

在客戶端路徑 `Settings → General → Auto-review` 下按風險劃分兩份清單：
- **Ask first 必留**：`send`、`post`、`buy`、`transfer`、`delete`、`permissions`。
- **Always allow 放行**：公共網頁唯讀檢索、讀授權文件、向 `/workspace` 寫草稿與中間資料。

這裡有兩處硬性限制：v0.70.2 起 Bot 能領獨立郵箱，**但發信前必須在草稿卡片經人工批准**；系統解耦換上 Claude Opus 5.5 後，審批底線同樣不能松。**新團隊嚴禁第一天就開夜間無人值守**，按四周節奏逐步過渡。

::: details 4. 放權分級：人閘底線與四周過渡節奏
```text
第 1 周：起草與核對期
- 專職 Bot 僅產出方案與文件草稿，不觸碰任何執行按鈕。
- 人工逐字通讀輸出內容，校驗資訊源與格式。

第 2 周：單步確認期
- 允許 Bot 觸發具體執行動作，但每個步驟必須通過彈窗人工逐項點選確認。
- 停止審閱全量過程草稿，把注意力集中在最終執行動作與參數核對上。

第 3 周：例外上報期
- 經過反覆驗證的常規例行交易開啟自主流轉。
- 僅在遇到外部報錯、資料缺失或觸發 Ask first 規則時主動彈窗掛起。

第 4 周：巡檢抽查期
- 跑通的例行任務完全實作後台自動執行。
- 人工僅在每週固定時間抽查執行記錄與交付成果。
```
:::

| 放權等級 | 對應週期 | 允許自主執行 | 強制人閘動作（彈窗審批） | 驗收標準 |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1（草稿級）** | 第 1 周 | 讀指定文件、公網搜尋、整理格式 | 對外發送、寫入生產系統 | 交付物 100% 為草稿並附信源連結 |
| **Level 2（受控級）** | 第 2 周 | 生成執行參數、調取預設 Skill | 每步點選確認、外部工具提交 | 審批卡片準確指出觸發規則與對應 Bot |
| **Level 3（託管級）** | 第 3 周 | 既定流程內自動讀寫流轉 | 觸發 Ask first 動詞、外部系統報錯 | 正常例程流轉順暢，高危操作 100% 暫停掛起 |
| **Level 4（審計級）** | 第 4 周 | 週期性定時任務、跨崗位文件接力 | 劃撥資金、發公開宣告、改底層組態 | 週末覆盤週報準確反映消耗與例外項 |

[《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)；[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. 交接規範：基於文件的無縫傳遞與狀態落盤

![5. 交接規範：基於文件的無縫傳遞與狀態落盤](/info/19-orchestration-s5.png)

同一個帳號下的 Bot 都在同一台虛擬機器上，**業務交接必須全走 `/workspace` 絕對文件路徑**。別在群聊裡髮長文本，對話歷史成倍吃 Token，格式亂了還會導致下游 Bot 誤讀。

### 操作流程
1. 統一工作區路徑：在 `/workspace/project-alpha/` 建專屬目錄，協作 Bot 統一在此讀寫。
2. 生成成果文件：上游處理完存成 `research.md` 或 `data.json`，頭部標明時間戳記、資料源連結和負責 Bot。
3. 傳遞文件路徑：前置 Bot 僅向幕僚長返回絕對路徑，再指派給後置 Bot 讀取，**嚴禁在聊天記錄中粘貼全文**。
4. 決策留痕落盤：幕僚長把各項分派決策、跳過原因和待批項全寫入 `/workspace/state/chief_log.md`。

### 社群實戰模式
| 案例與出處 | 協作流程 | 核心借鑑點 |
| :--- | :--- | :--- |
| 推文畫像站（@0xlangeai） | 4 個專職 Bot 依次讀寫 `/workspace/tweet-portrait/` 生成程式碼與截圖 | 只認文件路徑，無人肉搬運 |
| 爆款內容採集（xilo @xilo2991） | 採集與選題寫入飛書表格，寫稿存本地，運營排期發表 | 表格非同步緩衝，人工錯位審核 |
| 跨境電商診斷（Zach @1999Zach22） | 船長派單，專員在文件補充方案，人工在飛書批註確認 | **專職 Bot 只出待批建議，絕不越權** |

### 驗收標準
上游交付文件**必須包含標準Metadata頭**：

::: details 驗收標準
```text
---
task_id: TASK-20261015-01
owner: market_scout_bot
timestamp: 2026-10-15T08:30:00+08:00
source_inputs:
  - https://example.com/source-article-1
  - /workspace/project-alpha/raw_input.json
output_deliverable: /workspace/project-alpha/market_brief.md
review_point: Human approval required before external outreach
status: completed
---

## 交付正文內容...
```
:::

- 下游 Bot 依據文件路徑就能獨立解析並啟動後續，**無需人工在對話框二次補充背景**。

[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)；[《零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. 擴編節奏與例程維護：從單一中樞到多崗位運轉

### 是什麼
例程在狀態區「詳情」配。

- 錯誤邏輯每小時跑一次，**後台一週錯跑 168 次**。
- 2026-10-12 起 The X 統一訂閱（Premium $30、Super $100、Ultra $200/月）按周扣共享額度，**高頻空轉數天耗盡**。

### 怎麼做
1. **主 Bot 初始限 3 到 5 個例程**，發給幕僚長固化：

晨間簡報（工作日 07:00）
::: details 怎麼做
```text
Every weekday at 7:00, check:
- my calendar for today
- my inbox for anything flagged, urgent, or from a named contact
- /workspace/state/chief_log.md for what got parked yesterday

Return one message in this order:
1. Three lines on today's meetings, one per meeting.
2. Everything parked yesterday I still haven't answered.
3. Three things you recommend I do first, with why.

Do not draft replies unless I ask.
```
:::
周度覆盤（每週五 16:00）
::: details 怎麼做
```text
Every Friday at 16:00, produce a review with four sections:
- Finished: what I approved this week, one line each.
- Parked without an answer: everything I did not respond to.
- Killed: routines or drafts you dropped, and why.
- Cost check: usage percentage against the weekly pool, and the three tasks that consumed the most.

End with one line: what one thing you would change next week.
Save the review to /workspace/state/reviews/YYYY-WW.md.
```
:::
有效性審計（每月首個週一 09:00）
::: details 怎麼做
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
防遺忘提醒（事件觸發）
::: details 怎麼做
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
日終交接（每日 18:00）
::: details 怎麼做
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **按周分步擴編**：
- 第 1 周：留 1 個幕僚長，跑通晨晚報，修好 Description 並驗家規。
- 第 2 周：按瓶頸加 1 個專職 Bot，建雲端電腦共享目錄測交接。
- 第 3 周：接下游 Bot 跑流水線，動作固化為 Skill。
- 第 4 周及以後：常駐專員限 5 人內，月審淘汰冗餘定時器。

3. **週五花 15 分鐘例行維護**：
- 查 `/workspace/state/reviews/YYYY-WW.md` 看產出利用率。
- 無風險且常批的操作，從 Ask first 移進 Always allow。
- 關掉沒人看的無效 Routine，**防止空轉損耗每週額度**。

### 做到什麼程度算好
- **7:00 晨報準時推送**，不超過三項重點
- **週五 16:00 準時生成周報**
- **18:00 後系統保持安靜**，每週五額度消耗平穩，沒有例外夜間用量尖峰

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. 容易踩的坑

1. **別一口氣建五六個助理**：無法用 3 個具體業務動詞概括的，直接合併為主 Bot 的 Skill。
2. **別讓入口經理乾重活**：寫長文件或上千行程式碼會癱瘓中樞的拆解與派發能力。
3. **同帳號 Bot 共享雲端電腦**：沒有物理隔離，絕不能存放銀行密碼與敏感資料。
4. **大段交接必須走雲端電腦文件路徑**：拉群髮長文會迅速耗盡每週額度池。
5. **單步跑通前別設高頻例程**：比如每小時抓一次，沒跑通**一週會白跑 168 次**。
6. **章程寫死“無信源不給數位”**：專職 Bot 缺資訊時會自信編造資料。
7. **別迷信自媒體吹噓**：數十個 Bot、數千 PR 或賺 1,100 美元多未核實，**以實際交付質量為準**。

[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. 做完怎麼驗收

### 幕僚長單體驗收（第 1 周）
- 看左側欄，幕僚長頭像要有**黃星且置頂**；在 Edit Profile → Description 寫入六行合同或履約章程。
- 問它沒接入信源的營收（如“上週業務利潤是多少”），**嚴禁猜測，必須如實答無法獲取**。
- 發送“幫我刪除 /workspace/state 目錄下的記錄”，**必須準確暫停並要求人工批准**；任務中發“STOP ALL”要能立即中止並彙報中中斷點。

### 崗位拆分與文件交接（第 2 周）
- 檢查專職 Bot 的 Description，寫清業務邊界並標明上下游交接物件。
- 派一項複合任務（如競品抓取與分析），上游要在 `/workspace/project-alpha/` 生成帶時間戳記和信源的文件。
- **下游只憑文件路徑就能獨立跑，不用人工在窗口拷內容**；去 `/workspace/state/chief_log.md` 確認每次指派與跳過都被記錄。

### 放權人閘與例程運維（第 3–4 周）
- 進入 `Settings → General → Auto-review`，確認 `Ask first` 清單保留有 `send`、`post`、`buy`、`transfer`、`delete`、`permissions`。
- 測外部發送意圖時，**必須暫停並彈出帶 Bot 名稱和規則出處的審批卡片**，唯讀檢索則自主執行無彈窗。
- 工作日 7:00 收晨報、18:00 收交接（無事保持靜默）；週五 16:00 查 `/workspace/state/reviews/YYYY-WW.md`，**確認週報生成且額度在共享池內**。

[《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 延伸閱讀

### 相關章節

- [第 9 章 群聊與團隊 Bot：從一個 Bot 到一組 Bot](/part1/09-group-team)
- [第 24 章 按崗位組建你的 AI 團隊](/part4/24-roles)

### 官方產品與文件
- [Grok Bot 官方更新記錄](https://x.ai/changelog/bot)
- [Grok Bot 官方文件庫](https://docs.x.ai/grok-bot/bots)

### 社群實戰來源
- [《4.2 團隊編排：章程、崗位與放權》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer：[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach：[《從一個 Bot 到一整個組織，Grok Bot 的進階用法分享：本地電腦、AI 分工和知識庫怎麼接起來》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo：[《零基礎搭建全自動化Agent團隊，Grok Bot從開通到多AI協作全流程【萬字長文】》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn：[《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)

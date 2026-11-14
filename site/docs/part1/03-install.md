# 第 3 章 安裝登錄與第一個 Bot

**確認訂閱含 Bot 權益**，不然沒入口；登錄跳循環查隱私設定。別建無約束的“全能助手”白耗周配額。

1. 裝好桌面與行動裝置端，排除登錄報錯
2. **建專屬 Bot 填六行合同**
3. 派發首條落盤任務，對照清單驗收


![安裝登錄與第一個 Bot](/info/03-install.png)

## 訂閱方案核對與開通條件

下載前先看帳號資格，**Grok Bot 必須綁定有效訂閱才能用**。

| 方案名稱 | 價格 | 是否包含 Grok Bot | 額度說明 |
| :--- | :--- | :--- | :--- |
| The X Plus | $8 / 月 | 否 | 僅普通模型對話，無 Bot 權限 |
| The X Premium | $30 / 月（年付 $300） | 是 | 4x 額度，個人入門最低門檻 |
| The X Super | $100 / 月（年付 $1000） | 是 | 15x 額度 |
| The X Ultra | $200 / 月（年付 $2000） | 是 | 50x 額度 |
| Cursor Pro / Pro+ / Ultra | 見官網定價 | 是 | 依檔位提供每週額度 |
| Cursor Teams (自助席位) | 見官網定價 | 是 | 成員共享團隊配額 |

- **每月 8 美元的 Plus 檔不包含 Bot 權益**，買了用不了。
- **X 關聯額度與 Cursor 訂閱額度不疊加**，系統結算自動按每週用量更高的一方算。

方案底座機制參考社群文章 [《1.1 Grok Bot 是什麼：一頁看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc) 與 [《萬文長｜Grok Bot 從零入門第一次上》](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)。

## 桌面端下載與安裝

![桌面端下載與安裝](/info/03-install-s2.png)

macOS 支援 Apple silicon（M 系列）與 Intel，Windows 和 Linux 支援 x64 與 Arm64（Win 建議開硬體加速）。

1. 登錄 `cursor.com/dashboard/bot` 或直接去 `x.ai/bot` 下載安裝包。**若公司設備無權限，找管理員索取**。
2. macOS 把下載的應用拖進 `Applications` 資料夾，Windows 和 Linux 跑安裝嚮導。
3. **啟動客戶端看到登錄介面就成了**。具體操作可參考文件 [Grok Bot 快速入門](https://cursor.com/cn/docs/grok-bot/get-started)。

## 帳號登入與隱私模式組態

1. 啟動客戶端點 **登錄**，在瀏覽器直接用 Cursor 帳號認證，企業 SSO 會自動生效；如果是 Grok Business 席位，選 **Sign in with Grok** 登錄。
2. 認證完成後進客戶端“設定”，能看到帳號郵箱和方案狀態就說明成功了。

**舊版隱私模式（Privacy Mode (Legacy)）必須切到現行 Privacy Mode 才能繼續**。個人使用者在彈窗點確認即可；團隊成員需要讓管理員去 Team Settings 裡更新。

詳細說明參考官方文件 [入職](https://cursor.com/cn/help/grok-bot/onboarding) 與 [登錄 Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in)。

## 常見登錄問題與故障排查

盲目重裝沒用，多是快取或會話重新整理問題。

1. 客戶端升至最新並重登。
2. 清 `cursor.com` 與 `x.ai` 的 Cookie 或用無痕模式。
3. 登 `x.ai/bot` 確認網頁端能建立會話。
4. 剛改訂閱**靜置等 30 至 60 分鐘**，重新整理後報錯消除。

手機驗證連錯會觸發風控鎖定，無法自愈。排查無效或遇 OAuth 報錯，**去支援頁提工單**，附郵箱與截圖，寫明版本及步驟。

詳見 [登錄 Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in)。

## iOS 行動裝置端安裝與雙端協同

### 安裝與登錄
1. 系統需 **iOS 18 或更高版本**。
2. App Store 搜 Grok Bot 安裝，登錄同個 Cursor 帳號自動同步，**無需重複付費**。

### 雙端分工
- 手機端適合日常監控，能看實時螢幕，支援接管控制（Take over）輸驗證碼、審批（Allow / Deny）或啟停 Routine。
- **深度操作必須回桌面端**：最長 10 分鐘螢幕錄影教學（Teach a task）、測試 Routine（Test run）與維護雲端電腦（Update / Recover）。

### 通知管理
- **單個 Bot 靜音**：聊天頁點頂部名字關閉 **Notifications**，桌面端發訊息也能關。
- **全域關閉**：在系統“設定”中關閉 Grok Bot 的通知權限。

詳見 [行動裝置端 Grok Bot](https://cursor.com/cn/help/grok-bot/mobile)。

## 認識共享底座與建立第一個 Bot

![認識共享底座與建立第一個 Bot](/info/03-install-s6.png)

每個付費使用者都有一台常駐雲端虛擬機器，組態獨立 Linux、瀏覽器、終端與持久磁盤（早期測試組態約 8 核 16GB 記憶體，未核實，具體以官方為準）。

這台機器有三個直接影響操作的物理邊界：
- **所有 Bot 共享同一台機器**：共用 `/workspace` 與一套瀏覽器登錄態，分設 Bot 只是劃分崗位，沒有安全隔離。
- **跨 Bot 協作必須文件落盤**：聊天記錄互不相通，Bot A 必須把產物寫進 `/workspace` 文件，Bot B 才能讀取接力。
- **支援隨時查看與實時接管**：右側可展開雲端電腦畫面，遇到密碼、人機驗證或支付認證隨時接管，不要把憑證打在輸入框裡。

首次登錄會自動生成預設的 **Grok Bot**，手動新建與設定步驟如下：

1. **新建**：點側邊欄頂部 **+**（或 Cmd+N），選 **建立新 Bot**（Create new Bot）。在輸入框先輸名字也能直接點選建立。
2. **改名與標記**：右鍵選 **重命名機器人**，或點頂部名稱展開面板修改。下方可設職務標記（Label，手機端為 Title (optional)）。
3. **換頭像**：點選頂部名稱進詳情並點選頭像，支援選擇內建幾何圖形、輸入描述詞生成，或上傳 25 MB 以內的本地圖片（手機端可選相冊、生成或移除）。
4. **設職責**：**個人 Bot 已取消獨立設定頁，長期規則直接在首條訊息說明並要求它記住**。團隊 Bot 在詳情“關於”欄仍保留固定描述區。

- [更改 Bot 的名稱、頭像和職責](https://cursor.com/cn/help/grok-bot/edit-bot)
- [《萬字長文｜Grok Bot 從入門到精通｜金塵馬》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)

## 編寫職責：標準六行合同

### 合同結構與樣板

新手別給空泛頭銜，**把六項核心約束直接寫進第一條訊息**，讓它當成長期規則記住。

1. Own（負責結果）：明確長期負責的具體指標，不做泛用助手。
2. Sources（權威來源）：限定只看官網或指定連結，禁止使用不明信源。
3. Output（交付格式）：規定保存路徑、命名規則和摘要字數。
4. Approval（審批紅線）：發信、提交表單或刪文件等高危操作，必須等人工彈窗批准。
5. Failure（例外兜底）：遇到網頁失效或資料缺失，必須明確標註，嚴禁腦補推測。
6. Never（絕對禁區）：禁止改動源文件，禁止憑記憶概述，禁止點選付款按鈕。

Bot 命名好後，替換模版欄位直接發送。

::: details 合同結構與樣板
```text
請牢記你的長期工作職責，在今後的工作中始終遵循以下要求：

Own: 負責監控目標清單的每週功能與定價變動，輸出結構化對比材料。
Sources: 僅限使用目標官方網站的定價頁、Changelog 頁面以及我通過附件提供的官方說明文件。
Output: 提煉核心動態，附帶核對日期與原始出處連結，長文本與資料表格必須保存至 /workspace/research/ 下的 Markdown 文件中，對話框中只發簡要完成彙報。
Approval: 涉及發送任何郵件、對外發文、提交表單、刪除文件或進行任何費用支付前，必須停下來等待我的人工批准。
Failure: 若目標頁面無法訪問或內容缺失，在報告中明確標註為“未取得一手資料”，嚴禁推測或編造任何功能與價格。
Never: 嚴禁修改我上傳的任何源文件，在源系統可訪問時嚴禁依賴自身訓練記憶進行主觀概括。

今後的工作中請記住這些要求。
```
:::

### 實踐案例

- 金塵馬在 [《萬字長文｜Grok Bot 從入門到精通｜金塵馬》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee) 中，**把長期職責與單次需求嚴格分開**。

  長期規則管信源和交付，當次訊息只派具體調研主題；缺一手資料直接說明，嚴禁猜數位。
- Today 在 [《萬文長｜Grok Bot 從零入門第一次上》](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg) 中設定了安全邊界，**將唯讀與有外部後果的操作隔離開**。

  每次只調研一個競品並附帶公開來源連結，分清事實與推測；涉及登錄付款一律停下等確認。

演化規則參閱 [《1.1 Grok Bot 是什麼：一頁看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)。

## 派發第一條真實任務

![派發第一條真實任務](/info/03-install-s8.png)

**先從小任務上手**。寫任務記好 5 要素：講清目標與輸入，嚴格唯讀（禁改源文件、註冊與支付），定好落盤規格，標明接管節點。

附件總結髮：
```text
用五個要點總結這份文件。
在單獨的部分列出每個日期、決策和未解決的問題，併為每項註明對應章節出處。
不要更改源文件。
```

查競品定價落盤發：
::: details 派發第一條真實任務
```text
【目標】
調研 3 款主流程式碼編輯器（Cursor、VS Code、Zed）在 2026 年的最新公開定價方案與核心 AI 功能，產出一份選型對比參考材料。

【材料】
1. 僅限使用上述三款產品官方網站的定價頁、功能介紹頁與官方文件；第三方部落格僅作為輔助索引，必須找到官方頁面核實。
2. 記錄每一項資料的原始官方 URL 與資料核對日期。

【邊界】
1. 純唯讀檢索，嚴禁註冊任何帳號，嚴禁開啟任何試用，嚴禁輸入任何支付資訊。
2. 遇到需要登錄才能查看的頁面，直接跳過並記錄在未核實清單中。
3. 嚴禁改動 /workspace 下已有的其他項目文件。

【交付規格】
1. 在 /workspace/editor-research/ 目錄下生成對比報告文件 comparison.md。
2. 報告內包含一張 Markdown 資料表格，表頭列定義為：產品名稱、方案檔位、月付價格、年付價格、核心功能特徵、官網來源連結、核對日期。
3. 表格下方附帶一份 400 字以內的中文總結，指出各產品主要差異，並單獨開闢一節列出“未核實或存在矛盾的資訊”。
4. 對話框中僅需回覆已完成落盤的簡短提示及文件絕對路徑。

【暫停確認節點】
1. 遇到必須登錄、驗證碼攔截或點選付費的操作時，立刻停下並提示我接管。
2. 官網資訊前後出現明顯矛盾且無法核實時，停下說明情況由我判斷。
```
:::

遇登錄、2FA 或滑塊驗證時：
1. **點 Take over 手動處理**，弄完點 I'm done 繼續，跳過點 Skip。
2. 跑完**確認 `/workspace/editor-research/comparison.md` 完整保存**。

規範見 [使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started) 與 [入職](https://cursor.com/cn/help/grok-bot/onboarding)。

## 容易踩的坑

1. 8 美元 Plus 檔沒 Bot，**必須選每月 30 美元的 Premium 檔**。
2. 所有 Bot 共享雲端電腦與配額，先跑通一個，別建十幾個互相打架。
3. 別在聊天框發密碼或 API Key，用 Take over 接管輸入或填安全卡片。
4. 長文本**一律存入 `/workspace` 的 Markdown 文件**，防汙染上下文。
5. 登錄報錯別重裝，清理 `cursor.com` 和 `x.ai` 的 Cookie，或等 30 至 60 分鐘。
6. **不同 Bot 共享虛擬機器和瀏覽器會話**，不能隔離權限。
7. Teach a task、Test run 和系統恢復是桌面端獨有，iOS 端沒有。

## 做完怎麼驗收

1. 進 Usage & Billing，付費檔有效、用量正常。
2. 桌面端右屏能拉起，無 Reconnecting 報錯。
3. iPhone（iOS 18+）登相同 Cursor 帳號，無二次購買提示。
4. 發六行合同，Bot 明確回覆已記住長期規則。
5. 雲端電腦 `/workspace` 按指令生成目標文件。
6. 遇登錄等操作，Bot 主動暫停並彈 **Action needed** 卡片。
7. 故意喂死鏈，報告明確標註 **未取得一手資料**、不瞎編。

## 延伸閱讀

### 相關章節

- [第 4 章 交代任務：訊息、附件與一次好的交接](/part1/04-handoff)
- [第 25 章 常見問題與排錯](/part4/25-faq)

### 官方頁面
- [Grok Bot 快速入門 (Get Started)](https://cursor.com/cn/docs/grok-bot/get-started)
- [入職 (Onboarding)](https://cursor.com/cn/help/grok-bot/onboarding)
- [登錄 Grok Bot (Sign In)](https://cursor.com/cn/help/grok-bot/sign-in)
- [行動裝置端 Grok Bot (Mobile)](https://cursor.com/cn/help/grok-bot/mobile)
- [更改 Bot 的名稱、頭像和職責 (Edit Bot)](https://cursor.com/cn/help/grok-bot/edit-bot)

### 社群實戰
- [《1.1 Grok Bot 是什麼：一頁看懂》](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [《萬字長文｜Grok Bot 從入門到精通｜金塵馬》](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)
- [《萬文長｜Grok Bot 從零入門第一次上》](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)

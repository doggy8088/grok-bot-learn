import json,os,textwrap
R="/workspace/grok-bot-learn"; D=R+"/site/docs"
t=json.load(open(R+"/sources/feishu/tree.json"))
F={i:(x[2],"https://jcng5q8n0f3z.feishu.cn/wiki/"+x[1]) for i,x in enumerate(t)}
def f(i): return f"[{F[i][0]}]({F[i][1]})"
def c(p,title=None): return f"[{title or p}](https://cursor.com/cn/{p})"
OLD={7,8}
def w(path,s):
    p=D+"/"+path; os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w").write(textwrap.dedent(s).strip()+"\n")
def src(*items): return "\n## 來源\n\n"+"\n".join("- "+x for x in items)+"\n"
OUT="\n::: danger 已過時\n本文記錄的是 8–9 月舊開發者積分/舊資費規則，已被 2026-10-12～13 推行的 X 統一訂閱取代，僅作歷史參考。\n:::\n"
def stub(path,title,points,sources):
    w(path,f"# {title}\n\n::: info 提綱\n本頁目前為提綱，正文待補充。\n:::\n\n## 要點\n\n"+"\n".join("- "+p for p in points)+"\n"+src(*sources))

# ---------- 首頁 ----------
w("index.md",f"""
---
layout: home
hero:
  name: Grok Bot 學習站
  text: 從第一個 Bot 到一支 AI 團隊
  tagline: 基於 Cursor 官方文件 + 《Grok Bot 焚訣》知識庫整理
  actions:
    - theme: brand
      text: 開始入門
      link: /start/what-is
    - theme: alt
      text: 核心概念
      link: /core/bots
features:
  - title: 🐣 路徑一：新手
    details: 是什麼 → 方案選擇 → 快速入門 → 第一次好的交接。先跑通一個專職 Bot。
    link: /start/what-is
  - title: 💰 路徑二：省額度的個人使用者
    details: 例程頻率、群聊回覆、備份恢復——讓每週用量撐滿一週。
    link: /advanced/usage
  - title: 🏢 路徑三：團隊與工程
    details: 團隊編排、權限與人閘、團隊 Bot、企業身份與私有網路。
    link: /advanced/team-orchestration
---

::: warning 規則變動提示（2026-10-14 更新）
- **2026-10-12～13 官方推行 The X Subscription 統一訂閱**（Plus / Premium / Super / Ultra，Grok、Grok Bot、Cursor 共享每週用量池；Plus 檔不含 Grok Bot）。詳見 {f(16)}。
- 8–9 月關於「綁定 X 送開發者積分」和舊資費的文章（{f(7)}、{f(8)}）**已過時**。
- 社群與官方幫助中心的方案描述可能不同步，開通與付費**以官方方案頁和 changelog 為準**：{c('help/grok-bot/plans','方案和計費')}。
:::

## 本站怎麼讀

| 章節 | 內容 | 狀態 |
|-|-|-|
| [入門](/start/what-is) | 是什麼、怎麼選、方案、快速入門、FAQ | ✅ 已寫 |
| [核心概念](/core/bots) | Bot、訊息、共享電腦、記憶、技能與例程、外掛、群聊 | ✅ 已寫 |
| [進階](/advanced/usage) | 額度、編排、自動化、安全、備份、飛書/微信 | 📝 提綱 |
| [實戰案例](/cases/) | 社群長文摘要 + 原文連結 | 📝 摘要索引 |
| [團隊與企業](/admin/) | 身份、私有網路、代理、部署 | 📝 提綱 |
| [資源](/resources/) | 提示詞、術語、時間線 | 📝 提綱 |
""")

# ---------- 入門 ----------
w("start/what-is.md",f"""
# Grok Bot 是什麼

Grok Bot 提供**可長期協作的 AI 隊友**：每個 Bot 有名稱、職責和會隨時間積累的上下文，並在一台配備**瀏覽器、檔案系統和終端的持久化雲端電腦**上幹活——所以任務直接在真實工具裡完成，而不是停在聊天草稿裡。

## 它和普通聊天助手的區別

- **每個 Bot 都有一台電腦。** 能用外掛就用外掛，沒有外掛就用"電腦操作"（computer use）點網頁；合上筆記本工作也繼續。
- **設定就是發一條訊息。** 不需要工作流搭建器：建立 Bot、描述任務、按它的要求授權即可。
- **Bot 之間能協作。** 並行執行、互發訊息、群聊共享上下文、交接任務所有權。
- **示範一次就能學會。** 帶它走完一遍多步驟流程，它能存成技能並按計劃重複執行。
- **上下文持續積累。** 記憶、文件、瀏覽器會話、偏好跨會話保留。

## 必須知道的三條邊界

1. **所有 Bot 共用一台電腦。** 文件、瀏覽器登錄態、已裝工具對你名下所有 Bot 可見；不同使用者之間嚴格隔離。
2. **分 Bot ≠ 安全邊界。** 研究 Bot 登錄過的網站，財務 Bot 也能用。敏感資產不要指望靠"拆 Bot"隔離。
3. **對話上下文彼此隔離，交接靠落盤。** Bot 讀不到彼此的私聊；協作時把產出存到 `/workspace` 固定文件裡。

## 什麼樣的活適合交給它

用三條標準篩：**能否在網頁/API 上完整跑通**、**結果能否被人核驗**、**敏感步驟能否停下來等你確認**。高頻重複、可離線巡檢、產出明確的任務最合適；純本地程式碼重構仍適合本地命令列 Agent。

## 新手最常見的坑

- 一上來建十幾個 Bot → 額度耗盡、流程失控。**先跑通一個專職 Bot。**
- 讓主 Bot 親自幹所有細活 → 總控失焦。主 Bot 負責派活與驗收。
- 每 5 分鐘無過濾輪詢 → 幾天吃完一週額度。
- 把密碼貼進對話框 → 一律在雲端電腦畫面裡自己輸入。

## 平台

桌面端支援 macOS（Apple silicon / Intel）、Windows（x64 / Arm64）、Linux（x64 / Arm64），行動裝置端支援 iPhone；Bot 用的電腦執行在 Cursor 雲中。
{src(c('docs/grok-bot','官方：Grok Bot 總覽'), f(2), f(1))}
""")
w("start/compare.md",f"""
# 和 Muse、Hermes、dots、Cue 怎麼選

鐵柱的比喻：Grok Bot 和 Muse 像**品牌整機**——開箱即用，但有平台邊界；Hermes 像 **DIY 組裝機**——自由度高，要自己維護。

| 產品 | 中心物件 | 特點 | 適合 |
|-|-|-|-|
| **Grok Bot** | 崗位分工（多 Bot、團隊 Bot） | 共享雲端電腦、多 Bot 非同步協作、例程與技能 | 團隊業務自動化、檢索、巡檢、跨 Bot 交接 |
| OpenAI dots | 個人主 Dot | 常駐、自帶雲端電腦（2026-09-30 發表） | 個人伴隨、日常代辦 |
| Manus Cue | 獨立身份 Agent | 獨立郵箱/電話/錢包，便利與風險同步放大 | 自主跑腿、跨平台註冊 |
| Meta Muse | 個人生活與社交 | 深度整合 Meta 生態 | 家庭日程、生活瑣事 |
| Hermes | 自訂節點 | 開源自建 | 極客客製化、本地深度自動化 |

## 取捨建議

- 多崗位交接、共享文件、定時巡檢 → **Grok Bot**。
- 純程式碼實作與終端除錯 → 保留本地 CLI Agent（Codex CLI / Claude Code 等）。
- 偶發即時問答 → 普通對話模型即可，不值得常駐一台雲端電腦。
- 新上線的自主 Agent → 不要直接放開真實資產與全域發信權限。

## 落地三步

1. 列出想自動化的任務，逐條標註：能否網頁/API 閉環、是否可驗收、是否涉及不可撤銷操作。
2. 把"高頻重複、可巡檢、產出明確"的劃給 Grok Bot。
3. 每項任務標明歸屬工具與**停止確認點**。
{src(f(3), f(21))}
""")
w("start/plans.md",f"""
# 方案與訂閱

::: warning 規則變動頻繁
官方幫助中心與 2026-10-12 起的 X 統一訂閱說法並存。下單前務必打開官方頁面核對：{c('help/grok-bot/plans','方案和計費')}。
:::

## 官方幫助中心口徑

- 所有**付費個人 Cursor 方案**（Pro / Pro+ / Ultra）和 **Cursor 團隊版**都包含 Grok Bot，用同一個 Cursor 帳戶登入即可，層級越高每週用量越多。
- 也可**關聯個人 SuperGrok / SuperGrok Plus / SuperGrok Heavy / X Premium+**，或用自助式 **Grok Business** 席位通過 *Sign in with Grok* 登錄。SuperGrok Lite 不含 Grok Bot。
- 關聯是一項**用量授權**，不改變你的 Cursor 方案，兩者用量**不疊加**。
- **每週用量**每週重置；用盡後若開啟按需，可繼續按需計費。團隊版預設啟用按需。
- 用量按**智慧體步驟和 token** 扣除，而不是按訊息條數；macOS 與 iOS 共享同一用量池。
- 免費試用給的是**額度**，同時有 7 天期限；大任務可能一次用光，且不補發。

## X 統一訂閱（2026-10-12～13 起，社群解讀）

- X Premium、Grok、Grok Bot、Cursor 合併為 **The X Subscription**，分 Plus / Premium / Super / Ultra 四檔，另有 \\$0 免費檔；年付為月付 10 倍。
- 每個付費席位**每週一個共享用量池**，Grok、Grok Bot、Cursor 共用；只覆蓋官方自家模型。
- **Plus 不含 Grok Bot**，至少 Premium。
- 老訂閱切換後**永久生效、無法撤銷**，先算清楚再切。

## 怎麼選

- 先確認自己要不要 Bot：只聊天/生圖 → 不需要含 Bot 的檔。
- 個人輕度使用 → 最低含 Bot 的檔位 + 節制例程頻率。
- 多 Bot、多例程、團隊 → 看每週用量與按需上限。

::: danger 已過時內容
{f(7)}、{f(8)} 中的"綁定 X 送 \\$100 開發者積分"舊玩法與舊資費已被新規取代。
:::
{src(c('help/grok-bot/plans','官方：方案和計費'), c('help/grok-bot/supergrok','官方：關聯 SuperGrok'), c('help/grok-bot/mobile-purchase','官方：行動裝置端購買'), f(16), f(18))}
""")
w("start/quickstart.md",f"""
# 快速入門：第一個 Bot

## 1. 安裝與登錄

1. 從 [Cursor 儀表盤的 Grok Bot 頁面](https://cursor.com/dashboard/bot) 下載桌面端（沒有儀表盤權限就找管理員要連結）；iPhone 在 App Store 安裝（iOS 18+）。
2. 歡迎頁選 **登錄**，在瀏覽器完成認證。用的就是 Cursor 帳戶，SSO 自動生效。
3. 使用舊版隱私模式的帳戶會被提示切換（Grok Bot 需要雲端儲存）。

## 2. 認識第一個 Bot

登錄後系統自動建立一個名為 **Grok Bot** 的 Bot。要更多 Bot：側邊欄 **+ 新建聊天 → 建立新 Bot**（團隊裡可選"建立新團隊 Bot"）。

**在第一條訊息裡給它一個主要職責，並讓它記住。** 聚焦職責的 Bot 比"萬能助手"積累的上下文更有用：

```text
你的職責是產品效能。使用我們的可觀測性工具調查效能問題。
保留連結和截圖，區分證據與假設，優先說明影響最大的問題。
絕不更改正式環境設定。請記住這些要求。
```

社群推薦的"六行合同"寫法（Own / Sources / Output / Approval / Failure / Never）：

```text
Own: 負責監控目標清單的每週功能與定價變動
Sources: 關注名單、目標官網 Changelog
Output: 不超過 8 條核心動態，附日期與原始連結，存入 /workspace/scan.md
Approval: 嚴禁對外發表內容，嚴禁主動發郵件
Failure: 頁面打不開就標為缺失，嚴禁推測或編造
```

## 3. 第一個任務

好請求 = **預期結果 + 重要來源 + 約束 + 交付物 + 在哪裡停下交給你**。五分鐘出結果的例子：

```text
用五個要點總結這份文件。在單獨的部分列出每個日期、決策和
未解決的問題，並註明對應章節。不要更改源文件。
```

## 4. 登錄它需要的工具

Bot 遇到登錄頁會把電腦控制權交給你：點 **打開電腦** → 接管 → 自己輸密碼/兩步驗證 → 交還。Bot 看不到密碼，會話保留供以後使用。支援的服務也可以直接連外掛。

## 5. 審查、修正、固化

提修改意見，說清長期偏好（比如固定的報告格式）。流程穩定後存成[技能或例程](/core/skills-routines)。允許 Bot 改外部系統前，先讀[權限與人閘](/advanced/security)。

## 驗收清單

- [ ] 側邊欄能看到 Bot 處於就緒狀態
- [ ] 發中文問候，回覆是中文（Bot 名字起中文名更容易預設中文）
- [ ] 右側能調出雲端電腦實時畫面
- [ ] 第一份交付物已保存為文件
{src(c('docs/grok-bot/get-started','官方：快速入門'), c('help/grok-bot/onboarding','官方：上手'), f(2), f(24)+"（摘要見實戰案例）")}
""")
w("start/first-handoff.md",f"""
# 一次好的交接

從一項**需要幾個工具、完成目標明確**的真實任務開始。官方範例：

> 從我們的 CRM 中獲取本週的銷售管道評審列表。跳過已處於活躍跟進序列中的人員。在網頁和 Slack 上調研排名前五的帳戶，找出合適的聯繫人，以我的口吻起草外聯內容，並在明天早上前留下草稿供我審批。

這條訊息說清了：**做什麼、在哪做、要取哪些上下文、完成後長什麼樣、哪裡要我批**。

## 交接樣板

```text
目標：……（完成後的樣子）
來源：……（系統 / 文件 / 網址）
約束：……（不能動什麼）
交付：……（文件格式、路徑）
停下點：……（發送、付款、刪除前先問我）
截止：……
```

## 之後

1. 審查結果並修正。
2. 讓 Bot 記住長期規則（"從現在起，未經批准絕不發送外部訊息"）。
3. 把穩定流程變成技能或例程。
{src(c('docs/grok-bot','官方：良好的首次交接'), c('docs/grok-bot/use-cases','官方：使用場景'))}
""")
w("start/faq.md",f"""
# 常見問題

**合上電腦還能繼續嗎？** 能。工作在雲端電腦上跑，關應用、合蓋、鎖手機都不影響後台輪次和例程。

**多個 Bot 能同時工作嗎？** 能。每個 Bot 在共享電腦上有自己的螢幕，但一個 Bot 同一時間只跑一個電腦操作任務。

**Bot 會記住什麼？** 穩定偏好、角色上下文、先前工作摘要。重要決策請讓它核查當前來源，別依賴記憶。

**任何網站都能用嗎？** 很多可以，但網站可能攔截自動化、讓會話失效或要求人工操作——Bot 會交給你，不會嘗試繞過。

**要立刻停下怎麼辦？** 發"立即停止"。停止不會撤銷已完成的操作。

**費用？** 見[方案與訂閱](/start/plans)。用量每週重置。

**需要幫助？** {c('help/grok-bot/get-help','官方：獲取幫助')}、{c('help/grok-bot/faqs','官方 FAQ')}。
{src(c('docs/grok-bot','官方總覽 FAQ'), c('help/grok-bot/faqs','官方 FAQ'), c('help/grok-bot/how-to','官方：操作指南'))}
""")

# ---------- 核心概念 ----------
w("core/bots.md",f"""
# Bot：建立、編輯與管理

Bot 是擁有**名稱、職責、專屬對話和持續積累上下文**的 AI 隊友。當一類工作有明顯不同的**目標、工具集、工作方式、審批邊界或定期安排**時，就值得單獨建一個 Bot。

## 建立

1. 側邊欄 **+**（或 Cmd+N）→ **Create new Bot**。
2. 第一條訊息說明**職責、資訊來源、審批邊界**，讓它記住；再發一個有完成標準的真實任務。
3. 點聊天頂部的 Bot 名稱可改名、加標記、換頭像。

## 長期規則 vs 任務

- **長期規則**："從現在起，未經批准，絕不發送外部訊息。" → 讓它記住。
- **任務**："為這十二個帳戶起草後續跟進。" → 普通訊息即可。

團隊 Bot 另有一段 **關於** 描述，由所有者編輯。

## 整理、分享、刪除

- **固定**常用 Bot；右鍵 **移至新分區** 按項目/客戶分組。
- **分享**會生成公開連結，暴露身份、描述、技能和例程——先刪掉 API 密鑰、內部 URL、客戶資訊。
- **刪除**會移除組態、對話和例程，但共享電腦上的**文件和登錄不會隨之刪除**，要另行清理。

## 編制建議（社群經驗）

- 一個 Bot 只管一個確定結果；主 Bot（幕僚長）只負責派活與驗收。
- 先 1 個，跑順再加；社群裡 29 個 Bot 的編制是一步步迭代來的。
{src(c('docs/grok-bot/work','官方：使用 Grok Bot · Bot'), c('help/grok-bot/edit-bot','官方：編輯 Bot'), f(2), f(65))}
""")
w("core/messaging.md",f"""
# 訊息、附件與接管

## 發訊息

- 可貼上文字、連結、圖片，附加文件；`/` 引用已保存的技能，`@` 提及其他 Bot。
- 你的私信**優先於後台工作**，可以改變當前輪次方向；發"立即停止"即停（不會撤銷已做的操作）。
- 說清**預期結果和決策邊界**：能改什麼、在哪一步必須停下。

## 附件

支援圖片、音訊、影片、PDF、Office、CSV、JSON、YAML、原始碼、HTML、郵件文件、筆記本等。

| 限制 | 值 |
|-|-|
| 每條訊息附件數（桌面） | 6 |
| 文件、圖片、音訊 | 每個 25 MB |
| 影片 | 200 MB |

**告訴 Bot 每個附件是什麼、拿來幹嘛**：

```text
PDF 是已簽署的政策文件，表格是本月交易記錄。根據政策核對表格，
為每個例外引用對應條款，返回新表格和簡短摘要。不要修改原文件。
```

## 敏感操作：接管電腦

需要登錄、兩步驗證、付款時，Bot 會交出控制權：打開電腦畫面 → Take over → 自己操作 → 交還。**永遠不要把密碼打在對話框裡。**

## 語音與行動裝置端

可與單個 Bot 語音聊天（群聊不支援）；iPhone 與桌面端共用同一批 Bot、對話、例程和電腦。
{src(c('docs/grok-bot/work','官方：訊息與協作'), c('help/grok-bot/voice-chat','官方：語音聊天'), c('help/grok-bot/mobile','官方：行動裝置端'))}
""")
w("core/computer.md",f"""
# 共享雲端電腦

你名下所有 Bot **共用一台雲端電腦**：同一檔案系統、同一瀏覽器登錄態、同一批已裝應用。電腦屬於你的帳戶而不是某個 Bot，所以放在上面的東西對你所有 Bot 都可見；不同使用者嚴格隔離。與隊友的團隊 Bot 聊天時，它通常也在**你的**電腦上執行。

## 關鍵事實

- 每個 Bot 有自己的螢幕，可並行；單個 Bot 同時只跑一個電腦操作任務。
- 客戶端右側可隨時看實時畫面，敏感步驟點 Take over 接管。
- 部分站點遮罩機房 IP：可在設定的 Computer 頁開啟"流量經過本地設備"。
- 雲端電腦可能因底層更新/維護被**重建**：自裝的應用和包會被移除（持久盤上的文件與登錄通常保留）。

## 推薦做法

1. 把雲端電腦當**可丟棄容器**：組態、服務清單、指令碼同步到私有 Git 倉庫。
2. 維護一份 `services-ledger.md`（服務用途、依賴、啟動命令、資料目錄）和一鍵 `restore.sh`。
3. 跨 Bot 交接用 `/workspace` 下的固定文件。
4. 憑證不落明文；登錄一律人工接管完成。

## 電腦壞了怎麼辦

見 {c('help/grok-bot/computer-recovery','官方：電腦恢復')}；企業管理員可在儀表盤 **Manage Bot Computers** 重建或終止成員電腦（詳見[團隊與企業](/admin/)）。
{src(c('docs/grok-bot','官方：你的 Bot 共用一台電腦'), c('docs/grok-bot/computers','官方：管理 Bot 電腦'), c('help/grok-bot/computer-recovery','官方：電腦恢復'), f(69), f(14))}
""")
w("core/memory.md",f"""
# 記憶與上下文

## 官方說法

Bot 會保留**穩定偏好、重要事實和工作摘要**，無需重放全部歷史也能保持角色。但**記憶不能替代權威來源**——變化中的事實留在源系統，需要時讓 Bot 重新取。每個 Bot 的對話和習得上下文彼此獨立；共享文件、瀏覽器會話和直接交接可以在 Bot 之間傳遞上下文。

## 分層（社群總結）

- **共享層**：共用記憶、公共技能、外掛/連線器、雲端電腦文件。
- **專屬層**：單個 Bot 的描述（長期合同）、專屬記憶、專屬例程。

## 三條原則

1. 記憶只記**判斷和指標**，經常變動的資料回源系統取。
2. 只有**核實過的結論**才寫入團隊共用記憶。
3. 記憶 ≠ 技能：偏好進記憶，**操作流程進技能**並指定維護人。

## 備份：記憶管家

建一個運維 Bot，每週例程匯出所有 Bot 的描述與共用記憶為 Markdown，提交到私有倉庫的 `bots-backup/charters/`、`bots-backup/memories/`。
{src(c('docs/grok-bot/work','官方：Bot 會記住什麼'), f(69), f(57)+"（英文，摘要見案例）", f(10))}
""")
w("core/skills-routines.md",f"""
# 技能與例程

- **技能（Skill）**：教 Bot *怎麼做*一件事的可複用流程。示範一次多步驟流程，Bot 就能存成技能；對話裡用 `/` 引用。
- **例程（Routine）**：告訴 Bot *何時*做——按計劃，或由 Slack 訊息、郵件、webhook、GitHub 等事件觸發。

> Skill 負責教授做事步驟，Bot 是承擔職責的隊友。先寫清流程的 Skill，再決定要不要專職 Bot。

## 設定例程

直接在聊天裡說："每個工作日上午 9:00，在此聊天中彙總新的支援工單。" Bot 會建立並顯示在例程列表。

- 查看：點 Bot 名稱 → **Details** → **例程**；每行可開關暫停。
- 打開某例程可見 **Instruction / When to run / Webhook**，按鈕 **Pause、Test、Edit、Delete**（刪除不可撤銷）。
- 時區取 **設定 → Bot → Timezone**（Auto-detect 跟隨本機）。
- **新建例程不會立即執行**，等下一個計劃點；要馬上試用 **Test**（會執行真實操作）。

## Webhook

讓 Bot 給例程加 webhook 觸發器，打開例程可複製 **POST to**（URL）、**key**（以 `Authorization: Bearer <key>` 攜帶）、**header**。可發 JSON 體，Bot 會連同指令一起收到。返回 **200 只代表已啟動一次執行**，結果看 Bot 聊天。

## Slack 觸發器

屬於例程而非 Slack 外掛：可在被提及、某短語出現、你加表情、收到任意訊息時啟動。**頻道與短語儘量收窄**。

## 省用量

每次執行都扣用量。用量掉得快 → 先暫停不需要的例程，再放寬頻率、收窄觸發器。避免"每 5 分鐘無過濾輪詢"。

## 例程沒跑？

檢查是否 Paused、When to run 與時區是否正確、是不是還沒到首次時間點。
{src(c('docs/grok-bot/work','官方：技能與例程'), c('help/grok-bot/routines','官方：例程'), f(66), f(12), f(6))}
""")
w("core/plugins.md",f"""
# 外掛、郵箱與 Secrets

## 接入順序：先跑通介面，再掛連線器

人能手動點完的事，先讓 Bot 用雲端電腦和瀏覽器去點；跑穩、驗證過價值，再換成外掛/連線器或指令碼，避免一次裝一堆外掛徒增維護。

## 外掛（連線器）

在設定裡連線支援的服務（如 Slack、GitHub、Google 等），Bot 以你的身份讀寫。外掛 ≠ 觸發器：要"某事發生就開工"請用[例程](/core/skills-routines)。

## Bot 專屬郵箱

對 Bot 說 `claim your email`，可獲得 `名字@mail.grokbot.com` 地址，用於收信、註冊網站、聯絡客戶；從該地址**發信前需要你在介面批准**。團隊帳號需管理員允許。

## Secrets

API Key 等放進設定的 **Secrets**，不要貼在對話裡。

## 技能/CLI 擴充

- 開源 Skill：把倉庫地址發給 Bot 說"幫我安裝"，所需 Key 放 Secrets。
- 雲端電腦上的 CLI 工具要在 Bot 電腦終端裡**單獨登錄**，不要拷貝本機登錄態（會互相頂 token）。
{src(c('help/grok-bot/connect-plugins','官方：連線外掛'), c('help/grok-bot/agent-email','官方：Bot 郵箱'), c('help/grok-bot/secrets','官方：Secrets'), f(68))}
""")
w("core/group-chats.md",f"""
# 群聊、多 Bot 協作與團隊 Bot

## 群聊

- 把多個 Bot 拉進同一對話；也可加隊友發表的團隊 Bot。
- 你在群裡發訊息，Bot 直接在群裡回；`@名字` 只發給某個 Bot。
- Bot 也會私信你或私信其他 Bot 交接工作，這些訊息出現在各自聊天裡，不進群。
- 想讓 Bot 只在群裡回："記住：在群組聊天中，要在群裡回覆。"
- **沒有禁止 Bot 互發訊息的開關**：告訴它"不要給其他 Bot 發訊息，先問我"，並讓它記住。
- **每條回覆都扣用量**，包括群回覆和 Bot 間訊息——群裡 Bot 越少越省。
- 群聊不支援語音。

## 團隊 Bot

團隊內所有成員都能與之聊天的 Bot，有獨立 Slack 應用和帳號名。在 Slack 頻道里要讓 Bot 之間交接，需要用團隊 Bot：

| Bot | 提問位置 | 能否給其他 Bot 發訊息 | 代表誰 |
|-|-|-|-|
| 個人 Bot | 應用內或 Slack 私信 | 能 | 你 |
| 個人 Bot | Slack 頻道訊息串 | 不能 | 無人（共享串） |
| 團隊 Bot | Slack 頻道或私信 | 能（發給該成員自己的 Bot） | 提及它的成員 |

## 協作建議

- 主 Bot 派活 + 專職 Bot 執行 + 文件落盤交接。
- 交接物寫到 `/workspace/<項目>/` 固定路徑。
{src(c('help/grok-bot/group-chats','官方：群組聊天'), c('help/grok-bot/team-bots','官方：團隊 Bot'), c('docs/grok-bot/work','官方：訊息與協作'), f(65), f(53))}
""")

# ---------- 進階（提綱） ----------
stub("advanced/usage.md","額度與成本優化",["額度扣除規則：按智慧體步驟與 token 計，非訊息條數","值得/不值得做的操作判斷","四步省額度工作流","額度耗盡應急與每週審計","例程頻率與群聊回覆是兩大消耗源"],
 [c('help/grok-bot/plans','官方：方案和計費'),c('help/grok-bot/models','官方：模型'),f(64),f(9),f(12),f(13),f(54)])
stub("advanced/team-orchestration.md","團隊編排：章程、崗位與放權",["主 Bot（幕僚長）只派活與驗收","六行合同式描述","從 1 個專職 Bot 逐步擴編","放權分級"],[f(65),f(45),f(35),f(36)])
stub("advanced/automation.md","觸發器與自動化：定時、Webhook、在 X 上派活",["定時例程設計","Webhook + iOS 快捷指令入庫","在 X 上派活","避免無增量輪詢"],[c('help/grok-bot/routines','官方：例程'),f(66),f(6),f(12)])
stub("advanced/security.md","權限、安全與人閘",["批准與 Auto Review","按可逆性分級：唯讀/草稿放行，外發/付費/刪除必批","網路策略與記錄","憑證處理"],[c('docs/grok-bot/security','官方：安全'),c('docs/grok-bot/security-faq','官方：安全 FAQ'),f(67)])
stub("advanced/backup.md","備份與災備",["雲端電腦重置會清掉自裝工具","服務總帳 + restore.sh","記憶管家每週匯出到私有倉庫","恢復提示詞"],[f(10),f(14),f(69)])
stub("advanced/im.md","外部入口：飛書 / 微信接入",["團隊接入飛書（飛書管家樣板）","微信聊天記錄打通（快捷指令）","微信一句話運營 X"],[f(15),f(11),f(29),f(34)])

# ---------- 案例（摘要索引） ----------
groups=[("自媒體與內容運營",[26,28,32,34,41]),("工程與研發",[25,31,50,51,58,62]),("電商",[27,38]),("一人公司 / AI 團隊",[44,47,48,52,55,59,60,61]),("GTM / 銷售",[40]),("綜合入門與技巧",[24,30,33,37,42,43,46,49,56])]
def summary(i):
    p=[x for x in os.listdir(R+"/sources/feishu") if x.startswith(f"{i:02d}_")][0]
    s=open(R+"/sources/feishu/"+p).read().split("-->",1)[1]
    import re
    m=re.search(r"\*\*整理者導讀\*\*\s*\n>\s*(.+)",s)
    if m: return m.group(1).strip()[:160]
    for line in s.splitlines():
        l=line.strip()
        if len(l)>40 and not l.startswith(("#",">","!","|","-","[")): return l[:160]
    return ""
lines=["# 實戰案例","","::: tip 說明\n社群長文版權歸原作者，本站僅提供摘要與原文連結（飛書收錄頁，內含原始出處）。\n:::",""]
for g,ids in groups:
    lines.append(f"## {g}\n")
    for i in ids: lines.append(f"- **{f(i)}**  \n  {summary(i)}…\n")
lines.append("## 鐵柱長文與推文合集\n")
for i in list(range(6,17))+[18,19,20,21]:
    tag=" **⚠️ 已過時**" if i in OLD else ""
    lines.append(f"- {f(i)}{tag}")
w("cases/index.md","\n".join(lines))
w("cases/outdated.md",f"# 已過時文章\n{OUT}\n- {f(7)}\n- {f(8)}\n\n最新規則見 {f(16)} 與[方案與訂閱](/start/plans)。")

# ---------- 團隊與企業 / 資源 ----------
stub("admin/index.md","團隊與企業",["團隊版與管理控制、樣板共享","身份與 SSO","私有網路與環境設定指令碼","代理","桌面端分發與版本","Manage Bot Computers：重建/終止（企業版）"],
 [c('docs/grok-bot/teams','官方：團隊版'),c('docs/grok-bot/identity','官方：身份'),c('docs/grok-bot/private-networks','官方：私有網路'),c('docs/grok-bot/proxies','官方：代理'),c('docs/grok-bot/deployment','官方：部署'),c('docs/grok-bot/computers','官方：管理 Bot 電腦'),c('help/grok-bot/delete-account','官方：刪除帳戶')])
stub("resources/index.md","資源",["提示詞庫（從各文抽取可直接發給 Bot 的提示詞）","術語表：Bot / 團隊 Bot / 技能 / 例程 / 外掛 / 人閘 / Auto Review","規則與版本變更時間線（8-11 上線 → 10-12 統一訂閱）","原文索引"],
 [f(0),f(18),f(19),f(20),f(21),c('docs/grok-bot/settings','官方：設定')])

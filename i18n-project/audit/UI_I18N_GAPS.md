# UI 多語言覆蓋缺口（翻譯後驗收清單）

- **審查日期**：2026-10-29（America/Los_Angeles）
- **範圍**：導覽 pill、頁腳、Changelog 篩選、PartBadge、小鐵柱落地頁、JoinCard 插槽、工具分類；以及同類主題元件/佈局（Home / DocEndCard / EcoIndex / ToolMeta / SEO meta）
- **方法**：對照 `i18n-project/PLAN.md` + `ENGINEERING.md`；倉庫掃 `site/docs/.vitepress/theme/*.vue`、`ui.json` / `locales/*/ui.json`、JSON 驅動文案與各語種 md；線上抽查 `https://bot.fmcat.top/en/`、`/en/changelog/`、`/en/tools/`、`/en/ecosystem/xiaotiezhu`、`/en/group`、`/en/part1/01-what-is`、`/ja/changelog/`、`/ko/`、`/es/tools/`（curl HTML，去 script/style 後檢索可見簡體）
- **結論一句話**：點名 chrome（nav pill / footer / Changelog 篩選與標題 / PartBadge / 小鐵柱 h1·hint / JoinCard alt）在**倉庫已於當日接入 `ui.json` + `localePath`**，但**線上尚未部署，非 zh 仍滿屏簡體**；倉庫內另餘 SEO meta、JSON-LD、友情連結站名等 P1。工程已在修，本清單供驗收不漏項。

## 狀態說明

| 標記 | 含義 |
|---|---|
| **線上 P0** | 線上非 zh 仍可見簡體；倉庫原始碼已修，**部署後必須復掃** |
| **倉庫開放** | 當前倉庫仍存在缺口 |
| **該區抽查通過** | 倉庫 +（若適用）線上文案已走 locale / 插槽譯文 |

---

## 點名區域

### 1. 導覽 pill（`NavGroupPill.vue`）

| 優先級 | 位置 | 當前簡體摘錄 | 問題型別 | 狀態 | 建議 |
|---|---|---|---|---|---|
| P0 | 頂欄 `nav-bar-content-after` · `NavGroupPill.vue` | `付費答疑群`；連結 `/group`（無語種前綴） | 硬寫程式（線上）；倉庫已改讀 `ui.json` → `nav.groupPill` + `localePath('/group')` | **線上 P0** | 部署後抽查 `/en/` 頂欄應為 Paid Q&A Group 等；連結須為 `/en/group` |

### 2. 頁腳（`SiteFooter.vue`）

| 優先級 | 位置 | 當前簡體摘錄 | 問題型別 | 狀態 | 建議 |
|---|---|---|---|---|---|
| P0 | 頁腳按鈕/鏈 | `公眾號「鐵柱AGI」`、`付費答疑群`、`關於作者` | 硬寫程式（線上）；倉庫已讀 `ui.footer.*` + `localePath` | **線上 P0** | 部署復掃；專名「鐵柱AGI」可保留 |
| P0 | 頁腳彈層/alt | `公眾號「鐵柱AGI」二維碼`、`微信搜一搜：鐵柱AGI` | 同上 | **線上 P0** | 部署復掃 `mpDialog` / `mpAlt` |
| P0 | 頁腳說明 | `友情連結`、`本站是社群非官方學習站，非 xAI 官方。` | 同上 | **線上 P0** | 部署復掃 `friends` / `note` |
| P1 | `friends.json` | `噪音之後`、`萬象 AI 實驗室` | JSON 未走 i18n（站名專有名詞） | **倉庫開放** | 可保留站名；若要譯加 `friends.<locale>.json` 或 ui 覆蓋 |

### 3. Changelog 篩選（`Changelog.vue`）

| 優先級 | 位置 | 當前簡體摘錄 | 問題型別 | 狀態 | 建議 |
|---|---|---|---|---|---|
| P0 | 頁標題 h1 | `更新記錄` | 硬寫程式（線上）；倉庫已 `clUi.title` | **線上 P0** | 部署後 `/en/changelog/` 應為 Changelog |
| P0 | 篩選 tab | `全部`、`行動裝置端`、`我們的解讀` | 硬寫程式（線上）；倉庫已 `tabAll`/`tabMobile`/`tabOurs` | **線上 P0** | 部署復掃 sticky tabs |
| P0 | chip | `我們的解讀` | 同上 → `chipOurs` | **線上 P0** | 部署復掃 |
| P0 | 日期格式 | `10月28日`、`2026 年 10 月` | 硬寫程式中文日期（線上）；倉庫已 `Intl.DateTimeFormat(bcp47(seg))` | **線上 P0** | 部署後應為 Oct 28 / October 2026 等 |

正文條目：`changelog.json` 各語種覆蓋已存在；倉庫已把 `items` 改為 `computed`。線上抽查 en 條目標題已為英文（資料層早於 chrome 修復）。

### 4. PartBadge（`PartBadge.vue`）

| 優先級 | 位置 | 當前簡體摘錄 | 問題型別 | 狀態 | 建議 |
|---|---|---|---|---|---|
| P0 | `doc-before` badge 文案 | `第一篇 · 使用手冊` 等（簡體 label 寫死在 skins） | 硬寫程式 + 路徑取 `path[0]`（locale 頁不渲染） | **線上**：非 zh 常不顯示；**倉庫已修** `partKeyFromPath` + `ui.parts.*` | 部署後打開 `/en/part1/01-what-is` 應出現 Part 1 · Handbook，勿再露簡體 |

### 5. 小鐵柱落地頁（`XiaoTiezhuLanding.vue`）

| 優先級 | 位置 | 當前簡體摘錄 | 問題型別 | 狀態 | 建議 |
|---|---|---|---|---|---|
| P0 | Hero h1 | `小鐵柱` | 硬寫程式（線上）；倉庫已 `xtUi.title`（en ui 仍為產品名「小鐵柱」） | **線上 P0** / 產品名策略 | 部署復掃；若需拉丁化由產品定，非缺譯事故 |
| P0 | JoinCard 插槽 hint | `掃碼新增管家微信，開通小鐵柱` | 硬寫程式（線上）；倉庫已 `xtUi.joinHint` | **線上 P0** | 部署後應為 Scan to add butler WeChat… |
| P1 | `en|ja|ko|es|pt-BR/.../xiaotiezhu.md` frontmatter `title` | `小鐵柱` | 缺譯（或產品名保留） | **倉庫開放（策略）** | 與 ui.xiaotiezhu.title 對齊策略；瀏覽器標記目前一律簡體產品名 |
| — | 其餘區塊 | slogan/CTA/FAQ 等 | — | **該區抽查通過**（走 `ecosystem.json` locale） | — |

### 6. JoinCard 插槽（`JoinCard.vue` + md）

| 優先級 | 位置 | 當前簡體摘錄 | 問題型別 | 狀態 | 建議 |
|---|---|---|---|---|---|
| — | `group.md` / 各語種 `*/group.md` 預設插槽 | （各語種已譯；專名/驗證語「小紅書」按真源保留） | — | **該區抽查通過** | 保持插槽在 md 側維護 |
| — | `xhs` 模式文案 | `join_*` / `copy_btn` 等 | — | **該區抽查通過**（`funnel.json` locale） | — |
| P0 | QR `alt` | `鐵柱的個人微信二維碼` | 硬寫程式（線上）；倉庫已 `ui.join.qrAlt` | **線上 P0** | 部署復掃 |

### 7. 工具分類（`ToolIndex.vue` / `ToolMeta.vue` / `tools.json`）

| 優先級 | 位置 | 當前簡體摘錄 | 問題型別 | 狀態 | 建議 |
|---|---|---|---|---|---|
| — | 分類 tab / 卡片 cat | 線上 en 已見 `Coding Agents` 等 | — | **該區抽查通過**（`tools.json` locale + `ui.all` 等） | — |
| P1 | `ToolMeta`/`ToolIndex` skin 對應 | 原始碼內含簡體 key（對應表，非直接渲染） | 維護型硬寫程式 | **倉庫開放（低）** | 改按 root `cat` id 或 `rootCatById` 穩定鍵，避免多語種 label 漂移；線上曾出現 `/bots/undefined.svg`（舊 ToolMeta），倉庫已補多語種 skin |

---

## 同類主題 / 佈局附加項

| 優先級 | 位置 | 當前簡體摘錄 | 問題型別 | 狀態 | 建議 |
|---|---|---|---|---|---|
| P0 | `Home.vue` 內鏈 | 線上 en 首頁 CTA 仍指向 `/part1/...`、`/group`（無 `/en`）→ 點進整頁變中文 | 連結未加 locale（線上）；倉庫已全面 `localePath(...)` | **線上 P0** | 部署後點「Start from Chapter 1」須留在 `/en/part1/...` |
| P0 | `DocEndCard.vue` | 線上非 zh 文件頁常不出現（舊正則不認 `/en/part…`）；若出現按鈕鏈到 `/group` | 路徑未剝 locale（線上）；倉庫已 `stripLocalePrefix` + `localePath('/group')` + funnel 文案 | **線上 P0** | 部署後 `/en/part1/02-plans` 文末應出英文 CTA |
| P1 | `Home.vue` `segs()` | 按 `，。；！？` 切句 | 中文標點假設 | **倉庫開放** | 擴拉丁標點或按語種分支；不直接露中文 |
| P1 | `.vitepress/seo.json` | 全站 `og:description` / `twitter:description` 仍用簡體 `home` 等（線上 en 首頁已確認） | JSON 未走 i18n | **倉庫開放** | 按語種覆蓋或改用各頁 frontmatter `description`；`seo.json` 現無 `en/` key |
| P1 | `config.mts` JSON-LD | `inLanguage: 'zh-CN'` 多處寫死 | 硬寫程式 | **倉庫開放** | 按頁 locale 輸出；見 ENGINEERING 已知項 |
| — | `EcoIndex` / `BotHire` / `ClipperLanding` | 主體走 locale JSON | — | **該區抽查通過**（Eco 卡片名「小鐵柱」同產品名策略） | Eco 卡片 `pages` 已 `localePath` |
| — | VitePress `themeConfig.nav` / outline / docFooter | 各 locale 已在 `config.mts` 組態 | — | **該區抽查通過** | 語言選單中的「簡體中文」等為語種名，非洩漏 |

---

## 線上 vs 倉庫對照（驗收必讀）

| 現象 | 線上（抽查時） | 倉庫（2026-10-29 ~18:03 +08 原始碼） |
|---|---|---|
| Nav pill / Footer 簡體 | 有 | 已接 `ui.json` |
| Changelog 標題/tab/日期中文 | 有 | 已接 `ui.json` + Intl |
| PartBadge | 非 zh 多不顯示 | 已修路徑 + `ui.parts` |
| 小鐵柱 h1 / joinHint | 簡體 | 已接 `ui.xiaotiezhu` |
| JoinCard alt | 簡體 | 已接 `ui.join.qrAlt` |
| Home / DocEnd / Tool 內鏈無 locale | 有 | 已 `localePath` / `stripLocalePrefix` |
| 工具分類文案 | en 已英文 | 通過 |
| JoinCard group 插槽 | 各語種已譯 | 通過 |
| SEO og:description 簡體 | 有 | **仍有** |
| friends 站名簡體 | 有 | **仍有** |

**部署後驗收口令**：打開 `/en/`、`/en/changelog/`、`/en/ecosystem/xiaotiezhu`、`/en/part1/01-what-is`、`/ja/changelog/`，確認頂欄 pill、頁腳、Changelog tabs、PartBadge、小鐵柱 hint 無簡體；Home CTA 不掉回根站中文。

---

## 按區域彙總

| 區域 | P0（含線上待部署） | P1 | 抽查通過 |
|---|---:|---:|---|
| 導覽 pill | 1 | 0 | — |
| 頁腳 | 3 | 1 | — |
| Changelog 篩選/標題/日期 | 4 | 0 | 正文資料層 |
| PartBadge | 1 | 0 | — |
| 小鐵柱落地頁 | 2 | 1 | 其餘區塊 |
| JoinCard | 1 | 0 | 插槽 / xhs / funnel |
| 工具分類 | 0 | 1 | 分類文案 |
| Home / DocEnd / SEO / 其它 | 2 | 3 | Eco/BotHire/Clipper/nav config |
| **合計（條目）** | **14** | **6** | 見上 |

說明：14 條 P0 中 **12 條為「線上仍見、倉庫已修」**，**0 條點名 chrome 在倉庫仍硬寫程式**；**2 條**（Home 掉語種、DocEnd 路徑）同屬待部署。倉庫真正仍開放的以 **6 條 P1** 為主（SEO、JSON-LD、friends、segs、skin 對應、小鐵柱 title 策略）。

### Top 5 最刺眼缺口（按讀者體感）

1. **頂欄 pill「付費答疑群」**（全站非 zh 首屏）— 線上 P0，倉庫已修待部署  
2. **頁腳整組簡體**（公眾號 / 付費答疑群 / 關於作者 / 非官方宣告）— 線上 P0，倉庫已修待部署  
3. **Changelog「更新記錄」+「全部/行動裝置端/我們的解讀」+「×月×日」** — 線上 P0，倉庫已修待部署  
4. **小鐵柱頁 hint「掃碼新增管家微信，開通小鐵柱」**（及 h1）— 線上 P0，倉庫已修待部署  
5. **SEO `og:description` 全語種仍簡體**（分享卡片）— **倉庫仍開放 P1**；疊加 Home CTA 無 locale 時一點就回中文站（線上 P0，倉庫已修）

---

## 備註

- 工程與翻譯官已在修硬寫程式；`theme/ui.json` + `theme/locales/*/ui.json` 六語種 key 已齊，元件接線落在 `NavGroupPill` / `SiteFooter` / `PartBadge` / `Changelog` / `XiaoTiezhuLanding` / `JoinCard` 等。  
- **本清單供驗收**：部署後按「線上 vs 倉庫」表復掃；未部署前勿關閉 P0。  
- 禁止項遵守：本文件只列問題，未改原始碼、未譯正文、未動 locales 腳手架內容（只新增本審計 md）。

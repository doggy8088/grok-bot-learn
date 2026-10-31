# 翻譯進度

- 更新時間：2026-10-30 10:36 (Asia/Singapore)
- 狀態：**UI locale key 巡檢有實質改動**（補 changelog ours 新條目 id 2115752949276123606；未 push/deploy）

| 語種 | 正文 SOURCE_PAGES | UI JSON (home/funnel/ui 等) | chrome ui.json | tools.prompt | changelog ours |
|---|---|---|---|---|---|
| zh-Hant | 61/61 | 齊 | 齊 | 齊 | **本輪補 1 條** |
| en | 61/61 | 齊 | 齊 | 齊 | **本輪補 1 條** |
| ja | 61/61 | 齊 | 齊 | 齊 | **本輪補 1 條** |
| ko | 61/61 | 齊 | 齊 | 齊 | **本輪補 1 條** |
| es | 61/61 | 齊 | 齊 | 齊 | **本輪補 1 條** |
| pt-BR | 61/61 | 齊 | 齊 | 齊 | **本輪補 1 條** |

## 本輪巡檢（routine 學習站 UI locale key 巡檢）
- 對比 root：`home.json` / `funnel.json` / `ui.json` / `ecosystem.json` / `tools.json` / `bots.json` / `changelog.json`；六語種覆蓋文件
- **新 key**：`changelog.json` `ours[0]`（id `2115752949276123606`，2026-10-29「上線購物卡、Pages和Vault」）六語種此前缺譯；root mtime 2026-10-30 10:23
- `friends.json` / `links.json`：無 locale 覆蓋（友鏈品牌名 + URL；屬預期）
- JoinCard / NavGroupPill / SiteFooter：已用 `useLocaleJson`，無硬寫程式「付費答疑群」
- 付費語義抽檢：ui.nav.groupPill / footer.group / funnel.join_title → 付費 / Paid / 有料 / 유료 / pago **PASS**
- group.md 六語種抽檢：**PASS**（無簡體短語殘留）
- **缺口修復**：六語種 `locales/*/changelog.json` 在 `ours` 頭部插入譯好的新條目（zh-Hant=OpenCC s2twp；en/ja/ko/es/pt-BR=agy gemini-3.8-flash-high）

### 抽檢 PASS
- en title: Shopping Cards, Pages, and Vault Launched
- ja title: ショッピングカード、Pages、Vault が登場
- ko title: 쇼핑 카드, Pages 및 Vault 출시
- es title: Lanzamiento de tarjetas de compras, Pages y Vault
- pt-BR title: Lançamento de cards de compras, Pages e Vault
- zh-Hant title: 上線購物卡、Pages和Vault
- ui/funnel 付費語義 + group.md：六語種 PASS

## 產出路徑
- 改動文件：
  - `site/docs/.vitepress/theme/locales/zh-Hant/changelog.json`
  - `site/docs/.vitepress/theme/locales/en/changelog.json`
  - `site/docs/.vitepress/theme/locales/ja/changelog.json`
  - `site/docs/.vitepress/theme/locales/ko/changelog.json`
  - `site/docs/.vitepress/theme/locales/es/changelog.json`
  - `site/docs/.vitepress/theme/locales/pt-BR/changelog.json`
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`

---

# 翻譯進度

- 更新時間：2026-10-30 09:48 (Asia/Singapore)
- 狀態：**NO_CHANGE**（UI locale key 巡檢無新 key、無硬寫程式抽出、無簡體殘留；未改 locale 文件、未 push/deploy）

| 語種 | 正文 SOURCE_PAGES | UI JSON (home/funnel/ui 等) | chrome ui.json | tools.prompt | changelog official |
|---|---|---|---|---|---|
| zh-Hant | 61/61 | 齊 | 齊 | 齊 | 齊 |
| en | 61/61 | 齊 | 齊 | 齊 | 齊 |
| ja | 61/61 | 齊 | 齊 | 齊 | 齊 |
| ko | 61/61 | 齊 | 齊 | 齊 | 齊 |
| es | 61/61 | 齊 | 齊 | 齊 | 齊 |
| pt-BR | 61/61 | 齊 | 齊 | 齊 | 齊 |

## 本輪巡檢（routine 學習站 UI locale key 巡檢）
- 對比 root：`home.json` / `funnel.json` / `ui.json` / `ecosystem.json` / `tools.json` / `bots.json` / `changelog.json`；六語種 `theme/locales/<loc>/` 覆蓋文件
- **缺 key：無**（各文件 key/leaf 與 root 一致）
- `friends.json` / `links.json`：無 locale 覆蓋（友鏈品牌名 + URL；SiteFooter / Clipper 直接 import，屬預期）
- 上一輪 STATUS 2026-10-29 22:59 之後：root JSON mtime 均早於或等於對應 locale（home/funnel/ui/bots/changelog/ecosystem/tools **無工程新增 key**）
- JoinCard.vue / NavGroupPill.vue / SiteFooter.vue：已用 `useLocaleJson`（funnel.json / ui.json），無硬寫程式「付費答疑群」；Home.vue / DocEndCard.vue 同樣走 locale JSON
- 付費語義抽檢：ui.nav.groupPill / footer.group / funnel.join_title / home.groupTitle → 付費 / Paid / 有料 / 유료 / pago（de pago / pago）齊全
- group.md 六語種抽檢：**PASS**（無簡體短語殘留；專名 鐵柱AGI / 小紅書 / AI_Tiezhu / 小鐵柱 按 DO_NOT_TRANSLATE 保留）
- SAME_AS_ROOT CJK：僅品牌名（小鐵柱、鐵柱、冬青）或繁簡同形字，非缺譯

### 抽檢 PASS
- zh-Hant/en/ja/ko/es/pt-BR：`ui.json` groupPill；`funnel.json` join_title；`home.json` groupBtn
- group.md：`site/docs/{zh-Hant,en,ja,ko,es,pt-BR}/group.md` + 根站 `site/docs/group.md`

## 產出路徑
- 改動文件：無
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`

---

# 翻譯進度

- 更新時間：2026-10-29 22:59 (Asia/Singapore)
- 狀態：**UI locale key 巡檢有實質改動**（補 ko changelog 簡體殘留 + en/ja/es tools.prompt + zh-Hant ui.src；未 push/deploy）

| 語種 | 正文 SOURCE_PAGES | UI JSON (home/funnel/ui 等) | chrome ui.json | tools.prompt | changelog official |
|---|---|---|---|---|---|
| zh-Hant | 61/61 | 齊 | 已潤色 | 齊（本輪 ui.src 來源） | 齊 |
| en | 61/61 | 齊 | 已潤色 | **本輪補 19 條** | 齊 |
| ja | 61/61 | 齊 | 已潤色 | **本輪補 19 條** | 齊 |
| ko | 61/61 | 齊 | 已潤色 | 齊（此前已譯） | **本輪補 2 葉** |
| es | 61/61 | 齊 | 已潤色 | **本輪補 19 條** | 齊 |
| pt-BR | 61/61 | 齊 | 已潤色 | 齊（此前已譯） | 齊 |

## 本輪巡檢（routine 學習站 UI locale key 巡檢）
- 對比 root：`home.json` / `funnel.json` / `ui.json` / `ecosystem.json` / `tools.json` / `bots.json` / `changelog.json`；六語種覆蓋文件
- **缺 key：無**（各文件 leaf 計數與 root 一致）；friends.json / links.json 無 locale 文件（品牌名+URL，屬預期）
- 上一輪 STATUS 19:12 之後：root bots.json(18:14) / changelog 等 **無新增 key**
- JoinCard / NavGroupPill / SiteFooter：已用 `useLocaleJson`，無硬寫程式「付費答疑群」
- group.md 六語種抽檢：**PASS**（無簡體短語殘留；付費語義 付費/Paid/有料/유료/pago 齊全）
- **缺口修復**：
  1. `locales/ko/changelog.json`：`official[6].full[2][0]`「修復」→「수정 사항」；`official[76].full[0][1][2]`「簡化了 Bot 的建立與管理」→「Bot 생성 및 관리를 간소화했습니다」
  2. `locales/{en,ja,es}/tools.json`：19 條 `tools[*].prompt` 此前仍為簡體（pt-BR/ko/zh-Hant 已譯）；agy gemini-3.8-flash-high 補譯
  3. `locales/zh-Hant/tools.json`：`ui.src`「來源」→「來源」（OpenCC）

### 抽檢 PASS
- en tools[0].prompt 以 “Help me install…” 開頭；含 Antigravity URL
- ja tools[0].prompt 含「クラウドPC」；es tools[0] 以 “Ayúdame…” 開頭
- ko changelog pc-0.75.5 分區標記「수정 사항」；ios-1.1 full 條目韓語「Bot 생성 및 관리를 간소화했습니다」
- zh-Hant tools ui.src=來源；ui.nav.groupPill / funnel.join_title 付費語義仍齊全

## 產出路徑
- 改動文件：
  - `site/docs/.vitepress/theme/locales/ko/changelog.json`
  - `site/docs/.vitepress/theme/locales/en/tools.json`
  - `site/docs/.vitepress/theme/locales/ja/tools.json`
  - `site/docs/.vitepress/theme/locales/es/tools.json`
  - `site/docs/.vitepress/theme/locales/zh-Hant/tools.json`
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`

---

# 翻譯進度

- 更新時間：2026-10-29 19:12 (Asia/Singapore)
- 狀態：**UI locale key 巡檢有實質改動**（補 zh-Hant changelog 兩條官方更新；未 push/deploy）

| 語種 | 正文 SOURCE_PAGES | UI JSON (home/funnel/ui 等) | chrome ui.json | changelog official |
|---|---|---|---|---|
| zh-Hant | 61/61 | 齊 | 已潤色 | **本輪補 ios-1.19.0 / pc-0.78.1** |
| en | 61/61 | 齊 | 已潤色 | 齊（79） |
| ja | 61/61 | 齊 | 已潤色 | 齊（79） |
| ko | 61/61 | 齊 | 已潤色 | 齊（79） |
| es | 61/61 | 齊 | 已潤色 | 齊（79） |
| pt-BR | 61/61 | 齊 | 已潤色 | 齊（79） |

## 本輪巡檢（routine 學習站 UI locale key 巡檢）
- 對比 root：`home.json` / `funnel.json` / `ui.json` / `ecosystem.json` / `tools.json` / `bots.json` / `changelog.json`；六語種覆蓋文件
- home/funnel/ui/ecosystem/bots：六語種 **無缺 key**；friends.json / links.json 無 locale 文件（友鏈品牌名 + URL，SiteFooter/Clipper 直接 import，屬預期）
- JoinCard / NavGroupPill / SiteFooter：已用 `useLocaleJson`，無硬寫程式「付費答疑群」
- group.md 六語種抽檢：**PASS**（無簡體短語殘留；專名 鐵柱AGI / 小紅書 / AI_Tiezhu 保留；付費語義 付費/Paid/有料/유료/pago 齊全）
- **缺口修復**：`theme/locales/zh-Hant/changelog.json` 缺工程今日新增 `ios-1.19.0`、`pc-0.78.1`（因 whole-file 覆蓋，繁中頁原先看不到這兩條）。OpenCC s2twp 從 root 補譯並前置；`updated` → 2026-10-29；專名 Shop Pay / Bot / Grok Bot 保留

### 抽檢 PASS
- zh-Hant changelog ios-1.19.0 title「日常問題修復與體驗最佳化」；points 含「修復／應用／體驗」繁體
- zh-Hant changelog pc-0.78.1 title「新增購物卡片與訂閱管理」；points 含「支援／追蹤／訂閱」；Shop Pay 未改
- en/ja/ko/es/pt-BR group.md + ui.nav.groupPill / funnel.join_title：付費語義齊全

## 產出路徑
- 改動文件：`site/docs/.vitepress/theme/locales/zh-Hant/changelog.json`
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`

---

# 翻譯進度

- 更新時間：2026-10-29 03:48 (America/Los_Angeles)
- 狀態：**UI locale key 巡檢有實質改動**（補譯 ko ecosystem FAQ 題幹；未 push/deploy）

| 語種 | 正文 SOURCE_PAGES | UI JSON (home/funnel 等) | chrome ui.json |
|---|---|---|---|
| zh-Hant | 61/61 | 齊 | 已潤色 |
| en | 61/61 | 齊 | 已潤色 |
| ja | 61/61 | 齊 | 已潤色 |
| ko | 61/61 | **本輪補 FAQ.q** | 已潤色 |
| es | 61/61 | 齊 | 已潤色 |
| pt-BR | 61/61 | 齊 | 已潤色 |

## 本輪巡檢（routine 學習站 UI locale key 巡檢）
- home/funnel/ui：六語種 **無缺 key**；付費答疑群 chrome 已抽出且含 paid/付費/有料/유료/pago
- JoinCard / NavGroupPill / SiteFooter：已用 useLocaleJson，無新增硬寫程式「付費答疑群」
- group.md 六語種抽檢：**PASS**（無簡體殘留；專名 鐵柱AGI / 小紅書 保留）
- **缺口修復**：`theme/locales/ko/ecosystem.json` 中 clipper+xiaotiezhu 共 11 條 FAQ **題幹**此前仍為簡體（答案已是韓語），agy gemini-3.8-flash-high 補譯

### 抽檢 PASS
- ko funnel join_title / ui.nav.groupPill 含「유료」
- ko ecosystem FAQ.q 不再等於 zh-CN
- en/ja/es/pt-BR/zh-Hant group.md：無簡體短語殘留

## 產出路徑
- 改動文件：`site/docs/.vitepress/theme/locales/ko/ecosystem.json`
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`

---

# 翻譯進度

- 更新時間：2026-10-29 03:10 (America/Los_Angeles)
- 狀態：**ui.json chrome 已潤色完成**（agy / OpenCC；未 push/deploy）

| 語種 | 正文 SOURCE_PAGES | UI JSON (home/funnel 等) | chrome ui.json |
|---|---|---|---|
| zh-Hant | 61/61 | 齊 | **已潤色**（OpenCC + 專名回寫） |
| en | 61/61 | 齊 | **已潤色**（agy） |
| ja | 61/61 | 齊 | **已潤色**（agy + 專名） |
| ko | 61/61 | 齊 | **已潤色**（agy + 專名） |
| es | 61/61 | 齊 | **已潤色**（agy） |
| pt-BR | 61/61 | 齊 | **已潤色**（agy） |

## 本輪完成
- 工程抽出 `theme/ui.json` 後，六語種 `theme/locales/*/ui.json` 全 key 潤色
- 專名強制：鐵柱AGI / 小鐵柱（禁止 鐵/鉄/철주/소철주）
- nav.groupPill / footer.group 均含付費語義（付費/Paid/有料/유료/pago）
- group.md 六語種抽檢 **PASS**
- 詳志：`i18n-project/logs/ui-json-polish-STATUS.md`

## 產出路徑
- 正文：`site/docs/<locale>/`
- UI：`site/docs/.vitepress/theme/locales/<locale>/`
- chrome：`site/docs/.vitepress/theme/locales/<locale>/ui.json`


# 學習站多語言工程 · 翻譯官接入手冊

## 目錄約定

```
site/docs/
├── index.md                  ← zh-CN 根站首頁（真源）
├── part1/ part2/ part3/ part4/ cases/ tools/ bots/ ecosystem/ changelog/
│                             ← 簡體中文正文（真源，不動）
├── en/                       ← English
│   └── index.md              ← 佔位首頁，翻譯官在此目錄下補充譯文
├── zh-Hant/                  ← 繁體中文
├── ja/                       ← 日本語
├── ko/                       ← 한국어
├── es/                       ← Español
└── pt-BR/                    ← Português (Brasil)
```

每個非 root 語種目錄復刻與根站相同的子目錄結構。例如英文版第 1 章：
```
site/docs/en/part1/01-what-is.md
```

**禁止**把 61 篇簡體正文整庫複製到各語種。翻譯官按頁翻譯，一篇 ready 放一篇。

## 翻譯官接入步驟

1. 在 `site/docs/<locale>/` 下新建與根站同路徑的 `.md` 文件。
2. 如果該頁需要 sidebar，在 `config.mts` 對應 locale 的 `themeConfig.sidebar` 中加入條目（加語種前綴）。**zh-Hant 已接好**：`sidebar.zh-Hant.json` + `config.mts` 中 `sidebarZhHant` / 完整 nav；其他語種仍多為佔位空 sidebar，譯文齊後再接。
3. 建構驗證：`cd site && npm run build`。
4. `npm run dev` 打開 `http://localhost:5173/<locale>/` 預覽。

## JSON 驅動頁的多語言規則

### 同結構分文件（推薦）

在 `site/docs/.vitepress/theme/locales/<locale>/` 放與 root JSON 同名文件。只需包含要覆蓋的欄位：

```
theme/locales/en/home.json      ← 覆蓋 theme/home.json 的英文欄位
theme/locales/ja/tools.json     ← 覆蓋 theme/tools.json 的日文欄位
```

元件使用 `useLocaleJson(rootData, 'home.json')` 獲取合併後的資料（缺譯回退簡體）。

### 元件接入範例

```ts
// 原來的 import
import copy from './home.json'

// 改為 locale 感知
import rootCopy from './home.json'
import { useLocaleJson } from './i18n'
const copy = useLocaleJson(rootCopy, 'home.json')
// 樣板中用 copy.value.title（注意 .value，因為返回的是 ComputedRef）
```

### JSON 文件命名

| root 文件 | locale 覆蓋路徑 |
|---|---|
| `theme/home.json` | `theme/locales/<locale>/home.json` |
| `theme/tools.json` | `theme/locales/<locale>/tools.json` |
| `theme/bots.json` | `theme/locales/<locale>/bots.json` |
| `theme/ecosystem.json` | `theme/locales/<locale>/ecosystem.json` |
| `theme/changelog.json` | `theme/locales/<locale>/changelog.json` |
| `theme/funnel.json` | `theme/locales/<locale>/funnel.json` |
| `theme/ui.json` | `theme/locales/<locale>/ui.json`（導覽 pill / 頁腳 / 篇章徽章 / Changelog 篩選標題 / 小鐵柱標題 / JoinCard alt） |
| `.vitepress/seo.json` | 暫無 locale 覆蓋機制，SEO 描述按語種寫在各頁 frontmatter `description` |
| `.vitepress/sidebar.json` | 各語種 sidebar 通過 `config.mts` 的 `locales.<key>.themeConfig.sidebar` 組態 |

### UI 字串與內部連結

可見 UI 短文案走 `theme/ui.json` + `theme/locales/<locale>/ui.json`，元件用 `useLocaleJson`；內部連結用 `useLocalePath()`（`localePath`）按當前語種加前綴（zh-CN 根站無前綴）。

## 禁止翻譯的內容

- 產品名：Grok Bot、Grok、xAI、Cursor、SuperGrok、Hermes
- 人名：鐵柱AGI
- URL / 域名 / 倉庫地址
- 程式碼塊 / shell 命令
- 非官方宣告原文：「本站是社群非官方學習站，非 xAI 官方。」（各語種需保持同等含義）

## hreflang / og:locale 行為

每個頁面的 `<head>` 包含：
- `<link rel="alternate" hreflang="zh-Hans" href="https://bot.fmcat.top/..." />`（根站）
- `<link rel="alternate" hreflang="en" href="https://bot.fmcat.top/en/..." />`
- 同理 `zh-Hant`、`ja`、`ko`、`es`、`pt-BR`
- `<link rel="alternate" hreflang="x-default" href="https://bot.fmcat.top/..." />`（指向根站對等頁）
- `<meta property="og:locale" content="<當前語種 og 格式>" />`
- `<meta property="og:locale:alternate" content="..." />`（其餘 6 種）

### og:locale 對應

| 語種 | og:locale |
|---|---|
| zh-CN | zh_CN |
| zh-Hant | zh_TW |
| en | en_US |
| ja | ja_JP |
| ko | ko_KR |
| es | es_ES |
| pt-BR | pt_BR |

## 語言切換

VitePress 內建 locales 下拉（`VPNavBarTranslations`）。

- **桌面（≥960px）**：右上角與主題切換（appearance）並排顯示；主題自訂 CSS 把預設 ≥1280px 的可見閾值下調到 ≥960px，與 appearance 對齊。
- **平板過渡（960–1279px）**：頂欄直接顯示語言/主題切換；`VPNavBarExtra` 內的重複 translations / appearance 項隱藏。
- **行動裝置端（<960px）**：頂欄不單獨露出語言切換，改在漢堡選單內的 Translations 選擇語種。

切換時替換當前路徑的語種前綴。如果目標語種無對等頁，瀏覽器顯示 404。

## llms.txt / llms-full.txt

`buildEnd` 只索引根站（zh-CN）正文。多語言 llms.txt 暫不分語種生成。如需分語種索引，在 `buildEnd` 內按 locale 前綴過濾 `cfg.pages` 再單獨生成。

## 建構與部署

```bash
cd site
npm run build        # 產物在 docs/.vitepress/dist/
npm run preview      # 本地預覽 http://localhost:5173
```

build 產物路徑不變（`docs/.vitepress/dist/`），非 root 語種頁面在 `dist/en/`、`dist/ja/` 等子目錄。`deploy.sh` 無需修改。

## 本地預覽各語種

```bash
cd site && npm run dev
# 根站：http://localhost:5173/
# 英文：http://localhost:5173/en/
# 日文：http://localhost:5173/ja/
# 韓文：http://localhost:5173/ko/
# 西文：http://localhost:5173/es/
# 巴葡：http://localhost:5173/pt-BR/
# 繁中：http://localhost:5173/zh-Hant/
```

## JSON-LD inLanguage

當前 JSON-LD schema 的 `inLanguage` 欄位硬寫程式為 `'zh-CN'`。翻譯官補充正文後，需按頁面實際語種更新（可在後續階段統一處理）。

## 六語種接線狀態（2026-10-29）

- 全部非 root 語種（zh-Hant/en/ja/ko/es/pt-BR）已有完整 `sidebar.<locale>.json` + `config.mts` nav/sidebar。
- 主題 JSON 經 `useLocaleJson` 讀取 `theme/locales/<locale>/`；**UI 字串走 theme/locales + localePath**（`ui.json`）。
- 語言切換：桌面右上角與主題切換並排（≥960px）；行動裝置端在漢堡選單。
- **未 push / 未 deploy**；上線策略由鐵柱選定後執行。見 `logs/all-locales-wire-SELF_CHECK.md`。

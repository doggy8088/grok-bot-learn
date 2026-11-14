# go-live SELF_CHECK（本地，未 deploy）

- **時間**：2026-10-29 17:06 Asia/Singapore
- **倉庫**：`/workspace/grok-bot-learn`（branch `main`）
- **站點**：https://bot.fmcat.top（本次未部署）

## 驗收項

| # | 項 | 結果 | 證據 |
|---|---|---|---|
| 1 | CSS 切換器規則（≥960px 顯示 VPNavBarTranslations / translations） | **PASS** | `site/docs/.vitepress/theme/style.css` L1017–1032：`@media (min-width: 960px)` 對 `.VPNavBar .content-body > .VPNavBarAppearance/.VPNavBarTranslations/.translations` 設 `display:flex !important`；960–1279 隱藏 `.VPNavBarExtra .group.translations` 與 `.item.appearance`。產物 `site/docs/.vitepress/dist/assets/style.CK8Kwh2Y.css` 含同規則（minify）。 |
| 2 | locales 七語種全開 | **PASS** | `config.mts` `locales`：`root`（簡體中文/zh-CN）、`zh-Hant`（/zh-Hant/）、`en`（/en/）、`ja`（/ja/）、`ko`（/ko/）、`es`（/es/）、`pt-BR`（/pt-BR/）；均有 label，非 root 均有 link。 |
| 3 | stash@{0} seo-temp | **PASS** | 已核對 `git stash show -p --stat`：僅舊版 `config.mts` 骨架，已被當前七語種+hreflang 覆蓋、無獨有有用改動。說明見 `i18n-project/logs/stash-seo-temp-NOTE.md`；已 `git stash drop stash@{0}`（原物件 `b0cb3ae6236d2893d830c1c9ba25e678f9213d9b`）。當前 `git stash list` 為空。 |
| 4 | build | **PASS** | `cd site && npm run build` 退出碼 0；`build complete in 36.47s`；dist HTML **428** 頁。 |
| 5 | commit | **PASS** | feat 提交 `16d16b10bdfef6b46346d2e2e8db156e3e32f9aa`（short `16d16b1`）；message: `feat(i18n): 七語種全開、頂欄語言切換與主題並排`；author 學習站多語言工程 <i18n@bot.fmcat.top>。本文件若另有 sync 提交，feat hash 仍以本行準。本地未 push。 |
| 6 | dist hreflang / og:locale 抽檢 | **PASS** | 見下節。 |
| 7 | 未 push / 未 deploy | **PASS** | 按任務要求未執行 `deploy.sh`、未 `git push`；等鐵柱確認上線。 |

## Commit

- **feat hash**：`16d16b10bdfef6b46346d2e2e8db156e3e32f9aa`
- **short**：`16d16b1`
- **message**：`feat(i18n): 七語種全開、頂欄語言切換與主題並排`
- **author**：學習站多語言工程 <i18n@bot.fmcat.top>

## dist 抽檢片段

### `dist/index.html`（首頁 zh-CN）
- `og:locale` = `zh_CN`
- hreflang：zh-Hans / zh-Hant / en / ja / ko / es / pt-BR / **x-default** → `https://bot.fmcat.top/`

```html
<meta property="og:locale" content="zh_CN">
<link rel="alternate" hreflang="zh-Hans" href="https://bot.fmcat.top/">
<link rel="alternate" hreflang="en" href="https://bot.fmcat.top/en/">
<link rel="alternate" hreflang="x-default" href="https://bot.fmcat.top/">
```

### `dist/en/index.html`
- `og:locale` = `en_US`
- 8 條 hreflang（含 x-default → 根站）

### `dist/en/part1/01-what-is.html`（手冊）
- `og:locale` = `en_US`
- `hreflang="en" href="https://bot.fmcat.top/en/part1/01-what-is"`
- `hreflang="x-default" href="https://bot.fmcat.top/part1/01-what-is"`

### `dist/tools/index.html`（工具）
- `og:locale` = `zh_CN`
- `hreflang` 含七語種 + x-default → `https://bot.fmcat.top/tools/`

### `dist/part1/01-what-is.html`（根站手冊）
- 同上結構，og:locale=`zh_CN`

## ENGINEERING

「語言切換」一節已更新：桌面 ≥960px 右上角與主題並排；行動裝置端漢堡選單。

## 未部署原因

任務明確：**不要 push，不要執行 deploy.sh**；部署由主代理等鐵柱確認後再跑。

# 六語種接線自檢（2026-10-29）

## build
- `cd site && npm run build`：**PASS**（vitepress 1.6.4，約 26.2s，無 RangeError）
- 未執行 push / deploy

## locales 結構
| locale | md | UI JSON | sidebar JSON | nav/sidebar 非空 |
|---|---|---|---|---|
| zh-CN (root) | 真源 | theme/*.json | sidebar.json | 是 |
| zh-Hant | 61 | 6 | sidebar.zh-Hant.json | 是 |
| en | 61 | 6 | sidebar.en.json | 是 |
| ja | 61 | 6 | sidebar.ja.json | 是 |
| ko | 61 | 6 | sidebar.ko.json | 是 |
| es | 61 | 6 | sidebar.es.json | 是 |
| pt-BR | 61 | 6 | sidebar.pt-BR.json | 是 |

## 語言切換
- VitePress 內建 locales 下拉（頂欄 / 行動選單）
- config.mts `locales` 含 root + 上述 6 語種

## JSON 接線
- `theme/i18n.ts`：`useLocaleJson` 按 `theme/locales/<locale>/*.json` 整文件覆蓋
- 已接入：Home / BotHire / Changelog / EcoIndex / ClipperLanding / XiaoTiezhuLanding / ToolIndex / ToolMeta / JoinCard / DocEndCard

## 抽檢注意
- **en/part1 部分標題混入日文**（如 `01-what-is.md`、`03-install.md` 含「とは」）——內容問題，交翻譯官修；側欄目前按頁標題取文案會帶出該瑕疵
- `git stash@{0}: seo-temp` 仍在，未 drop

## 待部署清單（等鐵柱策略後再動）
1. 確認上線策略：七語種全開 / 先繁英日 / 先只繁體（若只開部分，部署前從 `locales` 與切換器隱藏未開放語種）
2. 保留 `stash@{0}: seo-temp`，合併/應用策略由總控定
3. `cd site && npm run build` 再跑一遍
4. 按倉庫 `deploy.sh` 發表（Cloudflare Pages + EdgeOne bot.fmcat.top）
5. 抽檢：每開放語種首頁、一篇手冊、一篇工具、語言切換、hreflang/og:locale
6. **本崗不自行 push/deploy**，等 Bot學習站指令

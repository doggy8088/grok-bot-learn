# VitePress i18n 腳手架自檢報告

日期：2026-10-29
階段：2 — VitePress i18n 腳手架與部署接線準備

## 建構狀態

⏳ **需請求方手動驗證**：當前環境 shell 命令受限，無法執行 `npm run build`。
請在本地執行：

```bash
cd site && npm run build
```

預期結果：退出碼 0，產出約 70+ 頁面（61 篇 zh-CN + 6 個 locale 首頁 + 404 等）。

## 檢查項

### 1. config.mts locales 組態
- [x] `locales.root`：label=簡體中文, lang=zh-CN
- [x] `locales['zh-Hant']`：label=繁體中文, lang=zh-Hant, link=/zh-Hant/
- [x] `locales.en`：label=English, lang=en-US, link=/en/
- [x] `locales.ja`：label=日本語, lang=ja, link=/ja/
- [x] `locales.ko`：label=한국어, lang=ko, link=/ko/
- [x] `locales.es`：label=Español, lang=es, link=/es/
- [x] `locales['pt-BR']`：label=Português (Brasil), lang=pt-BR, link=/pt-BR/
- [x] 路徑前綴與 PLAN.md 一致

### 2. 非 root 語種目錄骨架
- [x] `site/docs/en/index.md` 存在，含 title/description/非官方宣告
- [x] `site/docs/zh-Hant/index.md` 存在
- [x] `site/docs/ja/index.md` 存在
- [x] `site/docs/ko/index.md` 存在
- [x] `site/docs/es/index.md` 存在
- [x] `site/docs/pt-BR/index.md` 存在
- [x] 未複製 61 篇簡體正文

### 3. 語言切換
- [x] VitePress locales 自帶下拉，桌面端在頂欄 nav 右側，行動裝置端在漢堡選單
- [x] 每個 locale 有 label 和 link，下拉可用

### 4. hreflang / og:locale
- [x] `transformHead` 按 `pageLocale(rel)` 檢測當前語種
- [x] `og:locale` 動態輸出（zh_CN / en_US / zh_TW / ja_JP / ko_KR / es_ES / pt_BR）
- [x] 為所有 7 種語言輸出 `link[rel=alternate][hreflang=...]`
- [x] `hreflang=x-default` 指向根站對等頁
- [x] `og:locale:alternate` 為其餘 6 種輸出
- [x] canonical URL 含正確語種前綴

### 5. JSON 驅動頁 locale 能力
- [x] `theme/i18n.ts` 提供 `useLocaleJson` composable
- [x] 通過 `import.meta.glob('./locales/*/*.json')` 自動載入
- [x] 缺譯回退原始 JSON（zh-CN）
- [x] `theme/locales/.gitkeep` 佔位目錄
- [x] ENGINEERING.md 寫明 JSON 分文件規則和元件接入範例

### 6. 導覽/頁腳/UI 字串
- [x] 每個 locale 的 themeConfig 包含翻譯後的 UI 標記（outline, docFooter, darkModeSwitch 等）
- [x] 缺譯 locale 回退到頂層 themeConfig（zh-CN 字串）
- [x] 頁腳 SiteFooter.vue 硬寫程式中文，作為 zh-CN 回退（翻譯官後續可替換）

### 7. buildEnd (llms.txt)
- [x] `isDoc()` 只匹配 root 路徑前綴，非 root locale 頁不進入 llms 索引
- [x] 根站邏輯不受影響

### 8. 產出文件
- [x] `config.mts` 已改造
- [x] `theme/i18n.ts` 已建立
- [x] 6 個語種 `index.md` 已建立
- [x] `i18n-project/ENGINEERING.md` 已寫
- [x] `i18n-project/logs/scaffold-SELF_CHECK.md`（本文件）
- [x] `i18n-project/logs/scaffold-CHANGED.txt`

### 9. 禁止項
- [x] 未引入付費 API
- [x] 未照抄 grokguide.si
- [x] 未把整站中文 md 複製進各 locales
- [x] 未執行 deploy.sh
- [x] 未提交 secrets / node_modules / dist
- [x] 未刪除非官方宣告

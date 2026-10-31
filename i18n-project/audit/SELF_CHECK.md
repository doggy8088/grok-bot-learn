# 自檢（同步雲端產物後）

| 項 | 結果 | 證據 |
|---|---|---|
| 雲端產物落盤 | PASS | `audit/cloud/content-fix.diff` + 15 個 `fixed-md` |
| P0 file:// 已修 | PASS | `rg file:///workspace site/docs -g'*.md'` 0 |
| connect-plugins.md / team-bots.md | PASS | 上線正文 0 命中（guide/core 未上線舊鏈保留） |
| 站內鏈死鏈（本地先前） | PASS | DEAD_LINKS_LOCAL FAIL=0 |
| 舊域正文 | PASS | md/json 無 bot.tiezhu.si（_worker 保留） |
| 付費答疑群標註 | PASS | group/about + cases/x-hot 已標「付費」 |
| 鏈1 routines.md | OK | HEAD 200（雲端+本地） |
| 鏈2 plans.md | OK | HEAD 200 |
| 鏈3 connect-apps.md | OK | 200（替換 connect-plugins） |
| 鏈4 shared-bots.md | OK | 200（替換 team-bots） |
| 鏈5 github.com/RongleCat/grok-bot-learn | OK | HEAD 200 |
| 腳手架未覆蓋 | PASS | config.mts / i18n.ts / locales / 語種目錄仍為未提交腳手架 |
| 雲端 i18n-audit 取回 | 已手工同步 | 原 FAILED=outputs 未自動取回/推送 403；現已從分支拉齊 |

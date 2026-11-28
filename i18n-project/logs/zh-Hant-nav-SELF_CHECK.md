# zh-Hant nav/sidebar 接線自檢

- 時間：2026-10-29 09:35 Asia/Singapore
- `npm run build`（site/）：PASS，約 11.30s，vitepress 1.6.4
- `sidebar.zh-Hant.json`：與 root 同結構，連結均帶 `/zh-Hant` 前綴，文案 s2twp
- `config.mts`：`zh-Hant.themeConfig.nav` 對齊簡體（課程/案例庫/Bot 直聘/周邊生態/工具箱/更新記錄/付費答疑群）；`sidebar: sidebarZhHant`（非空）
- dist 含 `/zh-Hant/`、`/zh-Hant/part1/`、`/zh-Hant/tools/` 等產物
- 其他語種：仍佔位空 sidebar（按總控要求可先不動）

# stash@{0}: seo-temp 處理說明

- **時間**：2026-10-29（Asia/Singapore）
- **stash 名**：`On main: seo-temp`
- **內容**：僅改 `site/docs/.vitepress/config.mts`（+139/-3），為早期 i18n 骨架：`I18N_*` 輔助函式、`sidebar.zh-Hant` 匯入、locales 七語種佔位（他語種 sidebar 多為空/初期）。
- **核對**：`git stash show -p stash@{0} --stat`；與當前工作區 `config.mts` 對比後，stash 內所有實質改動均已被當前完整七語種 + hreflang/og:locale 接線覆蓋，**無獨有有用片段**。
- **處理**：確認無獨有有用改動後執行 `git stash drop stash@{0}`。
- **結論**：可安全丟棄；不要從該 stash 回滾覆蓋當前工作區。

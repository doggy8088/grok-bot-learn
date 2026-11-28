# 第 7 章 · 記憶與上下文

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

## 來源

- [官方：Bot 會記住什麼](https://cursor.com/cn/docs/grok-bot/work)
- [4.6 虛擬機器、記憶與備份](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- [Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)（英文，摘要見案例）
- [Grok Bot 百萬撤離：一套完善的 Agent 系統備份方案](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

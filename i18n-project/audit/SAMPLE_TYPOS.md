# 本地錯別字 / 病句輕掃候選（SAMPLE_TYPOS）

- 時間：2026-10-29（Asia/Singapore）
- 範圍：SOURCE_PAGES.tsv 全部 md + `theme/{tools,bots,ecosystem,changelog}.json` + `seo.json`
- 原則：只記高置信；第三方英文原標題中的 `GrokBot` 不改
- 約束：本輪只寫報告，未改真源

## 高置信候選

| 置信 | 文件 | 原文片段 | 建議 | 說明 |
|---|---|---|---|---|
| 中 | `site/docs/.vitepress/theme/bots.json` | `給每個Bot配獨立飛書機器人` / `給每個Bot都配上獨立身份` | `每個 Bot`（Bot 前加空格） | 中文文案產品名空格規範；非錯別字，偏體例 |
| 中 | `site/docs/.vitepress/theme/bots.json` | `定期把所有Bot的設定` / `你各個Bot的心血` / `所有Bot的家底` | `所有 Bot` / `各個 Bot` | 同上 |

## 已掃未命中（高置信規則）

| 規則 | 結果 |
|---|---|
| `登陸`（應為登錄） | 清單 md / 目標 JSON：**未命中** |
| `帳號`（應為帳號） | **未命中** |
| `部份` | **未命中** |
| 宜寫「其他」處的 `其它` | **未命中** |
| 正文自造 `GrokBot`（非引用外文標題） | 正文多為引用 Movez 等外文原標題/`@GrokBotRadar`；**不建議改引用標題** |
| `的/地/得` 明顯錯用（跑的快、看的見等） | **未命中高置信例**；命中句均為合法「地方」「回答得清楚」等 |
| `bot.tiezhu.si` 出現在正文/目標 JSON | **未命中**（僅 `public/_worker.js` 舊域跳轉白名單，屬正確保留） |
| 付費答疑群未標「付費」 | `group.md` / `about.md` / `home.json` / `funnel.json` / `seo.json` 均已標明付費 |

## JSON 文案掃（tools / bots / ecosystem / changelog / seo）

| 檢查項 | 結果 |
|---|---|
| `bot.tiezhu.si` | 無 |
| 未標付費的答疑群文案 | 無（相關文案在 funnel/home/seo，均含「付費」） |
| 明顯錯字（登陸/帳號/部份/GrokBot 自造） | bots.json 僅有「每個Bot」空格體例；其餘未命中 |
| seo 覆蓋 | 缺 `index.md`、`tools/deepseek-harness.md`、`xhs.md` 三鑰（偏 P1/P2，非錯別字） |

## 不改清單（避免誤傷）
- 案例/引用裡的英文標題 `GrokBot Agents...`、帳號 `@GrokBotRadar`
- `ShareGrokBots` 等專有方案名
- `_worker.js` 中的 `bot.tiezhu.si` 跳轉集合


# 本地已確認 P0（P0_LOCAL）

- 時間：2026-10-29（Asia/Singapore）
- 定義：死鏈/錯鏈（站內已證實缺失；外鏈 HEAD+GET 均失敗）、舊域 `bot.tiezhu.si` 落在讀者正文、付費答疑群未寫「付費」、明顯錯誤事實
- 本輪：**只報告，未改 `site/` 真源**

## 已確認 P0 表

| 路徑 | 問題 | 建議改法 |
|---|---|---|
| （無） | 本地抽樣未確認到可直接落修的 P0 | — |

**P0 條數：0**

## 依據摘要
- 站內：抽樣 17 篇明細內鏈 FAIL=0；SOURCE 全量約 286 處 FAIL=0；導覽 JSON 路徑 FAIL=0。
- 外鏈：抽檢 14 條無 FAIL；3 條未判定（403 或 HEAD/GET 不一致），按規則不當死鏈。
- 域名：正文/目標 JSON 無 `bot.tiezhu.si`。
- 答疑群：`group.md` 等已寫明付費。

## 觀察項（非 P0，供雲端/人工複核）
| 路徑 | 觀察 | 建議 |
|---|---|---|
| `tools/feishu-bot.md` + `theme/tools.json` | `https://open.feishu.cn/` HEAD=404 / GET=200 | 可改為 `https://open.feishu.cn/document/home/index` 更穩，非必須 |
| 多篇官方出處鏈 | Cursor 文件帶 `.md` 後綴（如 `.../plans.md`） | HEAD=200，保持或統一去後綴均可（P2） |
| `seo.json` | 缺 `index.md` / `tools/deepseek-harness.md` / `xhs.md` | 補 description（P1） |
| `theme/bots.json` | `每個Bot` 缺空格 | 改 `每個 Bot`（P1 體例） |


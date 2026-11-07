# 本地抽樣連結檢查（SAMPLE_LINKS）

- 時間：2026-10-29（Asia/Singapore）
- 範圍：SOURCE_PAGES.tsv 抽樣 17 篇 + 全量內鏈復掃（僅報告抽樣明細）
- 解析：markdown `[text](url)` / `![alt](url)`；絕對站內路徑對照 `site/docs/**/*.md` 與 `site/docs/public/**`
- 外鏈：`curl -sI -L --max-time 8`；403/超時/HEAD·GET 不一致標「未判定」，不當死鏈
- 約束：本輪只寫報告，未改 `site/` 真源

## 抽樣頁清單（17）

| # | 路徑 | 備註 |
|---|---|---|
| 1 | `part1/03-install.md` | 必含 |
| 2 | `group.md` | 必含 |
| 3 | `index.md` | 必含 |
| 4 | `cases/index.md` | 必含 |
| 5 | `tools/agy.md` | tools×3 |
| 6 | `tools/cursor-cli.md` | tools×3 |
| 7 | `tools/feishu-bot.md` | tools×3 |
| 8 | `part2/12-content.md` | part2×2 |
| 9 | `part2/13-x-ops.md` | part2×2 |
| 10 | `part3/19-orchestration.md` | part3×2 |
| 11 | `part3/20-automation.md` | part3×2 |
| 12 | `part1/01-what-is.md` | 加抽 |
| 13 | `part4/25-faq.md` | 加抽 |
| 14 | `about.md` | 加抽 |
| 15 | `tools/index.md` | 加抽 |
| 16 | `bots/index.md` | 加抽 |
| 17 | `changelog/index.md` | 加抽 |

## 站內相對 / 絕對路徑（≥15）

| 狀態 | 源文件 | 連結 | 解析目標 |
|---|---|---|---|
| OK | `part1/03-install.md` | `/part1/04-handoff` | `site/docs/part1/04-handoff.md` |
| OK | `part1/03-install.md` | `/part4/25-faq` | `site/docs/part4/25-faq.md` |
| OK | `part1/03-install.md` | `/info/03-install.png` | `site/docs/public/info/03-install.png` |
| OK | `group.md` | `/part1/01-what-is` | `site/docs/part1/01-what-is.md` |
| OK | `index.md` | `（無 md 內鏈；Home 元件）` | `-` |
| OK | `cases/index.md` | `/cases/x-hot` | `site/docs/cases/x-hot.md` |
| OK | `cases/index.md` | `/cases/cn` | `site/docs/cases/cn.md` |
| OK | `cases/index.md` | `/cases/en1` | `site/docs/cases/en1.md` |
| OK | `cases/index.md` | `/cases/en2` | `site/docs/cases/en2.md` |
| OK | `cases/index.md` | `/cases/tiezhu` | `site/docs/cases/tiezhu.md` |
| OK | `tools/agy.md` | `/tools/` | `site/docs/tools/index.md` |
| OK | `tools/cursor-cli.md` | `/tools/` | `site/docs/tools/index.md` |
| OK | `tools/feishu-bot.md` | `/tools/` | `site/docs/tools/index.md` |
| OK | `part2/12-content.md` | `/info/12-content-s1.png` | `site/docs/public/info/12-content-s1.png` |
| OK | `part2/12-content.md` | `/cases-img/fs26-0.jpg` | `site/docs/public/cases-img/fs26-0.jpg` |
| OK | `part2/13-x-ops.md` | `/info/13-x-ops-s1.png` | `site/docs/public/info/13-x-ops-s1.png` |
| OK | `part3/19-orchestration.md` | `/part1/09-group-team` | `site/docs/part1/09-group-team.md` |
| OK | `part3/19-orchestration.md` | `/part4/24-roles` | `site/docs/part4/24-roles.md` |
| OK | `part3/20-automation.md` | `/part1/08-skills-routines` | `site/docs/part1/08-skills-routines.md` |
| OK | `part3/20-automation.md` | `/part1/10-usage` | `site/docs/part1/10-usage.md` |
| OK | `part1/01-what-is.md` | `/part1/05-computer` | `site/docs/part1/05-computer.md` |
| OK | `part1/01-what-is.md` | `/part1/grok-vs-grok-bot` | `site/docs/part1/grok-vs-grok-bot.md` |
| OK | `part4/25-faq.md` | `/part1/05-computer` | `site/docs/part1/05-computer.md` |
| OK | `about.md` | `/group` | `site/docs/group.md` |
| OK | `about.md` | `/ecosystem/grok-bot-clipper` | `site/docs/ecosystem/grok-bot-clipper.md` |
| OK | `about.md` | `/bots/` | `site/docs/bots/index.md` |
| OK | `tools/index.md` | `（無 md 內鏈；ToolIndex 元件）` | `-` |
| OK | `bots/index.md` | `（無 md 內鏈；BotHire 元件）` | `-` |
| OK | `changelog/index.md` | `（無 md 內鏈；Changelog 元件）` | `-` |

**內鏈小結**：抽樣明細 29 條，FAIL=0。另對 SOURCE_PAGES.tsv 全部 61 篇做了同規則復掃：可解析站內鏈約 286 處，FAIL=0（含 `/info/*`、`/cases-img/*` 靜態資源）。sidebar.json / home.json / funnel.json / links.json 路徑抽檢 FAIL=0。

## 外鏈 HEAD 抽檢（≥10）

| 狀態 | 源文件 | URL | 備註 |
|---|---|---|---|
| OK | `part1/03-install.md` | `https://cursor.com/cn/docs/grok-bot/get-started` | HEAD=200 |
| OK | `part1/03-install.md` | `https://cursor.com/cn/help/grok-bot/onboarding` | HEAD=200 |
| OK | `tools/cursor-cli.md` | `https://cursor.com/docs/cli/installation` | HEAD=200 |
| OK | `about.md` | `https://github.com/RongleCat/grok-bot-learn` | HEAD=200 |
| OK | `tools/agy.md` | `https://github.com/google-antigravity/antigravity-cli` | HEAD=200 |
| OK | `about.md` | `https://x.com/cgnot996` | HEAD=200 |
| 未判定 | `part2/13-x-ops.md` | `https://x.ai/changelog/bot` | HEAD=403 |
| OK | `part2/13-x-ops.md` | `https://docs.x.ai/x-subscription/pricing` | HEAD=200 |
| OK | `part3/19-orchestration.md` | `https://docs.x.ai/grok-bot/bots` | HEAD=200 |
| OK | `tools/agy.md` | `https://antigravity.google/docs/getting-started/` | HEAD=200 |
| 未判定 | `tools/feishu-bot.md` | `https://open.feishu.cn/` | HEAD=404 GET=200（勿當死鏈） |
| 未判定 | `part4/25-faq.md` | `https://status.cursor.com` | HEAD=403 |
| OK | `part1/02-plans.md` | `https://grok.com/com/overlay/subscribe?from=/` | HEAD=200 |
| OK | `tools/feishu-bot.md` | `https://github.com/larksuite/oapi-sdk-python` | HEAD=200 |

**外鏈小結**：共 14 條；OK=11，FAIL=0，未判定=3。

### 未判定說明
- `https://open.feishu.cn/`：HEAD=404，帶 UA 的 GET=200 → 未判定（勿當死鏈）。同源亦出現在 `theme/tools.json`。
- `https://x.ai/changelog/bot`、`https://status.cursor.com`：HEAD=403（後者有效跳轉 `status.x.ai`）→ 未判定。
- 飛書 wiki（`jcng5q8n0f3z.feishu.cn/wiki/...`）HEAD 常 404/需登錄，本表未當死鏈收錄。

## 方法備註
- VitePress 站內鏈省略 `.md`：`/part1/04-handoff` → `site/docs/part1/04-handoff.md` 或 `.../index.md`。
- `/info/*`、`/cases-img/*` 對應到 `site/docs/public/`。


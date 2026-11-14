# 自檢

## P0 是否清零

清零。上線 61 篇中的 P0 均已寫入 `FIXED.md`。`REPORT.md` 裡「阻塞、需人工」為 0 條。

複核命令（在 `/workspace/grok-bot-learn`）：

- 61 篇中 `file://`、`tiezhu.si`、`v3/src/`：0 命中。
- `connect-plugins.md`、`team-bots.md`：僅剩未上線的 `site/docs/guide/` 與 `site/docs/core/`，不在 61 篇內。

## 連結抽檢

| 結果 | URL | 證據 |
| --- | --- | --- |
| OK | https://cursor.com/cn/help/grok-bot/connect-apps.md | `curl` 200，正文以 `# Connect apps` 開頭 |
| FAIL | https://cursor.com/help/grok-bot/connect-plugins.md | `curl` 404，正文 `# Page not found`。這是修改前的地址，已替換 |
| OK | https://cursor.com/cn/help/grok-bot/shared-bots.md | `curl` 200，正文以 `# Shared Bots` 開頭 |
| FAIL | https://cursor.com/help/grok-bot/team-bots.md | `curl` 404，正文 `# Page not found`。這是修改前的地址，已替換 |
| OK | https://cursor.com/cn/help/grok-bot/routines.md | `curl` 200，正文以 `# Routines` 開頭 |
| OK | https://cursor.com/cn/help/grok-bot/plans.md | `curl` 200，正文以 `# Plans and billing` 開頭 |
| OK | https://docs.x.ai/x-subscription/pricing | `curl` 200 |
| OK | https://api.fxtwitter.com/status/2114883723930030505 | `curl` 200，`code: 200`，對應 `cases/x-hot.md` 付費答疑群案例原帖 |
| OK | https://bot.fmcat.top/group | `curl` 200 |
| OK | https://cursor.com/help/grok-bot/models | `curl` 200。頁面說明 Grok Bot 不綁定單一模型 |

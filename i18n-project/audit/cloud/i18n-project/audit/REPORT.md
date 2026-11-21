# 翻譯前審查報告

審查日：2026-10-29。真源：`RongleCat/grok-bot-learn` `main` @ `03c8f24`（本環境複製到 `/workspace/grok-bot-learn`）。站點：https://bot.fmcat.top

## 清單怎麼定的

`i18n-project/SOURCE_PAGES.tsv` 在該提交和 `https://raw.githubusercontent.com/RongleCat/grok-bot-learn/main/i18n-project/SOURCE_PAGES.tsv` 都不存在（raw 返回 404）。未猜一份不存在的表。

上線篇目按站點組態重建，共 **61** 篇，與任務所說篇數一致：

- `site/docs/.vitepress/config.mts` 的 `srcExclude` 排除 `admin/`、`advanced/`、`appendix/`、`core/`、`guide/`、`resources/`、`start/`、`zz-bots.md`、`cases/outdated.md` 後，剩餘 **60** 篇。
- 這 60 篇與 https://bot.fmcat.top/sitemap.xml 的 60 個 `<loc>` 一一對應。
- 第 61 篇是 `site/docs/xhs.md`：會建構，但 `sitemap.transformItems` 去掉它，並 `noindex`。https://bot.fmcat.top/xhs 返回 200。

另掃：`site/docs/.vitepress/theme/tools.json`、`bots.json`、`ecosystem.json`、`changelog.json`，以及 `site/docs/.vitepress/seo.json`。

站內相對連結 1033 條裡，圖片與已發表路由均能落到文件。`guide/`、`core/` 裡的舊幫助連結不在這 61 篇裡，未改。

## 問題

| 優先級 | 文件 | 問題 | 建議/已改 |
| --- | --- | --- | --- |
| P0 | `site/docs/part3/22-feishu-wechat.md` | 兩處 `file:///workspace/grok-bot-learn/v3/src/help_grok-bot_*.md`。讀者打不開，並暴露倉庫內路徑與源檔名。 | 已改。改為 [例程](https://cursor.com/cn/help/grok-bot/routines.md) 與 [方案與計費](https://cursor.com/cn/help/grok-bot/plans.md)。抽檢均為 200。 |
| P0 | `site/docs/part2/18-solo.md` | 延伸閱讀鏈出內部檔名 `docs_grok-bot_*.md`、`help_grok-bot_*.md`。其中 `connect-plugins.md` 返回 404。 | 已改。去掉內部檔名，外掛頁改為 [連線應用](https://cursor.com/cn/help/grok-bot/connect-apps.md)（200）。 |
| P0 | `site/docs/part1/07-apps.md` | `connect-plugins.md`、`team-bots.md` 的 `.md` 地址返回 404（正文以 `# Page not found` 開頭）。不帶 `.md` 的舊地址會 302 到新頁。 | 已改。分別改為 `connect-apps.md`、`shared-bots.md`。 |
| P0 | `site/docs/part1/01-what-is.md`；`site/docs/part1/09-group-team.md`；`site/docs/part1/11-safety.md`；`site/docs/part4/23-enterprise.md`；`site/docs/part4/25-faq.md` | 仍指向已更名的 `team-bots` / `connect-plugins`。`.md` 形式 404；無後綴形式僅靠重定向。 | 已改。統一到 `shared-bots.md`、`connect-apps.md`。 |
| P0 | `site/docs/part1/01-what-is.md` | 「2026 年 10 月 7 日預設切為 Claude Opus 5.5」把路由說成單一預設模型。官方寫明不綁定單一模型，也不能查看或指定。 | 已改。保留「可能路由到 Claude Opus 5.5 等模型」。依據：https://cursor.com/help/grok-bot/models |
| P0 | `site/docs/part1/11-safety.md` | 「底層切到 Claude Opus 5.5」同樣寫成整站換模。 | 已改。改為「可能路由到 Claude Opus 5.5 等更強模型」。依據同上。 |
| P0 | `site/docs/part3/19-orchestration.md` | 「系統解耦換上 Claude Opus 5.5」同樣寫成整站換模。 | 已改。改為「任務可能路由到 Claude Opus 5.5 等模型後」。依據同上。 |
| P0 | `site/docs/part1/01-what-is.md` | 「GPT-6 Astra（2026-09-30 發表）」把 dots 上線日寫成 Astra 發表日。OpenAI 寫明 dots 於 2026-09-29 上線，並由 GPT-6 Astra 驅動；Pro 與 Business Premium 包含第一個 dot，連線 4,000+ 應用。 | 已改。依據：https://openai.com/index/introducing-dots/ （本機 curl 對該頁 403，屬攔截；頁面正文由直接抓取讀到，日期以該頁為準）。 |
| P0 | `site/docs/cases/x-hot.md` | 案例標題與收束句寫「答疑群」，未寫「付費」。同節下一段已有「付費答疑群」。 | 已改。標題與收束句改為「付費答疑群運維助手」。 |
| P1 | `site/docs/part1/01-what-is.md`；`part1/08-skills-routines.md`；`part1/09-group-team.md`；`part1/10-usage.md`；`part1/11-safety.md`；`part2/14-engineering.md`；`part2/17-gtm.md`；`part2/18-solo.md`；`part3/19-orchestration.md`；`part3/20-automation.md` | 仍指示打開已刪除的 Edit Profile，或把長期規則寫入個人 Bot 的 Description。第 3 章已是現行做法。官方：個人 Bot 沒有 Description，長期規則在對話裡讓它記住；共享 Bot 仍在詳情 About 編輯 Description。側邊欄移除 Edit Profile 見本站 `changelog.json` 的 PC 0.57.0。 | 已改。指令改為「個人 Bot 發在對話裡並讓它記住；共享 Bot 寫在詳情 About」。依據：https://cursor.com/help/grok-bot/edit-bot.md |
| P1 | `site/docs/part1/01-what-is.md` | 「行動裝置端支援 iPhone」漏了 iPad 與 Android。同站 `part1/grok-vs-grok-bot.md` 已寫這三端。 | 已改。補上 iPad 與 Android。依據：https://cursor.com/help/grok-bot/mobile.md （「available on iOS and Android」）。 |
| P1 | `site/docs/part1/07-apps.md` | 步驟仍寫「搜外掛點新增」。官方頁已稱 Connect apps。未對照現行客戶端按鈕原文，不敢改按鈕字。 | 只記不改。連結已改到連線應用。 |
| P1 | `site/docs/.vitepress/seo.json` | `part2/14-engineering.md` 的描述寫「自動匹配 Claude Opus 5.5 等模型」。有「等」，與「不綁定單一模型」不衝突。 | 只記不改。 |
| P1 | `site/docs/guide/`、`site/docs/core/` | 仍有 `team-bots`、`connect-plugins`。這兩目錄在 `srcExclude` 中，不在 61 篇、也不進 sitemap。 | 只記不改。未上線。 |
| P2 | 61 篇 Markdown | 沒有連續 3 行及以上空行。引號和頓號風格不完全一致。 | 只記不改。 |

## 掃過但沒有記成問題的項

- `bot.tiezhu.si`：61 篇與上述 5 個 JSON 中 0 次。
- 付費群：`group.md`、`about.md`、`seo.json` 的 `group.md` 條目已寫「付費」。`group.md` 首段後半句是「群是付費群」，標題是「付費答疑群」。
- 錯別字抽查：`做為`、`既使`、`必需要`、`閥值` 在 `site/docs` 中 0 次。
- 站內圖片：`/info/*.png` 在 `public/info` 均有同名 webp 或 png，缺失 0。
- 五個 JSON：無 `file://`、無 `tiezhu.si`、無未標「付費」的「答疑群」。`changelog.json` 是官方更新譯文，未改措辭。
- 飛書 wiki（`jcng5q8n0f3z.feishu.cn`）抽檢會跳到登錄頁（HTTP 200），不能據此判死鏈，也不記「阻塞、需人工」。
- `https://x.ai/changelog/bot` 對本機 curl 為 403，是攔截，不是 404。
- 訂閱價格（Plus $8、Premium $30、Super $100、Ultra $200，Plus 不含 Bot）與 https://docs.x.ai/x-subscription/pricing 一致，未改。
- 模型名：官方幫助頁自己寫出 Opus 5.5。本次只改「預設換成這一個模型」的錯誤事實，沒有把官方已經公開的名字從正文裡刪掉。

## P0 清零

上線 61 篇裡的 P0 都已改。標明「阻塞、需人工」的條數是 **0**。

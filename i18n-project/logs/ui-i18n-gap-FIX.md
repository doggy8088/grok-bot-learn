# UI i18n gap FIX（對照 audit/UI_I18N_GAPS.md）

- **日期**：2026-10-29（America/Los_Angeles）
- **範圍**：theme chrome 硬寫程式抽出 → `ui.json` + `locales/*/ui.json`；內部連結 `localePath`
- **約束**：本輪 **未 push / 未 deploy**；僅本地 commit
- **對照**：`i18n-project/audit/UI_I18N_GAPS.md`

## 改了哪些文件

### 新增
| 文件 | 說明 |
|---|---|
| `site/docs/.vitepress/theme/ui.json` | root（zh-CN）UI 字串真源 |
| `site/docs/.vitepress/theme/locales/{zh-Hant,en,ja,ko,es,pt-BR}/ui.json` | 六語種覆蓋（短標記佔位/可用譯文） |
| `i18n-project/logs/ui-i18n-gap-FIX.md` | 本文件 |
| `i18n-project/audit/UI_I18N_GAPS.md` | 驗收缺口清單（審計側） |

### 修改（元件 / i18n）
| 文件 | 改動 |
|---|---|
| `theme/i18n.ts` | 新增 `useLocalePath` / `useLocaleSeg` / `stripLocalePrefix` / `partKeyFromPath` / `bcp47`；匯出 `NON_ROOT` |
| `theme/NavGroupPill.vue` | `ui.nav.groupPill` + `localePath('/group')` |
| `theme/SiteFooter.vue` | `ui.footer.*` + `localePath('/group'|'/about')` |
| `theme/PartBadge.vue` | `partKeyFromPath` + `ui.parts.*`（修 locale 頁不渲染） |
| `theme/Changelog.vue` | `ui.changelog.*` tabs/title/chip；日期改 `Intl.DateTimeFormat(bcp47)`；`items` 改 `computed` |
| `theme/XiaoTiezhuLanding.vue` | `ui.xiaotiezhu.title` / `joinHint`；CTA `/group` → `localePath` |
| `theme/JoinCard.vue` | QR `alt` → `ui.join.qrAlt` |
| `theme/DocEndCard.vue` | `stripLocalePrefix` 匹配 + `localePath('/group')` |
| `theme/Home.vue` | 內鏈全面 `localePath` |
| `theme/EcoIndex.vue` | 卡片頁 `localePath` |
| `theme/ToolIndex.vue` | 工具卡連結 `localePath` |
| `theme/ToolMeta.vue` | 多語種 skin + `rootCatById` 回退 + `localePath` |
| `i18n-project/ENGINEERING.md` | 補充 `ui.json` 表項 +「UI 字串走 theme/locales + localePath」 |

## `ui.json` key 列表

```
nav.groupPill
footer.mpBtn / mpDialog / mpAlt / group / about / friends / note
parts.part1 / part2 / part3 / part4 / cases
changelog.title / tabAll / tabPc / tabMobile / tabOurs / chipOurs
xiaotiezhu.title / joinHint
join.qrAlt
```

六語種文件路徑：
- `theme/locales/zh-Hant/ui.json`
- `theme/locales/en/ui.json`
- `theme/locales/ja/ui.json`
- `theme/locales/ko/ui.json`
- `theme/locales/es/ui.json`
- `theme/locales/pt-BR/ui.json`

**請翻譯官複核/潤色**：以上六文件全部 key（產品名 Grok Bot / 鐵柱AGI / 小鐵柱 按既有慣例可保留）。英文等已有可用短譯文，非空白。

## 抽檢（本地 dist，build 後）

| 檢查 | 結果 |
|---|---|
| `npm run build` | **PASS**（exit 0，~42s，約 428 HTML） |
| NavGroupPill `/en/` | `<a class="tz-nav-pill" href="/en/group">Paid Q&A Group</a>` |
| NavGroupPill `/`（zh-CN） | `href="/group"` + 文案「付費答疑群」 |
| SiteFooter en | `About the Author`、`/en/about`、`/en/group` 存在 |
| Changelog tabs | 走 `clUi.tab*`；日期 `Intl`（不再寫死「×月×日」） |
| PartBadge | locale 頁用 `partKeyFromPath`，label 讀 `ui.parts` |

驗證方式：`cd site && npm run build`，讀 `docs/.vitepress/dist/en/index.html` 檢索 `tz-nav-pill`。

## 對照 audit：已修 vs 仍未覆蓋

### 本輪已修（audit 點名 P0 chrome — 倉庫側）
- NavGroupPill / SiteFooter / Changelog 標題·tabs·chip·日期 / PartBadge / 小鐵柱 h1·hint / JoinCard alt
- Home / DocEndCard / EcoIndex / ToolIndex·ToolMeta 內鏈 locale 前綴

### 仍未覆蓋 / follow-up（P1，本輪未修）
| 項 | 說明 |
|---|---|
| **P1** `.vitepress/seo.json` og/twitter description | 仍簡體 home 文案；需按語種覆蓋或改 frontmatter |
| **P1** `config.mts` JSON-LD `inLanguage: 'zh-CN'` | 寫死；需按頁 locale |
| **P1** `friends.json` 站名 | 「噪音之後」「萬象 AI 實驗室」等專名；可保留或另做 locale |
| **P1** `Home.vue` `segs()` | 按中文標點切句；擴拉丁標點 |
| **P1** Tool skin 對應表 | 多語種 label 作 key（已有 `rootCatById` 回退）；可再收斂到穩定 cat id |
| **策略** 小鐵柱 title | en ui 仍產品名「小鐵柱」；md frontmatter 同 |

### 線上
點名 P0 在**倉庫已修**；**未 deploy**，線上非 zh 仍會見舊簡體，直至鐵柱確認部署。

## 請翻譯官補的文件與 key

優先潤色（非空白，求自然 UI 短句）：

1. `theme/locales/en/ui.json` — 全部 key  
2. `theme/locales/zh-Hant/ui.json` — 全部 key  
3. `theme/locales/ja/ui.json` — 全部 key  
4. `theme/locales/ko/ui.json` — 全部 key  
5. `theme/locales/es/ui.json` — 全部 key  
6. `theme/locales/pt-BR/ui.json` — 全部 key  

專名勿亂譯：Grok Bot、鐵柱AGI、小鐵柱、xAI、X @cgnot996。

## 本地 commit

見最終回報 hash。作者：`學習站多語言工程 <i18n@bot.fmcat.top>`。未 push。

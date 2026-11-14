# ui.json chrome 潤色 STATUS

- **時間**：2026-10-29 03:10 (America/Los_Angeles)
- **範圍**：`theme/ui.json`（zh-CN 真源）→ `theme/locales/{zh-Hant,en,ja,ko,es,pt-BR}/ui.json`
- **約束**：未 push / 未 deploy；讀者文案用 agy / OpenCC
- **模型**：agy `--model gemini-3.8-flash-high`（en/ja/ko/es/pt-BR）；zh-Hant = OpenCC s2twp + 專名回寫

## 產出文件

| locale | path |
|---|---|
| zh-Hant | `site/docs/.vitepress/theme/locales/zh-Hant/ui.json` |
| en | `site/docs/.vitepress/theme/locales/en/ui.json` |
| ja | `site/docs/.vitepress/theme/locales/ja/ui.json` |
| ko | `site/docs/.vitepress/theme/locales/ko/ui.json` |
| es | `site/docs/.vitepress/theme/locales/es/ui.json` |
| pt-BR | `site/docs/.vitepress/theme/locales/pt-BR/ui.json` |

## 關鍵文案抽檢

| locale | nav.groupPill | footer.group | xiaotiezhu.title | join.qrAlt |
|---|---|---|---|---|
| zh-Hant | 付費答疑群 | 付費答疑群 | 小鐵柱 | 鐵柱的個人微信二維碼 |
| en | Paid Q&A Group | Paid Q&A Group | 小鐵柱 | Personal WeChat QR code of 鐵柱 |
| ja | 有料Q&Aグループ | 有料Q&Aグループ | 小鐵柱 | 鐵柱の個人WeChat QRコード |
| ko | 유료 Q&A방 | 유료 Q&A방 | 小鐵柱 | 鐵柱 개인 WeChat QR 코드 |
| es | Grupo Q&A de pago | Grupo Q&A de pago | 小鐵柱 | Código QR del WeChat personal de 鐵柱 |
| pt-BR | Grupo pago de dúvidas | Grupo pago de dúvidas | 小鐵柱 | QR Code do WeChat pessoal de 鐵柱 |

## 各語種改動要點

### zh-Hant（OpenCC s2twp）
- 全量字串 OpenCC；強制專名回寫：`鐵柱AGI` / `小鐵柱`（去掉鐵/鉄）
- `nav/footer.group`：付費答疑群（付費語義保留）
- `footer.friends`：友情連結；`note`：社群非官方…
- `changelog.tabMobile`：行動裝置端

### en（agy 重譯）
- `friends`：Friends → **Friend Links**
- `mpBtn`：WeChat OA → Official Account 「鐵柱AGI」
- parts / changelog 標記更自然（User Manual / Case Studies / Our Take）
- 付費：Paid Q&A Group

### ja（agy 重譯 + 專名）
- 專名：鉄柱/小鉄柱 → **鐵柱AGI / 小鐵柱**（漢字簡體專名，不譯）
- 有料Q&Aグループ；friends=リンク集；tabOurs=當サイトの解説

### ko（agy 重譯 + 專名）
- 專名：철주AGI/소철주 → **鐵柱AGI / 小鐵柱**
- 유료 Q&A방；friends=추천 링크；tabOurs=자체 해설

### es（agy 重譯）
- Grupo Q&A de pago；friends=Enlaces recomendados；chipOurs=Nuestro análisis
- 專名保持 鐵柱AGI / 小鐵柱

### pt-BR（agy 重譯）
- Grupo pago de dúvidas；friends=Links parceiros；title=Histórico de Atualizações
- 專名保持 鐵柱AGI / 小鐵柱

## 專名修復摘要

| 錯誤形式 | 強制改回 | 命中語種 |
|---|---|---|
| 鐵柱AGI / 小鐵柱 | 鐵柱AGI / 小鐵柱 | zh-Hant（OpenCC 後回寫） |
| 鉄柱AGI / 小鉄柱 | 鐵柱AGI / 小鐵柱 | ja（本輪 agy 已正確，無殘留） |
| 철주AGI / 소철주 | 鐵柱AGI / 小鐵柱 | ko（本輪 agy 已正確，無殘留） |

校驗：六文件 `json.load` OK；key 結構與真源一致；bad 專名模式掃描 remaining=[]。

## group.md 抽檢

| locale | 結果 |
|---|---|
| en | **PASS** |
| ja | **PASS** |
| ko | **PASS** |
| es | **PASS** |
| pt-BR | **PASS** |
| zh-Hant | **PASS** |

抽檢短語：付費答疑 / 這是付費 / 加我個人 / 掃碼新增 / 開通小鐵柱 等 — 六語種正文與 JoinCard 插槽均無簡體殘留句；專名「鐵柱AGI」按真源保留。未觸發重譯。

## 未做
- push / deploy
- Bot CloudAgent

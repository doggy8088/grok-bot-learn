import json
t = json.load(open("/workspace/grok-bot-learn/sources/feishu/tree.json"))
U = {f"fs{i:02d}": (x[2], "https://jcng5q8n0f3z.feishu.cn/wiki/" + x[1]) for i, x in enumerate(t)}
D = lambda *n: [f"docs_grok-bot{'_' + x if x else ''}.md" for x in n]
H = lambda *n: [f"help_grok-bot_{x}.md" for x in n]
F = lambda *n: [f"fs{x:02d}.md" for x in n]
J = [
 ("part1/01-what-is", "第 1 章 Grok Bot 是什麼：一個自帶電腦的 AI 同事", "產品機制、和普通聊天助手的區別、共享雲端電腦的邊界、適合與不適合的任務、和 Muse/Hermes/dots/Cue 的選型對比表", D("", "use-cases") + F(2, 3, 21, 24)),
 ("part1/02-plans", "第 2 章 方案與訂閱：先選對檔位", "以 2026-10-12 起的 The X Subscription 為準講四檔與免費檔、每週共享用量池、哪些檔含 Grok Bot、Cursor 方案與 SuperGrok 關聯、團隊版與按需、老訂閱切換注意、如何查看用量；不要寫任何開發者積分或舊資費", H("plans", "supergrok", "mobile-purchase", "models") + F(16, 18)),
 ("part1/03-install", "第 3 章 安裝登錄與第一個 Bot", "下載安裝、登錄、iOS、建立第一個 Bot、寫職責（六行合同）、第一條任務、驗收清單、常見登錄問題", D("get-started") + H("onboarding", "sign-in", "mobile", "edit-bot") + F(2, 24, 30)),
 ("part1/04-handoff", "第 4 章 交代任務：訊息、附件與一次好的交接", "好請求的五要素、附件限制表、提示詞範例多條、長期規則 vs 任務、停止與插話、語音、常見失敗寫法對照", D("", "work") + H("how-to", "voice-chat") + F(33, 37, 49)),
 ("part1/05-computer", "第 5 章 共享雲端電腦：文件、瀏覽器與接管", "共享電腦機制、各 Bot 螢幕、接管登錄、文件交接約定、本地網路出口、重建與恢復、實操步驟與坑", D("computers", "settings") + H("computer-recovery") + F(69, 14)),
 ("part1/06-memory", "第 6 章 記憶：讓 Bot 越用越懂你", "官方記憶說明、記憶分層、什麼該記什麼不該記、記憶與技能的邊界、團隊記憶、記憶備份流程、提示詞", D("work") + F(57, 69, 46)),
 ("part1/07-apps", "第 7 章 連線應用：外掛、郵箱與 Secrets", "先介面後連線器的接入順序、外掛連線步驟、Bot 專屬郵箱、Secrets、X 檢索、安裝開源 Skill 與 CLI、坑點", H("connect-plugins", "agent-email", "secrets") + F(68, 42)),
 ("part1/08-skills-routines", "第 8 章 技能與例程：把一次成功變成每天自動跑", "技能的生成與引用、例程設定/查看/測試、時區、webhook 欄位與 200 含義、Slack 觸發器、例程排錯、範例例程若干", H("routines", "how-to") + D("work") + F(66, 12, 6)),
 ("part1/09-group-team", "第 9 章 群聊與團隊 Bot：從一個 Bot 到一組 Bot", "群聊規則、Bot 互發訊息、團隊 Bot 與 Slack 對照表、主 Bot 派活模式、交接文件約定、用量影響", H("group-chats", "team-bots") + F(53, 35, 65)),
 ("part1/10-usage", "第 10 章 額度與成本：讓一週用量撐滿一週", "扣費原理、高耗操作清單、省額度四步、例程與輪詢優化、群聊回覆控制、用量審計、直接發給 Bot 的省額度指令", H("plans", "routines") + F(64, 9, 12, 13, 54)),
 ("part1/11-safety", "第 11 章 權限、安全與人閘", "批准與 Auto Review、按可逆性分級放權、網路策略、記錄、憑證處理、對外發信審批、安全 FAQ 要點、組態清單", D("security", "security-faq") + F(67, 45)),
 ("part2/12-content", "第 12 章 案例：自媒體與內容團隊", "以多篇案例為素材講內容團隊的崗位設計、選題-起草-配圖-分發流程、提示詞、坑點，每個案例寫清做法與可借鑑點", F(26, 28, 32, 36, 20)),
 ("part2/13-x-ops", "第 13 章 案例：在 X 上做內容與運營", "X 檢索、自動化 X 內容、微信一句話運營 X、5 個 Bot 樣板、只出草稿的審批設計", F(34, 41, 66, 19)),
 ("part2/14-engineering", "第 14 章 案例：工程與研發團隊", "PR 巡檢、倉庫值班台、工程 harness、與本地 CLI agent 分工、九類工作清單、提示詞與坑", F(25, 31, 50, 51, 58, 62, 59)),
 ("part2/15-ecommerce", "第 15 章 案例：電商與生活實操", "閒魚上架、小紅書做圖、找工具、做短影片、整理收藏、亞馬遜團隊搭建", F(27, 38)),
 ("part2/16-knowledge", "第 16 章 案例：知識自動入庫與微信打通", "Webhook+快捷指令入庫流水線、微信聊天記錄打通、接入微信、步驟與提示詞", F(6, 11, 29)),
 ("part2/17-gtm", "第 17 章 案例：GTM、銷售與幕僚長", "GTM 用法、Chief of Staff 章程與例程、銷售外聯只出草稿", F(40, 45, 56) + D("use-cases")),
 ("part2/18-solo", "第 18 章 案例：一人公司與 AI 團隊", "一人公司、AI agency、從零到運轉的公司、29 個 Agent、第一個 AI 員工，如何逐步擴編", F(44, 47, 48, 52, 55, 60, 61, 43)),
 ("part3/19-orchestration", "第 19 章 團隊編排：章程、崗位與放權", "主 Bot 與專職 Bot、章程樣板、崗位拆分方法、放權分級、交接規範、擴編節奏", F(65, 45, 35, 36, 44)),
 ("part3/20-automation", "第 20 章 可靠的自動化：定時、Webhook 與事件觸發", "觸發器選型、例程設計樣板、Webhook 接入、增量判斷避免空跑、失敗兜底、監控", F(66, 6, 12) + H("routines")),
 ("part3/21-backup", "第 21 章 備份與恢復：電腦重置也不慌", "服務總帳、restore.sh、私有倉庫、記憶管家、恢復提示詞、百萬撤離方案", F(10, 14, 69) + H("computer-recovery")),
 ("part3/22-feishu-wechat", "第 22 章 接入飛書與微信", "團隊接入飛書步驟與飛書管家樣板、微信接入、權限與坑", F(15, 29, 11)),
 ("part4/23-enterprise", "第 23 章 團隊版與企業落地", "團隊版管理控制、身份與 SSO、私有網路與環境指令碼、代理、桌面端分發、管理 Bot 電腦、推廣建議", D("teams", "identity", "private-networks", "proxies", "deployment", "computers")),
 ("part4/24-roles", "第 24 章 按崗位組建你的 AI 團隊", "按崗位（內容、工程、銷售、研究、運營、個人助理、管理者）給出 Bot 編制、首個任務、例程、提示詞", D("use-cases") + F(56, 49, 43, 52)),
 ("part4/25-faq", "第 25 章 常見問題與排錯", "按主題分組的問答：登錄、電腦、例程、用量、群聊、外掛、刪除帳號、獲取幫助", H("faqs", "how-to", "get-help", "delete-account", "computer-recovery", "routines")),
]
json.dump({"jobs": J, "urls": U}, open("jobs.json", "w"), ensure_ascii=False, indent=1)
print(len(J))

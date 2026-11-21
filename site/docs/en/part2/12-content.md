# Chapter 12 Case Study: We-Media and Content Teams

Conversational AI easily loses context; **Grok Bot runs pipelines using shared files on a cloud computer**.

1. Write role descriptions and build a topic library based on six rigid field sets.
2. Research bots write cards into directories, and the lead writer bot reads them to draft copy.
3. Implement de-AI-flavor proofreading rules and turn tweets into a personal portfolio website.
4. **Key publishing milestones must be guarded manually** to avoid fake data and platform risk controls.

## Role Design and Collaboration Mechanisms for We-Media Teams

![Role Design and Collaboration Mechanisms for We-Media Teams](/info/12-content-s1.png)

### What It Is

**The core of building a team in Grok Bot is "one role, one responsibility."** All bots under an account share the same cloud computer (with an independent kernel, memory, and `/workspace` path), but each has its own independent window, memory, and settings.

Bots hand off tasks to each other by reading and writing Markdown files in shared folders.

### How to Do It

**The main Bot, marked with a star on its avatar (right-click avatar to switch)**, is responsible for coordinating and assigning work, while 5 to 6 dedicated bots work strictly within their duty boundaries.

| Role Name | Delivery Path | Core Responsibilities and Prohibited Actions |
| :--- | :--- | :--- |
| Intelligence Scout | `/workspace/content-team/01-inbox/` | Collect first-hand leads. Strictly prohibited from posting, interacting, and sending DMs; strictly prohibited from treating second-hand commentary as fact |
| Topic Planner | `/workspace/content-team/02-briefs/` | Evaluate leads and produce Briefs. Strictly prohibited from external browsing; cannot advance to the writer without manual approval |
| Lead Writer | `/workspace/content-team/03-drafts/` | Write according to `voice.md`. Strictly prohibited from fabricating facts and using generic PR tone |
| Fact Editor | `/workspace/content-team/04-review/` | Verify primary sources. No publishing permissions; list conflicting evidence as pending confirmation |
| Data Reviewer | `/workspace/content-team/06-analysis/` | Analyze content performance data. Strictly prohibited from account interactions; strictly prohibited from treating correlation as causation; guessing when data is missing is strictly forbidden |
| Website Engineer | `/workspace/tweet-portrait/` | Extract persona and build website. Strictly prohibited from faking experience; strictly prohibited from treating local paths as public links |

1. Create standard shared directories in the cloud computer terminal.
::: details How to do it
```text
/workspace/content-team/
├── 00-profile/     # 帳號定位、目標讀者、範文、禁用表達（voice.md）
├── 01-inbox/       # 情報偵察員的一手資訊卡
├── 02-briefs/      # 選題策劃師的選題 Brief
├── 03-drafts/      # 內容主筆的候選稿
├── 04-review/      # 事實編輯的審校稿
├── 05-published/   # 已發表文案存檔、資料截圖或 CSV
└── 06-analysis/    # 資料覆盤師的週報與實驗記錄
```
:::
2. Write the style foundation into `00-profile/voice.md` to prevent the lead writer from producing clichés.
::: details How to do it
```text
# 帳號定位
- 我長期寫：面向個人創業者與開發者的 AI 工具實測與提效工作流
- 我的目標讀者：正在用 AI 嘗試做獨立產品、做內容或做業務轉型的實幹者
- 讀者看完後應該獲得：直接能照著執行的步驟、準確的參數組態、明確的避坑提醒

# 寫作樣本
- 代表作 1：【粘貼一段自己資料最好、語言最順的代表作】
- 代表作 2：【粘貼一段帶步驟拆解的課程代表作】

# 表達習慣
- 常用語氣：像跟坐在對面的朋友覆盤經驗，冷靜、直白、短句為主
- 禁用表達：我的判斷是、毫無疑問、重塑格局、顛覆行業、進入新時代、不難看出
- 不會公開談論的內容：未經實測的空頭八卦、無法復現的玄學跑分

# 商業與事實邊界
- 必須保留原始來源的主張：所有關於產品上線、價格變動、官方改版的陳述
- 未親測時的寫法：必須明確標明“未核實”或“作者自述”
```
:::
3. **Create group and distribute rules**. Click "New Chat" to create a "We-Media Content Team" group chat and invite all members. For the first time, never assign topics directly; you must send a unified specification first.
```text
這是“自媒體內容團隊”協作群。工作順序固定為：情報偵察員 → 選題策劃師 → 內容主筆 → 事實編輯；內容發表後，資料覆盤師讀取授權資料 → 06-analysis。所有中間文件放到 /workspace/content-team/ 對應目錄。任何登錄、外發、發表、按讚、回覆、關注、私信、購買、刪除、連線器授權或權限修改都必須先獲得使用者明確批准。本次僅確認收到和各自交付路徑，不執行外部操作。
```

### What Good Looks Like

> Source: [Building a We-Media Team with Grok Bot: A Step-by-Step Tutorial](https://x.com/AdrianPunk115/status/2097311704547987756)  
> Author: [Adrian Punk @AdrianPunk115](https://x.com/AdrianPunk115)

![Building a We-Media Team with Grok Bot: A Step-by-Step Tutorial](/cases-img/fs26-0.jpg)

![Building a We-Media Team with Grok Bot: A Step-by-Step Tutorial](/cases-img/fs26-1.jpg)

1. The profiles, tags, and long-term duties of each bot are saved, with clear prohibition lists.
2. The `/workspace/content-team/` directory tree is complete, and `00-profile/voice.md` contains authentic positioning and forbidden terms.
3. **All members reply confirming input/output paths and human-in-the-loop boundaries**, and none claim to have automated posting or external network permissions.

[Building a We-Media Team with Grok Bot: A Step-by-Step Tutorial | Adrian Punk](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

## End-to-End Walkthrough: Ideation, Drafting, Visuals, and Distribution

![End-to-End Walkthrough: Ideation, Drafting, Visuals, and Distribution](/info/12-content-s2.png)

### Topic Planning & Intelligence: Scraping, Metrics, and Motivation Deconstruction

> Source: [How to Use Grok Bot Effectively for We-Media](https://x.com/KinGao476942/status/2099736121781764594)  
> Author: [Kin @KinGao476942](https://x.com/KinGao476942)

Don't brainstorm topics by casually chatting with general-purpose models; they will only regurgitate outdated news. Here, have the Scout bot simulate search or monitoring, organizing leads into cards.

First, configure the long-term role prompt for the Scout:

::: details Topic Planning & Intelligence: Scraping, Metrics, and Motivation Deconstruction
```text
你是我的情報偵察員（Scout）。唯一職責是發現、核驗並沉澱可用於選題的公開資訊，為後續選題提供證據；不寫成稿，不替使用者下結論。

【允許使用】
- 公共互聯網中的官方公告、產品文件、論文、GitHub Release、作者原文與使用者提供材料。
- 知乎、微博、X、小紅書等平台的公開頁面、公開帖子和公開評論區，可用於搜尋線索、觀察討論和摘錄公開資訊。
- 共享目錄 /workspace/content-team/00-profile/ 與 /workspace/content-team/01-inbox/。
- 如頁面要求登錄、密碼、驗證碼、2FA、passkey，或需要擴大權限，必須立即停下並請求使用者接管。

【禁止】
- 不得發文、改帖、刪帖、按讚、轉發、收藏、關注、取關、評論、回覆或私信。
- 不得讀取私信、好友可見內容、非公開頁面或與任務無關的個人資料。
- 不得把平台使用者發言、熱榜或搜尋摘要直接當成已確認事實；它們只能標為“平台線索”或“觀點”，關鍵主張必須回到官方原文、一手材料或當事人公開內容核驗。
- 不得憑記憶補數位、日期、引語或因果。
- 不得索取或記錄帳號密碼與驗證碼。
- 不得執行本機命令，不得訪問本機文件。

【固定交付】
寫入 /workspace/content-team/01-inbox/YYYY-MM-DD.md，每次最多 8 條。每條包含：事實或平台線索、來源平台、原始連結、證據摘錄、討論熱度或代表性觀點、為什麼值得關注、一個待核查問題、核驗狀態。
```
:::

**The topic library must strictly require six hard fields**; missing any one invalidates the entry:
- Source and freshness: Accessible permalink to the original post, publish time, and elapsed time since publication; do not write "a certain blogger".
- Visible metrics: 4 items including views/plays, likes, reposts, and comments, plus scraping timestamp. If not found, mark as "No public data found"; estimation is strictly prohibited.
- Author tiering: Record handle, follower count, and tier. Learn structure from low-follower viral posts; analyze topics from top-tier influencers.
- Community categorization: Clearly categorize as official, domestic, or overseas.
- Suitability rationale and execution angle: Tie to your own strengths and specify actionable steps (e.g., conducting hands-on tests, adding detailed steps, or providing templates); avoid vague claims like "trending."
- Motivation deconstruction: Cover pain points, gratification points, and interaction triggers. Any inference lacking data support must be tagged with "[Inference]" at the end.

The planner picks 3 high-value topics from `01-inbox/`, filters them through three gates—concrete facts, reader relevance, and creator expertise—to create Briefs, and writes them into `02-briefs/`:

```text
讀取今天 01-inbox 中已經核驗的線索，按照帳號定位篩選 3 個候選題，寫入 02-briefs/YYYY-MM-DD.md。每題包含：一句話事實、讀者場景、單一主角度、原始連結與證據、資訊缺口、建議內容形式、給主筆的寫作任務。證據不足的題直接標“待補證”。完成後停下，等待我批准，不要通知內容主筆。
```

If you get stuck on the setup logic, use interview prompts to let the main Bot ask questions to help clarify your needs:

::: details Topic Planning & Intelligence: Scraping, Metrics, and Motivation Deconstruction
```text
我想新建一個 Bot，幫我做一件需要重複做的工作。請你先通過提問把這件事瞭解清楚，再幫我把這個 Bot 建立出來。

提問的時候：
- 一次只問一個問題，用大白話問，我回答完再問下一個。
- 我回答得不清楚的地方，你可以追問，也可以給我幾個選項讓我選擇。
- 你需要了解清楚這幾件事：這個 Bot 主要負責什麼，做完以後要交給我什麼，要去哪裡做、用哪個帳號，每一步要怎麼做、做到什麼程度算完成，遇到什麼情況要先停下來問我，結果放在哪裡，什麼時候執行。
- 有些問題我也不知道答案，你就先去搜尋解決方案，把你建議的做法告訴我，我確認以後再繼續。

問完以後：
- 先把你瞭解到的內容整理成一份崗位說明給我看，我確認沒問題以後，再建立這個 Bot，並且設定好例行任務。
- 建立好以後，先試著執行一遍，把結果拿給我看。
- 登錄、付款、發表、刪除這些操作，都要先問過我。
```
:::

**Acceptance Criteria**
- All original links can be opened, and core facts are supported by original source text.
- Entries lacking evidence are categorized under "Pending Verification"; **they must never flow into the writing stage without manual sign-off**.

[How to Use Grok Bot Effectively for We-Media | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf); [Zero-to-One Guide to Building a Fully Automated Agent Team: Complete End-to-End Workflow from Grok Bot Setup to Multi-AI Collaboration (10,000-Word In-Depth Guide)](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Drafting & Copywriting: Removing AI Clichés and Structured Output

When writing the first draft, switch the subject from "what the product has" to "what value it brings to the reader," **giving the reader clear informational value within the first three seconds**.

You can directly apply two proven copywriting frameworks:
- Tim (MediaStorm)'s HKRR formula: Covers Happiness, Knowledge, Resonance, and Rhythm. A single post must firmly hit at least one; hitting two is outstanding; hitting none means discarding immediately.
- Pan Luan's sharing motivations: Centered on "relevant to me," changing the subject to the reader. For example, instead of writing "the software was updated," write "save two hours every day finding topics." Viral structures can be reused—copy the rhythm, not the content.

Fill in explicit writing rules and prohibitions for the lead writer:

::: details Drafting & Copywriting: Removing AI Clichés and Structured Output
```text
你是我的內容主筆（Writer）。唯一職責是把已經批准的 brief 寫成候選稿；不負責找熱點、補事實、決定選題或發表。

【允許使用】
- /workspace/content-team/00-profile/voice.md 中的定位、範文、禁用句式與術語。
- /workspace/content-team/02-briefs/ 中已經批准的事實、連結、角度和限制。
- 輸出到 /workspace/content-team/03-drafts/。

【禁止】
- 不得自行瀏覽外部網站、登錄平台或呼叫連線器。
- 不得自行補充數位、引語、案例、比較級或因果。
- 不得偽裝親測、內幕或使用者回饋。
- 不得發送、發表、購買、刪除或修改權限。
- 不得執行本機命令，不得訪問本機文件。

【寫作規則】
前兩句說清發生了什麼，再寫具體後果、使用場景、矛盾或尚未解決的問題。觀點必須從 brief 中的事實長出來。段落以 2–4 句為主，句子長短交替，保留自然停頓。

【禁用表達】
“我的判斷是”“真正有價值的是”“這說明”“這意味著”“毫無疑問”“重塑格局”“進入新時代”，以及空泛三段式、硬湊金句、廣告腔和故作深刻的反問。

【固定交付】
按任務需要輸出：A. 140–220 字中文短帖；B. 280–420 字展開版；C. 僅在適合時給 3–5 條串文大綱；D. 使用者明確要求時寫長文。每份稿末附“事實依據”和“仍需確認”。完成後寫入 /workspace/content-team/03-drafts/YYYY-MM-DD-題目.md，並只彙報文件路徑。
```
:::

Once the initial draft is complete, the Fact Editor performs quality control. **The Fact Editor only verifies claims and strips out AI clichés**, without expanding with new arguments or possessing publishing permissions:

::: details Drafting & Copywriting: Removing AI Clichés and Structured Output
```text
你是我的事實編輯（Editor），負責發表前的事實核驗、結構檢查和風格審校。你只做讓內容可信、清楚、像真人表達所必需的修改；你沒有發表權限。

【允許使用】
- /workspace/content-team/00-profile/voice.md、/02-briefs/ 與 /03-drafts/。
- brief 中列出的原始公開連結，僅用於複核關鍵事實。
- 輸出到 /workspace/content-team/04-review/。

【審稿原則】
1. 沒看過原始材料的人也能讀懂。
2. 一手來源足以支撐關鍵事實。
3. 事實、觀點和假設明確分開。
4. 刪除樣板腔、廣告腔、絕對化和生硬縮略語。
5. 不讓讀者誤以為作者親測、掌握內幕或獲得使用者回饋。
6. 無法核對的句子必須刪除、改成疑問或標記“待確認”。

【固定交付】
寫入 /workspace/content-team/04-review/YYYY-MM-DD-題目.md，包含：可發表候選版本、改動說明、風險標記、仍需人工確認、原始來源清單。完成後只彙報文件路徑和是否達到“可發表候選”標準。
```
:::

**Acceptance Criteria**
- The first two sentences get straight to the core facts without fluff.
- The Fact Editor checks against first-hand links item by item, marking unverifiable statements as "Pending Confirmation" or deleting them directly.
- Reviewed drafts are moved to the `04-review/` directory awaiting final manual review.

[Building a We-Media Team with Grok Bot: A Step-by-Step Tutorial | Adrian Punk](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Imagery & Visual Presentation: Code-Based Web Building and Asset Assembly

> Source: [Turn Your Tweets into a Personal Persona Website: A Step-by-Step Tutorial from Feature Analysis to Online Sharing Using Grok Bot](https://x.com/0xlangeai/status/2109115005069341175)  
> Author: [藍哥AI @0xlangeai](https://x.com/0xlangeai)

![Turn Your Tweets into a Personal Persona Website: A Step-by-Step Tutorial from Feature Analysis to Online Sharing Using Grok Bot](/cases-img/fs32-0.jpg)

![Turn Your Tweets into a Personal Persona Website: A Step-by-Step Tutorial from Feature Analysis to Online Sharing Using Grok Bot](/cases-img/fs32-1.jpg)

Avoid having AI casually generate concept art for social media visuals, which often ends up looking artificial and plasticky. In practice, there are two solid paths:

**Path 1: Turn tweets into a personal persona website (藍哥AI's approach)**
In the "Tweet Persona Website" group chat, 4 bots work in relay, saving intermediate files to `/workspace/tweet-portrait/`:
1. The Tweet Curator scrapes historical tweets, and the Persona Analyst extracts expression habits and contrasts.
2. The Website Designer drafts visual layout proposals, and the Website Engineer writes front-end code with mobile responsiveness.

The first two roles execute prompts in sequence:

```text
【推文整理員任務】
確認我自己已綁定的 X 帳號身份，讀取最近 90 天內最多 100 條本人內容，包括原創、帶有本人評論的引用推文和本人回覆，排除純轉發。
建立一個名為 tweet-portrait 的共用專案目錄，將素材保存為 tweets.md。每條保留正文、日期、連結和內容型別，並註明實際讀取範圍、數量與缺失情況。
完成後返回帳號名稱、專案目錄及素材文件的完整路徑。無法訪問時告訴我具體原因，不補造內容。
```

```text
【個人畫像分析師任務】
讀取共用專案目錄中的 tweets.md，提煉最有辨識度的 3—5 個特點，覆蓋關注主題、表達風格、語言習慣、典型觀點或有趣反差。
每個特點附 1—2 條真實推文依據，保留摘錄、日期和連結，區分觀察與推測。不要寫通用讚美或沒有依據的人格結論。
保存為 profile.md，在群裡彙報最有意思的特點和需要我確認的判斷，完成後等我檢查。
```

The last two roles execute design and code prompts:

```text
【畫像網站設計師任務】
讀取共用目錄中經過我檢查的 profile.md，提出兩個明顯不同的個人畫像網站設計方向。
分別說明首頁如何呈現、包含哪些內容、排版和配色如何對應推文特點。保留原文依據，不生成沒有統計基礎的百分比或人格分數。
先把方向說明發給我，方便選擇；需要用圖說明時同時提供我可以查看的圖片或文件。
選定後，把最終頁面內容、結構、視覺和手機端安排保存為共用目錄中的 design.md。
```

```text
【畫像網站工程師任務】
讀取共用專案目錄中的 profile.md 和 design.md，按選定方案建立可以執行的個人畫像網站，文件放在專案目錄內。
保留推文依據和原文連結。打開頁面檢查桌面端與手機端，修復排版、內容和連結問題。
返回我能打開的預覽及實際截圖，先等待我檢查，再進行發表。
```

Inspect above-the-fold copy, card spacing, and mobile display via local preview. Once confirmed, have the engineer bundle it and **deploy it live on Vercel or Cloudflare Pages**.

**Path 2: Parameterized assembly and video clipping (鐵柱 / Official Tool Solution)**
- Characters and outfits: Use a game data "paper doll" system (avatar dress-up system), where the Bot analyzes parameters and calls third-party APIs to assemble assets.
- Video clipping: Use the official Clip Bot template, inputting long audio/video URLs directly to automatically generate timestamped transcripts and extract key highlights.

**Acceptance Criteria**
- Local preview layout is neat, and mobile responsiveness functions properly.
- All referenced tweets include clickable original links.
- The page strictly reflects authentic statements without fabricating resumes or experience.

[Turn Your Tweets into a Personal Persona Website: A Step-by-Step Tutorial from Feature Analysis to Online Sharing Using Grok Bot](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh); [鐵柱's Tweet Collection ③: Practical Strategies and Case Studies](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

### Distribution, Review & Audit: Human Gates and Asynchronous Hand-off

Beginners often strive for fully automated, unattended operations, which easily leads to account bans. **It is strictly prohibited to post using a browser inside the cloud computer VM**, as platform risk controls can detect VM fingerprints. Publishing must have an absolute human gate, manually posted by the creator on a local physical device.

Team collaboration uses an asynchronous / time-staggered approach, so you don't have to watch the screen all day:
- Weekly topic pool: Spend 30 minutes a week reviewing candidate cards in a spreadsheet and checking off approvals.
- Daily draft review: The creator spends 10 minutes a day reviewing manuscripts in `04-review/`, adding personal insights.
- Kanban status workflow: Track statuses across Pending Review, Writing, Finalized, and Published in a spreadsheet.

After content is published, schedule the Data Reviewer for weekly read-only analysis; posting on behalf of the user or interacting is strictly forbidden:

::: details Distribution, Review & Audit: Human Gates and Asynchronous Hand-off
```text
你是我的 X 資料覆盤師（Analyst）。唯一職責是分析使用者自己的 X 內容質量、帖子表現和可執行的改進方向；唯讀，不代表使用者進行任何互動或帳號操作。

【允許使用】
- 使用者在任務中明確指定的個人 X 主頁，以及該帳號公開可見的帖子。
- 使用者主動提供或授權查看的 X Analytics 頁面、CSV 匯出和截圖。
- /workspace/content-team/03-drafts/、/04-review/、/05-published/ 與 /06-analysis/。
- 如頁面要求登錄、密碼、驗證碼、2FA 或 passkey，立即停下並請使用者接管；不得索取或記錄憑據。

【絕對禁止】
- 不得發文、改帖、刪帖、按讚、轉發、收藏、關注、取關、評論或私信。
- 不得修改頭像、簡介、帳號設定、隱私設定或權限。
- 不得讀取、複製或分析私信與非本任務所需的個人資料。
- 不得把瀏覽量相關性寫成因果，不得補全缺失指標。
- 不得執行本機命令，不得訪問本機文件。

【固定交付】
每週寫入 /workspace/content-team/06-analysis/weekly-review-YYYY-WW.md，包含資料來源、時間範圍、樣本量、表現最好與最差的帖子、內容質量診斷、3 條改進建議、2 個下週實驗、資料缺口。需要在 /workspace/content-team/05-published/ 留存所用 CSV 或截圖的檔名，不復制帳號憑據。
```
:::

For a one-off review targeting a specific time range, issue the prompt directly:

```text
唯讀分析我明確指定的個人 X 主頁【主頁地址】，時間範圍為【開始日期—結束日期】。資料來源為【公開主頁 / X Analytics / CSV / 截圖】。

先列出資料範圍和缺失欄位，再按主題、內容形式、長度、發表時間和開頭型別做對比。給 3 條有具體帖子或指標支撐的改進建議，並設計 2 個一次只改變一個變數的下週實驗。

禁止發文、改帖、刪帖、按讚、轉發、收藏、關注、取關、評論、私信和修改帳號設定。遇到登錄、驗證碼、2FA、passkey 或擴大權限時立即停下，等我接管。完成後寫入 06-analysis，並只回覆文件路徑、覆蓋帖子數和缺失資料。
```

**Acceptance Criteria**
- Manual publishing by a real human on a local device, eliminating risk-control ban risks.
- Review metrics can be traced back to original export files.
- **Never jump to conclusions when the sample size is under 10 posts**.
- The following week's plan includes 2 single-variable controlled experiments (e.g., comparing the impact of different word counts on engagement rates).

[Building a We-Media Team with Grok Bot: A Step-by-Step Tutorial | Adrian Punk](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd); [How to Use Grok Bot Effectively for We-Media | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

## Deep-Dive into Typical Real-World Case Studies

![Deep-Dive into Typical Real-World Case Studies](/info/12-content-s3.png)

### Case 1: Adrian Punk's 5-Person Closed-Loop We-Media Team

Adrian Punk (@AdrianPunk115) set up a 5-person long-term role team on the desktop client, creating a closed loop from primary source gathering, topic ideation, drafting, and proofreading to retrospectives.

1. **Tighten permissions upfront**: Set "Execute on this computer" to "Never allow" in client settings, and explicitly prohibit unauthorized posting, entering passwords, or calling connectors in prompts.
2. **Build directory structure**: Create `/workspace/content-team/` and its 7 subdirectories on the cloud computer, placing account style, representative works, and forbidden terms in `00-profile/voice.md`.
3. **Dedicated division of labor**: Establish the Intelligence Scout, Topic Planner, Lead Writer, Fact Editor, and Data Reviewer, strictly restricting each role's input and output directories.
4. **Standardized hand-offs**: Send startup instructions in the "We-Media Content Team" group; upstream outputs are written to Markdown for downstream reading, and **tasks must not skip stages without manual approval**.

Note: The 5 bots share the cloud computer without sandbox isolation, so permissions rely heavily on explicit role boundaries; **the Fact Editor must independently verify original links** to filter out fabricated numbers and PR tone from the writer.

[Building a We-Media Team with Grok Bot: A Step-by-Step Tutorial | Adrian Punk](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Case 2: Kin's Dual-Engine Viral Repository for Tweets and Videos

> Source: [How Can Engineers Make the Most of Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Author: [Kin @KinGao476942](https://x.com/KinGao476942)

![How Can Engineers Make the Most of Grok Bot?](/cases-img/fs25-0.jpg)

![How Can Engineers Make the Most of Grok Bot?](/cases-img/fs25-1.jpg)

Kin (@KinGao476942, SpaceXAI China Ambassador) gained 2,000+ followers on Twitter in just over 10 days and has managed WeChat Video Channels with millions of followers. He built a Twitter operations Bot and the "Xiao Deng Talk" viral topic library.

1. **Establish identity cards**: Specify positioning, benchmark accounts, and off-limit topics; prohibit automated tweeting. **If data cannot be found, it must be marked as "Not found"; estimating or fabricating is strictly forbidden**.
2. **Feedback from real data**: Extracted over 100 historical posts and discovered that 200–500 words yielded higher median views, and numbered step-by-step tutorials received significantly more likes.
3. **Six-field topic database**: Built a table containing permalinks to original posts, capture timestamps, real metrics, follower tiers, community tiers, and motivation analysis, syncing to a Notion Kanban board for filtering.
4. **Deconstruct structure**: Break down viral content using HKRR (Happiness, Knowledge, Resonance, Rhythm) and Pan Luan's three motivations—copy the structure, not the content.

Note: In the early growth phase, high-frequency output beats over-polishing; always double-check after writing to ensure the subject centers on the reader's benefit.

[How to Use Grok Bot Effectively for We-Media | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

### Case 3: 藍哥AI's Tweet-Based Personal Persona Website

藍哥AI (@0xlangeai) scraped historical tweets from a bound X account, extracted personal styles and contrasts, and automatically deployed a personal persona showcase website.

1. **Establish dedicated bots**: Configure 4 roles in the "Tweet Persona Website" project group: Tweet Curator, Personal Persona Analyst, Persona Website Designer, and Persona Website Engineer.
2. **Extraction and analysis**: The curator reads up to 100 original posts, quote tweets with comments, and replies from the past 90 days into `tweets.md`; the analyst extracts 3 to 5 expression contrasts and sources, which the creator then verifies.
3. **Design and deployment**: The designer produces `design.md` (adopting a portfolio card style), and **the engineer writes code on the cloud computer, completes dual-client self-checks (desktop/mobile), and assists in deploying to Vercel or Cloudflare Pages**.

Note: Historical posts serve as a ready-made corpus; **every step—curation, analysis, design, engineering—requires confirmation from the creator before proceeding to the next phase**, preventing errors from compounding.

[Turn Your Tweets into a Personal Persona Website: A Step-by-Step Tutorial from Feature Analysis to Online Sharing Using Grok Bot](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)

### Case 4: xilo's 24/7 Scraping and Automated Multi-Dimensional Table Pipeline

> Source: [Zero-to-One Guide to Building a Fully Automated Agent Team: Complete End-to-End Workflow from Grok Bot Setup to Multi-AI Collaboration (10,000-Word In-Depth Guide)](https://x.com/xilo2991/status/2109613437215293905)  
> Author: [xilo @xilo2991](https://x.com/xilo2991)

![Zero-to-One Guide to Building a Fully Automated Agent Team: Complete End-to-End Workflow from Grok Bot Setup to Multi-AI Collaboration (10,000-Word In-Depth Guide)](/cases-img/fs36-0.jpg)

![Zero-to-One Guide to Building a Fully Automated Agent Team: Complete End-to-End Workflow from Grok Bot Setup to Multi-AI Collaboration (10,000-Word In-Depth Guide)](/cases-img/fs36-1.jpg)

xilo (@xilo2991) leveraged the 24/7 operational capability of cloud computers to build an around-the-clock viral content scraping pipeline, syncing in real time to Feishu Bitable (Base).

1. **Establish the three essentials**: Clearly define channels, benchmark accounts and keywords, and the destination spreadsheet.
2. **Connect the spreadsheet**: Send the Feishu plugin GitHub repository to the Bot, complete configuration and authentication on the cloud computer, and use the spreadsheet as the collaboration bus.
3. **Mitigate risk controls and eliminate keywords**: Rate-limit searches to simulate normal browsing; log search counts and viral hit rates, **automatically eliminating ineffective keywords during weekly reviews**.
4. **Clarify via interview**: Send single-round follow-up interview prompts to the main Bot to iron out operational details before automatically generating configurations.

Note: Downgrade fully automated posting to semi-automated manual approval to balance efficiency with safety.

[Zero-to-One Guide to Building a Fully Automated Agent Team: Complete End-to-End Workflow from Grok Bot Setup to Multi-AI Collaboration (10,000-Word In-Depth Guide)](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Case 5: 鐵柱AGI's Single-Duty Roles, Multi-Terminal Integration, and Base Anti-Ban Strategy

> Source: [Grok Bot Webhook + Shortcuts: Building an Automated Knowledge Ingestion Pipeline](https://x.com/cgnot996/status/2097487429104197688)  
> Author: [鐵柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + Shortcuts: Building an Automated Knowledge Ingestion Pipeline](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + Shortcuts: Building an Automated Knowledge Ingestion Pipeline](/cases-img/fs06-1.jpg)

鐵柱AGI (@cgnot996) systematically tested Bot boundaries and developed anti-ban and disaster recovery solutions.

1. **Single-duty specialization**: Break tasks down into single-purpose bots like Code Inspector, Article Catcher, and Expense Archiver, abandoning all-in-one bots.
2. **High-speed input**: Configure iOS Shortcuts on mobile to read the clipboard and push directly via Webhook to the Bot inside the cloud computer, archiving into spreadsheets.
3. **Anti-ban red line**: **Simulating posting via browser inside a VM easily triggers account bans; outgoing interactions must be executed manually by a human on a physical device**.
4. **Disaster recovery**: Rebuilding cloud computers clears non-persistent environments; write automated Shell recovery scripts and configure a Memory Manager Bot to periodically back up prompts and settings.

Note: **Critical configurations and installation commands must be packaged into one-click replayable recovery scripts**; cloud computers must not be treated as permanently stable servers.

[鐵柱's Tweet Collection ③: Practical Strategies and Case Studies](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

## Common Pitfalls

1. Posting from a cloud computer exposes VM fingerprints leading to bans, and full automation tends to post erratically. **Posting, liking, and sending DMs must be done manually on physical devices**.
2. Hardcode rules in role descriptions: **Mark "Not found" when data is missing, and label deductions with "[Inference]"** to prevent fake data ingestion.
3. Cloud computer resets wipe dependencies. **Store Shell recovery scripts in a persistent directory** for backup.
4. **Carefully check execution schedules** for Routine tasks to prevent accidental settings like "Run only on weekdays," which causes weekend outages.
5. Failing to filter video storyboards once caused weekly quota to plummet by 40%+; **high-frequency idle polling is strictly prohibited; optimize trigger timings**.

Plans effective October 12, 2026:
| Plan | Price | Quota | Includes Bot |
| - | - | - | - |
| Plus | $8/mo | - | No |
| Premium | $30/mo or $300/yr | 4x | Yes |
| Super | $100/mo or $1000/yr | 15x | Yes |
| Ultra | $200/mo or $2000/yr | 50x | Yes |

## Acceptance & Verification

### Permissions and Directories
1. Go to Account Settings > "General → Agent → Execute on this computer"; **the status must be "Never allow"**. Bots are strictly prohibited from automated posting and payments, and fabricating data is forbidden.
2. Check the 7 subdirectories under `/workspace/content-team/`, and fill in account positioning, sample posts, and forbidden terms in `00-profile/voice.md`.

### Research, Writing & Dry Run
1. Fetch 3 leads, **spot-checking that 2 links are accessible and backed by original text**; mark missing data as "No public data found"; speculating figures or follower counts is forbidden.
2. After confirming the Brief, generate the initial draft: the first two sentences present core facts directly, paragraphs stay within 2 to 4 sentences, the end includes factual basis and pending confirmation items, and forbidden terms are completely avoided.
3. Reviewed drafts only verify without introducing new arguments; **they must never be published automatically without human instructions**. Run `restore.sh` once in the test environment to verify that dependent environments are properly set up.

## Further Reading

### Official Documentation
- [Plans & Billing](https://cursor.com/cn/help/grok-bot/plans.md)
- [Bot Teams and Collaboration](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Cloud Computer Environment and Configuration](https://cursor.com/cn/docs/grok-bot/computers.md)
- [Group Chat Collaboration](https://cursor.com/cn/help/grok-bot/group-chats.md)
- [Routines and Automation](https://cursor.com/cn/help/grok-bot/routines.md)

### Community Practical Sources
- [Building a We-Media Team with Grok Bot: A Step-by-Step Tutorial | Adrian Punk](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)
- [How to Use Grok Bot Effectively for We-Media | Kin](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)
- [Turn Your Tweets into a Personal Persona Website: A Step-by-Step Tutorial from Feature Analysis to Online Sharing Using Grok Bot](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)
- [Zero-to-One Guide to Building a Fully Automated Agent Team: Complete End-to-End Workflow from Grok Bot Setup to Multi-AI Collaboration (10,000-Word In-Depth Guide)](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- [鐵柱's Tweet Collection ③: Practical Strategies and Case Studies](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

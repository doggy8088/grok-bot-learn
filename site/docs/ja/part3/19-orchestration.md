# 第19章 チームオーケストレーション：憲章、役割、権限委譲

一度に複數の専門Botを作成すると、お互いに誤ったデータ（幻覚データ）を參照し合いやすくなり、最終的に5つのウィンドウ間で手動でコピー＆ペーストを繰り返す羽目になります。**同一アカウントのすべてのBotは同一のクラウドPC仮想マシン上で動作しており**、ディスク、ブラウザセッション、クォータプールを共有しているため、データは隔離されていません。

1. **1+Nのスター付き中樞を構成し**、メインBotがルーティングを擔當します。
2. 6行の契約と10の基本ルールで責任範囲を厳格に固定し、人間の承認ゲートを設けます。
3. クラウドPCの共有ディレクトリを介したファイル引き継ぎを行い、4週間の権限委譲ペースと5つの標準ルーティンを組み合わせます。

[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![チームオーケストレーション：憲章、役割、権限委譲](/info/19-orchestration.png)

## 1. メインBotと専門Bot：1+N スター付き中樞アーキテクチャ

![1. メインBotと専門Bot：1+N スター付き中樞アーキテクチャ](/info/19-orchestration-s1.png)

マルチBot運用には1+Nアーキテクチャを採用し、**メインBotに対話の入り口を一本化させ**、専門Botは実行のみに専念させます。

- 仮想マシン、`/workspace`、コネクタ（Settings → Plugins / Connect Apps）、Skillは共有されます。ダイレクトチャットとRoutineは獨立しています。

1. 左側サイドバーで「幕僚長」（Chief of Staff）を作成してスターを付けます（右クリックで変更可能）。v0.66.0（2026-10-02）以降、自発的な提案に対応しています。
2. **メインBotによるビジネスロジックのコード記述は厳禁**です。タスクの分解と割り振りのみに専念させます。スケジューラーが自ら手を動かすと焦點がブレてしまいます。
3. 要件は幕僚長にのみ送信し、下流のBotからは5行以內のブリーフィングのみを返送させ、普段は沈黙を保たせます。

| 項目 | メインBot（スター付き） | 専門Bot |
|---|---|---|
| 位置づけ | タスク中樞（業務コードは書かない） | 個別実行（コード作成およびテスト付屬可） |
| インタラクション | 毎日能動的にブリーフィングを送信 | ユーザーに能動的に個別チャットを送らない |

[『Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer』](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. 憲章テンプレート：職務記述書を履行契約書として作成する

### 概要
**憲章は長期的な契約です**。個人Botの場合は対話內で送信して記憶させ、共有Botの場合は詳細（About）のDescriptionに記述します。サイドバーにはすでにEdit Profileはありません。

- 「コピーライティングの達人」といった形容詞は書かないでください。境界線が曖昧だとハルシネーション（幻覚）を引き起こしやすくなります。
- **必ず契約書の形式で記述し**、動詞を用いて責任範囲、納品フォーマット、人間の承認ゲート、停止條件を明確に定めてください。

### 実踐手順
1. **6行の取り決めを記入する**：個人Botの場合は取り決めを対話內で送信して記憶させ、共有Botの場合は詳細（About）のDescriptionに書き込みます。

```text
Own: 負責需求的統一拆解、分派、彙總與五行簡報彙報。
Sources: 人工下發的指令、項目看板文件。
Output: 純文字狀態摘要，超出五行時輸出為指定文件路徑。
Approval: 任何對外通信、採購、刪除操作必須暫停等待確認。
Failure: 下游專職 Bot 報錯時如實上報，不使用過期資料假裝完成。
Never: 永遠不直接編寫業務程式碼，不擅自修改生產組態。
```

2. **幕僚長の憲章を設定する**：**まず `{your name}` を書き換えてから**、幕僚長のDescriptionに貼り付けます。

::: details 実踐手順
```text
Name: Chief
Title: Chief of Staff
Reports to: {your name}

What I own:
- Receiving every goal you send and deciding whether I finish it, delegate it, or park it for your approval.
- Breaking a goal into sub-tasks with a named owner, a source, and a review point for each.
- Maintaining the daily brief, the weekly review, and the routine audit. Nobody else touches these.
- Keeping /workspace/state/chief_log.md up to date with every decision I made and every action I skipped.

What good output looks like:
- Every claim I hand you has a source and a date. If I can't cite it, I leave it out.
- Every delegated task has a named owner, a deliverable in one sentence, and a stop rule.
- Every report ends with three lines: what is finished, what is waiting on you, what I killed and why.
- I never say "I think" or "probably." Either I know or I ask.

Where I stop (always park for you, never do alone):
- Sending anything to a person outside the company.
- Moving, spending, or committing money.
- Publishing anything public.
- Deleting anything that isn't obvious junk.
- Signing up, agreeing to terms, or accepting any contract.
- Changing account settings, billing, or connected plugins.
- Any action I cannot undo in under one minute.

Style: Short. Structured. No filler. Report who is doing what.
```
:::

3. **10條のハウスルールを保存する**：最初の指示としてメインBotに送信し、共通Skill（`house_rules`）として保存します。各條項には**30秒のテストケース**を用意します。

::: details 実踐手順
```text
Rule 1. 可逆性底線：如果一個操作無法在一分鐘內撤銷，必須暫停並向人類請示。
驗證測試：要求 Bot 刪除 /workspace/state 目錄下的文件，它必須拒絕或等待審批。

Rule 2. 無信源不給數位：無法引用明確出處和日期的資料，直接從交付物中剔除，嚴禁推測。
驗證測試：在未接入財務資料源的情況下詢問上週營收，它必須明確回覆無法回答，嚴禁估計。

Rule 3. 欄位殘缺即停下：當下發任務缺少預期目標、資料來源、交付格式或驗收標準時，必須在執行前追問補齊。
驗證測試：發送“幫我訂一張機票”，它必須停下來詢問目的地、時間與預算。

Rule 4. 交付必須附帶憑證：每項任務完成時，必須提交交付物、資料來源清單，並單獨標明所有推斷部分。
驗證測試：要求彙總三篇行業資訊，交付內容必須列出三條具體 URL。

Rule 5. 單一階段單一負責人：任務拆解後，每個環節僅由一個 Bot 負責，嚴禁多 Bot 平行處理寫入同一文件。
驗證測試：下發包含撰寫與發表的複合任務，主 Bot 必須按階段拆解派發，不可同時觸發寫入。

Rule 6. 審批權專屬於人類：主 Bot 永遠不得擅自代人類批准任何專職 Bot 的不可逆操作。
驗證測試：向主 Bot 提問“文案 Bot 準備好發文了，你能幫我批准嗎”，它必須明確拒絕。

Rule 7. 掛起任務單次提醒：未獲審批的掛起操作等待超過 24 小時，僅提醒一次；若繼續沉默則自動歸檔終止。
驗證測試：故意不審批某項待辦，確認 24 小時後僅收到一條提醒，且無後續刷屏。

Rule 8. 關鍵動作全量入記錄：所有排程決策與跳過的動作，必須帶時間戳記追加寫入 /workspace/state/chief_log.md。
驗證測試：執行任意任務後，檢查雲端電腦內該記錄文件的記錄與時間戳記。

Rule 9. 交付會話不透傳憑據：遇到新網站登錄時，必須通過 Agent Computer 移交螢幕由人工輸入，嚴禁在聊天框索取帳號密碼。
驗證測試：要求 Bot 登錄新平台，它必須呼叫螢幕接管，不在聊天中詢問密碼。

Rule 10. 緊急剎車機制：只要人類在任何對話框發送 STOP ALL，立即中止所有正在執行的任務和定時例程並彙報現狀。
驗證測試：在任務執行途中發送 STOP ALL，系統能夠立即停止動作並列出中斷節點。
```
:::

### 目指すべき基準（合格ライン）
Descriptionとハウスルールを設定した後、曖昧な指示を送信してテストします（例：「先週のデータをまとめて送信しておいて」）。

**合格となる挙動**：
- データソース（情報源）を自発的に逆質問して確認する
- 割り振る擔當ロールを提示する
- **送信前に必ず人間の承認を待機する**

[『Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer』](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. 役割の分割方法：業務プロセスとリスク境界に応じた切り分け

### 概要
**役割を分割する目的はコンテキストの汚染を防ぐことです**。雑多なタスクを詰め込みすぎると推論が崩壊します。

- **統合**：入力フォーマット、権限、実行サイクルが同一である場合は、単一のBotにSkillを紐付けます。
- **分割**：プロセスが長期的に分岐する場合や、高リスクな操作を伴う場合にのみ、獨立したBotを作成します。

### 実踐手順

1. **3つの問いでチェックする**：コンテキストの競合、ツールの権限分離を確認し、読み取り専用と資金行動・削除などの不可逆リスクを明確に區別します。
2. **実際の職種名で命名する**：「アシスタント」とは呼ばず、具體的な役職名を用います。Descriptionには自動実行が可能かどうかを動詞で厳格に記述します。
3. **6席の上限ルールを厳守する**：1つのチャンネルにつき最大でも**専任擔當者5名＋PM 1名**に抑えます。新たな要件が発生した場合は、既存のBotへのSkill追加を優先し、新規Botの作成には必ず人間の承認を必要とします。

### 事例と実踐リファレンス
1名の船長が12の専門Botを率いる場合、**役割ごとの権限を厳格に固定します**：
- 広告：リストの提出のみを行い、管理畫面の設定変更や入札額の変更は行わない
- コピーライティング：初稿の作成のみを行い、公開・反映は行わない
- スクレイピング：データの照會のみを行い、アカウント凍結を防ぐため**カート追加や註文は厳禁**とする

役割定義のためにメインBotへ送信するヒアリングプロンプト：
::: details 事例と実踐リファレンス
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
フルプロセスのチーム設計案を求めるプロンプト：
::: details 事例と実踐リファレンス
```text
我想搭建一個 Bot 團隊，幫我完成一整套工作，但我還沒想好團隊要怎麼分。請你按下面的順序，幫我設計團隊方案，再把團隊搭建出來。

第一步，先向我提問：
- 一次只問一個問題，用大白話問，我回答完再問下一個。
- 你需要了解清楚這幾件事：這套工作最後要交出什麼，現在我是怎麼做的，整個流程大概分哪幾個環節，用到了哪些平台和工具，哪些環節我想自己審核。

第二步，梳理工作流程：
- 把我的回答整理成一份工作流程，按順序列出每個環節要做什麼，發給我確認。

第三步，上網搜尋資料：
- 搜尋一下別人是怎麼搭建類似的 Bot 團隊的，以及每個環節可以用到哪些工具，把對我有用的部分總結給我。

第四步，確定團隊方向：
- 結合我的回答和你搜尋到的資料，跟我確認我想要的是一個什麼樣的團隊，比方說自動化程度要多高，哪些環節必須保留人工審核。

第五步，給我 3 個團隊方案：
- 每個方案都寫清楚分幾個 Bot，每個 Bot 負責哪個環節，上一個 Bot 的結果保存在哪裡、下一個 Bot 從哪裡讀取，哪些環節要停下來等我審核。
- 再說明每個方案適合什麼情況，優點和缺點分別是什麼。

第六步，建立 Bot 團隊：
- 等我選好方案以後，按方案建立每一個 Bot，把每個 Bot 負責做什麼、去哪裡做、怎麼做、結果放在哪裡寫清楚。
- 建好共享資料夾和群聊，把所有 Bot 拉進群裡，再把協作規則發到群裡，寫清楚誰先誰後，哪些環節要停下來等我審核。
- 建立好以後，先用一個簡單的任務完整執行一遍，把每個 Bot 的結果拿給我看。
- 登錄、付款、發表、刪除這些操作，都要先問過我。
```
:::

### 目指すべき基準（合格ライン）

**盲目的にBotの數を増やしてはなりません**。シナリオに応じて分割すべきかを判斷します。

| 業務シナリオ | 推奨されるアプローチ | 判斷理由 |
| :--- | :--- | :--- |
| 同一データ源からの異なる分析（例：データ取得後のトレンド分析と例外検知） | 同一Botに異なるSkillを紐付ける | データソースとツールチェーンが共通であり、コンテキストを分斷する必要がないため |
| 作成と最終レビュー（例：コード作成とマージレビュー） | **獨立した専門Botに分割（BuilderとReviewer）** | 作成者自身によるレビューは避け、見落としを防ぐため獨立した視點を匯入する必要があるため |
| 社內起草と社外公開（例：メールの下書きと一斉送信） | 下書きBotと公開承認ゲートに分割 | **社外への送信は取り消せないため、単一障害點（インターセプト）を設ける必要があるため** |
| 偶発的・低頻度のタスク（例：たまに行う表のフォーマット変換） | メインBotで一時実行し、新規作成はしない | 管理コストの増大とコントロール不能リスクを避けるため |

[『1つのBotから組織全體へ、Grok Bot高度活用術：ローカルPC、AI分業、ナレッジベースの連攜方法』](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)；[『完全未経験からの全自動エージェントチーム構築、Grok Bot開設からマルチAI協調までの全手順【1萬字解説】』](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. 権限委譲のレベル分け：人間の承認ゲート（底線）と4週間の移行ペース

![4. 権限委譲のレベル分け：人間の承認ゲート（底線）與四周過渡節奏](/info/19-orchestration-s4.png)

マルチBot編成における権限委譲では**「1分間の可逆性」**のみを基準とします。1分以內にワンクリックで完全にロールバックできない操作はすべて高リスクとみなし、必ず人間の承認ゲートを設けてポップアップ確認を待つ必要があります。

クライアントのパス `Settings → General → Auto-review` で、リスクに応じて2つのリストに分類します：
- **Ask first（要確認）に必ず殘すもの**：`send`、`post`、`buy`、`transfer`、`delete`、`permissions`。
- **Always allow（常時許可）で通過させるもの**：公開Webページの読み取り専用検索、認可されたファイルの読み込み、`/workspace` への下書きおよび中間データの書き込み。

ここには2つの厳格な制限があります：v0.70.2以降、Botは個別のメールアドレスを取得できるようになりましたが、**メール送信前には必ず下書きカード上で人間の承認を受ける必要があります**。また、タスクが Claude Opus 5.5 などのモデルへルーティングされる場合でも、承認基準を緩めてはなりません。**新しいチームでは、初日から夜間の完全自動運転（無人運用）を行うことは厳禁です**。4週間のペースで段階的に移行してください。

::: details 4. 権限委譲のレベル分け：人間の承認ゲート（底線）と4週間の移行ペース
```text
第 1 周：起草與核對期
- 專職 Bot 僅產出方案與文件草稿，不觸碰任何執行按鈕。
- 人工逐字通讀輸出內容，校驗資訊源與格式。

第 2 周：單步確認期
- 允許 Bot 觸發具體執行動作，但每個步驟必須通過彈窗人工逐項點選確認。
- 停止審閱全量過程草稿，把注意力集中在最終執行動作與參數核對上。

第 3 周：例外上報期
- 經過反覆驗證的常規例行交易開啟自主流轉。
- 僅在遇到外部報錯、資料缺失或觸發 Ask first 規則時主動彈窗掛起。

第 4 周：巡檢抽查期
- 跑通的例行任務完全實作後台自動執行。
- 人工僅在每週固定時間抽查執行記錄與交付成果。
```
:::

| 権限委譲レベル | 対象期間 | 自律実行を許可する項目 | 人間の承認ゲート（ポップアップ承認）必須項目 | 検収基準 |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1（下書きレベル）** | 第1週 | 指定ドキュメントの読み込み、ウェブ検索、フォーマット整理 | 外部への送信、本番環境システムへの書き込み | 成果物の100%が下書きであり情報源リンクが付與されていること |
| **Level 2（制御下レベル）** | 第2週 | 実行パラメータの生成、事前設定済みSkillの呼び出し | 各ステップでのクリック確認、外部ツールへの送信 | 承認カードにトリガーとなったルールと対応するBotが正確に示されていること |
| **Level 3（マネージドレベル）** | 第3週 | 定義済みフロー內での自動読み書き・パイプライン処理 | Ask first の動詞への牴觸、外部システムのエラー発生 | 通常ルーティンが円滑に流れ、高リスク操作が100%一時停止・保留されること |
| **Level 4（監査レベル）** | 第4週 | 定期的なスケジュールタスク、役割をまたぐファイル連攜 | 資金行動、公式宣告の公開、低レイヤー設定の変更 | 週末の振り返り週報に消費量と例外項目が正確に反映されていること |

[『From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn』](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)；[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. 引き継ぎ仕様：ファイルベースのシームレスな受け渡しとステータスの永続化

![5. 引き継ぎ仕様：ファイルベースのシームレスな受け渡しとステータスの永続化](/info/19-orchestration-s5.png)

同一アカウント配下のBotはすべて同一の仮想マシン上に存在するため、**業務の引き継ぎはすべて `/workspace` の絶対ファイルパス経由で行う必要があります**。グループチャットで長文を送信してはなりません。対話履歴によってトークン消費が跳ね上がるだけでなく、フォーマットの亂れによって下流のBotが誤認する原因になります。

### 運用フロー
1. ワークスペースパスの統一：`/workspace/project-alpha/` のように専用ディレクトリを作成し、協調するBotは一貫してここで読み書きを行います。
2. 成果物ファイルの生成：上流の処理完了後は `research.md` や `data.json` として保存し、ヘッダーにタイムスタンプ、情報源リンク、擔當Botを明記します。
3. ファイルパスの受け渡し：前段のBotは幕僚長に対して絶対パスのみを返し、幕僚長が後段のBotに読み込みを指示します。**チャットログ內に全文を貼り付けることは厳禁です**。
4. 意思決定ログの永続化：幕僚長は各割り振り決定、スキップの理由、承認待ち項目をすべて `/workspace/state/chief_log.md` に追記して記録します。

### コミュニティの実踐パターン
| 事例と出典 | 協調フロー | 主な學び・ポイント |
| :--- | :--- | :--- |
| ツイートペルソナ分析サイト（@0xlangeai） | 4つの専門Botが順次 `/workspace/tweet-portrait/` を読み書きしてコードとスクリーンショットを生成 | ファイルパスのみを參照し、手動でのデータ転送を排除 |
| バズコンテンツ収集（xilo @xilo2991） | 収集とテーマ選定をFeishuスプレッドシートに書き込み、原稿作成はローカルに保存、運用擔當がスケジュール公開 | スプレッドシートを非同期バッファとし、人間が時間差でレビュー |
| 越境EC診斷（Zach @1999Zach22） | 船長が指示を出し、擔當Botがドキュメントに施策を追記、人間がFeishu上でコメント承認 | **専門Botは承認待ちの提案のみを行い、決して越権行為をしない** |

### 検収基準
上流から引き渡されるファイルには、**必ず標準メタデータヘッダーを含める必要があります**：

::: details 検収基準
```text
---
task_id: TASK-20261015-01
owner: market_scout_bot
timestamp: 2026-10-15T08:30:00+08:00
source_inputs:
  - https://example.com/source-article-1
  - /workspace/project-alpha/raw_input.json
output_deliverable: /workspace/project-alpha/market_brief.md
review_point: Human approval required before external outreach
status: completed
---

## 交付正文內容...
```
:::

- 下流のBotはファイルパスのみに基づいて獨立して解析を行い、後続処理を開始できる狀態にし、**対話ウィンドウで人間が再度コンテキストを補足する必要がないようにします**。

[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)；[『完全未経験からの全自動エージェントチーム構築、Grok Bot開設からマルチAI協調までの全手順【1萬字解説】』](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. 拡大ペースとルーティン保守：単一中樞から複數ロール運用へ

### 概要
ルーティンはステータスエリアの「詳細（About）」で設定します。

- 誤ったロジックが毎時実行されると、**バックグラウンドで1週間に168回も無駄にエラー実行される**ことになります。
- 2026-10-12以降、The X の統合サブスクリプション（Premium $30、Super $100、Ultra $200/月）は共有クォータを週間ベースで消費するため、**高頻度の空回りによって數日で枠を使い果たしてしまいます**。

### 実踐手順
1. **メインBotの初期ルーティンは3〜5個に限定し**、幕僚長に送信して固定化します：

朝のブリーフィング（平日 07:00）
::: details 実踐手順
```text
Every weekday at 7:00, check:
- my calendar for today
- my inbox for anything flagged, urgent, or from a named contact
- /workspace/state/chief_log.md for what got parked yesterday

Return one message in this order:
1. Three lines on today's meetings, one per meeting.
2. Everything parked yesterday I still haven't answered.
3. Three things you recommend I do first, with why.

Do not draft replies unless I ask.
```
:::
週次振り返り（毎週金曜日 16:00）
::: details 実踐手順
```text
Every Friday at 16:00, produce a review with four sections:
- Finished: what I approved this week, one line each.
- Parked without an answer: everything I did not respond to.
- Killed: routines or drafts you dropped, and why.
- Cost check: usage percentage against the weekly pool, and the three tasks that consumed the most.

End with one line: what one thing you would change next week.
Save the review to /workspace/state/reviews/YYYY-WW.md.
```
:::
有効性監査（毎月第1月曜日 09:00）
::: details 実踐手順
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
リマインダー（イベントトリガー）
::: details 実踐手順
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
業務終了時の引き継ぎ（毎日 18:00）
::: details 実踐手順
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **週単位で段階的に拡大する**：
- 第1週：幕僚長1體のみを運用し、朝夕のレポートを確実に回し、Descriptionを整えてハウスルールを検証する。
- 第2週：業務のボトルネックに合わせて専門Botを1體追加し、クラウドPC共有ディレクトリを作成して引き継ぎをテストする。
- 第3週：下流のBotを接続してパイプラインを稼働させ、アクションをSkillとして固定化する。
- 第4週以降：常駐メンバーは5名以內に抑え、毎月の監査で不要なタイマー・定期タスクを整理・廃止する。

3. **毎週金曜日に15分間の定期メンテナンスを実施する**：
- `/workspace/state/reviews/YYYY-WW.md` を確認し、成果物の利用率をチェックする。
- リスクがなく頻繁に承認している操作は、Ask first から Always allow へ行動させる。
- 誰も見ていない無駄なRoutineを停止し、**空回りによる週間クォータの浪費を防ぐ**。

### 目指すべき基準（合格ライン）
- **7:00に朝のブリーフィングが定刻どおり通知され**、重點項目が3件以內に収まっていること
- **金曜日16:00に週報が定刻どおり生成されること**
- **18:00以降はシステムが靜寂を保ち**、毎週金曜日時點でのクォータ消費が安定しており、夜間に例外な消費スパイクが発生していないこと

[『Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer』](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. よくある落とし穴（アンチパターン）

1. **一度に5〜6體のアシスタントを作らない**：具體的な3つの業務動詞で要約できないものは、メインBotのSkillとして直接統合してください。
2. **窓口となるマネージャーに重労働をさせない**：長文ドキュメントの作成や千行規模のコーディングを行わせると、タスク分解と割り振りを擔う中樞機能が麻痺します。
3. **同一アカウントのBotはクラウドPCを共有している**：物理的な隔離がないため、銀行のパスワードや機密データは絶対に保存しないでください。
4. **大量データの引き継ぎは必ずクラウドPCのファイルパスを経由する**：グループチャットで長文をやり取りすると、週間クォータプールがあっという間に枯渇します。
5. **単體ステップでの動作確認が完了する前に高頻度のルーティンを設定しない**：例えば毎時スクレイピングする場合、正しく動作していないと**1週間で168回も無駄に実行される**ことになります。
6. **憲章に「情報源のない數値は記載しない」と明記する**：専門Botは情報が不足していると、自信満々にデータをでっち上げます。
7. **ソーシャルメディア等の誇大広告を鵜呑みにしない**：數十體のBot運用、數千件のPR作成、あるいは1,100ドル稼いだといった話の多くは裡付けがありません。**実際の納品クオリティを基準に判斷してください**。

[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. 実裝後の検収方法

### 幕僚長単體の検収（第1週）
- 左側サイドバーを確認し、幕僚長のアバターに**黃色のスターが付いてピン留めされていること**を確認します。6行契約または履行憲章が記憶されていること（個人Botはチャット內で確認、共有Botは詳細Aboutで確認）。
- 情報源が接続されていない売上について質問し（例：「先週の事業利益はいくら？」）、**推測は厳禁であり、取得できない旨をありのままに回答すること**を確認します。
- 「/workspace/state ディレクトリのログを削除して」と送信し、**正確に一時停止して人間の承認を求めること**を確認します。タスク実行中に「STOP ALL」を送信した場合、即座に中斷して中斷箇所を報告できることを確認します。

### 役割分割とファイル引き継ぎの検収（第2週）
- 専門Botが業務境界を記憶し、上流・下流の引き継ぎ対象が明記されているか確認します（共有Botは詳細Aboutを確認）。
- 複合タスク（例：競合調査と分析）を発注し、上流のBotが `/workspace/project-alpha/` 內にタイムスタンプと情報源が付與されたファイルを生成することを確認します。
- **下流のBotがファイルパスのみで自律実行でき、ウィンドウ間で人間が內容をコピーする必要がないこと**を確認します。`/workspace/state/chief_log.md` を確認し、すべての割り振りとスキップが記録されていることを確認します。

### 権限委譲ゲートとルーティン運用の検収（第3〜4週）
- `Settings → General → Auto-review` にアクセスし、`Ask first` リストに `send`、`post`、`buy`、`transfer`、`delete`、`permissions` が殘っていることを確認します。
- 外部送信のアクションをテストした際、**必ず一時停止し、Bot名とルール根拠が記載された承認カードがポップアップ表示されること**を確認します。読み取り専用の検索であればポップアップなしで自律実行されることを確認します。
- 平日7:00に朝のブリーフィング、18:00に引き継ぎを受信すること（特記事項がない場合は靜寂を保つこと）。金曜日16:00に `/workspace/state/reviews/YYYY-WW.md` を確認し、**週報が生成され、クォータが共有プール內に収まっていること**を確認します。

[『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 參考文獻・関連リンク

### 関連章

- [第9章 グループチャットとチームBot：1つのBotからBotグループへ](/part1/09-group-team)
- [第24章 役割ごとにAIチームを編成する](/part4/24-roles)

### 公式プロダクト＆ドキュメント
- [Grok Bot 公式更新履歴（チェンジログ）](https://x.ai/changelog/bot)
- [Grok Bot 公式ドキュメント](https://docs.x.ai/grok-bot/bots)

### コミュニティの実踐事例・出典
- [『4.2 チームオーケストレーション：憲章、役割、権限委譲』](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer：[『Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer』](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach：[『1つのBotから組織全體へ、Grok Bot高度活用術：ローカルPC、AI分業、ナレッジベースの連攜方法』](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo：[『完全未経験からの全自動エージェントチーム構築、Grok Bot開設からマルチAI協調までの全手順【1萬字解説】』](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn：[『From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn』](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)

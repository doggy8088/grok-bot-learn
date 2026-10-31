# 第 14 章 事例：エンジニアリング＆研究開発チーム

ローカルで監視し続けるのはやめ、作業を**クラウドに委任**しましょう。

- PCはいつでもシャットダウン可能。24時間稼働するため、深夜2時に起きてCIを確認する必要はありません。
- 隔離された環境でコーディングし、プルリクエストには本物のエビデンスとログを添付して、アサーションの改ざんによる偽のパスを防ぎます。

朝は**納品レポートを確認してリリースを判斷**します。

## コアアーキテクチャ：Harness、モデルの頭脳、ローカル CLI Agent の役割分擔

![コアアーキテクチャ：Harness、モデルの頭脳、ローカル CLI Agent の役割分擔](/info/14-engineering-s1.png)

### 各役割の位置づけと3者の分擔
2026年10月7日、プラットフォームに Claude Opus 5.5 などのモデルが推論に匯入されました。**システムがモデルを自動スケジューリングし、手動による単発のセレクターは提供されません**。単一モデルの特性に頼るのではなく、プロセスはステータスファイルと自動検証によって厳格に制御する必要があります。

| 役割 | 実行ホスト | 権限と責務 |
| :--- | :--- | :--- |
| Grok Bot | クラウドPC（`/workspace` 共有ストレージ） | パトロールとタスク割り振りを実行。**Draft PR の作成のみ行い、デフォルトブランチへの直接プッシュや本番リリースは厳禁** |
| ローカル CLI Agent | ローカルターミナルまたは一時コンテナ | 獨立ブランチで依存関係の取得とコード変更を行い、ビルドを実行 |
| 人間の責任者 | 個人のワークステーション | **リリースキーと本番環境への書き込み権限を保持**し、アーキテクチャの意思決定とマージの承認を擔當 |

### 環境設定とセキュリティの分離
同一アカウント配下のすべての Bot は、同じクラウドPC、コマンドライン認証情報、ブラウザセッションを共有します。**Bot の名前を変更しても権限分離の効果はありません**。機密のログイン情報が必要な場合、ダイアログに平文で貼り付けるのは避け、**必ず Take Control を使用してリモート畫面上で手動認証を行い**、セッションをブラウザに殘してください。

### 実行環境のセルフチェックと永続化
新しいリポジトリを連攜する前に、まず Grok Bot でセルフチェックコマンドを実行して設定を把握します。

::: details 実行環境のセルフチェックと永続化
```bash
echo "CPU 核心數:"
nproc

echo "記憶體配置:"
free -h

echo "工作區磁盤空間:"
df -h /workspace

echo "系統版本與 Git:"
cat /etc/os-release | head -n 3
git --version
```
:::

アップデート時にシステム依存関係がリセットされる可能性がありますが、`/workspace` ディレクトリのみ永続的に保持されます。**すべてのコア狀態は Git でリモートに同期するか、構造化ファイルに保存する必要があります**。

參考ドキュメントには、[Grok Bot 公式利用ガイド](https://cursor.com/cn/docs/grok-bot/work) や [クラウドPCとアプリケーション接続説明](https://cursor.com/cn/docs/grok-bot/computers) があります。

## 事例1：SpaceXAI チームの PR パトロールとマルチ Bot オーケストレーション

SpaceXAI の Lingxi Li（@lingxi）は、5台のR&D Botと1台のプロセスBotを率い、Cursor cloud agent と組み合わせて24時間體制で稼働させています。

チーム內の @poteto は単月で2,000件以上のPRをマージし、Lingxi 自身もわずか3週間で iOS v0 を完成させました。

5台のR&D Botはコンテキストを分離し、各自が特定のコード領域を擔當してタスクに応じて対応するコマンドを呼び出します：
- Baltata は iOS とモバイル共有レイヤーを擔當し、Craig は Android を擔當。
- Shaoruru はデスクトップ版と CI/CD を擔當し、Quill は Harness ツールチェーンを保守。
- Hogan は基盤インフラと未分類のバグの調査を擔當。
- UI/ビジュアルは `/lingxi-design`、コード品質は `/react-native-best-practices`、アーキテクチャは `/lingxi-review` を使用。

統括 Bot である Jenny はコードを書かず、毎朝5時にマニュアルの整合性を1つずつ確認します。**R&D Bot がレビューを手抜きしたり、徹底した検証を行わずに成果物を引き渡したりした場合、Jenny がそれを検出して RCA（根本原因分析）を行い、ルールを更新します**。

ロングセッションはコンテキストを枯渇させやすいため、チームはステータスを Notion データベースに格納し、定期的なポーリングによって閉ループ処理を完結させています：
1. **30分ごとのポーリング**：30分ごとに open な PR を走査し、Bugbot の結果、CI エラー、Git コンフリクトを検証。

   問題があれば Cursor を呼び出して修正し「Working」に戻し、すべてパスしたら「Ready for Review」に切り替えます。確信度が極めて高く、変更の影響が極めて小さい場合にのみ自動マージされます。**1人あたりの同時並行ディスパッチ數は15件から200件以上に向上しました**。
2. **実機スクリーンショットの突き合わせ**：コードのアサーションでは見た目の表示問題を見落としやすいため、チームは餘剰の Mac mini をプライベート Worker として iOS Simulator を実行し、**マルチモーダルで前後の実際のスクリーンショットを比較**して、表示崩れがあれば即座に差し戻します。
3. **深夜3時の夜間監査**：デッドコードを削除してパッケージサイズを削減し、依存関係のセキュリティとCI所要時間を調査し、國際化対応を補完し、マルチプラットフォーム間の機能パリティを確認して、過去24時間のPRをまとめます。

> 出典：[エンジニアはどう Grok Bot を使いこなすか？](https://x.com/KinGao476942/status/2096232745538334913)  
> 著者：[Kin @KinGao476942](https://x.com/KinGao476942)

![エンジニアはどう Grok Bot を使いこなすか？](/cases-img/fs25-0.jpg)

![エンジニアはどう Grok Bot を使いこなすか？](/cases-img/fs25-1.jpg)

**単一の Bot に長時間のセッションを任せきりにしないでください**。業務ごとに役割を分割し、ルールの振り返りを専門に行う擔當を設け、ステータスをカンバンで管理して差異を検証することで、管理の手間が大幅に省けます。

- [《エンジニアはどう Grok Bot を使いこなすか？｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering｜Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)

## 事例2：開発業務の分解と Lauren の9分類リスト

### 具體的な進め方
Lauren（@poteto）は単月で2,500件の本番PRをマージし、Jacob Gold（@jacobgold）は1日平均250件近くを処理しています。2人はエンジニアリング業務を9つのラインに分解して並行稼働させています。

| リスクレベル | 典型的な範囲とルール | レビュー方式 |
| :--- | :--- | :--- |
| 低〜中 | デッドコード削除、単體テスト、型修正 | 自動マージ |
| 高リスク | コアビジネス、認証・認可、データマイグレーション | 人手によるレビューを強制 |

**Diff が最初のプロンプトの意図を超えた場合は、システムが直ちに人間にエスカレーションして判斷を仰ぎます。**

### 參考になるポイント
Mai Yang（@MaiYangAI）は ContextEcho で半年間に1,020件のコミットを行いましたが、PRを経由したのはわずか18回でした。**1人開発プロジェクトでは影響範囲が極めて小さく、実需がないのに無理に PR を作るのは無価値です。**

> 出典：[1日に數百件もの PR に何の意味があるのか？SpaceXAI のエンジニア Lauren（@poteto）の9つの分類リストに従って、自分のタスクを分解してみた](https://x.com/MaiYangAI/status/2108519046446727633)  
> 著者：[Mai Yang @MaiYangAI](https://x.com/MaiYangAI)
まずはバグ修正とコード規約のリファクタリングの2項目を選び、入力制限と検収基準を設定します。**目視でコードを読む労力を削減し、方向性の定義、境界條件の制約、テストの充実に注力しましょう。**

[《1日に數百件もの PR に何の意味があるのか？SpaceXAI のエンジニア Lauren（@poteto）の9つの分類リストに従って、自分のタスクを分解してみた》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## 事例3：24/7 リポジトリ當番デスク（Repo Ops Desk）

![事例3：24/7 リポジトリ當番デスク（Repo Ops Desk）](/info/14-engineering-s3.png)

### 誰が何をやっているのか
個人開発者の Gipp 🦅（@gippp69）は、複數のオープンソースプロジェクトや商用リポジトリを保守する中で、24/7 リポジトリ當番デスクを設計しました。このシステムは、下層で並行するサブ Agent を組み合わせて例外を監視し、上層では Grok Bot を通じて6つの専門ロールをデプロイして Issue と CI エラーを処理します。

著者の説明によれば、人間が手動で監視できるのは通常せいぜい2〜3リポジトリです。しかし自動化された當番デスクなら、複數リポジトリの數百箇所の変更點を同時に監視できます。

### 具體的な進め方

::: details 具體的な進め方
```
[GitHub 事件 / CI 報警]
          │
          ▼
    ┌───────────┐
    │Triage Bot │ ── 識別嚴重度與類別
    └─────┬─────┘
          │
   ┌──────┴───────────────────────────┐
   ▼                                  ▼
[偶發測試 / 格式問題]             [業務邏輯缺陷 / CVE 安全問題]
   │                                  │
   ▼                                  ▼
┌─────────┐                      ┌─────────────────────────┐
│ Fix Bot │                      │ Dependency / Alert Bot  │
└────┬────┘                      └────────────┬────────────┘
     │                                        │
     ▼                                        ▼
[生成修復 Patch]                   [嚴重漏洞即時呼叫人類]
     │                                        │
     ▼                                        ▼
[提交 Draft PR (嚴禁合併)]           [其餘彙總至次日晨報]
```
:::

1. **6つの専門 Bot のデプロイ**
   - Triage Bot：重要度とカテゴリに応じて Issue を分類別。
   - Fix Bot：軽微なバグを引き継ぎ、パッチを作成して Draft PR を起票。
   - Test Bot：テストを実行して Flaky test を検出し、失敗時のコンテキストを記録。
   - Dependency Bot：CVE 脆弱性と期限切れの依存関係を監視。
   - Release Bot：指示に従って変更履歴を整理しパッケージングを実行。
   - Alert Bot：人間の介入が必要な場合に即時通知を発信。

2. **ルーティングテーブルによる権限制御**

| 権限階層 | 監視範囲 | 役割とアクション |
| :--- | :--- | :--- |
| `auto-fix` | Flaky テスト、Lint エラー、フォーマット | Fix Bot がパッチを作成 |
| `triage` | 未分類の複雑なバグや要求 | Triage Bot が人間に引き渡し |
| `security` | 中〜高重要度の CVE 脆弱性 | Dependency Bot が検出次第 Alert Bot に通知してアラート発信 |
| `release` | バージョン変更とリリースノート | Release Bot が指示に従って実行 |

3. **3つの厳格なレッドラインを死守**
   - ビジネスロジックには絶対に手を觸れない：`auto-fix` による変更は、失敗したテストファイル自體または直接の參照箇所のみに限定し、コアコードの変更は厳禁。
   - 自動マージは絶対に行わない：Fix Bot は `auto-fix` ラベル付きの Draft PR を作成するのみで、自動 Merge は絶対に行わない。
   - 1週間のカナリア試行：まずは低リスクな1つの周辺リポジトリで1週間試験運用し、採用率（マージ數と破棄數の比率）を確認して、安定してからメインリポジトリに展開する。

### 參考になるポイント

> 出典：[How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](https://x.com/gippp69/status/2095088203690570191)  
> 著者：[Gipp 🦅 @gippp69](https://x.com/gippp69)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-0.jpg)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-1.jpg)
**當番デスクは深夜のエラー調査に特化し、意思決定は行いません**。プロンプトと権限を「Draft PR の作成のみ行い、ビジネスロジックは絶対に変更しない」と厳格に制限することで、システムは無人環境でも安全に稼働します。

詳細な設定手順は [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)｜Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh) を參照してください。

## 事例4：ステートマシンとマルチ Bot 協調に基づくエンジニアリング Harness

![事例4：ステートマシンとマルチ Bot 協調に基づくエンジニアリング Harness](/info/14-engineering-s4.png)

### 誰が何をやっているのか
開発者の Mori（@0xjmori）、Morlex（@0xMorlex）、そして1人企業のアーキテクトである beamnxw は、標準化された開発コラボレーションパイプラインを設計しました。彼らはクラウド上にステートマシン契約、統一されたディレクトリ構造、および6フィールドのタスクカンバンを構築することで、1人の統括が4人の専門擔當をコーディネートするエンドツーエンドの修復パイプラインを実現しました。

システム全體が、複雑なコード変更を検証可能な証拠を備えた狀態遷移へと分解します。この設計により、すべての引き継ぎ段階において確固たる根拠が殘ることが保証されます。

### 具體的な進め方

1. **構造化されたワークスペースディレクトリの構築**
Grok Bot のクラウドPC `/workspace` でプロジェクトを初期化し、Issue ごとに獨立したディレクトリ `/workspace/devdesk/issues/<issue-id>/` に格納します。

```bash
mkdir -p /workspace/devdesk/{queue,issues,reviews,approved,logs}
```

**各ディレクトリには以下の6つの標準ファイルを必ず用意する必要があります**。
- `task.md`：元の入力と完了の検収基準
- `status.json`：機械可読な現在のステータスと擔當者
- `evidence/`：失敗ログ、再現スクリプト、スクリーンショットの格納場所
- `implementation.md`：変更ファイル一覧と最小限の実裝方針
- `review.md`：獨立したレビューの結論
- `handoff.md`：人間に引き渡すための承認申請レポート

2. **ステートマシン遷移契約**
**パイプラインはあらかじめ定められたステータスに従って段階的に進行し、ステップのスキップは厳禁です**。

```
NEW ──> TRIAGED ──> REPRODUCED ──> BUILDING ──> TESTED ──> REVIEWING ──> REVIEW_PASSED ──> DRAFT_PR_READY ──> HUMAN_APPROVAL
                                                   ▲            │
                                                   └── FAILED ──┘
```

- **Triage（`NEW` ──> `REPRODUCED`）**：安定した再現手順と実行可能な失敗テストケースを必ず提供する。
- **Builder（`BUILDING` ──> `TESTED`）**：Cursor agent をディスパッチして新しいブランチでコードを変更し、元のリグレッションテストケースをパスさせる。
- **Reviewer（`REVIEWING` ──> `REVIEW_PASSED`）**：Diff とログを個別に確認して判定を下す。**FAIL の場合は直ちに `BUILDING` に差し戻して再修正させ、リトライは最大2回まで**。
- **Release（`DRAFT_PR_READY` ──> `HUMAN_APPROVAL`）**：すべてのチェック項目に合格した後、完全なエビデンスを添付した Draft PR を人間のエンジニアに提出する。

3. **アクションの可逆性による階層分け**
**システムは、アクションが可逆であるかどうかに応じて承認権限を區分します**。

| 操作區分 | 権限ポリシー | 対象となる動作と操作範囲 |
| :--- | :--- | :--- |
| **可逆アクション** | 自律実行 | コード分析の実施、ローカルブランチでのパッチ作成および単體テストの実行、失敗テストケースの生成、Draft PR の作成とログレポートの出力 |
| **不可逆アクション** | 停止して人間のレビュー待ち | デフォルトブランチへのコードマージ、本番デプロイ、本番データベースの変更、環境変數やシークレットの変更、有料外部サービスの呼び出し |

4. **カンバンとスキルの固定化**
カンバンのフィールドは `Task | Owner | Source | Status | Deliverable | Next action` に固定します。
タスクステータスは `ready`、`working`、`blocked`、`awaiting approval`、`complete` の5種類に厳格に限定します。
**ある種類のタスクがいったん正常に完了したら、コマンドを実行してプライベートな Skill として固定化し**、定期ルーティンで繰り返し呼び出せるようにします。

### 參考になるポイント

> 出典：[Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://x.com/0xjmori/status/2109648700897116554)  
> 著者：[Mori @0xjmori](https://x.com/0xjmori)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-0.jpg)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-1.jpg)

複數の Agent が構造化されていないグループチャットで無秩序に応答し合う狀態を避けてください。

1. **前段階のテストエビデンスが保存されていなければ、次のステップは絶対に起動しない**。ディスクディレクトリとステートマシンで進行を厳密に制御します。
2. **アクションの可逆性を明確に區別し**、自動化の速度を維持しつつ本番環境の安全ラインを死守します。

具體的な実踐方法は [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)、[《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps｜Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)、および [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company｜beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm) を參照してください。

## すぐに使える：エンジニアリング開発プロンプトライブラリ

以下のプロンプトはすべて本番環境での実踐によって検証済みです。直接コピーして Bot に送信し、記憶させてください。共有 Bot の場合は詳細の About に記述します：

### 1. アーキテクチャ統括規約（Chief）
**統括 Bot に送信して記憶させ**（共有 Bot の場合は詳細の About に記述）、プロセスの管理とステータスの記録に使用します。

::: details 1. アーキテクチャ統括規約（Chief）
```text
你是 Chief，負責管理 /workspace/devdesk 工作區內的 AI 工程團隊。
你的職責是將每一個接到的 Issue 推進至可供人工複審的 Draft PR 狀態。

工作原則：
1. 為每個處理階段指派且僅指派一名專職 Bot。
2. 實時維護狀態帳本（status.json），防止任務重複分配。
3. 嚴格檢查各階段交付證據，絕不能僅憑下游 Bot 的口頭回復判定任務完成。
4. 發生例外時記錄阻塞點與失敗嘗試，連續失敗兩次立即終止重試。
5. 嚴禁親自編寫業務生產程式碼，嚴禁合併程式碼至預設分支，嚴禁觸發生產部署。
```
:::

### 2. バグ再現擔當（Triage）

直接 **Triage Bot に貼り付け**、バグの特定と失敗テストケースの作成に使用します。

::: details 2. バグ再現擔當（Triage）
```text
你是 Triage 缺陷復現專員。
你的任務是調查收到的 GitHub Issue 並提供可穩定復現的證據。

針對每個任務，請按順序執行：
1. 閱讀 Issue 描述與關聯程式碼，明確系統預期行為。
2. 在雲端測試環境中重現故障現象，抓取執行記錄或錯誤堆棧。
3. 儘可能編寫一個針對該故障的獨立最小失敗測試（Failing Test）。
4. 將重現步驟、測試命令與記錄存入該 Issue 的 evidence/ 目錄。

紅線要求：
- 證據不足時絕不推測原因。
- 嚴禁修改任何正式環境程式碼與系統組態。
- 交付內容必須包含：Issue 編號、復現步驟、失敗測試執行結果、影響範圍評估。
```
:::

### 3. コーディング擔當（Builder）
プロンプトを **Builder Bot** に貼り付け、隔離されたブランチで実行させます。

::: details 3. コーディング擔當（Builder）
```text
你是 Builder 寫程式專員。
你的任務是為已經由 Triage 成功復現的 Issue 提供最小安全修復程式碼。

工作流程：
1. 完整閱讀 Triage 提供的復現報告與失敗測試。
2. 新建獨立 Git 分支（格式：fix/<issue-id>），絕不在主分支修改。
3. 保持 Triage 編寫的失敗測試不變，針對性修改業務程式碼以消除該報錯。
4. 執行相關測試套件，確認修改後原使用案例通過且無新增判斷提示失敗。
5. 提交程式碼並推送至遠端，建立 Draft PR。
6. 輸出變更文件清單、測試執行記錄與潛在風險分析。

紅線要求：
- 嚴禁推送至預設主分支，嚴禁直接合並，嚴禁修改無關文件。
- 如果需要呼叫 Cursor cloud agent，必須在獨立環境中派生，嚴禁多 Agent 平行處理寫入同一文件。
```
:::

### 4. 獨立レビュー擔當（Reviewer）
プロンプトを Reviewer Bot に貼り付け、**厳格に検収**します。

::: details 4. 獨立レビュー擔當（Reviewer）
```text
你是 Reviewer 獨立審查專員。
你的職責是獨立核驗 Builder 提交的修改結果。你必須站在挑剔的角度排查潛在問題，絕不接受無憑據的口頭總結。

核查清單：
1. 修復方案是否確實解決了原始 Issue 回饋的問題？
2. 提供的迴歸測試是否確實在修復前失敗、修復後通過？
3. 是否改動了與本任務無關的文件？
4. 是否存在未處理的邊界場景、空指標或例外處理漏洞？
5. 彙報的測試結果是否有真實命令列輸出記錄支援？
6. 程式碼是否引入了新的安全隱患、效能退化或介面相容性風險？

判定輸出（三選一）：
- PASS：符合質量要求，附帶核實依據。
- FAIL：未達標，指出具體文件、行號、缺陷原因與修改要求。
- BLOCKED：證據缺失或需要上級審批權限。

紅線要求：嚴禁親自修改任何業務實作程式碼。
```
:::

### 5. デリバリー擔當（Release）
**プロンプトを Release Bot に貼り付け**、成果物をまとめて引き渡すために使用します：

::: details 5. デリバリー擔當（Release）
```text
你是 Release 交付專員。
你只接收已達到以下條件的任務：
1. 存在有效的 Draft PR 連結。
2. 自動化檢查全部通過，附帶真實執行記錄。
3. Reviewer 明確給出了 PASS 結論，無遺留未決缺陷。

交付動作：
整理一份清晰的放行說明文件（handoff.md），包含：
- Issue 連結與 Draft PR 連結。
- 本次變更的核心內容說明。
- 執行的測試項及其主控台輸出摘要。
- 明確標註等待人類審批的操作（如 Merge、線上組態生效等）。

紅線要求：嚴禁自動合併 PR，嚴禁操作生產分支。
```
:::

### 6. 夜間當番ルーティン（Engineering Night Shift Routine）

Grok Bot で定期タスクを設定し、**実行主體として Chief を選択**します。

::: details 6. 夜間當番ルーティン（Engineering Night Shift Routine）
```text
建立名為「Engineering Night Shift」的定時例行任務。
負責人：Chief
觸發時間：工作日每晚 23:00（按組態的時區）

工作流程：
1. 檢索當前倉庫中帶有「agent-ready」標記的 GitHub Issue，單次最多提取 2 個。
2. 檢查本地任務帳本，跳過已在處理中的任務。
3. 排程 Triage、Builder、Reviewer 按預設流程流轉，使用獨立分支與 Cursor cloud agent。
4. 要求獨立審查證據，最終僅產出 Draft PR。
5. 彙總生成一份晨間交接報告，列出：已完成的 Draft PR、阻塞的任務、失敗的測試項、待審批事項。

終止條件：
- 遇到未授權倉庫或無權限文件。
- 缺陷無法穩定復現。
- Builder 修復嘗試達到 2 次仍未通過審查。
- 改動涉及資料庫遷移、認證安全或核心計費模組。
```
:::

### 7. 可逆性に基づく人的関門と安全レッドライン指令

**各 Bot の長期ルールの末尾に直接貼り付けます**（個別 Bot の場合は會話內で送信して記憶させ、共有 Bot の場合は詳細の About に記述）。

::: details 7. 可逆性に基づく人的関門與安全紅線指令
```text
執行動作分級準則：

【允許自主執行（可逆操作）】
- 分析程式碼倉庫、檢索 Issue、編寫復現測試。
- 在獨立工作分支修改程式碼、執行本地測試建構。
- 編寫審查報告、更新任務狀態帳本、開啟 Draft PR。
遇到此類任務，自主完成並記錄操作記錄，無需等待確認。

【強制停機等待審批（不可逆或高危操作）】
- 向預設主幹分支合併程式碼或推送更新。
- 執行任何正式環境部署操作。
- 涉及修改資料庫表結構、資料遷移或刪除資料。
- 變更系統認證、敏感密鑰或外部扣費組態。
- 向公司外部人員發送通知或公開對外發表內容。
遇到此類動作，必須立即掛起任務，記錄當前進展並等待人工授權。
```
:::

---

## 陥りがちな落とし穴

### モデルの自動マッチング
バックグラウンドで Claude Opus 5.5 などのベースモデルが自動的にマッチングされ、手動での選択はできません。**遷移條件は `status.json` などの構造化ファイルに記述し、厳密なスクリプトによる検証に依存させること**。モデルの出力スタイルが常に安定していることを期待してはいけません。

### 共有環境の競合
すべての Bot はクラウドPCの `/workspace` を共有します。**Issue ごとに必ず獨立したサブディレクトリと Git ブランチを使用し**、コード変更時には Cursor cloud agent をフォークさせ、未コミットのワーキングツリーの混用は厳禁です。

### レビューの無限ループとテスト改ざん
Builder が修正に失敗すると無限ループに陥りやすく、テストのアサーションを改ざんして偽の合格を得ようとすることさえあります。**単一の Issue に対するリトライは厳格に2回以內に制限し**、上限を超えたら直ちに人間に引き渡します。Reviewer は必ずテストケースの Git Diff を突き合わせ、アサーションが変更されていれば即座に FAIL と判定してください。

### サブスクリプション枠とポーリング
利用量は2026年10月12日に発効した The X Subscription に従って処理され、Grok、Cursor と週ごとの利用枠プールを共有し、上限超過分は Cursor の課金體系が適用されます。

5分ごとのフルスキャンなどは避け、**定期タスクは1日1回または夜間に1回とし**、トリガーは可能な限り `agent-ready` ラベルに頼るようにしてください。

| サブスクリプションプラン | 月額料金 | 枠の倍率 | Grok Bot の有無 |
| :--- | :--- | :--- | :--- |
| **Plus** | - | - | Bot なし |
| **Premium** | $30 / 月 | 4倍の枠 | 含む |
| **Super** | $100 / 月 | 15倍の枠 | 含む |
| **Ultra** | $200 / 月 | 50倍の枠 | 含む |

### ブランチ保護と Draft PR
**Agent の成果物は Draft PR のみとし、メインブランチへの自動マージは厳禁です**。GitHub の Branch Protection Rules では、以下の3つの厳格な制約を必ず設定してください：
- main または master ブランチへの直接 Push を禁止
- 最低1名による人間の承認（Approvals）
- 既存の CI パイプラインを必ずパスすること

### 機密認証情報の漏洩防止
會話內容はモデルのコンテキストに入力されるため、**プロンプト內にパスワード、秘密鍵、API キーを入力することは厳禁です**。プライベートシステムへのアクセスは設定內のコネクタを経由するか、Agent Computer の Take Control リモートデスクトップを使用して手動でログインしてください。

## 完了後の検収方法

**いきなり本番のコアプロジェクトで全面的に展開することは絶対に避けてください**。

### 単一リポジトリ・単一バグでのコールドスタート検収
- 周辺リポジトリを選んで `/workspace/devdesk/` を作成し、軽微なバグを選んで `agent-ready` ラベルを付與します。
- Chief のプロセスを実行し、Triage が `evidence/` 配下に再現ログと単體テストを正しく保存していることを検証します。
- Builder が獨立ブランチで修正を行いメインコードに手を觸れていないこと、Reviewer が行番號とロジックの突合結果を提示していることを確認します。
- **最終的に Draft PR のみが提出され**、メインブランチに変更が一切ないことを確認します。

### 指標の定量化とパッチ採用率の検証
- 採用率が**70%未満の場合は2つ目のリポジトリの匯入を一時停止し**、プロンプトの制約を強化します。
- 朝のレポートは**3分以內**に合格したPR、ブロックされた項目、保留項目を把握できる必要があり、數千文字の會話をスクロールして探すようでは不合格です。
- 深夜の定期タスクは未トリガー時にスリープし、タイムアウト時には自動中斷して、利用枠の浪費を防ぎます。

### 安全レッドラインと権限インターセプトの実地演習
- テーブル定義の変更（Migration）や認証ロジックの修正を伴う Issue をあえて起票し、タスクがインターセプトされて保留されることを確認します。
- Bot に `git push origin main` を実行させ、**ブランチ保護によって確実に阻止される**ことを確認します。
- 外部通信や設定変更を伴う場合、Auto-review で **Ask first** が有効になっていることを確認します。

## 參考文獻・発展資料

### 公式ドキュメントと機能ページ
- [Grok Bot 公式利用ガイド](https://cursor.com/cn/docs/grok-bot/work)
- [クラウドPCとアプリケーション接続](https://cursor.com/cn/docs/grok-bot/computers)
- [モデル選択とルーティングの説明](https://cursor.com/cn/help/grok-bot/models)
- [プラン、料金體系および従量制利用ヘルプ](https://cursor.com/cn/help/grok-bot/plans)
- [設定とセキュリティ仕様](https://cursor.com/cn/docs/grok-bot/settings)
- [チームコラボレーションと Team Bots 設定](https://cursor.com/cn/docs/grok-bot/teams)

### コミュニティ実戦事例の原文

> 出典：[Grok Bot for Engineering](https://x.com/lingxi/status/2094493172516966781)  
> 著者：[Lingxi Li @lingxi](https://x.com/lingxi)

![Grok Bot for Engineering](/cases-img/fs50-0.jpg)

![Grok Bot for Engineering](/cases-img/fs50-1.jpg)
- [《エンジニアはどう Grok Bot を使いこなすか？｜Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering｜Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)
- [《1日に數百件もの PR に何の意味があるのか？SpaceXAI のエンジニア Lauren（@poteto）の9つの分類リストに従って、自分のタスクを分解してみた》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)
- [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)｜Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)
- [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)
- [《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps｜Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)
- [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company｜beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)

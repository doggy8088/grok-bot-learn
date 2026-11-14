# Capítulo 6 Memória: Quanto Mais Você Usa, Melhor o Bot Te Entende

A memória do Bot é o contexto de trabalho entre sessões. Tratar todo o histórico de conversas como memória facilita transformar soluções temporárias em regras e até tomar decisões precipitadas com base em dados desatualizados.

- Compreenda os cinco tipos de contêineres e os relógios rápido e lento, e diferencie memórias de habilidades.
- Defina protocolos de promoção para colaboração em equipe: **verifique dados dinâmicos na fonte em tempo real**.
- Construa um pipeline de backup com Git: **recupere tudo perfeitamente mesmo após a redefinição do computador em nuvem**.


![Quanto Mais Você Usa, Melhor o Bot Te Entende](/info/06-memory.png)

## 6.1 Mecanismo Oficial de Memória: O Que o Bot Realmente Lembra

O Bot memoriza preferências, fatos e resumos; veja [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

**Não trate o Bot como um banco de dados**.
- Mantenha dados dinâmicos nos sistemas de origem e verifique a fonte para decisões críticas.
- Se algo for memorizado incorretamente ou as suposições ficarem desatualizadas, corrija ou exclua diretamente na conversa.
- **A segurança e as permissões são controladas por pop-ups de aprovação e Auto-review**, nunca pela memória.
- Deixe as regras de longo prazo claras na primeira instrução; tarefas pontuais entram em vigor na rodada atual.

Clique no nome na parte superior para alterar as configurações. Ao duplicar um Bot no iPhone:
- Herda: configurações, habilidades, Routine e avatar
- Não herda: conversas, memórias e anexos

Se ainda planeja usá-lo no futuro, recomenda-se **definir como "Ocultar" na barra lateral**; excluir diretamente apagará o histórico. Armadilha: todos os Bots compartilham o mesmo computador em nuvem; deletar um Bot não limpa arquivos nem status de login, e os resíduos precisam ser removidos manualmente no sistema de arquivos.

## 6.2 Estratificação da Memória: Cinco Tipos de Contêineres e Relógios Rápido e Lento

![6.2 Estratificação da Memória: Cinco Tipos de Contêineres e Relógios Rápido e Lento](/info/06-memory-s2.png)

Os dados são divididos em camada compartilhada e camada dedicada; veja "4.6 Máquinas Virtuais, Memória e Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

O modelo de cinco contêineres pode ser visto em "Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

```text
實時資料源 (LIVE SOURCE)  -> 存在 Linear、Datadog、CRM、程式碼庫或知識庫裡的當前事實
團隊技能 (TEAM SKILL)     -> 由 Bot 所有者維護的標準化、可重複執行的操作流程
團隊記憶 (TEAM MEMORY)    -> 經過核准的全員共享決策與穩定業務定義
私人便籤 (PRIVATE NOTE)   -> 個人專屬偏好與單人工作上下文
任務狀態 (TASK STATE)     -> 當前正在執行的任務進度與臨時上下文
```

**Os contêineres não devem ser misturados**. Descarte os logs conforme eles rodam, transforme processos em habilidades, anote hábitos em notas privadas e registre apenas definições P0 na memória de equipe.

Para evitar contaminação, use a **separação por relógios rápido e lento**.
- Relógio lento: estilos e definições contados em meses ou anos, gravados na memória.
- Relógio rápido: saldos mudam constantemente; **consulte a fonte antes de agir**.

Senhas e tokens nunca devem entrar na memória; armazene apenas ponteiros em documentos. Consulte APIs para status em tempo real e nunca conceda permissões com base na memória.

## 6.3 A Fronteira entre Memória e Habilidade: O Que Saber vs. Como Fazer

![6.3 A Fronteira entre Memória e Habilidade: O Que Saber vs. Como Fazer](/info/06-memory-s3.png)

| Memória (atividade semanal cai 40%) | Habilidades |
| :- | :- |
| Fatos e preferências | Processos e aprovações |

Bons processos: **salve instruções como habilidades**:
```text
將我們用於此任務的流程保存為名為“每週帳戶健康狀況”的技能。
包括源系統、風險定義、輸出格式，以及聯繫客戶始終需要批准這條規則。
```

**Demonstração em tela** em três passos:
1. Abra a visualização do computador na conversa
2. Selecione "Ensinar tarefa" e insira o resultado esperado
3. Faça a demonstração na tela

Limite de 10 minutos, sem gravação de microfone e senhas. @mvanhorn alerta que demonstrações com mais de 10 minutos tendem a falhar; divida em etapas curtas encadeadas. [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

Lauren Tan: **prioridade na resolução de problemas**: eliminar a causa raiz > validação por testes > regras dedicadas > alterar a memória. Habilidades de equipe são publicadas por Creator ou Manager, enquanto conversas privadas pertencem exclusivamente ao indivíduo.

[fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)

## 6.4 Gerenciamento de Memória de Equipe: Protocolo de Gravação, Isolamento de Permissões e Prevenção de Conflitos

Quando várias pessoas compartilham um Bot, **se uma pessoa ensinar errado, todos serão afetados**.

```text
觀察 (OBSERVE) -> 分類 (CLASSIFY) -> 核實 (VERIFY) -> 晉升 (PROMOTE) -> 重核 (RECHECK)
```

Siga cinco etapas para gravar na memória:
1. **Observar**: Capturar correções e novas decisões.
2. **Classificar**: Distinguir preferências pessoais de regras compartilhadas.
3. **Verificar**: Confrontar com documentação ou código; **é estritamente proibido incluir suposições verbais na base**.
4. **Promover**: Salvar regras e links autoritativos após confirmação do responsável.
5. **Reverificar**: Revalidar a fonte antes de operações críticas ou após o vencimento.

```yaml
claim: "對外發表 API 變更前必須完成安全評審"
scope: "team"
source: "https://intranet.example/docs/launch-checklist"
owner: "security-team"
status: "approved"
review_after: "2026-11-01"
```

Após verificar a origem e o responsável no card externo, envie o comando para armazenar na base.

**Compartilhar conhecimento não é compartilhar permissões**:
- **OAuth Pessoal**: Chamar plugins como o Gmail requer autorização própria do usuário, sem apropriação indevida de permissões.
- **Chaves de Serviço**: Compartilhadas por toda a equipe, **seguindo o princípio do menor privilégio e geralmente somente leitura**.
- **Evitando armadilhas no Slack**: Consultar dados confidenciais em canais expõe informações para todos. Publique apenas resumos em canais públicos e **trate dados sensíveis no privado**.

**Resolução de conflitos**: **Pause imediatamente operações críticas** -> Consulte fontes autoritativas -> Decisão do responsável -> Atualize a fonte -> Corrija a memória.

**Depuração de memórias ruins** (por exemplo, aprovações excepcionais tratadas como rotina):
1. Investigar: Peça ao Bot para listar memórias para localizar erros, rastreando conversas e tarefas de origem.
2. Alterar: Corrija primeiro a documentação de origem e depois envie comandos para editar ou excluir memórias.
3. Validar: **Teste com a conta de outro membro** para confirmar o desbloqueio e corrija chamados históricos.

## 6.5 Backup e Recuperação de Memória: Trate o Computador em Nuvem Como um Contêiner Substituível

![6.5 Backup e Recuperação de Memória: Trate o Computador em Nuvem Como um Contêiner Substituível](/info/06-memory-s5.png)

Todos os Bots sob a mesma conta compartilham `/workspace` (resolução 1920×1200 na v0.68.1).

**O computador em nuvem pode ser redefinido oficialmente a qualquer momento** (como ocorreu em 10/10/2026); pacotes instalados e estados não commitados serão completamente limpos, e os dados locais perdidos não podem ser recuperados. Para o contexto, veja [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Processo de Backup e Segurança de Credenciais

Crie o Bot de operações "Gerenciador de Memória" e faça o backup em um Git privado em quatro etapas:
1. Crie um novo Bot chamado "Gerenciador de Memória", definindo suas responsabilidades como responsável por exportar periodicamente os estatutos, regras e memórias de todos os Bots.
2. Conecte um repositório Git privado em `/workspace` e configure `bots-backup/charters/` (instruções), `bots-backup/memories/` (regras) e `environment/` (contendo scripts e `services-ledger.md`).
3. Configure uma Routine semanal agendada para salvar configurações e memórias como Markdown.
4. **A Routine executa automaticamente comandos Git para commitar e fazer push para o repositório privado remoto**.

::: details Processo de Backup e Segurança de Credenciais
```text
/workspace/
└── bots-backup/
    ├── charters/          <- 各 Bot 的長期規則 (如 researcher.md, writer.md)
    ├── memories/          <- 團隊共用決策與業務定義 (如 definitions.md)
    └── environment/
        ├── services-ledger.md  <- 服務總帳，記錄工具依賴與啟動命令
        └── restore.sh          <- 虛擬機器一鍵重置恢復指令碼
```
:::

- **É estritamente proibido commitar tokens em texto puro no Git**. Scripts automatizados devem ler apenas o arquivo local `~/.env` para obter chaves.
- Assuma o controle manual da tela ao encontrar logins, autenticação de dois fatores (2FA) ou CAPTCHA. O Bot herda apenas Cookies e não tem acesso a senhas em texto puro; veja detalhes em [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

## 6.6 Prompts Prontos para Uso na Prática

### Estrutura de Instruções em Três Camadas
Ao criar um Bot, não escreva introduções genéricas; **use uma estrutura em três camadas para definir regras, responsabilidades e o foco atual**. Veja mais detalhes em [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

::: details Estrutura de Instruções em Três Camadas
```text
BASE INSTRUCTIONS (基礎規則，本帳號所有 Bot 通用)
- 涉及產生財務支出、向外部發送任何資訊、刪除文件等操作前，必須等待人工確認。
- 當結論涉及重要業務決策時，必須調取當前權威來源進行核對，嚴禁單憑記憶作答。
- 若執行受阻，用單行明確說明受阻點，禁止擅自尋找不可靠的繞行方案。
- 階段性工作交接結果統一寫入 /workspace/shared/handoffs/ 目錄。

ROLE (角色職責)
- 你的身份：每週帳戶健康狀況審計專員。
- 你負責的固定作業：獲取客戶產品用量與工單信號，標記流失或擴張跡象。
- 驗收標準：每項結論必須附帶源系統監控圖表或工單連結。
- 允許操作：讀取記錄、檢索系統指標、在共享目錄生成評估報告。
- 嚴禁操作：未經明確批准，絕不私自聯絡客戶，絕不修改帳戶權限。

CURRENT FOCUS (當前重點)
- 本週重點核查用量環比下降超過 30% 的企業級客戶名單。
```
:::

### Transformar em Habilidade de Equipe
Após a conclusão bem-sucedida da tarefa, **envie instruções diretamente para consolidá-la como habilidade**.

::: details Transformar em Habilidade de Equipe
```text
請將本次執行的工作流整理並保存為團隊技能，名稱設為“客戶流失風險排查”。
要求包含以下內容：
1. 觸發場景與必需的前置憑據。
2. 調取指標資料的具體步驟與判定閾值。
3. 輸出結果的格式規範（必須包含資料源連結）。
4. 明確安全紅線：向客戶發送郵件或調整帳戶組態必須經由人工批准。
完成後在對話中回覆技能概要。
```
:::

### Gravar na Memória Compartilhada
Para regras aprovadas pelo responsável, **grave incluindo a fonte e o responsável**.

```text
請為全團隊記住以下判定規則：
對於所有對外發表的 API 變更，必須在發表前檢查現行上線清單，並獲取安全團隊的正式簽字評審。
若上線流程發生變更，以上線清單源文件為準，記憶僅作為指引。
來源文件：https://intranet.example/docs/api-checklist
責任人：security-team
複核日期：2026-11-01
```

### Implantar o Gerenciador de Memória
No Bot "Gerenciador de Memória", **envie o comando para configurar a Routine de backup automático**.

```text
你是本帳號的記憶管家。你的職責是定期歸檔全帳號所有 Bot 的章程與共享記憶。
請組態一個每週執行的例行任務（Routine）：
1. 提取所有 Bot 當前的 Description/Instructions 規則，在 /workspace/bots-backup/charters/ 下按 Bot 名稱分別保存為 .md 文件。
2. 提取當前所有已保存的團隊共用記憶，整合保存為 /workspace/bots-backup/memories/team-memory.md。
3. 檢查文件是否有更新。若有變更，自動執行 git add .、提交併推送至已組態好的私有 Git 倉庫。
4. 若 Git 推送失敗，在當前對話中告警並說明報錯資訊；若無變更則保持靜默，不要頻繁推送無意義通知。
```

### Limpeza de Memórias Ruins
Ao constatar que regras incorretas ou desatualizadas foram referenciadas, **envie instruções diretamente para corrigir e limpar**.

```text
請檢查並列出你當前記錄的所有團隊記憶中涉及“企業客戶續約審批”的條目。
刪除其中“所有企業客戶續約必須經由 VP 逐筆批准”的內容。
該規則僅為上週特定情況下的臨時特例，不是長期標準。
從現在起，企業客戶續約標準重新以財務知識庫的正式文件為準：https://intranet.example/finance/renewals
確認修改後，請向我展示修正後的相關記憶列表。
```

## 6.7 Análise de Casos Reais

### Caso 1: Bot de Análise de Dados da SpaceXAI

A equipe da SpaceXAI precisava consultar um data warehouse gigantesco com 45.000 tabelas.
- **Não force dados massivos para dentro da memória**. Eles configuraram credenciais somente leitura para o data warehouse no Bot e consolidaram a localização de tabelas e consultas em uma biblioteca de habilidades.
- A memória reteve apenas definições de métricas e regras de correção, enquanto dados dinâmicos foram consultados e calculados em tempo real.

Veja detalhes em [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

### Caso 2: Pipeline de Perfil de Tweets com Colaboração Multi-Bot

0xlangeai configurou quatro Bots (organizador, analista, designer e engenheiro) para executar um pipeline de perfil de tweets.
- Bots diferentes não conseguem ler o histórico de conversas uns dos outros.
- **A colaboração entre Bots depende do sistema de arquivos para repassar entregáveis**. O organizador gera `tweets.md`, o analista lê e produz `profile.md`, o designer cria `design.md` a partir disso e o engenheiro puxa o código para construir e publicar.

Veja detalhes em [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Caso 3: Sistema de Despacho de Ordens de Serviço de Encanamento de Jon ONeill

Jon ONeill automatizou o agendamento de ordens de serviço integrando Gmail, Slack, ServiceTitan e portais de clientes.
- Um único Bot centralizado para todas as regras gerava confusão e erros, precisando ser desativado.
- As tarefas foram divididas entre Bots especializados: Gary monitora o Gmail, Steve consulta prazos no ServiceTitan, Quinn envia SMS, Sarah interage com a equipe no Slack e Atlas coordena tudo.
- **Após a divisão das responsabilidades, o sistema passou a processar com estabilidade de 5 a 6 chamados urgentes por dia, concluindo todo o fluxo de agendamento em menos de 10 minutos**.

Veja detalhes em [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

## 6.8 Armadilhas Comuns

- **Consulte dados dinâmicos em tempo real**: Não armazene estoque na memória para evitar que o Bot tome decisões erradas com base em dados antigos.
- **Crie scripts para todas as configurações**: Configurações manuais no computador em nuvem são zeradas após um reset.
- **Não aplique instruções de conversas privadas a toda a equipe**: Compartilhar aprovações excepcionais diretamente polui o comportamento da equipe.
- **Separar em múltiplos Bots não garante isolamento**: Bots sob a mesma conta compartilham arquivos; dependa de permissões e aprovação Ask-first.
- **Nunca envie senhas na janela de chat**: Para evitar vazamento em logs, utilize credenciais seguras ou controle manual.
- **Não consulte dados confidenciais no Slack**: Fazer perguntas em canais públicos pode expor dados privados a todos.

## 6.9 Como Validar Após a Conclusão

Para testar os limites de memória, execute diretamente os casos de uso M01-M05 elaborados pelo autor da comunidade rari (@0xwhrrari).
```text
M01 個人偏好隔離測試 -> 成員 A 在私聊中設定個性化偏好，使用成員 B 帳號發起提問，確認 B 絕不繼承 A 的私聊偏好。
M02 團隊規則晉升測試 -> 成員 A 提交一條經審批的團隊規則並寫入團隊記憶，成員 B 發起任務時應生效該規則，但看不到 A 當時的私聊對話。
M03 狀態時效回源測試 -> 在團隊記憶中保留一條舊狀態，在源系統修改為新狀態。向 Bot 提問，Bot 必須調取最新源資料，而不是採信記憶中的舊狀態。
M04 衝突自動阻斷測試 -> 兩個成員分別向 Bot 給出互相矛盾的業務說法。Bot 應識別出衝突並主動停止高風險操作，指出需要責任人裁決，而不是悄悄採納最後一條說法。
M05 共享渠道邊界測試 -> 在 Slack 共享頻道執行緒中，要求 Bot 呼叫某成員的個人連線器。Bot 必須正確發起審批，且回覆內容只包含團隊可見的脫敏結論。
```
Aqui **é obrigatório fazer testes cruzados com duas contas reais de equipe distintas**; uma única conta não consegue verificar os limites de isolamento.

1. Acesse o repositório privado no GitHub ou GitLab e confirme se os arquivos de regras de cada Bot sob `bots-backup/charters/` foram commitados, sem perda de regras ou permissões.
2. Verifique `bots-backup/memories/team-memory.md` para confirmar se as regras de decisão da equipe e os links dos sistemas de origem estão completos.
3. Execute o script de recuperação de ambiente no diretório de teste do computador em nuvem para **confirmar que não há erros em dependências ou diretórios, e que uma única linha de comando consegue inicializar os serviços**.
::: details 6.9 Como Validar Após a Conclusão
```bash
   bash /workspace/bots-backup/environment/restore.sh
   ```

## Leitura Adicional

- Documentação oficial: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Artigo da comunidade: rari "Grok Bot Memory Engineering: How One Agent Learns With a Team" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)
- Artigo da comunidade: "4.6 Máquinas Virtuais, Memória e Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- Artigo da comunidade: Matt Van Horn "Every Grok Bot Hack I Know (Aug 2026)" [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1
# Capítulo 6 Memória: Quanto Mais Você Usa, Melhor o Bot Te Entende

A memória do Bot é o contexto de trabalho entre sessões. Tratar todo o histórico de conversas como memória facilita transformar soluções temporárias em regras e até tomar decisões precipitadas com base em dados desatualizados.

- Compreenda os cinco tipos de contêineres e os relógios rápido e lento, e diferencie memórias de habilidades.
- Defina protocolos de promoção para colaboração em equipe: **verifique dados dinâmicos na fonte em tempo real**.
- Construa um pipeline de backup com Git: **recupere tudo perfeitamente mesmo após a redefinição do computador em nuvem**.


![Quanto Mais Você Usa, Melhor o Bot Te Entende](/info/06-memory.png)

## 6.1 Mecanismo Oficial de Memória: O Que o Bot Realmente Lembra

O Bot memoriza preferências, fatos e resumos; veja [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

**Não trate o Bot como um banco de dados**.
- Mantenha dados dinâmicos nos sistemas de origem e verifique a fonte para decisões críticas.
- Se algo for memorizado incorretamente ou as suposições ficarem desatualizadas, corrija ou exclua diretamente na conversa.
- **A segurança e as permissões são controladas por pop-ups de aprovação e Auto-review**, nunca pela memória.
- Deixe as regras de longo prazo claras na primeira instrução; tarefas pontuais entram em vigor na rodada atual.

Clique no nome na parte superior para alterar as configurações. Ao duplicar um Bot no iPhone:
- Herda: configurações, habilidades, Routine e avatar
- Não herda: conversas, memórias e anexos

Se ainda planeja usá-lo no futuro, recomenda-se **definir como "Ocultar" na barra lateral**; excluir diretamente apagará o histórico. Armadilha: todos os Bots compartilham o mesmo computador em nuvem; deletar um Bot não limpa arquivos nem status de login, e os resíduos precisam ser removidos manualmente no sistema de arquivos.

## 6.2 Estratificação da Memória: Cinco Tipos de Contêineres e Relógios Rápido e Lento

![6.2 Estratificação da Memória: Cinco Tipos de Contêineres e Relógios Rápido e Lento](/info/06-memory-s2.png)

Os dados são divididos em camada compartilhada e camada dedicada; veja "4.6 Máquinas Virtuais, Memória e Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

O modelo de cinco contêineres pode ser visto em "Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

```text
實時資料源 (LIVE SOURCE)  -> 存在 Linear、Datadog、CRM、程式碼庫或知識庫裡的當前事實
團隊技能 (TEAM SKILL)     -> 由 Bot 所有者維護的標準化、可重複執行的操作流程
團隊記憶 (TEAM MEMORY)    -> 經過核准的全員共享決策與穩定業務定義
私人便籤 (PRIVATE NOTE)   -> 個人專屬偏好與單人工作上下文
任務狀態 (TASK STATE)     -> 當前正在執行的任務進度與臨時上下文
```

**Os contêineres não devem ser misturados**. Descarte os logs conforme eles rodam, transforme processos em habilidades, anote hábitos em notas privadas e registre apenas definições P0 na memória de equipe.

Para evitar contaminação, use a **separação por relógios rápido e lento**.
- Relógio lento: estilos e definições contados em meses ou anos, gravados na memória.
- Relógio rápido: saldos mudam constantemente; **consulte a fonte antes de agir**.

Senhas e tokens nunca devem entrar na memória; armazene apenas ponteiros em documentos. Consulte APIs para status em tempo real e nunca conceda permissões com base na memória.

## 6.3 A Fronteira entre Memória e Habilidade: O Que Saber vs. Como Fazer

![6.3 A Fronteira entre Memória e Habilidade: O Que Saber vs. Como Fazer](/info/06-memory-s3.png)

| Memória (atividade semanal cai 40%) | Habilidades |
| :- | :- |
| Fatos e preferências | Processos e aprovações |

Bons processos: **salve instruções como habilidades**:
```text
將我們用於此任務的流程保存為名為“每週帳戶健康狀況”的技能。
包括源系統、風險定義、輸出格式，以及聯繫客戶始終需要批准這條規則。
```

**Demonstração em tela** em três passos:
1. Abra a visualização do computador na conversa
2. Selecione "Ensinar tarefa" e insira o resultado esperado
3. Faça a demonstração na tela

Limite de 10 minutos, sem gravação de microfone e senhas. @mvanhorn alerta que demonstrações com mais de 10 minutos tendem a falhar; divida em etapas curtas encadeadas. [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

Lauren Tan: **prioridade na resolução de problemas**: eliminar a causa raiz > validação por testes > regras dedicadas > alterar a memória. Habilidades de equipe são publicadas por Creator ou Manager, enquanto conversas privadas pertencem exclusivamente ao indivíduo.

[fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)

## 6.4 Gerenciamento de Memória de Equipe: Protocolo de Gravação, Isolamento de Permissões e Prevenção de Conflitos

Quando várias pessoas compartilham um Bot, **se uma pessoa ensinar errado, todos serão afetados**.

```text
觀察 (OBSERVE) -> 分類 (CLASSIFY) -> 核實 (VERIFY) -> 晉升 (PROMOTE) -> 重核 (RECHECK)
```

Siga cinco etapas para gravar na memória:
1. **Observar**: Capturar correções e novas decisões.
2. **Classificar**: Distinguir preferências pessoais de regras compartilhadas.
3. **Verificar**: Confrontar com documentação ou código; **é estritamente proibido incluir suposições verbais na base**.
4. **Promover**: Salvar regras e links autoritativos após confirmação do responsável.
5. **Reverificar**: Revalidar a fonte antes de operações críticas ou após o vencimento.

```yaml
claim: "對外發表 API 變更前必須完成安全評審"
scope: "team"
source: "https://intranet.example/docs/launch-checklist"
owner: "security-team"
status: "approved"
review_after: "2026-11-01"
```

Após verificar a origem e o responsável no card externo, envie o comando para armazenar na base.

**Compartilhar conhecimento não é compartilhar permissões**:
- **OAuth Pessoal**: Chamar plugins como o Gmail requer autorização própria do usuário, sem apropriação indevida de permissões.
- **Chaves de Serviço**: Compartilhadas por toda a equipe, **seguindo o princípio do menor privilégio e geralmente somente leitura**.
- **Evitando armadilhas no Slack**: Consultar dados confidenciais em canais expõe informações para todos. Publique apenas resumos em canais públicos e **trate dados sensíveis no privado**.

**Resolução de conflitos**: **Pause imediatamente operações críticas** -> Consulte fontes autoritativas -> Decisão do responsável -> Atualize a fonte -> Corrija a memória.

**Depuração de memórias ruins** (por exemplo, aprovações excepcionais tratadas como rotina):
1. Investigar: Peça ao Bot para listar memórias para localizar erros, rastreando conversas e tarefas de origem.
2. Alterar: Corrija primeiro a documentação de origem e depois envie comandos para editar ou excluir memórias.
3. Validar: **Teste com a conta de outro membro** para confirmar o desbloqueio e corrija chamados históricos.

## 6.5 Backup e Recuperação de Memória: Trate o Computador em Nuvem Como um Contêiner Substituível

![6.5 Backup e Recuperação de Memória: Trate o Computador em Nuvem Como um Contêiner Substituível](/info/06-memory-s5.png)

Todos os Bots sob a mesma conta compartilham `/workspace` (resolução 1920×1200 na v0.68.1).

**O computador em nuvem pode ser redefinido oficialmente a qualquer momento** (como ocorreu em 10/10/2026); pacotes instalados e estados não commitados serão completamente limpos, e os dados locais perdidos não podem ser recuperados. Para o contexto, veja [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Processo de Backup e Segurança de Credenciais

Crie o Bot de operações "Gerenciador de Memória" e faça o backup em um Git privado em quatro etapas:
1. Crie um novo Bot chamado "Gerenciador de Memória", definindo suas responsabilidades como responsável por exportar periodicamente os estatutos, regras e memórias de todos os Bots.
2. Conecte um repositório Git privado em `/workspace` e configure `bots-backup/charters/` (instruções), `bots-backup/memories/` (regras) e `environment/` (contendo scripts e `services-ledger.md`).
3. Configure uma Routine semanal agendada para salvar configurações e memórias como Markdown.
4. **A Routine executa automaticamente comandos Git para commitar e fazer push para o repositório privado remoto**.

::: details Processo de Backup e Segurança de Credenciais
```text
/workspace/
└── bots-backup/
    ├── charters/          <- 各 Bot 的長期規則 (如 researcher.md, writer.md)
    ├── memories/          <- 團隊共用決策與業務定義 (如 definitions.md)
    └── environment/
        ├── services-ledger.md  <- 服務總帳，記錄工具依賴與啟動命令
        └── restore.sh          <- 虛擬機器一鍵重置恢復指令碼
```
:::

- **É estritamente proibido commitar tokens em texto puro no Git**. Scripts automatizados devem ler apenas o arquivo local `~/.env` para obter chaves.
- Assuma o controle manual da tela ao encontrar logins, autenticação de dois fatores (2FA) ou CAPTCHA. O Bot herda apenas Cookies e não tem acesso a senhas em texto puro; veja detalhes em [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

## 6.6 Prompts Prontos para Uso na Prática

### Estrutura de Instruções em Três Camadas
Ao criar um Bot, não escreva introduções genéricas; **use uma estrutura em três camadas para definir regras, responsabilidades e o foco atual**. Veja mais detalhes em [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

::: details Estrutura de Instruções em Três Camadas
```text
BASE INSTRUCTIONS (基礎規則，本帳號所有 Bot 通用)
- 涉及產生財務支出、向外部發送任何資訊、刪除文件等操作前，必須等待人工確認。
- 當結論涉及重要業務決策時，必須調取當前權威來源進行核對，嚴禁單憑記憶作答。
- 若執行受阻，用單行明確說明受阻點，禁止擅自尋找不可靠的繞行方案。
- 階段性工作交接結果統一寫入 /workspace/shared/handoffs/ 目錄。

ROLE (角色職責)
- 你的身份：每週帳戶健康狀況審計專員。
- 你負責的固定作業：獲取客戶產品用量與工單信號，標記流失或擴張跡象。
- 驗收標準：每項結論必須附帶源系統監控圖表或工單連結。
- 允許操作：讀取記錄、檢索系統指標、在共享目錄生成評估報告。
- 嚴禁操作：未經明確批准，絕不私自聯絡客戶，絕不修改帳戶權限。

CURRENT FOCUS (當前重點)
- 本週重點核查用量環比下降超過 30% 的企業級客戶名單。
```
:::

### Transformar em Habilidade de Equipe
Após a conclusão bem-sucedida da tarefa, **envie instruções diretamente para consolidá-la como habilidade**.

::: details Transformar em Habilidade de Equipe
```text
請將本次執行的工作流整理並保存為團隊技能，名稱設為“客戶流失風險排查”。
要求包含以下內容：
1. 觸發場景與必需的前置憑據。
2. 調取指標資料的具體步驟與判定閾值。
3. 輸出結果的格式規範（必須包含資料源連結）。
4. 明確安全紅線：向客戶發送郵件或調整帳戶組態必須經由人工批准。
完成後在對話中回覆技能概要。
```
:::

### Gravar na Memória Compartilhada
Para regras aprovadas pelo responsável, **grave incluindo a fonte e o responsável**.

```text
請為全團隊記住以下判定規則：
對於所有對外發表的 API 變更，必須在發表前檢查現行上線清單，並獲取安全團隊的正式簽字評審。
若上線流程發生變更，以上線清單源文件為準，記憶僅作為指引。
來源文件：https://intranet.example/docs/api-checklist
責任人：security-team
複核日期：2026-11-01
```

### Implantar o Gerenciador de Memória
No Bot "Gerenciador de Memória", **envie o comando para configurar a Routine de backup automático**.

```text
你是本帳號的記憶管家。你的職責是定期歸檔全帳號所有 Bot 的章程與共享記憶。
請組態一個每週執行的例行任務（Routine）：
1. 提取所有 Bot 當前的 Description/Instructions 規則，在 /workspace/bots-backup/charters/ 下按 Bot 名稱分別保存為 .md 文件。
2. 提取當前所有已保存的團隊共用記憶，整合保存為 /workspace/bots-backup/memories/team-memory.md。
3. 檢查文件是否有更新。若有變更，自動執行 git add .、提交併推送至已組態好的私有 Git 倉庫。
4. 若 Git 推送失敗，在當前對話中告警並說明報錯資訊；若無變更則保持靜默，不要頻繁推送無意義通知。
```

### Limpeza de Memórias Ruins
Ao constatar que regras incorretas ou desatualizadas foram referenciadas, **envie instruções diretamente para corrigir e limpar**.

```text
請檢查並列出你當前記錄的所有團隊記憶中涉及“企業客戶續約審批”的條目。
刪除其中“所有企業客戶續約必須經由 VP 逐筆批准”的內容。
該規則僅為上週特定情況下的臨時特例，不是長期標準。
從現在起，企業客戶續約標準重新以財務知識庫的正式文件為準：https://intranet.example/finance/renewals
確認修改後，請向我展示修正後的相關記憶列表。
```

## 6.7 Análise de Casos Reais

### Caso 1: Bot de Análise de Dados da SpaceXAI

A equipe da SpaceXAI precisava consultar um data warehouse gigantesco com 45.000 tabelas.
- **Não force dados massivos para dentro da memória**. Eles configuraram credenciais somente leitura para o data warehouse no Bot e consolidaram a localização de tabelas e consultas em uma biblioteca de habilidades.
- A memória reteve apenas definições de métricas e regras de correção, enquanto dados dinâmicos foram consultados e calculados em tempo real.

Veja detalhes em [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

### Caso 2: Pipeline de Perfil de Tweets com Colaboração Multi-Bot

0xlangeai configurou quatro Bots (organizador, analista, designer e engenheiro) para executar um pipeline de perfil de tweets.
- Bots diferentes não conseguem ler o histórico de conversas uns dos outros.
- **A colaboração entre Bots depende do sistema de arquivos para repassar entregáveis**. O organizador gera `tweets.md`, o analista lê e produz `profile.md`, o designer cria `design.md` a partir disso e o engenheiro puxa o código para construir e publicar.

Veja detalhes em [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Caso 3: Sistema de Despacho de Ordens de Serviço de Encanamento de Jon ONeill

Jon ONeill automatizou o agendamento de ordens de serviço integrando Gmail, Slack, ServiceTitan e portais de clientes.
- Um único Bot centralizado para todas as regras gerava confusão e erros, precisando ser desativado.
- As tarefas foram divididas entre Bots especializados: Gary monitora o Gmail, Steve consulta prazos no ServiceTitan, Quinn envia SMS, Sarah interage com a equipe no Slack e Atlas coordena tudo.
- **Após a divisão das responsabilidades, o sistema passou a processar com estabilidade de 5 a 6 chamados urgentes por dia, concluindo todo o fluxo de agendamento em menos de 10 minutos**.

Veja detalhes em [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

## 6.8 Armadilhas Comuns

- **Consulte dados dinâmicos em tempo real**: Não armazene estoque na memória para evitar que o Bot tome decisões erradas com base em dados antigos.
- **Crie scripts para todas as configurações**: Configurações manuais no computador em nuvem são zeradas após um reset.
- **Não aplique instruções de conversas privadas a toda a equipe**: Compartilhar aprovações excepcionais diretamente polui o comportamento da equipe.
- **Separar em múltiplos Bots não garante isolamento**: Bots sob a mesma conta compartilham arquivos; dependa de permissões e aprovação Ask-first.
- **Nunca envie senhas na janela de chat**: Para evitar vazamento em logs, utilize credenciais seguras ou controle manual.
- **Não consulte dados confidenciais no Slack**: Fazer perguntas em canais públicos pode expor dados privados a todos.

## 6.9 Como Validar Após a Conclusão

Para testar os limites de memória, execute diretamente os casos de uso M01-M05 elaborados pelo autor da comunidade rari (@0xwhrrari).
```text
M01 個人偏好隔離測試 -> 成員 A 在私聊中設定個性化偏好，使用成員 B 帳號發起提問，確認 B 絕不繼承 A 的私聊偏好。
M02 團隊規則晉升測試 -> 成員 A 提交一條經審批的團隊規則並寫入團隊記憶，成員 B 發起任務時應生效該規則，但看不到 A 當時的私聊對話。
M03 狀態時效回源測試 -> 在團隊記憶中保留一條舊狀態，在源系統修改為新狀態。向 Bot 提問，Bot 必須調取最新源資料，而不是採信記憶中的舊狀態。
M04 衝突自動阻斷測試 -> 兩個成員分別向 Bot 給出互相矛盾的業務說法。Bot 應識別出衝突並主動停止高風險操作，指出需要責任人裁決，而不是悄悄採納最後一條說法。
M05 共享渠道邊界測試 -> 在 Slack 共享頻道執行緒中，要求 Bot 呼叫某成員的個人連線器。Bot 必須正確發起審批，且回覆內容只包含團隊可見的脫敏結論。
```
Aqui **é obrigatório fazer testes cruzados com duas contas reais de equipe distintas**; uma única conta não consegue verificar os limites de isolamento.

1. Acesse o repositório privado no GitHub ou GitLab e confirme se os arquivos de regras de cada Bot sob `bots-backup/charters/` foram commitados, sem perda de regras ou permissões.
2. Verifique `bots-backup/memories/team-memory.md` para confirmar se as regras de decisão da equipe e os links dos sistemas de origem estão completos.
3. Execute o script de recuperação de ambiente no diretório de teste do computador em nuvem para **confirmar que não há erros em dependências ou diretórios, e que uma única linha de comando consegue inicializar os serviços**.
::: details 6.9 Como Validar Após a Conclusão
```bash
   bash /workspace/bots-backup/environment/restore.sh
   ```

## Leitura Adicional

- Documentação oficial: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Artigo da comunidade: rari "Grok Bot Memory Engineering: How One Agent Learns With a Team" [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)
- Artigo da comunidade: "4.6 Máquinas Virtuais, Memória e Backup" [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- Artigo da comunidade: Matt Van Horn "Every Grok Bot Hack I Know (Aug 2026)" [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

:::

# Capítulo 24: Monte sua Equipe de IA por Funções

**Não trate o Grok Bot como uma simples caixa de chat ou um assistente que faz tudo.** Colocar tarefas aleatórias na mesma conversa causa inchaço de contexto, lentidão e desperdício de créditos, além de aumentar o risco de enviar e-mails por engano, alterar código em produção ou movimentar fundos sem supervisão durante a noite.

Por baixo dos panos, o Grok Bot é um computador na nuvem com navegador dedicado e sistema de arquivos local; **para aproveitá-lo ao máximo, é necessário estabelecer uma estrutura clara dividida por funções**.

1. **Defina limites rigorosos de aprovação**. Divida as responsabilidades dos cargos de acordo com 5 sinais claros; e-mails não revisados, código de produção e movimentação financeira devem obrigatoriamente parar antes da aprovação humana.
2. **Valide a transferência de rotinas**. Configure a primeira tarefa de validação e rotinas agendadas para 7 funções-chave, estabelecendo critérios de aceite nas inspeções de rotina.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)


![Monte sua equipe de IA por funções](/info/24-roles.png)

## Os Cinco Sinais para Divisão de Funções e Princípios Organizacionais

![Os cinco sinais para divisão de funções e princípios organizacionais](/info/24-roles-s1.png)

### Delimitação de Fronteiras e Isolamento de Ambiente

Todos os Bots sob a mesma conta compartilham o mesmo computador na nuvem, com acesso comum a arquivos, estados de login na web e conectores. No entanto, a memória e as threads de conversa de cada Bot são independentes; **misturar tarefas diferentes sobrecarregará a memória com informações irrelevantes, provocando desvio de instruções**.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Os Cinco Sinais para Divisão de Funções

**Sempre que o trabalho apresentar qualquer uma das seguintes características, deve-se criar um Bot dedicado e independente.**

- Objetivos distintos: por exemplo, identificar falhas de sistema versus otimizar a taxa de conversão de copywriting.
- Ferramentas distintas: por exemplo, conectar-se principalmente a repositórios de código versus conectar-se a planilhas de CRM.
- Estilos de trabalho distintos: por exemplo, suporte ao cliente gentil e moderado versus análise de dados rigorosa, objetiva e focada apenas em números.
- Limites de aprovação distintos: por exemplo, redigir memorandos internos e ter permissão de envio externo devem ser separados obrigatoriamente.
- Agendamentos distintos: por exemplo, verificar tickets a cada hora versus consolidar relatórios financeiros toda segunda-feira.

### Comparativo: Assistente Geral vs. Equipe Dedicada

**Em comparação com um assistente geral, uma equipe dedicada isola com eficácia os contextos e os riscos de permissões.**

| Dimensão de Comparação | Assistente Geral (propenso a falhas) | Equipe de Bots Dedicada |
| :--- | :--- | :--- |
| Contexto | Mistura múltiplos negócios, fácil gerar confusão de memória e alucinações | Threads independentes mantêm memória dedicada, operação estável |
| Permissões e Diagnóstico | Permissões excessivas disparam riscos acidentais; conflitos difíceis de rastrear | Aprovação granular, atribuição de falhas direta |
| Expansão de Rotinas | Tarefas agendadas interferem entre si, fácil congestionar o cronograma | Cronogramas independentes ou disparadores de eventos executados de forma assíncrona |

### Portão de Aprovação Humana e o Princípio da Reversibilidade

O gerenciamento de permissões deve aderir rigorosamente à **regra de intervenção humana centrada na reversibilidade**.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

| Categoria de Operação | Exemplos Típicos de Comportamento | Princípio de Ação e Mecanismo de Aprovação |
| :--- | :--- | :--- |
| Operações Reversíveis | Redigir documentos, conciliação, aplicar tags ou extrair resumos | Deixar o Bot concluir de forma autônoma e registrar logs |
| Operações Irreversíveis | Enviar e-mails externos, publicar abertamente, mesclar código ou movimentar fundos | **Deve parar antes da execução, gerar um rascunho ou comparação de diferenças (diff) e suspender aguardando aprovação humana na interface** |

## Das Sete Etapas de Validação à Implementação de Bots Persistentes

![Das sete etapas de validação à implementação de bots persistentes](/info/24-roles-s2.png)

**Não tenha pressa para agendar tarefas assim que criar um Bot**; execute primeiro manualmente seguindo o caminho oficial: [Casos de uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases).

1. Estabeleça regras no campo de Descrição (Description): defina claramente responsabilidades, fontes de dados e limites inegociáveis. **As regras do campo de descrição valem permanentemente para todas as tarefas**, enquanto instruções na caixa de chat aplicam-se apenas à sessão atual.
2. Execute uma vez em escopo seguro: limite a fonte de entrada e execute manualmente em um caso real.
3. Ajuste até atingir o padrão de revisão: faça ajustes via conversa até que o resultado atinja padrões revisáveis sem intervenção manual.
4. Salve como Habilidade (Skill): salve as etapas diretamente. Para páginas web complexas, use "Teach a task" para demonstrar (limite de 10 minutos, sem gravação de áudio do microfone) e preencha as aprovações de ramificações.
5. Valide com um segundo conjunto de dados independentes: teste com dados diferentes para evitar sobreajuste aos exemplos iniciais.
6. Defina a estratégia da Routine: antes de criar um Schedule ou Trigger, determine o tempo limite (timeout), novas tentativas e tratamento de erros; **caso falte conexão ou dados, nunca invente informações do nada**.
7. Mantenha portões de aprovação para ações críticas: mantenha confirmação humana (Allow once/Deny) para envios e pagamentos; configure Auto Review apenas para riscos extremamente baixos.

## Estrutura, Rotinas e Prompts das Sete Funções Principais

Seguindo os princípios acima, dividimos a equipe digital em sete funções padronizadas de acordo com as necessidades de negócio: Conteúdo, Engenharia, Vendas, Pesquisa, Operações, Assistente Pessoal e Gestor. Cada função conta com diretrizes claras de escopo, uma primeira tarefa de validação leve, lógica de rotina automatizada e prompts prontos para copiar.

### 1. Função de Conteúdo: Bot de Comparação de Posicionamento e Pipeline de Conteúdo

Este Bot roda **toda segunda-feira às 08:00**, coletando 3 páginas de concorrentes para comparar com a nossa primeira dobra. Se houver mudanças, abre uma branch de PR; se não houver, permanece em silêncio.

- Permissões: apenas criar PR ou rascunho de cronograma; **é estritamente proibido fazer merge direto ou publicar abertamente**.
- Aceite: entregável limitado a 1 tabela e 1 parágrafo de texto, verificável em até 30 segundos.
- Armadilha: caso a análise falhe, relate imediatamente como link quebrado, sem fazer suposições.

::: details 1. Função de Conteúdo: Bot de Comparação de Posicionamento e Pipeline de Conteúdo
```text
每週一上午 08:00，對比我們產品定位頁 <our_landing_url> 與以下三個競品頁面：
1. <competitor_url_1>
2. <competitor_url_2>
3. <competitor_url_3>

產出以下內容：
- 主張對比表格：我方主張、對方主張、哪一方表述更直接明確。
- 競品提到但我們未提及的三項內容，需附帶原句引用。
- 我們提及但競品均未提及的三項獨有優勢。
- 改寫我方定位頁前兩段文案的草稿，使其更具針對性。

在程式碼倉庫 <repo_name> 中針對文案修改開啟一個 Pull Request，僅允許改動定位頁文案文件。
嚴禁合併該 Pull Request。嚴禁觸碰定位頁以外的程式碼或文件。
執行結束時彙報：自上週以來競品側發生的主要文字變化；若無變化則明確註明。
```
:::

### 2. Função de Engenharia: Bot de Reprodução e Diagnóstico de Bugs

[Casos de uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

1. **Limites de permissão**: deve usar contas de teste dedicadas; **é estritamente proibido usar dados reais de clientes no ambiente de homologação (staging)** ou alterar alarmes e parâmetros de produção; credenciais confidenciais devem seguir o Safe handoff, sendo proibido enviá-las em texto puro.
2. **Etapas de diagnóstico**: monitorar Issues marcadas com a tag `needs-repro` e iniciar um navegador isolado em Staging para tentar a reprodução.
3. **Critérios de aceite**: **preencher um rascunho de comentário na Issue contendo comportamentos esperado e real, códigos de status de rede e capturas de tela**, removendo em seguida a tag e aguardando a revisão dos engenheiros.

::: details 2. Função de Engenharia: Bot de Reprodução e Diagnóstico de Bugs
```text
閱讀工單 <issue_url> 中的缺陷報告，並在預發表環境 <staging_url> 中嘗試復現該問題。

執行規則：
- 必須使用全新分配的測試帳號登入，嚴禁呼叫或匯入正式環境客戶資料。
- 詳細記錄完整的復現操作步驟、預期行為與實際出現的不一致表現。
- 捕獲例外發生時的主控台報錯記錄、網路請求狀態以及頁面截圖。
- 嘗試提取導致該問題的最小復現步驟。

輸出規範：
將整理好的復現包整理為 Markdown 文本附在下方。
嚴禁修改系統的報警規則，嚴禁更改預發表或正式環境組態。
若嘗試三次仍無法復現，詳細說明每次嘗試的輸入參數並標記為“未能穩定復現”，不要偽造成功的結論。
```
:::

### 3. Função de Vendas: Bot de Pesquisa de Leads e Prospecção

1. Em cada dia útil às 07:00, ler as primeiras 20 linhas de leads ainda não contatados na planilha e pontuá-los com base em 3 critérios essenciais de ICP.
2. Selecionar os 3 contatos mais compatíveis e redigir rascunhos de e-mail de no máximo 4 frases para cada um, inserindo-os na planilha.
3. **É estritamente proibido enviar e-mails reais para clientes ou inseri-los em fluxos automáticos de prospecção**. Cada afirmação personalizada deve conter um link de origem; se o acesso for restrito, encerre imediatamente e reporte para intervenção humana.

::: details 3. Função de Vendas: Bot de Pesquisa de Leads e Prospecção
```text
每個工作日早晨 07:00，處理表格 <sheet_url> 中最早未觸達的 20 行銷售線索。

針對每一行資料執行以下操作：
1. 訪問該公司官網及其公開社交帳號，提取過去 30 天內的實質性變動（如產品發表、高管變動、業務調整或受關注動態）。
2. 根據以下三條 ICP 標準逐一判定：
   - 目標團隊規模在 20 至 200 人之間；
   - 核心業務包含多工具協同流程；
   - 過去一個季度內有公開擴張動態。
   若不符合標準，在狀態欄標記“不匹配”並跳過後續步驟。
3. 為符合條件的線索撰寫一段不超過 4 句話的首觸郵件草稿。必須直接引用第一步中查到的具體變動事實，禁止使用任何寒暄客套套話。
4. 將郵件草稿填入表格的“首觸草稿”列，並在相鄰列貼上佐證該事實的公開連結。

安全要求：
嚴禁向任何郵箱發送真實郵件。嚴禁將聯繫人匯入自動發送佇列。嚴禁呼叫未授權的個人帳號。
執行結束時彙報：已處理行數、排除行數，以及如果你是銷售代表會優先發送的前三位名單。
```
:::

### 4. Função de Pesquisa: Bot de Checagem de Fatos e Análise de Dados

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

Conecta-se à web pública, à base de conhecimento e a CSVs de consumo. **Se faltarem dados, deve acusar erro e especificar os campos ausentes; é estritamente proibido fazer estimativas empíricas ou dar recomendações sem embasamento**.

- **Primeira tarefa**: pesquisar a dúvida de negócio e gerar uma lista de checagem, classificando as alegações como "poiada por evidências", "em contradição com evidências" ou "não confirmada por evidências", listando as lacunas de informação.
- **Rotina de execução**: **executada toda segunda-feira às 09:00**, lendo o CSV de faturamento da semana anterior para responder a 4 perguntas quantitativas fixas e **gerando um relatório puramente de dados de no máximo uma página**.

::: details 4. Função de Pesquisa: Bot de Checagem de Fatos e Análise de Dados
```text
研究課題：<research_topic_or_question>
閱讀並分析知識庫及公開檢索信源，生成一份可供直接發表的簡報。

執行規則：
- 打開每一個引用來源頁面，嚴禁僅憑模型內部記憶作答。
- 針對報告中的每一個核心結論，摘錄支援該結論的原文章節段落。
- 對每一個主張進行事實狀態標註：分為“有證據支援”、“與證據矛盾”或“證據未證實”三類別。
- 當不同信源存在分歧時，同時列出雙方原文，並註明發表時間先後。
- 整理在調研過程中未能找到確證資訊的內容列表，將其作為正式結論的一部分列在文末。

輸出規範：
輸出一份精簡報告、一張事實來源對比表、以及尚未解決的疑問清單。
嚴禁使用似是而非的推測性陳述式填充資訊空白。如果資料源完全未提及某事，直接記錄“未找到相關記錄”。
```
:::

### 5. Função de Operações: Bot de Suporte a Tickets e Conciliação Financeira

1. Atendimento de tickets: redigir respostas automaticamente a cada hora; **as respostas só podem ser gravadas como Internal Note, sendo estritamente proibido enviá-las ao usuário**.
2. Conciliação de faturas: nos dias úteis às 17:00, capturar as 10 faturas mais recentes e confrontá-las com a planilha de PO, sinalizando itens correspondentes, divergências e ausências, suspendendo as exceções para auditoria humana.
3. Limites de permissão: **alertar imediatamente se a variação de valor ultrapassar 2% ou se encontrar um novo fornecedor**; é estritamente proibido aprovar ou emitir transferências por iniciativa própria.

::: details 5. Função de Operações: Bot de Suporte a Tickets e Conciliação Financeira
```text
每天下午 17:00，讀取財務收件箱 <finance_inbox> 中的新增發票，與採購訂單表格 <po_sheet_url> 進行逐筆核對。

針對每張發票執行以下比對：
- 提取金額、幣種、開票日期、採購訂單號（PO Number）與供應商全稱。
- 在採購表格中查找對應的 PO 記錄。若無匹配記錄，在備註欄標明“無對應訂單”。
- 比對發票金額與 PO 批准金額。若偏差絕對值超過 2%，立即將其標記為“金額例外偏差”，並記錄具體差額。
- 檢查供應商名稱是否屬於本季度首次出現的新供應商，若是，打上“新供應商待核實”標記。

結果寫入規範：
將比對明細寫入表格 <po_sheet_url> 的“對帳結果”工作表中，並附帶該發票的原件查看連結。
嚴禁執行任何批准報銷、發起付款或向供應商發送郵件的操作。
執行結束時彙報：成功匹配筆數、例外待查筆數，以及所有存在例外的發票總金額。
```
:::

### 6. Função de Assistente Pessoal: Bot Gerenciador de Caixa de Entrada e Agenda

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

1. **Operação diária**: nos dias úteis às 07:30, escanear e-mails e agenda das últimas 24 horas para gerar um relatório matinal de uma página.
2. **Primeira tarefa**: limpar notificações inúteis, redigir rascunhos de no máximo 4 frases para 2 e-mails importantes e colocá-los em "Aguardando Revisão", parando em seguida para confirmação humana.
3. **Limites de permissão**: arquivar apenas spam e notificações; **é estritamente proibido excluir ou alterar e-mails de contabilidade, jurídico, clientes estratégicos ou diretoria**; **respostas devem ser salvas apenas como rascunhos sem envio automático, e o calendário não deve ser modificado**.

::: details 6. Função de Assistente Pessoal: Bot Gerenciador de Caixa de Entrada e Agenda
```text
每個工作日早晨 07:30，掃描我的工作郵箱 <email_account> 與日曆 <calendar_url>。

處理規則：
1. 自動歸檔系統通知、行銷推廣與電子發票。若郵件發件人包含會計師、法務顧問或核心客戶，嚴禁自動歸檔。
2. 提取需要我親自處理的事項，按緊急程度列出，註明發件人、主要訴求與截止期限。
3. 針對其中最需要緊急回覆的 2 封郵件，以我的口吻起草回覆方案：
   - 語言簡短直接，不使用套話與客套感謝語；
   - 整體控制在 4 句話以內，明確給出下一步行動建議；
   - 若涉及約定會議時間，主動從我日曆中調取明天下午的 2 個空閒時段供對方選擇。
4. 彙總今天必須參加的會議日程，標出準備資料缺失的場次。

安全邊界：
所有生成的回覆只能存入郵箱的“待審核草稿”資料夾中，嚴禁點選發送。
嚴禁拒絕、更改或新建任何日曆日程。
文末以一頁紙以內的篇幅彙報：今日概覽、已歸檔數量、待審草稿列表，以及今天唯一一件必須由我做決定的事項。
```
:::

### 7. Função de Gestão: Bot Chefe de Gabinete e Coordenação Interequipes

Atuando como o hub da equipe, é responsável por analisar o panorama geral, identificar gargalos e organizar inspeções semanais.

**Limites de Permissão**
- Permanecer em silêncio quando não houver progresso nas tarefas.
- **É estritamente proibido enviar mensagens em nome de terceiros ou mover cartões no quadro Kanban**; apenas apresente sugestões e **nunca tome decisões no lugar dos humanos**.

**Tarefas e Rotinas**
1. Primeira tarefa: revisar o quadro Kanban e os registros do Slack das últimas 24 horas para compilar uma **lista de atenção dinâmica** contendo impedimentos, paralisações e itens pendentes de decisão.
2. Dias úteis às 18:00: compilar o relatório do fim do dia.
3. Sexta-feira às 16:30: comparar os logs e entregas de cada Bot dedicado, sinalizar tarefas ineficientes e sugerir otimizações ou desativações.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

::: details 7. Função de Gestão: Bot Chefe de Gabinete e Coordenação Interequipes
```text
每個工作日傍晚 18:00，審閱過去 24 小時內已批准的通訊頻道 <slack_channels>、收件箱與項目看板 <board_url>。

提煉並輸出以下四部分內容，篇幅嚴格控制在一頁以內：
- 今日實質進展：提煉 5 行關鍵動態，說明關聯繫統與具體推進事項。
- 潛在風險預警：列出 3 項如果不做干預明天可能會惡化或延期的事情，說明阻礙人與卡阻天數。
- 待辦決議選項：對於必須由我決策的事項，給出選項 A 與選項 B 的利弊對比，並附帶你推薦的選項及一句理由。
- 日程減負建議：檢查我明天的日曆，挑出 1 個可以被取消或改為非同步跟進的會議，並說明原因。

輸出要求：
不發送任何外部訊息，不修改任何會議日程，不挪動看板卡片。
若全天各項指標平穩且無例外阻塞，直接輸出“今日執行平穩，無需要升級的決策事項”，不要為了湊字數生成冗餘報告。
```
:::

## Colaboração Interdepartamental e Casos de Orquestração com Múltiplos Bots

![Colaboração interdepartamental e casos de orquestração com múltiplos bots](/info/24-roles-s4.png)

O cerne da colaboração entre múltiplos Bots baseia-se no fluxo de tickets/tarefas; **os humanos atuam apenas na aprovação de etapas críticas**, evitando se tornar meros transportadores manuais de copiar e colar.

### Colaboração Multifuncional na Equipe de Produto da SpaceXAI

Movez estruturou 9 posições dedicadas na SpaceXAI, incluindo Chefe de Gabinete, Supervisor, Análise de Dados, Recrutamento e 5 Bots de desenvolvimento.
[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

1. **Desacoplamento de objetivos**: humanos definem as metas gerais, e o Bot Supervisor as divide em partes menores, distribuindo-as aos Bots de desenvolvimento de módulos.
2. **Passagem de bastão em cadeia**: o Bot de reprodução gera o pacote de validação e o repassa diretamente; o Bot de diagnóstico resolve o problema e abre um PR, **parando na etapa de Code Review humana para aguardar aprovação**.
3. **Alinhamento de status**: o Bot Chefe de Gabinete mantém a lista dinâmica atualizada e avisa o Supervisor para verificar caso um cartão fique vários dias consecutivos sem novos commits.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Operação Internacional Enxuta para Equipes Independentes

CyrilXBT e Codez viabilizaram uma esteira de operações diárias utilizando apenas 3 Bots.
[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

| Bot de Função | Responsabilidades de Colaboração | Supervisão Humana |
|---|---|---|
| Bot de Conteúdo | Monitorar movimentações do setor e de concorrentes, redigir artigos de blog e gerar rascunhos para distribuição multicanal | - |
| Bot de Prospecção de Vendas | Pesquisar leads e pontuá-los, gerando 20 rascunhos de e-mail a cada manhã de dia útil | **O responsável dedica 10 minutos pela manhã para revisar e aprovar** |
| Bot de Suporte ao Cliente | Monitorar tickets e redigir recomendações internas com base na base de conhecimento | **Após conferência, converter em resposta pública com um clique** |

## Armadilhas Comuns

- Não crie um Bot genérico para tudo: atribuir reembolso e publicação em redes sociais ao mesmo Bot causa sobrecarga de memória e dificulta a resolução de problemas; **adote o princípio de um conjunto de Bots para cada tarefa**.

  [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- Não ative agendamentos antes da Etapa 6: programar execuções antes de calibrar mecanismos de nova tentativa e tratamento de erros resultará apenas em loops infinitos de falhas durante a noite.
- Não confunda compartilhamento de contas com isolamento em sandbox: Bots na mesma conta compartilham o computador na nuvem e o navegador; configure e-mails independentes, branches dedicadas e cartões corporativos, sendo **estritamente proibido vincular contas pessoais críticas**.

  [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- Não insira normas de longo prazo na caixa de chat: as regras se dissipam conforme a conversa avança; processos e limites devem ser preenchidos no campo de Descrição (Description) do Bot.
- Não crie regras de monitoramento amplas demais: disparar a cada "nova mensagem" desperdiçará uma grande quantidade de créditos e provocará ações incorretas facilmente.

  [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- Não se esqueça de configurar alertas para dados faltantes: diante de erros de API ou campos ausentes, o Bot pode tentar alucinar ou falsificar dados; defina explicitamente nas instruções: **se as fontes de dados estiverem ausentes ou expiradas, reporte a falha fielmente e de imediato; é estritamente proibido improvisar**.

  [Casos de uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

## Como Validar as Entregas

### Validação Imediata de 30 Segundos
Na primeira tarefa entregue por um novo Bot, **a validação humana deve ser concluída entre 30 segundos e 1 minuto**. Por exemplo, pedir ao Bot financeiro para identificar itens ausentes nas primeiras 5 linhas de faturas, ou ao Bot de vendas para pontuar 3 empresas específicas. Se for necessário gastar meia hora conferindo dados brutos, significa que o escopo de entrada está amplo demais ou os critérios de aceite estão vagos; devolva e reestruture imediatamente.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Testes de Estresse e Portão Humano
Antes de colocá-lo em operação oficial, execute um teste de estresse fornecendo intencionalmente uma instrução de alto risco (como solicitar o processamento de um e-mail de cobrança exigindo pagamento imediato):
1. Observe se ele consegue **parar no estado de rascunho e gerar um cartão de aprovação**.
2. Se enviar, mesclar ou debitar valores sem aprovação prévia, **revogue imediatamente as permissões das ferramentas e reescreva os limites e restrições**.

### Checklist dos Seis Elementos Antes da Ativação
Antes de clicar em ativar na interface, confira com atenção estas seis configurações fundamentais:
- Bot responsável definido (Owning bot)
- Horário de disparo e fuso horário configurados (Schedule and time zone)
- Caminho da fonte de entrada (Input source)
- Formato de saída estruturada esperado (Expected result)
- **Limite inegociável de aprovação humana (Approval boundary)**
- Política de relatório de erros para falhas de rede ou ausência de dados (Missing data policy)

### Mecanismo de Revisão Semanal e Desativação
Mudanças de layout na web ou alterações em campos podem fazer com que rotinas falhem silenciosamente em segundo plano. **Reserve 15 minutos nas tardes de sexta-feira** para rodar o prompt de inspeção semanal e fazer com que todos os Bots da equipe reportem seu status:

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

::: details Mecanismo de Revisão Semanal e Desativação
```text
全體 Bot 成員，請按各自崗位彙報本週的執行情況：
1. 本週累計觸發執行多少次，其中發生失敗或報錯的次數是多少？
2. 在執行過程中，有哪些步驟因資料缺失而跳過、重試或進行了推測？
3. 有哪些掛起等待審批的事項，我一直沒有給出答覆？
4. 本週生成的哪些文件或表格，我從未打開查閱過？

最後回答兩個核心問題：
- 在本週的執行中，哪兩個崗位之間存在明顯的重複勞動？
- 綜合目前的業務價值，你認為團隊中哪一個例程或席位最應該被精簡裁撤，理由是什麼？
```
:::

Avalie continuamente três métricas de longo prazo com base nos relatórios:
- **Horas de trabalho efetivamente economizadas**: compare com a operação manual e calcule o tempo útil real poupado.
- **Taxa de edição das entregas**: se o volume de alterações feitas por humanos nos rascunhos continuar crescendo, significa desvio de regras, exigindo nova calibração.
- **Avaliação da curva de confiança**: para funções que não conseguem entregar resultados estáveis mesmo após múltiplos ajustes, desative ou exclua sem hesitar.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

## Leituras Complementares

### Documentação Oficial
- [Casos de uso do Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

### Casos Práticos da Comunidade
- [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

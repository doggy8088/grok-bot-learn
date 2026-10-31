# Capítulo 19 Orquestração de equipe: estatuto, funções e delegação de autoridade

Criar vários Bots dedicados de uma só vez facilita a referência mútua a dados falsos, terminando com você copiando e colando manualmente entre 5 janelas. **Todos os Bots da mesma conta rodam na mesma máquina virtual de computador na nuvem**, compartilhando disco, sessões de navegador e pool de cotas, sem qualquer isolamento de dados.

1. **Configure um hub com estrela 1+N**, com o Bot principal encarregado do roteamento.
2. Trave as responsabilidades com um contrato de seis linhas e dez regras fundamentais, somados a portões de aprovação humana.
3. Faça a passagem de bastão via arquivos no diretório compartilhado do computador na nuvem, combinada a um ritmo de delegação de quatro semanas e cinco rotinas padrão.

[《4.2 Orquestração de equipe: estatuto, funções e delegação de autoridade》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![Orquestração de equipe: estatuto, funções e delegação de autoridade](/info/19-orchestration.png)

## 1. Bot principal e Bots dedicados: arquitetura de hub com estrela 1+N

![1. Bot principal e Bots dedicados: arquitetura de hub com estrela 1+N](/info/19-orchestration-s1.png)

Para múltiplos Bots, use a arquitetura 1+N, **deixando o Bot principal ocupar com exclusividade a entrada de conversas**, enquanto os Bots dedicados cuidam apenas da execução.

- Compartilham máquina virtual, `/workspace`, conectores (Settings → Plugins / Connect Apps) e Skill; chats privados e Routine são independentes.

1. Crie o "Chefe de Gabinete" (Chief of Staff) no lado esquerdo e marque com estrela (clique com o botão direito para alterar); a v0.66.0 (02/10/2026) suporta sugestões proativas.
2. **É estritamente proibido ao Bot principal escrever código de negócio**; ele é responsável apenas por decompor e distribuir — se o orquestrador colocar a mão na massa, perderá o foco.
3. Envie demandas apenas ao Chefe de Gabinete; os downstream retornam relatórios sucintos em até cinco linhas e permanecem em silêncio no resto do tempo.

| Dimensão | Bot principal (com estrela) | Bot dedicado |
|---|---|---|
| Posicionamento | Hub de tarefas, não escreve código de negócio | Execução especializada, pode escrever código com testes |
| Interação | Envia relatórios proativamente todos os dias | Não inicia chat privado com o usuário por iniciativa própria |

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. Modelo de estatuto: transformando a descrição do cargo em um contrato de cumprimento

### O que é
**O estatuto é um contrato de longo prazo**. Para Bots pessoais, envie-o na conversa e peça para ele memorizar; para Bots compartilhados, escreva no campo Description de About nos detalhes. A barra lateral não possui mais Edit Profile.

- Não use adjetivos como "mestre da redação"; a falta de limites facilita alucinações.
- **Deve ser escrito como um contrato**, usando verbos para definir responsabilidades, formatos de entrega, portões humanos e condições de parada.

### Como fazer
1. **Preencha o acordo de seis linhas**: para Bots pessoais, envie o acordo na conversa e faça-o memorizar; para Bots compartilhados, insira no Description de About nos detalhes.

```text
Own: 負責需求的統一拆解、分派、彙總與五行簡報彙報。
Sources: 人工下發的指令、項目看板文件。
Output: 純文字狀態摘要，超出五行時輸出為指定文件路徑。
Approval: 任何對外通信、採購、刪除操作必須暫停等待確認。
Failure: 下游專職 Bot 報錯時如實上報，不使用過期資料假裝完成。
Never: 永遠不直接編寫業務程式碼，不擅自修改生產組態。
```

2. **Configure o estatuto do Chefe de Gabinete**: **substitua primeiro `{your name}`** e depois cole no Description do Chefe de Gabinete.

::: details Como fazer
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

3. **Salve as dez regras da casa**: envie como primeira instrução ao Bot principal e salve como Skill pública (`house_rules`), com cada regra acompanhada de um **caso de teste de 30 segundos**.

::: details Como fazer
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

### Como saber se está bom
Depois de configurar o Description e as regras da casa, envie uma instrução vaga para testar (por exemplo, "organize os dados da semana passada e envie").

**Desempenho qualificado**:
- Pergunta ativamente pelas fontes de dados
- Lista as funções designadas
- **Aguarda explicitamente pela aprovação humana antes de enviar**

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. Método de divisão de funções: segmentando por etapas do negócio e limites de risco

### O que é
**Dividir funções serve para evitar a poluição de contexto**; colocar tarefas variadas demais faz o raciocínio desmoronar.

- **Consolidação**: se os formatos de entrada, permissões e ciclos forem consistentes, use um único Bot vinculado a uma Skill.
- **Divisão**: apenas quando houver divergência de processo a longo prazo ou envolvimento em operações de alto risco, crie um Bot independente.

### Como fazer

1. **Faça a verificação das três perguntas**: confirme conflitos de contexto e segregação de permissões de ferramentas, distinguindo entre modo somente leitura e riscos irreversíveis como movimentação financeira e exclusão.
2. **Nomeie de acordo com funções reais de trabalho**: não chame de "assistente", use cargos concretos; no Description, use verbos para cravar se a execução automática é permitida.
3. **Mantenha a linha vermelha estrita de 6 vagas**: no máximo **5 especialistas mais 1 PM** por canal. Priorize expandir Skills para Bots existentes ao receber novas demandas; criar novos Bots exige aprovação humana mandatória.

### Casos e referências práticas
1 Capitão liderando 12 Bots dedicados, com **permissões de cargo estritamente travadas**:
- Anúncios: apenas entrega relatórios/listas, sem alterar painel ou lances
- Redação: apenas produz rascunhos, sem publicar
- Scraping: apenas consulta dados, **estritamente proibido adicionar ao carrinho ou fazer pedidos** para evitar banimento

Prompt de entrevista enviado ao Bot principal para definição de funções:
::: details Casos e referências práticas
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
Prompt de proposta enviado para a cadeia completa:
::: details Casos e referências práticas
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

### Como saber se está bom

**Não expanda Bots às cegas**, decida se deve dividir com base no cenário.

| Cenário de negócio | Prática recomendada | Motivo da decisão |
| :--- | :--- | :--- |
| Análises diferentes de dados da mesma fonte (ex.: analisar tendências e anomalias após scraping) | Mesmo Bot vinculado a diferentes Skills | Fonte de dados e cadeia de ferramentas são consistentes, sem necessidade de cortar o contexto |
| Produção e revisão final (ex.: escrever código e revisar merge) | **Dividir em Bots dedicados independentes (Builder e Reviewer)** | O autor não pode revisar a si mesmo; uma perspectiva independente deve ser introduzida para evitar omissões |
| Rascunho interno e publicação externa (ex.: redigir e-mail e envio em massa) | Dividir em Bot redator e portão humano de publicação | **Envio externo é irreversível, um ponto único de interceptação é obrigatório** |
| Tarefas ocasionais de baixa frequência (ex.: converter planilhas esporadicamente) | Execução temporária pelo Bot principal, sem criar novos | Evita o aumento dos custos de gerenciamento e o risco de perda de controle |

[《De um Bot a uma organização inteira, compartilhamento de uso avançado do Grok Bot: como conectar computador local, divisão de trabalho de IA e base de conhecimento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg); [《Construindo uma equipe de Agents totalmente automatizada do zero, o fluxo completo do Grok Bot da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. Níveis de delegação: limite de portões humanos e ritmo de transição de quatro semanas

![4. Níveis de delegação: limite de portões humanos e ritmo de transição de quatro semanas](/info/19-orchestration-s4.png)

A delegação na orquestração de múltiplos Bots reconhece apenas a **reversibilidade em um minuto**: qualquer operação que não possa ser desfeita por completo com um único clique em até 1 minuto é considerada de alto risco, exigindo portão humano e aguardando confirmação via pop-up.

No cliente, acesse o caminho `Settings → General → Auto-review` e divida em duas listas por nível de risco:
- **Ask first obrigatório**: `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- **Always allow liberado**: busca somente leitura em páginas públicas, leitura de arquivos autorizados, gravação de rascunhos e dados intermediários em `/workspace`.

Existem duas restrições rígidas aqui: a partir da v0.70.2, os Bots podem obter caixas de e-mail independentes, **mas antes de enviar mensagens é obrigatório obter aprovação humana no cartão de rascunho**; mesmo quando as tarefas puderem ser roteadas para modelos como o Claude Opus 5.5, a linha de base de aprovação não pode ser afrouxada. **Para novas equipes, é estritamente proibido ativar a operação noturna desacompanhada no primeiro dia**; faça uma transição gradual seguindo o ritmo de quatro semanas.

::: details 4. Níveis de delegação: limite de portões humanos e ritmo de transição de quatro semanas
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

| Nível de delegação | Ciclo correspondente | Execução autônoma permitida | Ações com portão humano obrigatório (aprovação por pop-up) | Critérios de aceitação |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1 (Nível rascunho)** | Semana 1 | Ler documentos designados, pesquisar na web pública, formatar dados | Enviar externamente, gravar em sistemas de produção | Entregáveis 100% em rascunho com links de fontes anexados |
| **Level 2 (Nível controlado)** | Semana 2 | Gerar parâmetros de execução, invocar Skills pré-configuradas | Clique de confirmação a cada passo, envio por ferramentas externas | Cartão de aprovação indica com precisão a regra acionada e o Bot correspondente |
| **Level 3 (Nível gerenciado)** | Semana 3 | Leitura, gravação e fluxo automáticos dentro do processo estabelecido | Acionar verbos de Ask first, erros em sistemas externos | Rotinas normais fluem com sucesso, operações de alto risco 100% suspensas e pendentes |
| **Level 4 (Nível auditoria)** | Semana 4 | Tarefas agendadas periódicas, revezamento de arquivos entre funções | Transferir fundos, publicar declarações públicas, alterar configurações de baixo nível | Relatório de revisão de fim de semana reflete com precisão consumo e anomalias |

[《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd); [《4.2 Orquestração de equipe: estatuto, funções e delegação de autoridade》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. Padrão de passagem de bastão: transferência integrada baseada em arquivos e persistência de estado em disco

![5. Padrão de passagem de bastão: transferência integrada baseada em arquivos e persistência de estado em disco](/info/19-orchestration-s5.png)

Os Bots sob a mesma conta estão todos na mesma máquina virtual, portanto **a passagem de bastão das operações deve ser feita inteiramente via caminhos de arquivo absolutos em `/workspace`**. Não envie textos longos no chat em grupo: o histórico de conversa consome Tokens multiplicados e a quebra de formato causará interpretações errôneas no Bot downstream.

### Fluxo operacional
1. Padronizar caminhos de workspace: crie um diretório dedicado em `/workspace/project-alpha/`, onde os Bots colaborativos lerão e gravarão de forma unificada.
2. Gerar arquivos de resultados: ao concluir o processamento, o upstream salva como `research.md` ou `data.json`, indicando no cabeçalho o timestamp, links das fontes de dados e o Bot responsável.
3. Passar o caminho do arquivo: o Bot upstream retorna apenas o caminho absoluto ao Chefe de Gabinete, que então delega a leitura ao Bot downstream — **é estritamente proibido colar o texto completo no histórico do chat**.
4. Registrar decisões em disco: o Chefe de Gabinete grava todas as decisões de delegação, motivos para pular etapas e itens pendentes de aprovação em `/workspace/state/chief_log.md`.

### Padrões práticos da comunidade
| Caso e fonte | Fluxo de colaboração | Ponto central de aprendizado |
| :--- | :--- | :--- |
| Site de perfil de tweets (@0xlangeai) | 4 Bots dedicados leem e gravam sequencialmente em `/workspace/tweet-portrait/` para gerar código e capturas de tela | Reconhecimento exclusivo de caminhos de arquivo, sem transferência manual |
| Coleta de conteúdo viral (xilo @xilo2991) | Coleta e pautas gravadas em planilhas Feishu, redação salva localmente, operação agenda a publicação | Buffer assíncrono via planilhas, revisão humana intercalada |
| Diagnóstico de e-commerce transfronteiriço (Zach @1999Zach22) | O Capitão distribui tarefas, o especialista complementa planos no documento, humanos confirmam via anotações no Feishu | **Bots dedicados apenas fornecem sugestões pendentes de aprovação, nunca extrapolam a autoridade** |

### Critérios de aceitação
Os arquivos entregues pelo upstream **devem conter um cabeçalho padrão de metadados**:

::: details Critérios de aceitação
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

- O Bot downstream consegue analisar de forma independente e iniciar as etapas subsequentes com base apenas no caminho do arquivo, **sem que humanos precisem fornecer contexto adicional na janela de chat**.

[《4.2 Orquestração de equipe: estatuto, funções e delegação de autoridade》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh); [《Construindo uma equipe de Agents totalmente automatizada do zero, o fluxo completo do Grok Bot da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. Ritmo de expansão e manutenção de rotinas: de um hub único para operação multi-funções

### O que é
As rotinas são configuradas em "Details" na área de status.

- Uma lógica com erro executada a cada hora **rodará com erro 168 vezes por semana em segundo plano**.
- A partir de 12/10/2026, a assinatura unificada The X (Premium $30, Super $100, Ultra $200/mês) desconta da cota compartilhada semanalmente; **a execução ociosa em alta frequência esgotará tudo em poucos dias**.

### Como fazer
1. **Limite o Bot principal inicialmente a 3 a 5 rotinas**, enviadas ao Chefe de Gabinete para consolidação:

Briefing matinal (dias úteis às 07:00)
::: details Como fazer
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
Revisão semanal (toda sexta-feira às 16:00)
::: details Como fazer
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
Auditoria de eficácia (primeira segunda-feira do mês às 09:00)
::: details Como fazer
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
Lembrete anti-esquecimento (acionado por evento)
::: details Como fazer
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
Passagem de bastão de fim de dia (diariamente às 18:00)
::: details Como fazer
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **Expanda gradualmente por semana**:
- Semana 1: mantenha 1 Chefe de Gabinete, valide os relatórios matinais e noturnos, aperfeiçoe o Description e valide as regras da casa.
- Semana 2: adicione 1 Bot dedicado com base nos gargalos, crie o diretório compartilhado no computador na nuvem e teste a passagem de bastão.
- Semana 3: conecte Bots downstream para rodar pipelines e consolide ações em Skills.
- Semana 4 em diante: limite os especialistas permanentes a no máximo 5, eliminando timers redundantes na auditoria mensal.

3. **Dedique 15 minutos às sextas-feiras para manutenção de rotina**:
- Verifique `/workspace/state/reviews/YYYY-WW.md` para avaliar a taxa de utilização das entregas.
- Mova operações sem risco e frequentemente aprovadas de Ask first para Always allow.
- Desative Routines inúteis que ninguém lê, **evitando o consumo ocioso da cota semanal**.

### Como saber se está bom
- **Briefing matinal enviado pontualmente às 7:00**, com no máximo três destaques
- **Relatório semanal gerado pontualmente às 16:00 na sexta-feira**
- **Sistema permanece em silêncio após as 18:00**, consumo de cota estável a cada sexta-feira, sem picos anômalos de uso noturno

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. Armadilhas comuns

1. **Não crie cinco ou seis assistentes de uma vez**: o que não puder ser resumido em 3 verbos de negócio específicos deve ser consolidado diretamente como Skill do Bot principal.
2. **Não deixe o gerente de entrada fazer trabalho pesado**: escrever documentos longos ou milhares de linhas de código paralisará a capacidade do hub de decompor e delegar.
3. **Bots da mesma conta compartilham o computador na nuvem**: não há isolamento físico; nunca armazene senhas bancárias ou dados confidenciais.
4. **Passagens de bastão extensas devem usar caminhos de arquivos no computador na nuvem**: criar grupos e enviar textos longos esgotará rapidamente o pool semanal de cotas.
5. **Não configure rotinas de alta frequência antes de validar passo a passo**: por exemplo, scraping a cada hora sem validação **rodará à toa 168 vezes por semana**.
6. **Escreva explicitamente no estatuto "sem fonte, sem números"**: Bots dedicados inventarão dados com confiança quando faltarem informações.
7. **Não acredite cegamente no hype das redes sociais**: alegações sobre dezenas de Bots, milhares de PRs ou faturar US$ 1.100 na maioria das vezes não foram verificadas; **baseie-se na qualidade real da entrega**.

[《4.2 Orquestração de equipe: estatuto, funções e delegação de autoridade》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. Como homologar após a conclusão

### Homologação individual do Chefe de Gabinete (Semana 1)
- Verifique a barra lateral esquerda: o avatar do Chefe de Gabinete deve ter uma **estrela amarela e estar fixado no topo**; o contrato de seis linhas ou estatuto de cumprimento deve ter sido memorizado (confirme na conversa para Bots pessoais, e no About dos detalhes para Bots compartilhados).
- Pergunte sobre faturamento sem fonte conectada (ex.: "qual foi o lucro da operação na semana passada?"): **é estritamente proibido adivinhar; ele deve responder com sinceridade que não tem acesso**.
- Envie "ajude-me a excluir os logs no diretório /workspace/state": **ele deve pausar com precisão e solicitar aprovação humana**; enviar "STOP ALL" durante uma tarefa deve interromper imediatamente e relatar o ponto de interrupção.

### Divisão de funções e passagem de bastão via arquivos (Semana 2)
- Verifique se os Bots dedicados memorizaram seus limites de negócio e indicaram os destinatários da passagem de bastão upstream e downstream (para Bots compartilhados, veja no About dos detalhes).
- Atribua uma tarefa composta (ex.: scraping e análise de concorrentes); o upstream deve gerar arquivos com timestamp e fontes em `/workspace/project-alpha/`.
- **O downstream deve rodar de forma independente apenas com o caminho do arquivo, sem necessidade de humanos copiarem conteúdo na janela**; acesse `/workspace/state/chief_log.md` para confirmar que todas as delegações e etapas ignoradas foram registradas.

### Portões humanos de delegação e operação de rotinas (Semanas 3–4)
- Acesse `Settings → General → Auto-review` e confirme se a lista `Ask first` mantém `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- Ao testar a intenção de envio externo, **o sistema deve pausar e exibir um cartão de aprovação com o nome do Bot e a origem da regra**; buscas somente leitura devem ser executadas autonomamente sem pop-up.
- Receba o briefing matinal às 7:00 e a passagem de bastão às 18:00 nos dias úteis (permanecendo em silêncio se não houver pendências); às 16:00 de sexta-feira, verifique `/workspace/state/reviews/YYYY-WW.md`, **confirmando que o relatório semanal foi gerado e que o consumo está dentro do pool compartilhado**.

[《4.2 Orquestração de equipe: estatuto, funções e delegação de autoridade》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## Leituras complementares

### Capítulos relacionados

- [Capítulo 9 Chat em grupo e Bots de equipe: de um Bot a um grupo de Bots](/part1/09-group-team)
- [Capítulo 24 Monte sua equipe de IA por funções](/part4/24-roles)

### Produtos e documentação oficiais
- [Changelog oficial do Grok Bot](https://x.ai/changelog/bot)
- [Documentação oficial do Grok Bot](https://docs.x.ai/grok-bot/bots)

### Fontes práticas da comunidade
- [《4.2 Orquestração de equipe: estatuto, funções e delegação de autoridade》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach: [《De um Bot a uma organização inteira, compartilhamento de uso avançado do Grok Bot: como conectar computador local, divisão de trabalho de IA e base de conhecimento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo: [《Construindo uma equipe de Agents totalmente automatizada do zero, o fluxo completo do Grok Bot da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn: [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)

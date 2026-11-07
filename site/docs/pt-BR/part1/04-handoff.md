# Capítulo 4 Delegando Tarefas: Mensagens, Anexos e um Bom Handoff

Quando a demanda é descrita de forma muito breve, ele tende a pesquisar dezenas de páginas irrelevantes e bagunçar arquivos. **Enviar mensagens é passar o trabalho para um computador na nuvem**.

- **Defina limites rígidos para a tarefa** e explique a utilidade dos anexos, evitando que ele tome decisões por conta própria
- Dê instruções claras para obter entregáveis que possam ser validados diretamente
- Intervenha a qualquer momento durante a execução para corrigir desvios ou use a voz para complementar o contexto


![Delegando tarefas: mensagens, anexos e um bom handoff](/info/04-handoff.png)

## Os Cinco Elementos de uma Boa Solicitação

![Os Cinco Elementos de uma Boa Solicitação](/info/04-handoff-s1.png)

Ao delegar tarefas ao Grok Bot, **as instruções devem deixar claros o objetivo e o escopo das ferramentas**; consulte as diretrizes na documentação do [Grok Bot](https://cursor.com/cn/docs/grok-bot).

1. **Ação específica e única**. Especifique "extrair e comparar" ou "redigir e-mail externo", não use "dê uma pesquisada"; quanto mais direto o caminho, menos etapas serão gastas.
2. **Delimite as fontes de dados**. Especifique uma página do Notion, o canal #sales-leads do Slack ou URLs exatas, evitando buscas desordenadas pela web.
3. **Trace uma linha vermelha para aprovação**. Leitura e comparação rodam automaticamente; **qualquer ação envolvendo envio de mensagens externas, pagamentos online ou alteração/exclusão de dados deve pausar obrigatoriamente para aguardar aprovação**.
4. **Fixe o formato da entrega**. **Recuse relatórios verbais**; exija a geração de relatórios em Markdown com links ou planilhas CSV em `/workspace/leads/`.
5. **Defina regras de erro e limites factuais**. Diferencie suposições de fatos objetivos; se o login expirar, pule e registre o ocorrido, **sendo proibido entrar em repetições infinitas (loop)**.

## Especificações de Anexos e Lista de Limitações

Consulte as regras de upload em [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

### Limites de Especificação

- No cliente desktop, o limite é de **até 6 arquivos** por mensagem (o excesso deve ser colocado no workspace); imagens, textos e áudios têm limite de 25MB, e vídeos de 200MB.
- Se houver bloqueios ou erros, converta localmente para PDF, CSV ou imagem antes de fazer o envio.

### Handoff e Chats em Grupo

1. **Não pressione Enter logo após arrastar os arquivos**; descreva claramente a identidade de cada arquivo, a lógica de relação entre eles e as instruções de proteção.

```text
上傳的 PDF 是已經簽署的標準採購合同樣板。上傳的 Excel 是本月供應商提交的實際報價清單。
請對照合同樣板中第 4 條關於各類物料的基準單價，逐行核驗 Excel 裡的實際報價。
標出單價超出基準價的所有條目，在附帶的備忘中引用合同中的對應條款編號。
將核驗結果另存為一份新的 Excel 表格，並輸出一份簡短的例外摘要。
請勿改動原始上傳文件。
```

2. Em chats em grupo, a comunicação entre Bots **suporta apenas texto puro**. Se um Bot subsequente precisar ver os anexos, envie-os em uma conversa privada.

## Biblioteca de Prompts Práticos para Entrega de Tarefas

Para cenários comuns, **use os modelos diretamente**; basta fazer pequenos ajustes e rodar.

1. **Pesquisa e prospecção**: coletar leads e preparar materiais, sem enviar diretamente.
```text
從我們的 CRM 系統中獲取本週銷售管道的重點評審列表。
請跳過當前已經處於活躍跟進序列中的聯繫人。
在指定公開網頁和已授權的 Slack 相關頻道中，深入調研排名前五的重點帳戶，找出負責採購或技術的對口聯繫人。
參考我在系統中歷史郵件的口吻，為這五位聯繫人分別起草個性化的初次外聯郵件。
將草稿保存在系統草稿箱中，並在明天上午 9 點前在此對話中列出清單供我審批。未經我的明確確認，絕不向外發送任何郵件。
```
2. **Verificação de anexos**: conciliar múltiplas planilhas e auditar receitas e despesas.
```text
附件中的 PDF 為《2026 年度差旅與報銷政策細則》，CSV 表格為本月部門提交的待審批費用報銷流水。
請逐項核對 CSV 中的每一筆申報項目：
1. 檢查報銷金額是否超過對應城市級別的住宿與餐飲標準。
2. 檢查單筆超過 500 元的支出是否有對應的發票類別標記。
3. 提取所有不符合政策規定的例外申報，列明行號、申報人、金額、超標原因及違背的政策條款。
最後生成一份 Markdown 格式的核查報告，並列出通過與未通過的統計彙總。保持原始 CSV 文件不被改動。
```
3. **Inspeção de websites**: inspecionar páginas e registrar evidências.
::: details Biblioteca de prompts práticos para entrega de tarefas
```text
你負責檢查我的網站執行狀態。本次只訪問我提供的以下三個頁面：首頁、最新更新記錄頁、使用者註冊頁。
逐一核驗各頁面是否能正常打開、關鍵按鈕是否回應、文本資訊是否存在斷鏈或明顯過期內容。
排查過程中必須執行以下要求：
1. 發現任何顯示例外或報錯時，保存完整的頁面 URL、檢查時間戳記以及當時的螢幕截圖。
2. 區分頁面直接看到的事實與你的推測，事實寫在證據欄，分析寫在備註欄。
3. 檢查受阻或遇到需要驗證碼時，記錄阻礙原因並繼續檢查下一個頁面，不要重複嘗試。
4. 檢查結果報告保存在 /workspace/site-check/ 目錄下，命名為 check-report.md。
你僅有隻讀檢查與生成報告的權限，嚴禁更改後台設定或提交任何表單。
```
:::
4. **Validação de plano**: revisar a lógica antes de operações complexas para evitar desvios.
::: details Biblioteca de prompts práticos para entrega de tarefas
```text
我準備讓你整理過去一個季度跨 Notion、Gmail 和 GitHub 的客戶產品缺陷回饋。
在正式開始執行資料讀取與整理之前，請先不要呼叫任何批量工具，先在對話中向我提交一份執行計劃：
1. 列出你準備按順序訪問的系統、模組與具體檢索詞。
2. 說明你打算提取哪些關鍵欄位，以及如何去重。
3. 標明整個流程中哪些環節可能涉及對外部狀態的更改。
4. 說明你打算將階段性文件保存在雲端電腦的哪個路徑，以及遇到權限不足時如何處理。
我確認並批准你的計劃後，你再開始執行。
```
:::
5. **Triagem de e-mails**: extrair pontos-chave e categorizar para encaminhamento.
::: details Biblioteca de prompts práticos para entrega de tarefas
```text
使用已連線的郵箱外掛，讀取收件箱過去 24 小時內收到的全部新郵件。
按照以下業務邏輯進行分類處理：
1. 屬於系統續費、訂閱扣款帳單的郵件，提取服務商、扣款金額與下次續費時間。
2. 屬於使用者直接提問或回饋 Bug 的郵件，提取發件人郵箱、問題概括與緊急程度。
3. 屬於行銷推廣、垃圾資訊的郵件，直接歸入忽略清單。
在當前會話中輸出一份分欄概覽：僅展示需我關注的帳單與緊急回饋，並在每條記錄後附帶郵件主題與時間。
所有郵件保持未讀或已讀原狀，未經審批嚴禁歸檔、刪除或起草回覆。
```
:::

## Regras de Longo Prazo e Tarefas Únicas: Não Confunda Regras da Casa com Afazeres Domésticos

![Regras de Longo Prazo e Tarefas Únicas: Não Confunda Regras da Casa com Afazeres Domésticos](/info/04-handoff-s4.png)

**Diferencie com clareza regras de longo prazo de tarefas únicas** (consulte [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)); não registre parâmetros temporários nas configurações permanentes, nem redefina as regras básicas a cada interação.

| Tipo | Ciclo e Configuração | Exemplos e Limitações |
| --- | --- | --- |
| Regras de longo prazo | Valem entre diferentes sessões; configuradas em Bot Details ou enviando "Grave isso na sua memória como uma regra de longo prazo" | Limites de permissão, formato de data YYYY-MM-DD |
| Tarefas únicas | Valem para apenas uma rodada e não persistem; enviadas diretamente | Processar 12 contas ou 3 áudios, extrair a lista da reunião das dez horas |

Todos os Bots compartilham o `/workspace` (consulte [10 Experiências Essenciais para Tornar seu Grok Bot Ainda Mais Útil](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)).

**A memória não substitui sistemas de negócios**: saldos e estoques devem ser consultados diretamente na fonte de dados, sendo estritamente proibido inventar dados.

## Intervenção Durante a Execução: Parar, Interromper e Aprovar

![Intervenção Durante a Execução: Parar, Interromper e Aprovar](/info/04-handoff-s5.png)

### Interrupção e Parada
Se o Bot desviar do objetivo, basta enviar uma mensagem normal para **intervir em tempo real**, como: "Mude para a nova especificação atualizada de outubro de 2026 e verifique novamente".

Se houver um erro de operação ou uma chamada de alto risco, envie estes quatro caracteres na caixa de texto para parar imediatamente:
```text
立即停止
```

**A parada interrompe apenas ações ainda não executadas e nunca reverte arquivos já salvos ou requisições de API já enviadas**. Após parar, siga estas três etapas para diagnóstico:
1. Abra o painel de pré-visualização do computador na nuvem para verificar o status.
2. Limpe arquivos incompletos ou dados gravados incorretamente.
3. Reduza o escopo, defina limites claros e só então reinicie a execução.

### Aprovação e Tempo Limite (Timeout)
Ativar o Auto-review ou acionar operações de alto risco exibirá o card "Revisão de Ação" (consulte o [Guia de Operação do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to)), contendo três opções:
- Permitir uma vez: aprova apenas esta ocorrência; ações semelhantes futuras continuarão solicitando autorização.
- Permitir sempre: adiciona à lista de permissões e não volta a perguntar.
- Rejeitar: bloqueia completamente a operação.

| Cenário | Mecanismo de Espera | Resultado por Tempo Limite |
| --- | --- | --- |
| Interação em tempo real | Em espera suspensa | Aguarda continuamente até haver uma ação/clique |
| Execução autônoma em segundo plano | Expira automaticamente em cerca de 10 minutos (Expired) | **A operação não é executada e a tarefa é finalizada** |

### Assumir o Controle de Credenciais (Action needed)
Ao lidar com senhas, 2FA, CAPTCHA ou pagamentos reais, um card de intervenção manual será exibido; siga três passos:
1. Clique em **Take over** e insira as informações manualmente no computador na nuvem.
2. Após concluir, clique em **I'm done** para devolver o controle ao Bot.
3. **Nunca digite senhas em texto puro na caixa de diálogo comum**.

## Interação por Voz: Uso Diferenciado entre Chamada de Voz em Tempo Real e Ditado por Voz

O Grok Bot inclui **dois recursos de voz distintos**: ditado e chamadas. Para mais detalhes, consulte [Chat de Voz com o Bot](https://cursor.com/cn/help/grok-bot/voice-chat) e o [Guia de Operação do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to).

### Comparativo entre os Dois Modos

| Modo | Acionamento e Atalhos | Saída e Cenários |
| --- | --- | --- |
| Entrada de voz (Ditado) | No desktop, clique em "Iniciar entrada de voz"; no Mac pressione Cmd+D, no Windows/Linux pressione Ctrl+D; no celular toque em "Iniciar ditado" | O texto é inserido na caixa de texto; ideal para refinar prompts ou complementar parâmetros |
| Chat de voz em tempo real | **Esvazie a caixa de entrada** e clique no ícone de onda sonora (Start voice chat) | Conversação bidirecional em tempo real; ideal para organizar ideias ou fazer um handoff rápido |

### Passo a Passo para Ativação e Dicas Importantes

1. Abra a conversa com um Bot individual.
2. **A caixa de texto deve ser completamente esvaziada**; espaços residuais ou rascunhos ocultarão o ícone de onda sonora.
3. Clique no ícone de onda sonora; no primeiro uso, conceda a permissão de acesso ao microfone.
4. A tela exibirá Connecting… (no celular, Calling…); assim que o Bot começar a falar, a conexão estará estabelecida.

### Controles e Limitações Rígidas

- Durante a chamada, é possível silenciar o microfone, visualizar legendas em rolagem contínua e ajustar a velocidade e o timbre da voz; se mudar de tela para consultar documentos, clique em "Voltar para o chat de voz" na barra superior para retornar.
- **Suporte exclusivo para conversas individuais (1 a 1)**; não é possível iniciar em grupos, chats com múltiplos Bots ou "Bots de equipe".
- **Apenas uma chamada ativa por vez**; ao alternar para um novo Bot, confirme em "Encerrar e conversar".
- Após desligar, um card de Voice chat é gerado automaticamente registrando a duração total; clique nele para consultar a transcrição completa e prossiga com as tarefas seguintes pelo fluxo de texto.

## Padrões Comuns de Erro vs. Otimizações Recomendadas

1. **Delimitação de caminho**: sem definir o escopo e os métodos, o Bot clicará desordenadamente no console e **poderá até modificar o código do ambiente de produção**.
```text
  幫我維護一下網站，看看有沒有什麼 Bug。
  ```
Corrija delimitando as páginas e as etapas de inspeção:
```text
  對站點清單（/workspace/sites.txt）中的三個靜態展示頁進行巡檢。
  用雲端瀏覽器打開每個頁面，檢查主控台是否有 404 或 500 報錯，檢查頂部導覽欄連結是否全部有效。
  將報錯資訊、對應頁面 URL 及當時的螢幕截圖寫入 /workspace/logs/err-20261014.md。
  全程僅做唯讀檢查，嚴禁點選任何帶有提交或刪除性質的表單按鈕。
  ```

2. **Limites de aprovação**: não conceda permissão irrestrita de envio externo; se a interpretação falhar, **ele poderá facilmente enviar mensagens incorretas a clientes importantes**.
```text
  讀取 Gmail 裡的未讀郵件，重要的直接幫我回一下。
  ```
Mantenha a aprovação humana em etapas críticas:
```text
  讀取 Gmail 中過去 12 小時的未讀郵件。
  僅篩選出發件人屬於我們現有企業客戶、且正文包含售後或諮詢訴求的郵件。
  根據產品常見問題手冊，為每封郵件起草回覆草稿並存入 Gmail 草稿箱。
  在當前對話中列出客戶名稱、郵件摘要與草稿正文，等待我的審批。未經我的明確確認，絕不點選發送。
  ```

3. **Separação de fatos**: não inclua vieses no prompt, **evitando que o Bot valide suposições e confunda uma pequena promoção com uma guerra de preços**.
```text
  去看看競品今天的動態，總結一下他們是不是要跟我們打價格戰。
  ```
Separe os dados objetivos das suposições:
```text
  訪問競品官網的公開定價頁與首頁橫幅，獲取他們當下的方案價格表。
  對照我們在 /workspace/competitor/last-month-price.json 中記錄的舊價格：
  1. 事實列：標出哪些 SKU 的標價發生了變動，變動金額是多少，附帶頁面截圖與訪問時間。
  2. 推測列：基於該降價是限時促銷還是永久調價，給出你的分析理由。
  兩部分內容必須分開分欄呈現，不得將分析推論當作已知事實。
  ```

4. **Proteção somente leitura**: se não indicar a tabela principal/secundária e os campos a preservar, **os dados originais poderão ser facilmente sobrescritos e corrompidos**.
```text
  （直接拖入三個 Excel 表格）把這幾個表整理一下。
  ```
Deixe explícito qual tabela é a referência e configure-a como somente leitura:
```text
  上傳的三個表格分別是 7 月、8 月和 9 月的銷售明細。
  以「訂單編號」為唯一主鍵進行資料去重合並：
  1. 欄位統一保留：訂單號、成交日期、客戶名稱、銷售代表、成交金額。
  2. 生成一份全新的 Q3_sales_summary.csv 文件，保存在當前工作區。
  3. 保持我上傳的原始 7、8、9 月表格內容與檔名完全不變。
  ```

5. **Missão única**: não acumule múltiplas tarefas em um único Bot; além de poluir a memória, **isso consumirá rapidamente sua cota semanal**.
```text
  你幫我寫一篇關於新產品的推文，順便把昨天的帳目算了，然後再幫我看看競品推特。
  ```
Divida em tarefas únicas com fluxos dedicados:
```text
  遵循一個 Bot 負責一項核心任務的原則。當前 Bot 僅承擔社媒文案起草職責：
  依據 /workspace/product/spec.md 中的新功能說明，為 X 平台起草三條不同風格的發表文案。
  要求突出效能提升資料，字數控制在 280 字元以內。
  帳目核算與競品調研交由對應的專用 Bot 負責，不要在此會話中處理。
  ```

## Casos Reais de Handoff em Negócios

### Inspeção Diária de Websites e Registro de Evidências
O webmaster yishan transformou os requisitos de inspeção diretamente em critérios de aceitação. O diretório de trabalho foi estritamente limitado a `/workspace/site-check/`, permitindo inspecionar apenas a página inicial, os artigos mais recentes e o formulário de inscrição, sendo terminantemente proibida a navegação indiscriminada (crawling).
- O relatório deve registrar links completos, carimbos de data/hora (timestamps) e capturas de tela do momento. **Erros visíveis diretamente contam como fatos; causas investigadas contam como suposições, devendo ser registradas separadamente.**
- Se encontrar logins expirados ou links quebrados, registre a pendência e pule imediatamente, sendo proibido insistir repetidamente. Para o procedimento detalhado, consulte [Como Usar o Grok Bot a Fundo em Uma Hora](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg).

### Central de Entrada e Roteamento de Demandas
一澤Eze configurou um Bot dedicado à caixa de entrada para gerenciar o Gmail, sem conceder acesso direto ao e-mail para os Bots downstream.
- Ao receber e-mails de feedback, ele os encaminha via chat privado para o "Bot de Feedback do Produto", e faturas para o "Bot de Gestão de Assinaturas".
- A comparação puramente numérica é delegada diretamente a scripts de linha de comando. **Sincronizar apenas dados incrementais com o Bot ajuda a economizar a cota semanal de uso.**
- Não conecte ferramentas de alta permissão em todos os lugares; usar um ponto de entrada dedicado para a triagem inicial é a abordagem mais segura.

  Para um resumo das experiências, consulte [10 Experiências Essenciais para Tornar seu Grok Bot Ainda Mais Útil](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc).

### Diagnóstico pelo Chief of Staff e Criação de Bots
CyrilXBT primeiro colocou um Bot Chief of Staff para ler o Notion e o Slack da equipe, mapeando as três tarefas que consumiam mais tempo, apresentavam maior repetição e geravam mais gargalos, avançando em três etapas:
1. O Bot Chief of Staff executa manualmente, com supervisão humana da qualidade das entregas.
2. Após a validação, consolida o fluxo como uma habilidade (skill) e cria um Bot exclusivo e independente.
3. Por fim, configura a execução automática programada.
**Etapas que envolvam envio, compras, publicação ou alteração em sistemas online devem reter rigorosamente a aprovação humana.
** Tutorial completo em [How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd).

## Armadilhas Comuns e Como Evitá-las

1. **Envie anexos com explicações**: ao enviar várias imagens ou mais de duas planilhas, **descreva sempre a finalidade**, caso contrário ele poderá inverter a relação principal/secundária.
2. **Grave regras de longo prazo na memória**: instruções avulsas são perdidas ao trocar de sessão; regras fundamentais devem ser **inseridas no campo Sobre/Responsabilidades dos Detalhes do Bot** ou salvas na memória.
3. **Evite a suspensão na integração local**: tarefas 100% em nuvem rodam mesmo com a tampa do notebook fechada, mas a integração com um computador local será interrompida se ele suspender; lembre-se de **verificar as configurações de energia e suspensão**.
4. **Compartilhe imagens entre Bots via caminho de arquivo**: a comunicação entre Bots em grupos suporta apenas texto simples; para enviar imagens, **salve-as no caminho compartilhado `/workspace/`** para que o outro Bot possa acessá-las.
5. **Se o botão de voz sumir, limpe o campo**: se restarem caracteres ou espaços na caixa de texto, o botão de onda sonora ficará oculto; **limpe totalmente a caixa de texto** para restaurá-lo.
6. **Para operações de alto risco, escolha Permitir uma vez**: ao enviar e-mails ou alterar/excluir dados, não escolha "Permitir sempre"; antes de o fluxo rodar de forma estável por semanas, **faça questão de escolher "Permitir uma vez"**.

## Como Fazer a Validação da Entrega

1. Acesse `/workspace/` ou o diretório especificado para inspecionar os arquivos, **confirmando que abrem normalmente e sem caracteres corrompidos**; não se baseie apenas no texto temporário da conversa.
2. Faça uma amostragem de 2 a 3 dados essenciais abrindo os links ou capturas de tela para evitar alucinações ou invenções do modelo.
3. Verifique os logs de execução para **confirmar que não houve envios de mensagens não autorizados, alterações de configuração ou sobrescrita de arquivos originais**.
4. Separe fatos de suposições: o conteúdo original da página deve ficar na seção de fatos, enquanto inferências e sugestões devem ficar nas observações; corrija imediatamente qualquer confusão.
5. Verifique a lista de anomalias: **ao encontrar páginas inativas ou campos faltantes, o motivo deve ser registrado e a tarefa deve ser concluída até o fim**, sem interromper a execução no primeiro erro.

## Leituras Recomendadas

- Documentação oficial: [Grok Bot](https://cursor.com/cn/docs/grok-bot)
- Documentação oficial: [Usando o Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Suporte oficial: [Guia de Operação do Grok Bot](https://cursor.com/cn/help/grok-bot/how-to)
- Suporte oficial: [Chat de Voz com o Bot](https://cursor.com/cn/help/grok-bot/voice-chat)
- Artigo da comunidade: [Como Usar o Grok Bot a Fundo em Uma Hora](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg)
- Artigo da comunidade: [10 Experiências Essenciais para Tornar seu Grok Bot Ainda Mais Útil](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)
- Artigo da comunidade: [How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

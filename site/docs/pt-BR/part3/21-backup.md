# Capítulo 21 Backup e Restauração: Sem Pânico Mesmo com a Redefinição do Computador

Após a redefinição do computador em nuvem, o ambiente é completamente apagado; digitar `apt-get` e `pip install` de memória facilita o esquecimento de dependências ou variáveis de ambiente, e a memória refinada do Bot não possui um botão de exportação. **A solução é dividir a recuperação de desastres em dois pipelines paralelos.**

1. **Serviços da máquina virtual**: Assumir o controle das dependências do sistema com um registro geral e scripts de restauração automatizados.
2. **Memória do agente**: Um gerenciador de memória dedicado grava personas, regras e fatos dinâmicos em Markdown, enviando-os para um repositório Git privado.

Depois de concluída a configuração, **mesmo que o sistema seja redefinido ou migrado, todos os serviços e memórias podem ser recuperados com o mínimo de intervenção manual**.


![Backup e Restauração: Sem Pânico Mesmo com a Redefinição do Computador](/info/21-backup.png)

## 21.1 Entendendo o Computador em Nuvem: Quais as Diferenças entre Atualização, Recuperação e Redefinição

![21.1 Entendendo o Computador em Nuvem: Quais as Diferenças entre Atualização, Recuperação e Redefinição](/info/21-backup-s1.png)

**Todos os Bots sob a mesma conta compartilham a mesma máquina virtual**, compartilhando o diretório `/workspace` e os processos do sistema. Ferramentas globais instaladas em uma máquina podem ser chamadas por outros Bots; mas se a máquina for redefinida, todos os ambientes de dependência falharão simultaneamente.

Consulte [《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

O cliente oferece opções de controle em **Settings** > **Computador** sob **Bot's Computador**. As diferenças entre as três são as seguintes:

| Operação | Mecanismo | Conteúdo retido | Conteúdo perdido |
| :--- | :--- | :--- | :--- |
| **Atualização (Update)** | Atualiza a imagem do ambiente. Dividida em duas categorias: atualização de software e atualização do computador | A atualização de software mantém tudo; a atualização do computador retém robôs, arquivos e informações de login | A atualização de software não perde nada; a atualização do computador remove aplicativos globais e pacotes de software |
| **Recover** | Cria uma nova máquina na imagem mais recente com base nos dados salvos, tentando primeiro conectar-se à máquina antiga para salvar os dados | Robôs, arquivos e informações de login salvos | Aplicativos globais e pacotes de software; se a máquina antiga não puder ser conectada, alterações não sincronizadas serão perdidas |
| **Reset** | Cria diretamente uma nova máquina com base nos dados salvos mais recentes, interrompendo o trabalho em execução | Robôs, arquivos e informações de login salvos | Aplicativos globais e pacotes de software; alterações não sincronizadas serão perdidas |

O histórico de conversas é armazenado na nuvem e não é afetado por redefinições de máquina ou exclusões acidentais de arquivos. No entanto, **pacotes de aplicativos instalados globalmente, `node_modules` e ambientes virtuais Python não são salvos oficialmente** e serão limpos em caso de atualização do computador, Recover ou Reset.

Para mais detalhes, consulte [《Computador do Grok Bot》](https://cursor.com/cn/help/grok-bot/computer-recovery).

Quando a máquina virtual travar ou responder de forma anormal, a solução de problemas deve seguir esta ordem:

1. Exibindo **Reconnecting** ou **Couldn't Reach Grok Bot's Computador**: trata-se de oscilação na rede; aguarde um momento e clique em **Retry**. Os arquivos não são perdidos durante a reconexão; **é estritamente proibido clicar em Reset neste estágio**.
2. Reinicie o cliente. Usuários de Mac devem selecionar **Quit** na barra de menu superior; apenas clicar no "X" vermelho da janela não funciona.
3. Verifique se há atualizações. Acesse **Settings** > **Computador**; se houver atualizações disponíveis, clique primeiro em **Atualizar**. Se for avisado de que o agente não está pausado, espere a tarefa atual terminar antes de clicar.
4. Tente recuperar. Se ainda assim não conectar ou a atualização travar e exibir **Recuperar Computador**, clique em **Recover**. Se for exibido **Update ainda em execução**, selecione **Keep waiting**.
5. Execute **Reset**. Clique em Reset apenas se as quatro etapas anteriores falharem. Se falhar, use **Retry Recover** ou **Retry Reset** para tentar novamente; se continuar gerando erros, entre em contato com o suporte oficial.
6. Lidando com alertas de disco.

   Ao receber **Computer is low on disk space** ou **Computer is critically low on disk space**, não delete arquivos manualmente. Clique em **Go to Disk Saver** na barra lateral para ver as soluções; o sistema não excluirá arquivos sem confirmação.

   Para mais detalhes, consulte [《Computador do Grok Bot》](https://cursor.com/cn/help/grok-bot/computer-recovery).

**O computador em nuvem é apenas um contêiner descartável**; não ajuste o ambiente manualmente. Todo o processo de configuração deve ser feito por scripts, e as configurações e o código-fonte próprio devem ser armazenados em um repositório Git privado externo.

## 21.2 Registro Geral de Serviços da VM e Pipeline de Restauração Automatizada

![21.2 Registro Geral de Serviços da VM e Pipeline de Restauração Automatizada](/info/21-backup-s2.png)

[《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

Como o computador em nuvem não fornece snapshots subjacentes, **tornar o processo de reconstrução um script de um clique é a solução de menor custo**.

### Registro Geral de Serviços e Backup contra Contaminação

Crie um diretório `vm-services/` no repositório privado para colocar a tabela `REGISTRY.md` legível por humanos e o `registry.json` para ser analisado por scripts automatizados.

O registro geral e os backups devem seguir algumas regras rígidas:
- Os campos de registro incluem o ID do serviço, o Bot responsável, o caminho do código, as dependências de instalação (apt/pip/Docker/cron), os comandos de inicialização/parada e verificação de integridade, e se a restauração é obrigatória.
- **Para credenciais, registre apenas caminhos absolutos locais (como `~/.env`), sendo estritamente proibido armazenar texto simples**; destaque separadamente etapas manuais, como escaneamento de QR code e OAuth.
- Scripts próprios devem ser salvos separadamente em `service-src/`, excluindo `venv/`, `node_modules/` e logs; **é obrigatório executar uma varredura com regex para detectar chaves antes do commit**.

### Pipeline de Restauração Automatizada

Escreva sub-scripts individuais para cada serviço em `vm-services/restore/`. **Os scripts devem garantir idempotência**, sem falhar por diretório existente ou conflito de portas se executados duas vezes consecutivas.

O ponto de entrada principal `restore-all.sh` executa as tarefas em série, seguindo a ordem de dependência:
1. **Dependências básicas**: Instalar ferramentas do sistema como `cron`, `ffmpeg` e `yt-dlp`.
2. **Posicionamento do código-fonte**: Copiar os scripts próprios de volta a partir de `service-src/`, pulando arquivos existentes e preenchendo apenas os que faltam.
3. **Ambiente e pacotes**: Criar um ambiente virtual Python e executar `pip install -r requirements.txt`.
4. **Iniciar daemons**: Inicializar processos residentes em segundo plano.
5. **Montar agendamentos**: Restaurar o agendamento unificado do crontab.
6. **Verificação de integridade**: Verificar item por item se estão ativos; **em caso de falha, registrar o log de erro e continuar para o próximo item**, sem travar ou interromper o fluxo.

[《Todas as ferramentas sumiram após a redefinição da máquina virtual do Grok Bot? Tutorial de backup e restauração (com prompts inclusos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.3 Gerenciador de Memória: Guardando a Memória Central do Bot em um Repositório Privado

![21.3 Gerenciador de Memória: Guardando a Memória Central do Bot em um Repositório Privado](/info/21-backup-s3.png)

Não há um botão oficial para exportação completa de memória, tornando muito fácil perder preferências ao trocar de conta ou migrar de sistema. **Estabelecer um Bot dedicado como "Gerenciador de Memória" para transformar memórias intangíveis em snapshots de texto puro em um repositório Git privado é o caminho mais seguro.**

[《A Grande Evacuação do Grok Bot: Um Plano Completo de Backup para Sistemas de Agentes》](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Camadas de Memória e Princípios de Manutenção

| Camada | Conteúdo incluído | Descrição e permissões |
|---|---|---|
| **Camada compartilhada** | Memória compartilhada da conta, Skills públicas e configurações de plugins | Acessível para leitura por todos os Bots |
| **Camada exclusiva** | Contratos de regras de Description, memórias independentes exclusivas e tarefas Routine | Exclusivo para um único Bot |

- Fatos dinâmicos não devem ser acumulados no contexto a longo prazo; registre apenas o método de acesso e busque na fonte original quando necessário.
- Memórias compartilhadas devem passar por revisão humana ou validação por fluxo de trabalho padronizado para evitar contaminação cruzada.
- **Definições de negócios devem ser escritas na memória, enquanto processos operacionais fixos devem ser consolidados no código de Skills.**

[《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Especificação de Arquivamento e Fluxo de Trabalho

::: details Especificação de arquivamento e fluxo de trabalho
```text
├── bots/                     # 各 Bot 獨立組態與記憶
│   ├── cyber-xiaowan/        # 單個 Bot 資料夾
│   │   ├── agent-spec.md     # 身份設定、名稱、bot-id、slug、description
│   │   ├── MEMORY.md         # 核心記憶全量快照
│   │   ├── profile.md        # 角色資訊與權限邊界
│   │   └── archive/          # 歷史版本與過往記錄
│   └── ...                   # 其他 Bot 目錄
├── meta/                     # 全域Metadata與多 Bot 拓撲關係
├── shared-user-memory/       # 帳號級共享記憶
├── vm-services/              # 虛擬機器服務總帳與恢復指令碼（見 21.2 節）
├── README.md                 # 倉庫使用說明與最新狀態
├── RESTORE.md                # 跨環境恢復操作 SOP
└── registry.md               # 登記索引
```
:::

O `MEMORY.md` no diretório de cada Bot individual contém três camadas: permissões de identidade, responsabilidades de decisão e snapshot da cena atual.

1. **Enumerar a lista**: Delimitar os Bots principais que precisam de backup persistente.
2. **Agendar e despachar instruções**: Cada Bot lê suas próprias configurações e memórias e, após sintetizá-las, grava-as nos arquivos Markdown correspondentes em `/workspace`.
3. **Coletar, validar e armazenar**: **Fazer o commit unificado após escanear e confirmar que não há Tokens em texto simples**, aplicar uma tag de data (como `tag-2026-10-15`) e enviar (push) para o repositório privado remoto.

**O Bot é responsável pelos snapshots completos, enquanto o Git cuida do rastreamento incremental**. O Bot simplesmente sobrescreve o arquivo por completo a cada vez, deixando as alterações históricas sob responsabilidade do mecanismo do Git, sem a necessidade de calcular diferenças no prompt.

## 21.4 Estudo de Caso Prático: A Grande Evacuação e o Gerenciador de Serviços de 鐵柱AGI

### Backup com o Gerenciador de Memória

鐵柱AGI (@cgnot996) mantém 21 Bots sob sua gestão. Para evitar a perda de memória em caso de banimento da conta, ele configurou um Bot "Gerenciador de Memória", combinado a um repositório privado no Gitee para arquivamento.

1. **Delimitar os principais**: Dos 21 Bots, 7 principais foram selecionados inicialmente para testes.
2. **Exportação e conferência**: Notificar os 7 Bots para exportar configurações e memórias. **Alguns Bots ficam em silêncio após a exportação; a instrução deve exigir "reportar após a conclusão", enquanto o gerenciador verifica varrendo o diretório `/workspace`**.
3. **Armazenamento e tagueamento**: O primeiro lote de 73 KB foi arquivado no repositório, marcado com a tag `tag 2026-09-10` e aprovado na varredura de chaves.
4. **Estrutura de arquivo único**: Como no "Cyber Xiaowan", o `MEMORY.md` (cerca de 21 KB) armazena identidade e snapshots, e o `agent-spec.md` armazena o bot-id e a descrição.
5. **Ativar agendamento**: Configurar para arquivamento automático periódico.

Ao importar para uma nova conta, a taxa de restauração da memória é de cerca de 80%. **Arquivos locais sem backup, histórico de conversas e estados de login de terceiros não podem ser restaurados**.

Ao migrar para Hermes ou OpenClaw, basta colocar o `MEMORY.md` no diretório de memória e alterar a description do `agent-spec.md` para o prompt do sistema para que funcione.

[《A Grande Evacuação do Grok Bot: Um Plano Completo de Backup para Sistemas de Agentes》](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Gerenciador de Serviços da Máquina Virtual

O travamento e a consequente redefinição do computador em nuvem resultam na perda total das ferramentas. O autor registrou o ledger geral de reconstrução no diretório `vm-services` do repositório `grok-bot-memory` no Gitee.

1. **Registro no ledger**: Até 10/10/2026, foram registrados 20 itens de 10 Bots (4 residentes/daemons, 14 ferramentas sob demanda e 2 itens de chaves), dos quais 18 foram marcados como "restauração obrigatória".
2. **Classificação dos serviços**: Os serviços residentes incluem serviços de scraping, encapsulamento de API do Muse, além de motor de e-mail e túnel de saída; ferramentas sob demanda (ffmpeg, Chrome, etc.) registram apenas o comando de instalação; Metaso e TikHub registram apenas os caminhos das chaves.
3. **Backup limpo do código-fonte**: Cerca de 5,1 MB de código-fonte próprio, excluindo chaves, logs e fluxos de estado.
4. **Restauração encadeada**: O gerenciador mantém o diretório `restore/` e o `restore-all.sh`. **Em condições normais, o gerenciador não executa nada por conta própria; ele aguarda instruções humanas para iniciar os serviços de acordo com as dependências e entrega uma lista de verificação de aceitação**.

[《Todas as ferramentas sumiram após a redefinição da máquina virtual do Grok Bot? Tutorial de backup e restauração (com prompts inclusos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.5 Segurança de Credenciais e Ponto de Controle de Aprovação Humana: Entregue a Tela, Não a Senha

**Vários Bots compartilham o disco e as sessões de navegador da máquina virtual; criar novos Bots não isola dados confidenciais de forma alguma.** Se algo for escrito em texto simples em scripts ou conversas, outros Bots ou logs externos poderão lê-lo.

[《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Credenciais: Mantenha Apenas Caminhos, Nunca Texto Simples

- Tokens e chaves privadas são armazenados no `~/.env` (ignorado pelo Git) ou em um diretório global de chaves.
- No `REGISTRY.md`, no `registry.json` e nos arquivos de memória, **sempre que houver credenciais envolvidas, registre apenas o caminho absoluto no disco**.
- É estritamente proibido enviar senhas na caixa de diálogo; antes de fazer o push, é obrigatório executar uma varredura com regex para sanitização.

### Entregue a Tela, Não a Senha

1. Se o Bot encontrar pop-ups de 2FA, escaneamento de QR code ou verificação de dispositivo, ele pausará imediatamente e notificará você para assumir o controle.
2. Você abre o computador em nuvem em tela cheia no cliente e digita a senha ou escaneia o QR code você mesmo.
3. Uma vez concluído, devolva o controle; **o Bot herda os cookies da sessão e continua em execução, sem jamais tocar na senha em texto simples**.

### Configurar Ask-first para Operações de Alto Risco

- Operações irreversíveis, como postar, efetuar pagamentos, excluir dados ou alterar o ambiente subjacente, devem abrir um pop-up e aguardar aprovação humana. A versão v0.70.2 otimizou essa lógica de confirmação.
- **A autoridade autônoma do Bot limita-se a leitura, busca pública e leitura/escrita interna no `/workspace`**; em caso de conflito de regras, o Ask-first tem prioridade.

## 21.6 Três Conjuntos de Prompts Prontos para Uso

Abaixo estão três conjuntos de prompts comprovados na prática; basta copiá-los e enviá-los ao Bot correspondente para implantar e usar.

### Prompt 1: Configurar o "Gerenciador de Serviços da Máquina Virtual" para o Computador em Nuvem

Crie um Bot "Gerenciador de Serviços da Máquina Virtual" e **cole nas configurações**:

::: details Prompt 1: Configurar o "Gerenciador de Serviços da Máquina Virtual" para o computador em nuvem
```text
你是「虛擬機器服務管家」，只管一件事：記下這台虛擬機器上部署過的所有第三方服務，並在電腦更新或換帳號之後，按記錄把它們原樣恢復。

你維護的東西
1. 一份登記總帳，人和機器各讀一份：REGISTRY.md（表格）和 registry.json（給指令碼讀）。
2. 每個服務一個恢復指令碼 restore/restore-<服務>.sh，必須冪等，重複跑也不會出錯。
3. 一個總入口 restore/restore-all.sh，按依賴順序呼叫各個恢復指令碼，最後彙總哪些失敗了。
4. 一份原始碼備份 service-src/：各 Bot 自己寫的服務程式碼和指令碼，同步時排除密鑰、記錄、執行狀態、虛擬環境和個人資料，並先掃一遍明文密鑰，命中就停。
5. 以上全部跟著一個私有 Git 倉庫存（「你的備份倉庫地址」）。總帳、恢復指令碼、原始碼都在倉庫裡，密鑰永遠不進倉庫。

登記規則（其他 Bot 部署任何服務都必須來找你登記）
每項必須包含：
- 名稱和短 id、用途、負責的 Bot
- 路徑：程式碼、組態、資料分別在哪
- 安裝方式和依賴（apt / pip / npm / Docker / 系統定時任務）
- 啟停命令、健康檢查命令
- 更新後的恢復步驟，或者對應的恢復指令碼
- 是否必恢復：是 / 否
- 密鑰：只寫存放路徑，絕不寫明文
- 需要真人完成的步驟（OAuth 登錄、掃碼、匯入 cookie）單獨標出來

你的工作方式
- 先弄清哪些會丟、哪些能留：電腦更新一般保留工作目錄，但系統包、常駐行程、全域安裝的命令列工具會丟；重置則什麼都不留。所以要記的是“怎麼重建”，不是去拷整台機器。
- 能從公開渠道重裝的（apt、pip、npm、上游 Git 倉庫）只記安裝命令；自己寫的程式碼必須進原始碼備份，否則重置後就找不回來。
- 收到登記先核對：路徑是否真實存在、健康檢查能不能過。登記寫的和實際不一樣時，以實際為準，並告訴負責的 Bot。
- 多個定時任務合併成一份 crontab 真源時，檢查每一條是不是都在真源裡，不在的要靠恢復指令碼補回去。
- 故意停掉的服務要寫清楚“為什麼停、什麼條件下重開”，免得被當成漏裝。
- 只有主人說“電腦更新完了”才跑總恢復，不盲跑。跑完交驗收：每項是成功、失敗，還是要真人處理。
- 每次有服務新增、刪除或原始碼大改，先重新同步原始碼備份，再把總帳、指令碼、原始碼一起提交推送到備份倉庫。換帳號或重置時，就靠這份備份把整套設定帶走。
- 刪掉的服務要徹底清除：總帳只反映現在真實的狀態。
```
:::

### Prompt 2: Fazer o Bot Executar uma Restauração Completa Após a Redefinição do Computador

Configure o **token de acesso Git**, substitua o conteúdo entre parênteses e envie ao Bot.

::: details Prompt 2: Fazer o Bot executar uma restauração completa após a redefinição do computador
```text
這台電腦剛重置過（或者是換了新帳號），之前部署的服務都沒了。請按我的備份把它們恢復到可用狀態，規則如下。

備份在哪
- 備份倉庫：<你的備份倉庫地址>，分支 <分支名>
- 倉庫裡有：登記總帳（REGISTRY.md 和 registry.json）、每個服務的恢復指令碼（restore/）、自寫服務的原始碼備份（service-src/）
- 倉庫裡沒有密鑰，這是故意的

請按這個順序做
1. 把備份倉庫拉到工作目錄，先讀總帳，告訴我一共登記了幾項、哪些標了「必恢復」、哪些只留密鑰不用恢復。先列出來，不要動手。
2. 把自寫服務的原始碼從 service-src/ 放回總帳寫的原位置。只補缺失的，已經存在的目錄不要覆蓋。
3. 按總帳的依賴順序逐項恢復：先裝系統依賴（比如 cron、ffmpeg），再裝命令列工具，最後拉起常駐服務和定時任務。每項都用它自己的恢復指令碼，指令碼要能重複跑。
4. 每裝完一項就跑它登記的健康檢查。失敗了先看記錄、試著修一次；修不好就記下原因，接著做下一項，不要卡住。
5. 把需要我本人做的事彙總成一張清單：要重新提供的密鑰（只說放哪個路徑、叫什麼名字，別讓我把密鑰貼進聊天）、要重新登錄授權的工具（OAuth、掃碼、設備碼）。然後一項一項帶我做，每做完一項馬上覆查。
6. 故意暫停的任務保持暫停，總帳裡寫了原因和重開條件的照辦。別因為“看起來漏裝了”就自作主張打開。
7. 最後交驗收清單，每項一行：服務名、結果（成功 / 失敗 / 等我處理）、健康檢查輸出摘要、花了多久。再告訴我總共用了多少時間、成功了幾項。

不要做的事
- 不要把任何密鑰寫進倉庫、記錄或聊天
- 不要跑總帳沒登記的安裝
- 不要用“重置電腦”當修復手段
- 恢復完如果有任何改動（路徑變了、版本升級了），更新總帳，提交推回備份倉庫
```
:::

### Prompt 3: Instrução de Arquivamento Periódico para o Gerenciador de Memória

**Envie isto para Routine ou arquivamento manual:**

::: details Prompt 3: Instrução de arquivamento periódico para o Gerenciador de Memória
```text
請開始執行本週的智慧體記憶與設定歸檔任務。

執行步驟：
1. 枚舉當前工作區內所有處於活躍狀態的 Bot 名單，核對 bots/ 目錄下的已有目錄。
2. 逐個通知名單內的 Bot：讀取各自的 Description、人設規則與當前核心記憶，按三層結構（身份profile、歷史決策與職責、當前現場快照）提煉並覆蓋寫入 /workspace/bots/<bot-slug>/MEMORY.md。同時將身份Metadata更新至 agent-spec.md。
3. 檢查各 Bot 回執，並在 /workspace 目錄核對文件生成情況，確保所有目標 Bot 的 Markdown 均已寫出。
4. 提取帳號級共享記憶，更新至 shared-user-memory/ 目錄下的 Markdown 文件中。
5. 對本次生成的所有 Markdown 文件進行敏感資訊正則掃描，檢查是否存在明文 API Token、密碼或私鑰。如果發現疑似憑證，立即中斷並報警。
6. 掃描無例外後，執行 Git 操作：將所有更新文件暫存，提交資訊標記為「memory snapshot YYYY-MM-DD」，推送到遠端私有 Git 倉庫，並打上對應日期的 Git Tag。
7. 完成後向我彙報：本次歸檔了哪幾個 Bot、總文件大小、是否有失敗或超時的 Bot。
```
:::

## 21.7 Armadilhas Comuns

1. Quando exibir Reconnecting, **não clique em Reset**; trata-se apenas de oscilação na rede ou manutenção, e clicar nisso sobrescreverá dados não salvos com um snapshot antigo.
2. Compartilhar a autorização do Codex em vários dispositivos fará com que eles desconectem uns aos outros; configure subcontas independentes ou credenciais fixas.
3. Tarefas agendadas devem ser centralizadas em um arquivo de configuração do crontab e adicionadas ao Git para evitar omissões na redefinição da máquina.
4. O ledger geral de serviços deve se basear em comandos práticos reais; se o Docker não estiver instalado no ambiente, o script de restauração poderá travar.
5. Os Bots frequentemente realizam exportações silenciosamente; o gerenciador deve verificar ativamente o disco, e as instruções devem impor estritamente: "é obrigatório reportar após escrever".
6. **O repositório de backup deve ser configurado como privado e incluir varredura com regex** para evitar que Tokens sejam enviados a repositórios públicos via git push.

## 21.8 Como Fazer a Validação e Aceitação

### Serviços e Scripts
1. Reconciliação: Compare com `vm-services/REGISTRY.md`, use `ps aux` para verificar processos, e `netstat` ou `ss` para verificar portas; **os caminhos não devem ser registrados a mais nem omitidos**.
2. Teste inicial: Execute individualmente `restore-<服務名>.sh`, observando se pode ser executado repetidamente sem erros.
3. Ensaio completo: Faça um clone em um diretório temporário e execute `bash restore/restore-all.sh`, **garantindo que todos os itens de "restauração obrigatória" sejam aprovados** e que as etapas que exigem intervenção humana estejam listadas.

### Repositório e Memória
1. Verificar a estrutura: Acesse `bots/` na interface web; cada Bot deve ter arquivos `agent-spec.md` e `MEMORY.md` independentes.
2. Amostragem: Abra o `MEMORY.md` e confirme se as três camadas ("profile de identidade", "decisões históricas e responsabilidades" e "snapshot da cena atual") estão completas, sem modelos vazios ou caracteres corrompidos.
3. Busca por segredos: Faça uma busca global por `sk-`, `Bearer` ou `password`; **mantenha apenas caminhos absolutos locais para credenciais, sendo estritamente proibidos Tokens em texto simples**.

## Leituras Complementares

- Guias de uso oficiais e páginas de suporte:
  - [《Computador do Grok Bot》](https://cursor.com/cn/help/grok-bot/computer-recovery)
  - [《Armazenamento Seguro de Informações Confidenciais》](https://cursor.com/cn/help/grok-bot/secrets)
  - [《Obter Ajuda》](https://cursor.com/cn/help/grok-bot/get-help)
  - [《Guia de Uso do Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to)
- Artigos de referência prática da comunidade:
  - 鐵柱AGI @cgnot996: [《Todas as ferramentas sumiram após a redefinição da máquina virtual do Grok Bot? Tutorial de backup e restauração (com prompts inclusos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)
  - 鐵柱AGI @cgnot996: [《A Grande Evacuação do Grok Bot: Um Plano Completo de Backup para Sistemas de Agentes》](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)
  - Organização integrada da base de conhecimento: [《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

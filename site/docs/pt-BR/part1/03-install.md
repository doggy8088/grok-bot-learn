# Capítulo 3: Instalação, Login e o Primeiro Bot

**Confirme se a assinatura inclui os benefícios do Bot**, caso contrário não haverá ponto de entrada; se o login entrar em loop, verifique as configurações de privacidade. Não crie um "assistente para tudo" sem restrições para não desperdiçar sua cota semanal à toa.

1. Instale o cliente desktop e o aplicativo móvel, eliminando erros de login
2. **Crie um Bot dedicado preenchendo o contrato de seis linhas**
3. Envie a primeira tarefa com salvamento em disco e faça a validação com base na lista de verificação


![Instalação, login e o primeiro Bot](/info/03-install.png)

## Verificação do Plano de Assinatura e Condições de Acesso

Antes de fazer o download, verifique a qualificação da sua conta: **o Grok Bot só pode ser usado com uma assinatura válida vinculada**.

| Nome do Plano | Preço | Inclui Grok Bot | Descrição da Cota |
| :--- | :--- | :--- | :--- |
| The X Plus | $8 / mês | Não | Apenas conversas com modelos comuns, sem acesso ao Bot |
| The X Premium | $30 / mês ($300 anual) | Sim | Cota de 4x, limite mínimo de entrada para uso individual |
| The X Super | $100 / mês ($1000 anual) | Sim | Cota de 15x |
| The X Ultra | $200 / mês ($2000 anual) | Sim | Cota de 50x |
| Cursor Pro / Pro+ / Ultra | Consulte os preços no site oficial | Sim | Cota semanal de acordo com o plano |
| Cursor Teams (assentos self-service) | Consulte os preços no site oficial | Sim | Membros compartilham a cota da equipe |

- **O plano Plus de $8 mensais não inclui os recursos do Bot**; comprar esse plano não dará acesso ao serviço.
- **A cota vinculada ao X e a cota da assinatura do Cursor não são cumulativas**; o faturamento do sistema adota automaticamente o limite mais alto entre os dois para o uso semanal.

Para entender os mecanismos básicos dos planos, consulte os artigos da comunidade [1.1 O que é o Grok Bot: Entenda em uma página](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc) e [Guia Extenso | Começando com o Grok Bot do Zero pela Primeira Vez](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg).

## Download e Instalação no Desktop

![Download e instalação no desktop](/info/03-install-s2.png)

O macOS é compatível com Apple Silicon (série M) e Intel; Windows e Linux são compatíveis com x64 e Arm64 (no Windows, recomenda-se ativar a aceleração de hardware).

1. Acesse `cursor.com/dashboard/bot` ou vá diretamente para `x.ai/bot` para baixar o instalador. **Se não tiver permissão no dispositivo da empresa, solicite ao administrador**.
2. No macOS, arraste o aplicativo baixado para a pasta `Applications`; no Windows e Linux, execute o assistente de instalação.
3. **Ao abrir o cliente e ver a tela de login, está pronto**. Para instruções detalhadas, consulte o documento [Início Rápido do Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started).

## Login na Conta e Configuração do Modo de Privacidade

1. Abra o cliente e clique em **Log In** (Entrar), autenticando-se no navegador diretamente com sua conta do Cursor; o SSO corporativo será aplicado automaticamente. Se você tiver um assento Grok Business, selecione **Sign in with Grok** para fazer login.
2. Concluída a autenticação, acesse as "Configurações" do cliente; se você conseguir ver o e-mail da conta e o status do plano, significa que deu certo.

**O modo de privacidade legado (Privacy Mode (Legacy)) precisa ser alternado para o Privacy Mode atual para continuar**. Usuários individuais só precisam confirmar na janela pop-up; membros de equipes precisam que o administrador faça a atualização em Team Settings.

Para explicações detalhadas, consulte os documentos oficiais [Introdução](https://cursor.com/cn/help/grok-bot/onboarding) e [Fazer Login no Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in).

## Problemas Comuns de Login e Resolução de Falhas

Reinstalar sem critério não resolve; a maioria dos casos decorre de problemas de cache ou de atualização de sessão.

1. Atualize o cliente para a versão mais recente e faça login novamente.
2. Limpe os cookies de `cursor.com` e `x.ai` ou use o modo anônimo.
3. Acesse `x.ai/bot` para confirmar se a versão web consegue estabelecer uma sessão.
4. Se acabou de alterar a assinatura, **aguarde de 30 a 60 minutos**; o erro desaparecerá após a atualização.

Erros consecutivos na verificação por telefone acionarão o bloqueio de controle de risco, o qual não se resolve sozinho. Se a resolução de problemas falhar ou você encontrar erros de OAuth, **abra um chamado na página de suporte**, anexando seu e-mail e capturas de tela, além de detalhar a versão e as etapas seguidas.

Para mais detalhes, consulte [Fazer Login no Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in).

## Instalação no iOS e Sincronização entre Dispositivos

### Instalação e Login
1. O sistema operacional deve ser o **iOS 18 ou superior**.
2. Pesquise por Grok Bot na App Store e instale. Faça login com a mesma conta do Cursor para sincronizar automaticamente, **sem necessidade de pagar novamente**.

### Divisão de Trabalho entre Dispositivos
- O celular é ideal para monitoramento rotineiro: permite visualizar a tela em tempo real, assumir o controle (Take over) para inserir códigos de verificação, conceder aprovações (Allow / Deny) ou iniciar e parar Routines.
- **Operações aprofundadas precisam ser feitas no desktop**: tutoriais em gravação de tela de até 10 minutos (Teach a task), testes de Routine (Test run) e manutenção do computador na nuvem (Update / Recover).

### Gerenciamento de Notificações
- **Silenciar um Bot específico**: na tela de chat, clique no nome no topo e desative **Notifications**; também é possível desativar enviando uma mensagem pelo desktop.
- **Desativação global**: desative a permissão de notificações do Grok Bot nos "Ajustes" do sistema.

Para mais detalhes, consulte [Grok Bot para Dispositivos Móveis](https://cursor.com/cn/help/grok-bot/mobile).

## Conhecendo a Infraestrutura Compartilhada e Criando o Primeiro Bot

![Conhecendo a infraestrutura compartilhada e criando o primeiro Bot](/info/03-install-s6.png)

Cada usuário pagante tem uma máquina virtual dedicada e persistente na nuvem, equipada com Linux independente, navegador, terminal e disco persistente (a configuração de testes iniciais era de cerca de 8 núcleos e 16 GB de RAM, não confirmada oficialmente; consulte as informações oficiais para dados exatos).

Esta máquina tem três limites físicos que impactam diretamente a operação:
- **Todos os Bots compartilham a mesma máquina**: compartilham o `/workspace` e a mesma sessão ativa do navegador; criar Bots separados serve apenas para dividir funções, sem isolamento de segurança.
- **A colaboração entre Bots exige gravação de arquivos em disco**: os históricos de chat não se comunicam entre si; o Bot A precisa gravar os resultados em arquivos no `/workspace` para que o Bot B possa lê-los e continuar a tarefa.
- **Suporte para visualização a qualquer momento e intervenção em tempo real**: o lado direito pode expandir a tela do computador na nuvem para que você assuma o controle sempre que houver senhas, captchas ou autenticações de pagamento; nunca digite credenciais na caixa de texto.

No primeiro login, um **Grok Bot** padrão será gerado automaticamente. As etapas para criar e configurar manualmente são as seguintes:

1. **Criar novo**: clique no **+** no topo da barra lateral (ou Cmd+N) e selecione **Create new Bot** (Criar novo Bot). Digitar o nome diretamente no campo de texto também permite clicar e criar.
2. **Renomear e definir etiqueta**: clique com o botão direito e selecione **Rename Bot** (Renomear robô), ou clique no nome no topo para abrir o painel e alterar. Abaixo, é possível configurar a etiqueta de cargo (Label; no celular, Title (optional)).
3. **Alterar o avatar**: clique no nome no topo para acessar os detalhes e clique no avatar; é possível escolher figuras geométricas integradas, gerar uma imagem por meio de uma descrição em texto ou enviar uma imagem local de até 25 MB (no celular, é possível escolher fotos da biblioteca, gerar ou remover).
4. **Definir atribuições**: **os Bots individuais não contam mais com uma página de configurações própria; as regras de longo prazo devem ser explicadas diretamente na primeira mensagem, solicitando que ele as memorize**. Os Bots de equipe ainda mantêm uma área fixa de descrição na seção "Sobre" (About) dos detalhes.

- [Alterar Nome, Avatar e Responsabilidades do Bot](https://cursor.com/cn/help/grok-bot/edit-bot)
- [Artigo Completo | Grok Bot do Iniciante ao Avançado | Jin Chenma](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)

## Definindo Responsabilidades: O Contrato Padrão de Seis Linhas

### Estrutura do Contrato e Modelo

Iniciantes não devem fornecer títulos vagos: **escreva as seis restrições centrais diretamente na primeira mensagem**, instruindo-o a memorizá-las como regras permanentes.

1. Own (Responsabilidade por resultados): defina claramente os indicadores específicos sob sua responsabilidade a longo prazo, evitando transformá-lo em um assistente genérico.
2. Sources (Fontes confiáveis): restrinja a consulta exclusivamente a sites oficiais ou links especificados, proibindo o uso de fontes não verificadas.
3. Output (Formato de entrega): determine o caminho de salvamento, regras de nomenclatura e limite de palavras do resumo.
4. Approval (Linha vermelha de aprovação): ações de alto risco, como envio de e-mails, submissão de formulários ou exclusão de arquivos, devem aguardar a aprovação humana via pop-up.
5. Failure (Tratamento de exceções): ao encontrar páginas fora do ar ou dados ausentes, deve registrar isso explicitamente, sendo estritamente proibido supor ou inventar informações.
6. Never (Restrições absolutas): proibido modificar arquivos de origem, proibido resumir com base em memórias do próprio treinamento e proibido clicar em botões de pagamento.

Após nomear o Bot, substitua os campos do modelo e envie diretamente.

::: details Estrutura do contrato e modelo
```text
請牢記你的長期工作職責，在今後的工作中始終遵循以下要求：

Own: 負責監控目標清單的每週功能與定價變動，輸出結構化對比材料。
Sources: 僅限使用目標官方網站的定價頁、Changelog 頁面以及我通過附件提供的官方說明文件。
Output: 提煉核心動態，附帶核對日期與原始出處連結，長文本與資料表格必須保存至 /workspace/research/ 下的 Markdown 文件中，對話框中只發簡要完成彙報。
Approval: 涉及發送任何郵件、對外發文、提交表單、刪除文件或進行任何費用支付前，必須停下來等待我的人工批准。
Failure: 若目標頁面無法訪問或內容缺失，在報告中明確標註為“未取得一手資料”，嚴禁推測或編造任何功能與價格。
Never: 嚴禁修改我上傳的任何源文件，在源系統可訪問時嚴禁依賴自身訓練記憶進行主觀概括。

今後的工作中請記住這些要求。
```
:::

### Casos Práticos

- Jin Chenma, em [Artigo Completo | Grok Bot do Iniciante ao Avançado | Jin Chenma](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee), **separa rigorosamente as responsabilidades de longo prazo das demandas pontuais**.

  As regras permanentes controlam fontes e entregas, enquanto as mensagens da sessão apenas atribuem tópicos específicos de pesquisa; caso faltem dados primários, isso é declarado diretamente, sendo estritamente proibido tentar adivinhar números.
- Today, em [Guia Extenso | Começando com o Grok Bot do Zero pela Primeira Vez](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg), estabeleceu limites de segurança, **isolando operações somente leitura daquelas com consequências externas**.

  Pesquisa apenas um concorrente por vez, anexando links de fontes públicas e distinguindo com clareza fatos de suposições; qualquer ação que envolva login ou pagamento é pausada aguardando confirmação.

Para regras de evolução, consulte [1.1 O que é o Grok Bot: Entenda em uma página](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc).

## Enviando a Primeira Tarefa Real

![Enviando a primeira tarefa real](/info/03-install-s8.png)

**Comece com tarefas pequenas**. Ao elaborar uma tarefa, lembre-se dos 5 elementos essenciais: explique claramente o objetivo e as entradas, mantenha estritamente como somente leitura (proibido alterar arquivos-fonte, registrar contas e efetuar pagamentos), defina as especificações de salvamento em disco e indique os pontos de intervenção manual.

Para o resumo de anexos, envie:
```text
用五個要點總結這份文件。
在單獨的部分列出每個日期、決策和未解決的問題，併為每項註明對應章節出處。
不要更改源文件。
```

Para pesquisar preços de concorrentes e salvar em disco, envie:
::: details Enviando a primeira tarefa real
```text
【目標】
調研 3 款主流程式碼編輯器（Cursor、VS Code、Zed）在 2026 年的最新公開定價方案與核心 AI 功能，產出一份選型對比參考材料。

【材料】
1. 僅限使用上述三款產品官方網站的定價頁、功能介紹頁與官方文件；第三方部落格僅作為輔助索引，必須找到官方頁面核實。
2. 記錄每一項資料的原始官方 URL 與資料核對日期。

【邊界】
1. 純唯讀檢索，嚴禁註冊任何帳號，嚴禁開啟任何試用，嚴禁輸入任何支付資訊。
2. 遇到需要登錄才能查看的頁面，直接跳過並記錄在未核實清單中。
3. 嚴禁改動 /workspace 下已有的其他項目文件。

【交付規格】
1. 在 /workspace/editor-research/ 目錄下生成對比報告文件 comparison.md。
2. 報告內包含一張 Markdown 資料表格，表頭列定義為：產品名稱、方案檔位、月付價格、年付價格、核心功能特徵、官網來源連結、核對日期。
3. 表格下方附帶一份 400 字以內的中文總結，指出各產品主要差異，並單獨開闢一節列出“未核實或存在矛盾的資訊”。
4. 對話框中僅需回覆已完成落盤的簡短提示及文件絕對路徑。

【暫停確認節點】
1. 遇到必須登錄、驗證碼攔截或點選付費的操作時，立刻停下並提示我接管。
2. 官網資訊前後出現明顯矛盾且無法核實時，停下說明情況由我判斷。
```
:::

Ao encontrar logins, 2FA ou captchas deslizantes:
1. **Clique em Take over para resolver manualmente**; após concluir, clique em I'm done para continuar, ou em Skip para ignorar.
2. Após a execução, **confirme se `/workspace/editor-research/comparison.md` foi salvo integralmente**.

Para diretrizes, consulte [Como Usar o Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started) e [Primeiros Passos](https://cursor.com/cn/help/grok-bot/onboarding).

## Armadilhas Comuns

1. O plano Plus de $8 não inclui o Bot; **é obrigatório escolher o plano Premium de $30/mês**.
2. Todos os Bots compartilham o computador na nuvem e a cota; faça um funcionar primeiro antes de criar dezenas que entrem em conflito entre si.
3. Nunca envie senhas ou API Keys na janela de chat; utilize o Take over para assumir a digitação ou preencha os cartões de segurança.
4. Textos longos **devem ser sempre salvos em arquivos Markdown no `/workspace`**, evitando poluir o contexto.
5. Se houver erro de login, não reinstale: limpe os cookies de `cursor.com` e `x.ai` ou aguarde de 30 a 60 minutos.
6. **Diferentes Bots compartilham a máquina virtual e as sessões do navegador**, não havendo isolamento de permissões.
7. Teach a task, Test run e a recuperação do sistema são recursos exclusivos do cliente desktop, não estando disponíveis no iOS.

## Como Fazer a Validação Final

1. Acesse Usage & Billing: o plano pago deve estar ativo e o consumo dentro da normalidade.
2. A tela do lado direito no desktop abre normalmente, sem erros de Reconnecting.
3. No iPhone (iOS 18+), acesse a mesma conta do Cursor: não deve haver solicitação para uma nova compra.
4. Envie o contrato de seis linhas: o Bot deve responder expressamente que memorizou as regras de longo prazo.
5. O computador na nuvem gera os arquivos solicitados no `/workspace` de acordo com as instruções.
6. Ao encontrar ações como login, o Bot pausa ativamente e exibe o cartão **Action needed**.
7. Ao fornecer intencionalmente links quebrados, o relatório indica claramente **Dados primários não obtidos** sem inventar informações.

## Leituras Complementares

### Capítulos Relacionados

- [Capítulo 4: Delegando Tarefas: Mensagens, Anexos e uma Boa Passagem de Bastão](/part1/04-handoff)
- [Capítulo 25: Perguntas Frequentes e Solução de Problemas](/part4/25-faq)

### Páginas Oficiais
- [Início Rápido do Grok Bot (Get Started)](https://cursor.com/cn/docs/grok-bot/get-started)
- [Primeiros Passos (Onboarding)](https://cursor.com/cn/help/grok-bot/onboarding)
- [Fazer Login no Grok Bot (Sign In)](https://cursor.com/cn/help/grok-bot/sign-in)
- [Grok Bot Mobile (Mobile)](https://cursor.com/cn/help/grok-bot/mobile)
- [Alterar Nome, Avatar e Responsabilidades do Bot (Edit Bot)](https://cursor.com/cn/help/grok-bot/edit-bot)

### Práticas da Comunidade
- [1.1 O que é o Grok Bot: Entenda em uma página](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [Artigo Completo | Grok Bot do Iniciante ao Avançado | Jin Chenma](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)
- [Guia Extenso | Começando com o Grok Bot do Zero pela Primeira Vez](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)

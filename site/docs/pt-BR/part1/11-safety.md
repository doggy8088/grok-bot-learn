# Capítulo 11: Permissões, Segurança e Human-in-the-Loop

Não seja extremista ao usar o Grok Bot. **Confirmar manualmente cada etapa é exaustivo**, e **delegar poder excessivo facilita a exclusão acidental de configurações de produção**; abrir múltiplos Bots também não garante isolamento.

As principais linhas de defesa de segurança incluem:
- Delegar permissões em níveis de acordo com a reversibilidade da ação
- Configurar o Auto Review para interceptações a nível de máquina
- Bloquear vias de vazamento de rede e credenciais
- **Estabelecer mecanismos de auditoria diária e disjuntores de emergência**

![Permissões, Segurança e Human-in-the-Loop](/info/11-safety.png)

## Mecanismos de Isolamento e Fatos Subjacentes: O Que os Bots Sob a Mesma Conta Compartilham

![Mecanismos de Isolamento e Fatos Subjacentes: O Que os Bots Sob a Mesma Conta Compartilham](/info/11-safety-s1.png)

### O que é
O Grok Bot é executado em microVMs Firecracker exclusivas do Cursor, com isolamento físico no nível de hardware subjacente entre usuários.

No entanto, **todos os Bots sob a mesma conta compartilham o mesmo computador na nuvem**, compartilhando o diretório `/workspace`, bem como os cookies e o estado de login do navegador; os tokens OAuth são armazenados no back-end e não são salvos em disco.

### Como fazer
**Ter múltiplos Bots não oferece isolamento de ambiente**. Se um Bot estiver conectado ao painel interno, outros Bots também poderão operar diretamente.

Se você precisar de isolamento rigoroso, deverá abrir uma conta separada do Cursor; mesmo ao chamar um [Bot de equipe](https://cursor.com/cn/help/grok-bot/shared-bots.md) criado por colegas, ele ainda será executado no seu próprio computador na nuvem.

**Excluir um Bot no cliente não limpa os arquivos locais nem o estado de login**. Ao concluir um projeto, três limpezas manuais são obrigatórias:
1. Fazer logout no navegador do computador na nuvem
2. Revogar as autorizações OAuth em plataformas de terceiros
3. Limpar arquivos confidenciais dentro de `/workspace`

### Qual é o padrão de excelência
- **Fronteiras físicas claras**: o isolamento subjacente de microVMs é eficaz.
- **Tarefas estritamente separadas**: nunca misture operações de alto risco com scraping externo não confiável sob a mesma conta.
- **Credenciais totalmente limpas**: nenhuma sessão órfã após a conclusão do projeto; consulte [《4.4 權限、安全與人閘》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd).

## Classificação de Ações: Dividindo Permissões pela Regra de Reversibilidade em Um Minuto

![Classificação de Ações: Dividindo Permissões pela Regra de Reversibilidade em Um Minuto](/info/11-safety-s2.png)

**O critério de delegação é um só: a ação pode ser desfeita em até 1 minuto (60 segundos)?** Operações que podem ser restauradas facilmente são liberadas diretamente; operações que não podem ser revertidas com rapidez devem passar por aprovação obrigatória.

| Categoria de Operação | Ações Típicas | Estratégia e Interceptação |
| :--- | :--- | :--- |
| Leitura e consulta | Ler `/workspace`, consultar saldo de API | Execução autônoma, liberação direta |
| Modificações e testes locais | Modificar arquivos temporários, rodar `git status` | Execução autônoma, restrita ao diretório de trabalho |
| Comunicação externa | Enviar e-mails, enviar mensagens diretas | Controle humano obrigatório, permitida apenas a criação de rascunhos |
| Ativos e contratos | Transferências/pagamentos, alterar planos de assinatura | Execução autônoma estritamente proibida, proibido tocar no checkout |
| Sistema e permissões | Excluir arquivos não residuais, alterar configurações de produção | Controle humano obrigatório, interceptação por regra (Ask first) com confirmação única |

1. **Inclua nas regras globais do Bot: "Se uma operação não puder ser revertida em um minuto, você deve parar e me perguntar".**
2. A partir de 07/10/2026, as tarefas podem ser roteadas para modelos mais avançados, como o Claude Opus 5.5; quanto mais propensos à inferência autônoma, mais firmemente você deve blindar os limites de permissão.
3. Os cartões de aprovação no cliente expiram por timeout em cerca de 10 minutos. **As rotinas noturnas (Routines) nunca devem aguardar aprovação para envio de mensagens**; defina o resultado final como "salvar em arquivo local" ou "gerar cartão de rascunho", evitando interrupções por erros de timeout.

Critérios de aceitação:
- Preparação concluída de forma autônoma dentro da sandbox e do diretório de trabalho.
- **Pausa ativa aguardando confirmação humana via cartão** antes de acionar ações irreversíveis.
- Tarefas automatizadas noturnas não são interrompidas por timeout. [《4.4 權限、安全與人閘》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## Mecanismo de Aprovação e Interceptação de Ações pelo Auto Review

![Mecanismo de Aprovação e Interceptação de Ações pelo Auto Review](/info/11-safety-s3.png)

### O que é
Ao executar operações controladas, o Bot exibe um cartão com três opções: **Allow once, Always allow e Deny** (idêntico no cliente para iPhone).

O Auto Review subjacente pré-revisa comandos shell e chamadas de plugins, além de controlar o uso do computador, gravações automatizadas e delegações de Agent.
**Gravações na memória e a maioria das alterações de configuração não passam por revisão**, portanto isso não substitui aprovações item por item.

### Como fazer
1. Em planos corporativos (Enterprise), ative o bloqueio do **modo Enforce Auto-review** no painel do Cursor, exceto para grupos configurados como "Don't enforce for this group".
2. Para uso individual, no cliente acesse Configurações > General > Auto-review > Custom Rules; **em caso de conflito de regras, Ask first prevalece**.
   - Ask first: interceptação obrigatória com cartão pop-up
   - Allow automatically: liberação automática quando não houver risco

Insira ações de alto risco diretamente na lista de regras do Ask first:
```text
send, post, buy, transfer, delete, permissions, production, terms
```
**As regras devem ser vinculadas a comportamentos específicos** (como "perguntar antes de enviar e-mails externos"); regras amplas como "permitir todos os scripts shell" são estritamente proibidas.

### Critérios de aceitação
- Ações de alto risco geram **100% de cartões de confirmação pop-up**
- Operações cotidianas de leitura/gravação de baixo risco não são interceptadas incorretamente
- Em caso de conflito, adota-se o plano de interceptação mais rigoroso; consulte [Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security)

## Gerenciamento de Credenciais e Padrões de Transição Humano-Máquina

**Passe a sessão, não os segredos**. O Bot opera usando a sua identidade; em caso de login, autenticação de dois fatores (2FA) ou pagamento, você mesmo deve assumir o controle pessoalmente. Nunca envie senhas na caixa de chat.

1. **Assumir a tela**: clique em "Take over" no topo da janela para digitar pessoalmente ou preencher com o 1Password. Para mecanismos de mascaramento, consulte [安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets).
2. **Permissões somente leitura**: conceda chaves externas apenas para consulta; transferências ou gravações são estritamente proibidas.
3. **Permissões locais**: vá em Configurações > Computer > Your computer > Execution on this computer e, entre as três opções, escolha "Never allow" (as outras opções são "Ask every time" e "Always allow").

### Critérios de aceitação
- Nenhum registro de senha ou código 2FA no chat e nos logs de `/workspace`.
- Serviços externos utilizam exclusivamente estados de login da sessão.
- A execução local é desativada por padrão.

## Mecanismo de Aprovação para Envios Externos e Ações Irreversíveis

### Mecanismos e armadilhas comuns
- **Nunca marque "Close drafts" em ambientes de produção**: a v0.64 adicionou essa opção nos cartões de e-mail e Slack; marcá-la ignorará o rascunho e fará o envio direto externamente.
- **Ações irreversíveis têm forte interceptação subjacente**: a v0.70.2 trava diretamente a execução antes de enviar mensagens, postar, comprar ou excluir se o contexto não contiver uma confirmação explícita feita na hora.

### Etapas de configuração
1. **Finalize o Prompt com instruções rígidas de parada:**
```text
核對行銷活動資料，並起草一份推薦的預算調整方案。不要更改行銷活動，也不要聯繫代理商。在展示當前值、建議值和預期影響之後，請求批准。
```
2. **Consolidar o contrato de seis linhas**: para Bots pessoais, envie as regras abaixo na conversa e peça para que ele as memorize; para Bots compartilhados, insira-as na descrição (Description) da seção About dos detalhes:
```text
Own: 唯一負責的業務結果與目標
Sources: 允許讀取的應用、資料源網址或本地絕對路徑
Output: 交付格式、字數限制與落盤文件位置
Approval: 在執行前必須停下來等待人工批准的動作清單（never publish, never email, never modify without approval）
Failure: 當外部資料源缺失、超時或失效時的應對規則（如實報錯並停止，嚴禁編造資料）
Never: 絕對禁止觸碰的系統操作或越權行為
```
3. **Implantar o contrato de Chefe de Gabinete (Chief of Staff)**: para tarefas complexas, utilize o Chief of Staff do kocer como ponto de entrada único. Para o Bot controlador pessoal, envie o contrato na conversa e peça para ele memorizar; para Bots compartilhados, insira-o na descrição (Description) da seção About:
::: details 組態步驟
```text
Name: Chief
Title: Chief of Staff
Reports to: 你的名字

What I own:
- 接收你發送的每一個目標，並決定是由我完成、委派還是暫存等待批准。
- 將目標拆解為子任務，為每個子任務明確指定負責人、資料源和評審節點。
- 維護每日簡報、每週覆盤和日常 Routine 審計。其他人不得改動這些。
- 實時更新 /workspace/state/chief_log.md，記錄我做出的每一項決定和跳過的每一項操作。

What good output looks like:
- 提交的每一個資料都必須標明來源和日期。如果無法引證，直接捨棄。
- 每一個委派的任務都必須有明確的負責人、一句簡短的目標說明和停止規則。
- 每一份報告末尾必須附帶三行：已完成的內容、等待你確認的內容、已被我廢棄的內容及原因。
- 嚴禁出現“我認為”或“可能”。要麼確認，要麼停下來詢問。

Where I stop (始終暫存等待批准，絕不單獨執行):
- 向公司外部人員發送任何資訊。
- 轉移、花費或承諾任何資金。
- 對外公開公開發表任何內容。
- 刪除任何不是明顯垃圾的文件。
- 註冊帳戶、同意任何條款或接受任何合同。
- 更改帳戶設定、帳單組態或已連線的外掛。
- 任何無法在一分鐘內撤銷的操作。

Style: 簡短、結構化、無廢話。如實彙報進展。
```
:::
Envie as dez regras fundamentais para o Bot e salve como a Skill `house_rules`:
::: details 組態步驟
```text
Rule 1. 可逆性底線：如果我無法在一分鐘內撤銷某項操作，我必須暫停並請求批准。
Rule 2. 無來源不填數位：如果我無法標明數位的出處，我必須將其剔除，嚴禁臆測。
Rule 3. 欄位不全不假定：如果任務缺少交付結果、資料源、產出形式或審查節點，必須先問清楚再開始。
Rule 4. 交付必帶憑證：每項完成的工作都要交出最終成果、來源清單，並將推斷部分單獨列出。
Rule 5. 各階段單一負責人：進行任務委派時，每個階段只能由一個 Bot 負責，嚴禁向同一文件平行處理寫入。
Rule 6. 審批權專屬於人：我絕不代替人類審批其他 Bot 的不可逆操作，只有你能批准。
Rule 7. 沉默即是狀態：如果掛起的操作 24 小時未收到回覆，我只提醒一次，隨後停止執行。
Rule 8. 凡操作必有記錄：我的每一次決策和跳過的每一次操作，都要帶時間戳記寫入 /workspace/state/chief_log.md。
Rule 9. 會話替代機密：我絕不在聊天中要求或粘貼密碼、密鑰或 Token。登錄一律通過人工接管完成。
Rule 10. 緊急熔斷開關：一旦收到 STOP ALL 訊息，我立即中止所有正在執行的任務和 Routine，彙報當前狀態並等待指令。
```
:::

### Critérios de aceitação
- **O Bot não consegue enviar externamente ignorando o rascunho**, e os cartões de comunicação externa exigem confirmação humana secundária obrigatória.
- Ao receber o comando emergencial `STOP ALL`, **consegue suspender instantaneamente todas as tarefas em andamento**.

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## Políticas de Rede e Confinamento de Fronteiras

### Permissões centrais
**As políticas de conectores e as políticas de rede são completamente independentes**. Desativar plugins no painel administrativo não impede o Bot de usar o navegador integrado para acessar a internet pública.

**Os Controles de Rede (Network Controls) são exclusivos do plano Enterprise**; os planos Teams possuem acesso total por padrão e não contam com painel de configuração. A configuração deve ser feita no painel do Cursor em Grok Bot > Network > Grok Bot Network Access.

### Modos de acesso
| Modo | Regras Efetivas | Cenário Aplicável |
| :--- | :--- | :--- |
| **Allow All Network Access** | Permite o acesso a todos os destinos da rede pública (padrão) | P&D exploratório, operações sem dados sensíveis |
| **Defaults + Team Allowlist** | Libera domínios básicos do sistema mais a lista personalizada da equipe | Vasta maioria dos ambientes corporativos de produção |
| **Team Allowlist Only** | Libera apenas a lista personalizada e o essencial para manter a máquina virtual | Ambientes rigorosos de conformidade e auditoria |

Suporta domínios da web, bem como faixas de IP e portas para TCP bruto, sem limite na quantidade de entradas. Computadores em execução sincronizam automaticamente em cerca de um minuto; máquinas suspensas aplicam as alterações no próximo despertar. As políticas de grupo de diretório têm prioridade sobre as políticas de equipe; ao ativar o bloqueio global (Lock), ele entra em vigor para todos os membros.

### Armadilhas comuns e redes privadas
- Os IPs estáticos de saída compartilhados são comuns a todos os clientes e **nunca devem ser usados para identificar uma equipe específica**. Caso precise liberar acessos na rede interna, solicite a faixa de IPs mais recente à equipe da sua conta.
- Liberar `api2.cursor.sh` no gateway enquanto descriptografa domínios aninhados fará com que a máquina trave em Setting up computer; **é obrigatório colocar `*.cursorvm.com` e `*.*.cursorvm.com` na lista de permissões em todos os profiles e ignorar a descriptografia de certificados**.

  Consulte [組態 TLS 檢查代理](https://cursor.com/cn/docs/grok-bot/proxies).
- Para acessar recursos da rede interna, você pode ativar o encaminhamento de tráfego do desktop (Allow Local Egress Routing) ou usar scripts de configuração de ambiente de equipe (Team Setup Scripts) para instalar um cliente VPN de forma unificada durante a inicialização.

  Consulte [連線到私有網路](https://cursor.com/cn/docs/grok-bot/private-networks).

### Qual é o padrão de excelência
- **Bloqueio explícito de solicitações desnecessárias para a rede externa**
- Bloqueio de transferências externas não autorizadas de arquivos
- Gateway da rede interna liberando corretamente os domínios aninhados, sem travamentos na conexão das máquinas virtuais

## Auditoria de Logs e Rastreamento de Execução

- **Logs de auditoria (Enterprise)**: registram alterações de permissões e configurações, com suporte para integração direta a SIEMs.
- **Gravação de operações (Enterprise)**: registra comandos shell anonimizados. **Desativada por padrão e mantida apenas por 90 dias**; não pode ser consultada no painel administrativo padrão, exigindo configuração do OpenTelemetry para exportação a um coletor próprio, identificando a tag `cursor.surface=grok_bot`.
- **Logs de estado local**: na ausência do plano Enterprise, o Bot registra as decisões e o tempo gasto nas aprovações em `/workspace/state/chief_log.md`.

Configure uma Routine leve para **verificar automaticamente comandos anômalos e loops infinitos todas as sextas-feiras à tarde**:

::: details 記錄審計與執行追蹤
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

**Critérios de aceitação**: alterações auditáveis no SIEM, comandos rastreáveis e histórico de operações mantido localmente. Consulte [Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security).

## Casos de Uso Típicos de Human-in-the-Loop no Negócio

### Candidatura ativa a vagas (Prática de PatBergie)
- O front-end é dividido entre 8 Bots especializados que coletam vagas, pesquisam históricos e redigem currículos e primeiras mensagens personalizados, salvando-os como rascunhos.
- **As permissões de envio externo dos Bots são totalmente blindadas**; a confirmação do conteúdo e o clique em "Enviar" no e-mail devem ser feitos manualmente pelo próprio usuário.

### Comparação de preços de compras (Solução ShareGrokBots)
- O Prompt é configurado como somente leitura, monitorando apenas o estoque, coletando cupons e gerando tabelas de comparação de preços, sendo estritamente proibido adicionar itens ao carrinho e finalizar compras automaticamente.
- Mesmo que a v0.70.2 ofereça suporte a pagamentos via X Money e Stripe Link, deve haver confirmação secundária via pop-up para cada transação, **com o pagamento por QR code sendo feito pessoalmente por um humano**.

### Auditoria de assinaturas (Caso CarlySotura)
A auditoria de faturas de SaaS relatou uma economia de $720. O cancelamento de assinaturas envolve a perda definitiva de dados e nunca deve receber autorizações vagas como "cancele tudo"; o processo deve seguir duas etapas obrigatórias:
1. Diagnóstico: o Bot exporta os comprovantes em modo somente leitura e gera uma lista de cancelamento.
2. Execução: aprovação humana item por item, **concedendo permissão de cancelamento único apenas aos itens aprovados**, registrando capturas de tela imediatamente após o cancelamento como comprovante.

### Colaboração em P&D (Prática da equipe SpaceXAI)
- O Bot coleta Issues, cria branches de desenvolvimento, executa testes no computador na nuvem e abre PRs aguardando a conclusão bem-sucedida do CI.
- As permissões de Merge, criação de Tags e implantação de releases são bloqueadas, **exigindo que engenheiros seniores cliquem manualmente para mesclar após o Code Review**.

### Governança de credenciais (Prática de 0xwhrrari)
- A autenticação OAuth segue as permissões individuais do membro solicitante, com responsabilidades bem definidas; configurar diretamente uma API Key global criaria uma porta dos fundos compartilhada por toda a equipe.
- **É estritamente proibido configurar chaves de nível de administrador da organização para Bots públicos**; todas as credenciais compartilhadas devem ser isoladas em sandbox com base no princípio de menor privilégio.

[《4.4 權限、安全與人閘》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)

## Principais Pontos do FAQ de Segurança

- **Isolamento multilocatário (multi-tenant)**: entre usuários, há isolamento no nível de kernel com o Firecracker; no entanto, **todos os Bots do mesmo usuário compartilham a mesma máquina virtual, disco persistente e ambiente de navegador**.

  Consulte [Grok Bot 安全常見問題](https://cursor.com/cn/docs/grok-bot/security-faq).
- **Implantação e residência**: **executado integralmente na nuvem dos EUA gerenciada pelo Cursor**, sem suporte a implantação local/on-premise, VPC própria ou imagens personalizadas; o plano US-only para Enterprise não o inclui por padrão, e garantias formais por escrito exigem contato específico com a equipe da conta.
- **Permissões e modelos**: administradores **não podem forçar o envio de conectores**, podendo apenas permitir ou bloquear; listas de permissão corporativas de modelos não se aplicam a ele, que orquestra de forma unificada modelos da xAI e de subprocessadores secundários, sem oferecer seletor de alternância.
- **Encerramento e dados**: finalizar a máquina virtual no painel encerra apenas a execução, **mantendo o disco persistente e sem revogar permissões de acesso**; após o encerramento do serviço e mediante solicitação por escrito, os dados são excluídos em até 30 dias, com backups diários criptografados para recuperação externa.
- **Certificações de segurança**: a empresa controladora possui as certificações ISO/IEC 27001 e 42001 emitidas pela Schellman, com o Grok Bot formalmente incluído no escopo.

## Checklist de Configuração de Permissões para Produção

1. Execução na máquina física: em Settings → Computer, selecione obrigatoriamente **Never allow**.
2. Auditoria e interceptação: ative o Enforce no Auto-review e preencha todos os verbos irreversíveis em Custom Rules.
3. Proteção de envio externo: **mantenha a opção "Close drafts" desmarcada nos cartões de e-mail e Slack da v0.64**.
4. Regras contratuais: envie o contrato de seis linhas para o Bot memorizar (em Bots compartilhados, insira na seção About dos detalhes) e salve as dez regras fundamentais como a Skill `house_rules` para servir como prompt inicial.
5. Rede e proxy: selecione "Defaults + Team Allowlist" em Network, libere `*.cursorvm.com` no gateway e ignore a descriptografia.
6. Auditoria e disjuntor: integre as gravações com OpenTelemetry exportando `cursor.surface=grok_bot`; em emergências, **envie `STOP ALL` no chat para congelar instantaneamente todas as Routines**.

## Armadilhas Mais Comuns

- Bots na mesma conta compartilham o nível subjacente; não é possível isolar ativos criando múltiplos Bots.
- Não marque "Close drafts" na v0.64; ignorar a confirmação fará com que alucinações sejam enviadas diretamente.
- Não agende Routines com aprovação de madrugada: o timeout de 10 minutos do pop-up travará o processo; durante a noite, gere apenas rascunhos ou salve localmente.
- Apenas desativar plugins não é suficiente; sem configurar os Network Controls, páginas da web ainda poderão ser abertas.
- Não envie senhas ou códigos 2FA na caixa de chat; clique em **Take over** para preenchê-los manualmente.
- Se não houver necessidade de depuração local, trave a política de execução em **Never allow**.
- Excluir o Bot não limpa o disco nem o estado de login; é necessário acessar o computador na nuvem para fazer logout e limpar.

## Como Validar Após a Configuração

1. **Proteção contra solicitação de credenciais**: peça diretamente ao Bot as senhas e contas salvas no navegador e as variáveis de ambiente. **O Bot deve recusar explicitamente**, sem expor senhas reais na janela.
2. **Proteção contra envio direto não autorizado**: peça para ele enviar diretamente um relatório de pesquisa em `/workspace` para test@example.com. **O Bot deve interceptar e gerar um rascunho**, aguardando confirmação.
3. **Teste de interceptação de aprovação**: envie o comando `rm -rf /workspace/test_dir` para disparar o cartão. **Antes de clicar manualmente em "Allow once"**, nada deve ser excluído no computador na nuvem.
4. **Teste de notificação de exceções**: forneça links corrompidos ou caminhos falsos para ele consolidar dados financeiros. **Após a falha de leitura, ele deve parar e relatar o erro com precisão**, sendo estritamente proibido inventar dados falsos.
5. **Teste de disjuntor de emergência**: envie diretamente `STOP ALL` durante a execução de uma tarefa. **O progresso deve ser congelado instantaneamente e as chamadas interrompidas**, relatando o status atual e aguardando novas instruções no local.
6. **Verificação de logs de auditoria**: abra `/workspace/state/chief_log.md`; **todas as decisões críticas e carimbos de data/hora (timestamps) devem estar registrados por completo**; no plano Enterprise, acesse o Audit Log no painel para verificar os registros.

## Leituras Adicionais

- Capítulo relacionado: [第 5 章 共享雲端電腦：文件、瀏覽器與接管](/part1/05-computer)
- Capítulo relacionado: [第 25 章 常見問題與排錯](/part4/25-faq)
- Documentação oficial: [Grok Bot 安全](https://cursor.com/cn/docs/grok-bot/security)
- Documentação oficial: [Grok Bot 安全常見問題](https://cursor.com/cn/docs/grok-bot/security-faq)
- Documentação oficial: [面向 Teams 和企業版的 Grok Bot](https://cursor.com/cn/docs/grok-bot/teams)
- Documentação oficial: [組態身份與訪問](https://cursor.com/cn/docs/grok-bot/identity)
- Documentação oficial: [連線到私有網路](https://cursor.com/cn/docs/grok-bot/private-networks)
- Documentação oficial: [組態 TLS 檢查代理](https://cursor.com/cn/docs/grok-bot/proxies)
- Suporte oficial: [安全儲存機密資訊](https://cursor.com/cn/help/grok-bot/secrets)
- Suporte oficial: [哪些 AI 模型為 Grok Bot 提供支援？](https://cursor.com/cn/help/grok-bot/models)
- Suporte oficial: [Grok Bot 電腦](https://cursor.com/cn/help/grok-bot/computer-recovery)
- Suporte oficial: [團隊 Bot](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- Artigo original da comunidade: [《4.4 權限、安全與人閘》](https://jcng5q8n0f3z.feishu.cn/wiki/Fxfiwuf4TiCqHTkTzFgcosQ7nzd)
- Artigo original da comunidade: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

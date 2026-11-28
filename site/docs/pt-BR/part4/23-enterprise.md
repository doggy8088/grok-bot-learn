# Capítulo 23: Versão Teams e Implementação Corporativa

Ao implantar o Grok Bot para equipes, os principais pontos de bloqueio costumam ser estes:

- O gateway intercepta na fase de handshake, fazendo com que o **computador na nuvem não conecte**.
- A VM Linux não possui cliente MDM instalado e é classificada pelo IdP corporativo como dispositivo não confiável.
- Existem riscos de vazamento de credenciais e invasão de rede interna, além da falta de métodos de distribuição silenciosa do cliente.

Configurando adequadamente o **SSO e as isenções no gateway de segurança**, liberando o acesso à rede privada, é possível gerenciar com sucesso o ciclo de vida em lote.


![Versão Teams e Implementação Corporativa](/info/23-enterprise.png)

## Controles de Gerenciamento Teams e Enterprise: Arquitetura e Limites de Capacidade

![Controles de Gerenciamento Teams e Enterprise: Arquitetura e Limites de Capacidade](/info/23-enterprise-s1.png)

### O que é

**Cada usuário conta com uma Firecracker microVM exclusiva na nuvem**; as instruções e aprovações são enviadas localmente, enquanto o código e o navegador rodam na nuvem.

Vale um alerta: **todos os Bots da conta compartilham essa mesma VM**, com arquivos e estados de login totalmente integrados.

Em 12/10/2026, o plano The X Subscription dividiu as permissões em duas edições:

- **Versão Teams**: ativada por padrão para todos os membros, utiliza IP de saída estático compartilhado e inclui auditoria básica e regras de equipe.
- **Versão Enterprise**: suporta autorização baseada em grupos e SCIM 2.0, permite uso de sudo e lista de permissões de rede, e traz gravação de operações e exportação via OpenTelemetry (com a tag `cursor.surface=grok_bot`).

Consulte a documentação em [Grok Bot para Teams e Enterprise](https://cursor.com/cn/docs/grok-bot/teams).

### Como fazer

As configurações de rotina são feitas na [página do Grok Bot no painel do Cursor](https://cursor.com/dashboard/bot), divididas em quatro etapas principais.

1. Definir permissões e opções básicas
- Durante a fase de testes graduais (rollout), clique em **Manage Group Access** para selecionar o grupo piloto; desative os Cloud Agents se não utilizar codificação na nuvem; mantenha o compartilhamento público de modelos desativado para evitar vazamentos.
- **Recomenda-se definir a execução local como Never allow**, além de desativar o roteamento de saída local para evitar desvios no tráfego.
- Para os Bots da barra lateral, selecione All team ou grupos específicos na coluna Auto-add para fixá-los.

2. Configurar travas de aprovação e regras
- Ative o modo **Enforce Auto-review** para impedir que os membros desativem a revisão por conta própria no cliente.
- Operações de alto risco, como deploy em produção ou envio de e-mails externos, devem ser configuradas como Ask first; operações estritamente de leitura, como Allow automatically.
- **Quando houver conflito entre regras de equipe e individuais, o sistema forçará obrigatoriamente o Ask first**.

3. Configurar rede e segredos
- Na rede, selecione apenas a lista de permissões da equipe ou adicione valores padrão, preenchendo domínios e faixas de IP; para evitar alterações no sistema, é possível desativar o sudo, que vem habilitado por padrão.
- **Em Team Secrets, a equipe pode adicionar no máximo 100 itens**, com limite de 32 KB por item e capacidade total máxima de 96 KB; o texto simples não é exibido após salvar.
- Nomes de variáveis de segredos não podem utilizar `PATH`, `HOME` nem nomes reservados do sistema que comecem com `SAND_` ou `LD_`.

4. Configurar políticas em nível de grupo
- Acesse os grupos em [Members > Groups](https://cursor.com/dashboard/members?subtab=groups); o **princípio de configuração é que as regras só podem ser flexibilizadas, nunca endurecidas**.
- Marcar Don't enforce for this group desbloqueia a restrição de revisão automática.
- As políticas de rede são uma exceção: o grupo substitui diretamente a equipe; se um membro pertencer a vários grupos, a rede seguirá a configuração mais restritiva, enquanto as permissões seguirão a mais ampla.

### O que define um bom resultado

- No painel, os grupos piloto e os grupos não autorizados estão claramente diferenciados, e pessoas não autorizadas não conseguem ativar o Bot no cliente.
- As regras de equipe e de Auto-review estão bloqueadas; os membros conseguem ver as regras de equipe na página de configurações do cliente, mas os botões de edição e exclusão estão desativados.
- Operações de alto risco (comunicação externa, destruição de arquivos, comandos com privilégios) acionam a interceptação para aprovação em 100% dos casos.

---

## Identidade e SSO: Habilitando o Acesso Global e a Compatibilidade com Confiança de Dispositivos

### O que é

O Grok Bot utiliza o sistema de contas do Cursor, **não sendo necessário criar um aplicativo separado no IdP**. Documentação de referência: [Configurar Identidade e Acesso](https://cursor.com/cn/docs/grok-bot/identity).

O Bot roda em uma VM Linux na nuvem sem MDM instalado, não atendendo aos requisitos do FastPass ou Hybrid Join. **Lembre-se de nunca desativar a conformidade de dispositivos globalmente**; configure uma política de liberação para os grupos-alvo antes das regras de bloqueio.

### Como fazer

- **Expansão de atribuição no Okta**: acesse o aplicativo Cursor em **Assignments** > **Assign to Groups** e marque os grupos de negócios; ao ativar o SCIM, sincronize a atribuição e o envio (Push Groups).

  **SAML SSO e SCIM devem ser atribuídos simultaneamente**; se o SSO for esquecido, o login será bloqueado.
- **Expansão de atribuição no Entra ID**: no aplicativo Cursor, clique em **Users and groups** > **Add user/group** para adicionar grupos (requer licença P1/P2; não suporta grupos aninhados); atribua os mesmos grupos ao aplicativo de provisionamento sincronizado.
- **Liberação de Linux no Okta**: crie uma nova regra `Grok Bot computer (Linux)` antes das regras de bloqueio da política de autenticação.

  Restrinja os usuários ao grupo do Cursor, **selecione Other Desktop em Device platform** (não há opção dedicada para Linux), escolha Any em Device state; selecione Password + Another factor para autenticação, sem marcar restrições contra phishing.
- **Liberação de Linux no Entra ID**: crie uma política de alta prioridade especificando o grupo do Cursor e os aplicativos-alvo; inclua Linux em Device platforms e exclua Windows e macOS; em Grant, marque Require multifactor authentication; **a política de conformidade existente deve obrigatoriamente excluir esse grupo ou a plataforma Linux**.

### O que define um bom resultado

- Os usuários corporativos fazem login no cliente desktop usando o SSO empresarial sem receber o erro `User is not assigned to this application`.
- No navegador do Bot, o acesso à rede interna é concluído com senha mais autenticação em dois fatores, sem exibir pop-ups do FastPass ou bloqueios de não conformidade do dispositivo.
- **Quando os funcionários acessam de seus computadores pessoais, as regras originais de FastPass e conformidade de dispositivos continuam vigorando rigorosamente**.

## Acesso à Rede Privada: Roteamento Desktop e Automação de Scripts Team Setup

![Acesso à Rede Privada: Roteamento Desktop e Automação de Scripts Team Setup](/info/23-enterprise-s3.png)

### O que é

O Grok Bot é executado na nuvem, portanto **o acesso à intranet exige a liberação da rede privada**.

- Roteamento via cliente desktop: ideal para depuração temporária. Ao ativar `Settings > Computer > Route traffic through this computer` no cliente, o tráfego passa pela placa de rede da máquina local, e os administradores podem desativá-lo com um clique no painel.
- Instalação de cliente via Team Setup: para acesso contínuo e **exclusivo da versão Enterprise**. A equipe de TI mantém um script centralizado, que é acionado automaticamente na inicialização ou atualização do Bot para integrá-lo à rede interna.

Para mais detalhes, consulte [Conectar a Redes Privadas](https://cursor.com/cn/docs/grok-bot/private-networks).

### Como fazer

Os scripts de configuração de ambiente da equipe ficam sob **Bot Computers** no painel e são executados como usuário comum via `sudo` na máquina virtual Debian Linux. **O script é executado ao ligar a máquina e atualizado ciclicamente cerca de uma vez ao dia, com limite de tempo de 30 minutos**.
- Se o código de saída de `check` for 0, a instalação é ignorada; após a instalação, o `check` é executado novamente para validação.
- **Falhas na execução não impedem a inicialização do computador**, sendo feita nova tentativa no próximo ciclo de atualização.

#### Solução de Conexão de Rede com Tailscale

1. Abra o **Team Secrets**, adicione a chave de autenticação do Tailscale `TS_AUTHKEY` (com o valor `tskey-auth-...`) e vincule uma tag de ACL dedicada no console do Tailscale (como `tag:grok-bot`) para **restringir rigorosamente as permissões de acesso**.
2. Acesse os scripts de configuração de ambiente da equipe, clique em **+** para criar um novo manifesto, preencha o Manifest ID com `private-network-tailscale` e alterne para o modo JSON ou formulário para preencher a configuração:

::: details Solução de Conexão de Rede com Tailscale
```json
{
  "manifestId": "private-network-tailscale",
  "entries": [
    {
      "id": "install-tailscale",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\ncurl -fsSL https://tailscale.com/install.sh | sh\nsudo tailscale up --authkey=\"$TS_AUTHKEY\" --accept-routes --hostname=\"grok-vm-${USER}\"",
      "check": "command -v tailscale && tailscale status"
    }
  ]
}
```
:::

#### Solução de Conexão com Cloudflare Tunnel

- Serviços HTTP privados: acesse diretamente o domínio roteado pelo túnel, com autenticação gerenciada pelo Cloudflare Access e concluída interativamente no navegador do Bot.
- Serviços TCP privados (como bancos de dados e SSH): instale o `cloudflared` no manifesto e, quando precisar se conectar, execute o comando no shell para **abrir uma porta de encaminhamento local**:

`cloudflared access tcp --hostname db-internal.corp.com --url localhost:5432`

::: details Solução de Conexão com Cloudflare Tunnel
```json
{
  "manifestId": "private-network-cftunnel",
  "entries": [
    {
      "id": "install-cloudflared",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\ncurl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null\necho 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared bullseye main' | sudo tee /etc/apt/sources.list.d/cloudflared.list\nsudo apt-get update && sudo apt-get install -y cloudflared",
      "check": "command -v cloudflared"
    }
  ]
}
```
:::

#### Liberando Endpoints do Plano de Controle nas Políticas de Rede

Se a equipe ativar o controle de rede **apenas lista de permissões da equipe**, **é obrigatório incluir o plano de controle da ferramenta de rede na lista de permissões**, caso contrário o cliente não conseguirá concluir a autenticação. Por exemplo, ao usar o Tailscale, libere os domínios do servidor de coordenação e dos servidores relay DERP na política; as alterações de política levam cerca de 1 minuto para serem propagadas para a máquina virtual.

### O que define um bom resultado

- Os computadores Bot novos ou recriados aparecem automaticamente na lista de dispositivos do console de gerenciamento do Tailscale ou Cloudflare com status online após a inicialização ser concluída.
- O script `check` do manifesto retorna 0 de forma estável nas atualizações periódicas diárias subsequentes, sem reexecutar a lógica de instalação.
- Os tokens confidenciais são injetados exclusivamente via Team Secrets, sem nenhuma credencial em texto simples no texto do manifesto ou nos logs de execução.

---

## Evitando Armadilhas com Proxies e Gateways Corporativos: Regras de Liberação e Isenção de Inspeção TLS

Gateways corporativos (como Zscaler e Palo Alto) frequentemente permitem que o chat funcione normalmente, mas **impedem capturas de tela ou o controle do terminal**.

A causa raiz é que o plano de controle utiliza conexões persistentes de streaming HTTP/2 ou SSE sob o domínio aninhado de segundo nível `<computer>.<cluster>.cursorvm.com`, as quais regras comuns de nível único não conseguem mapear.

Consulte a explicação oficial em [Configurar Proxy com Inspeção TLS](https://cursor.com/cn/docs/grok-bot/proxies).

### Pontos principais de configuração

O gateway deve liberar os seguintes domínios, **desativando o buffer de resposta e isentando a inspeção TLS**, para evitar falhas no handshake ponta a ponta e tempos limites no streaming:
- `*.cursor.sh`: APIs principais
- `*.cursorvm.com` e **`*.*.cursorvm.com`**: canal de controle, deve oferecer suporte a curingas de dois níveis
- `*.cursor-cdn.com`, `*.cursorapi.com`, `downloads.cursor.com` e o site principal: recursos estáticos e download de atualizações

Após configurar as políticas, **certifique-se de sincronizá-las com a configuração de roaming Off-Network**, evitando falhas de conexão quando os funcionários estiverem fora da rede ou trabalhando em casa.

### Diagnóstico de dispositivos e validação

Siga o passo a passo de diagnóstico no terminal do computador do funcionário:

1. Verifique se o certificado foi adulterado; o emissor legítimo deve ser **Amazon RSA**:
```bash
   curl -v https://api2.cursor.sh |& grep -C1 issuer:
```
2. Verifique a resolução de DNS de múltiplos níveis; se falhar, compare com `nslookup test.us9.cursorvm.com 1.1.1.1`:
```bash
   nslookup test.us9.cursorvm.com
```
3. Verifique o streaming: os dados devem ser exibidos linha por linha; se houver uma pausa de alguns segundos seguida pela exibição de todo o bloco de uma vez, isso indica que o buffer do gateway não foi desativado.

Critério de aceitação: **tanto na rede corporativa quanto em roaming doméstico, a conexão com o computador na nuvem deve ocorrer em até 5 segundos**, com o certificado passando diretamente pela Amazon RSA e a conexão persistente de streaming sem atrasos de buffer.

## Distribuição do Cliente Desktop e Controle de Versão

### Plataformas e mecanismos de atualização

| Plataforma | Formato de instalação | Lógica de atualização |
| --- | --- | --- |
| macOS | `.dmg` (Apple Silicon / Intel) | Verifica atualizações automaticamente na inicialização, **não suporta desativação por política** |
| Windows | Setup `.exe` (x64 / Arm64) | Verifica atualizações automaticamente na inicialização, não suporta desativação por política |
| Linux | `.deb`, `.rpm`, AppImage | deb e rpm são gerenciados pelo gerenciador de pacotes; AppImage verifica atualizações automaticamente |
| iOS | App Store | Requer iOS 18 ou superior |
| Android | Google Play | Requer Android 9 ou superior, suporta distribuição gerenciada |

Consulte as instruções oficiais de implantação em [Implantar o Grok Bot na sua Organização](https://cursor.com/cn/docs/grok-bot/deployment).

### Implantação e controle de versão

1. **Obter os pacotes de instalação**
   Não baixe os pacotes manualmente pelo navegador; faça a chamada diretamente ao feed JSON oficial: `https://api2.cursor.sh/updates/api/download/stable/{platform}/sand`.
   `{platform}` oferece suporte a macOS (`darwin-arm64`, `darwin-x64`), Windows (`win32-x64-user`, `win32-arm64-user`) e Linux (`linux-x64`, `linux-arm64`).
```bash
curl -s https://api2.cursor.sh/updates/api/download/stable/win32-x64-user/sand
```
   A API retorna `version`, `commitSha`, `downloadUrl`, além de `debUrl` e `rpmUrl` para Linux. Para macOS e Windows, também é possível montar diretamente os endereços dos pacotes de instalação de acordo com o padrão:
   - Windows: `https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe`
   - macOS: `https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg`

2. **Distribuição via MDM**
   - Windows (Intune / SCCM): adicione `/S` aos parâmetros para instalação silenciosa. Por padrão, o instalador grava em `%LOCALAPPDATA%\Programs` do usuário atual, portanto **deve ser executado no contexto do usuário (User Context)**.

     Nunca utilize a conta SYSTEM local, caso contrário a instalação será feita no caminho incorreto e os funcionários não encontrarão o aplicativo.
```cmd
  Grok_Bot_1.0.0_Setup.exe /S
  ```
   - macOS (Jamf / Kandji / Intune): basta implantar o `.dmg` correspondente à arquitetura no diretório `/Applications`.
   - Linux (Ansible / Puppet): instale o pacote `.deb` ou `.rpm`, e o sistema gravará automaticamente as configurações dos repositórios oficiais.

3. **Controle e bloqueio de versão**
   No macOS e no Windows, não é possível desativar completamente a atualização automática por meio de políticas.

No Linux, é possível bloquear a versão por meio do gerenciador de pacotes ou pausar a sincronização definindo `Enabled: no` em `/etc/apt/sources.list.d/grok-bot.sources` e `enabled=0` em `/etc/yum.repos.d/grok-bot.repo`:
```bash
  sudo apt-mark hold grok-bot
  ```
   O Cursor estabelece um prazo de suporte para versões antigas. **Se o cliente estiver abaixo do limite mínimo suportado, um pop-up em tela cheia com Update required bloqueará o uso obrigatoriamente**; no Linux, versões bloqueadas que expirarem também serão impedidas de rodar. A equipe de operações precisa **realizar rollouts graduais de novas versões estáveis testadas a cada duas a quatro semanas**.

### Critérios de aceitação

- Os dispositivos de trabalho concluem a instalação silenciosa via MDM, garantindo que **a área de trabalho esteja pronta assim que o novo colaborador ligar o computador**.
- A equipe de TI mantém um ritmo regular de renovação de versões, concluindo a rotação de versões dentro da organização antes que ocorram bloqueios forçados pela plataforma oficial.

## Gerenciamento de Computadores Bot: Operações em Lote e Ciclo de Vida

![Gerenciamento de Computadores Bot: Operações em Lote e Ciclo de Vida](/info/23-enterprise-s6.png)

### Operações principais e permissões

O acesso é feito na seção **Bot Computers** da [página do Grok Bot no painel do Cursor](https://cursor.com/dashboard/bot), clicando em **Manage Bot Computers**.

**Esse recurso é exclusivo para administradores de organização (Organization Admins) da versão Enterprise**; administradores comuns de equipe não visualizam esse acesso.

Consulte a documentação em [Gerenciar Computadores Grok Bot](https://cursor.com/cn/docs/grok-bot/computers).

| Nome da operação | Comportamento subjacente | Status de retenção de dados e arquivos | Cenários aplicáveis |
| --- | --- | --- | --- |
| **Recriar VMs (Recreate VMs)** | Reinstala com a imagem mais recente e executa novamente os scripts de ambiente | **Preservado**. O disco permanece intacto; Bots, arquivos pessoais e cookies são mantidos, removendo apenas softwares do sistema instalados manualmente | Aplicação de alterações nos scripts de ambiente, rollout gradual de nova imagem |
| **Encerrar VMs (Terminate VMs)** | Destrói imediatamente instâncias ativas ou em suspensão, interrompendo o processamento atual | **Preservado**. Mantém o disco; ao enviar uma nova mensagem no cliente, uma máquina virtual limpa será reiniciada | Resolução de travamentos de instância, liberação de recursos na nuvem |
| **Excluir máquina virtual e dados** | Destrói a máquina virtual e exclui permanentemente o armazenamento persistente vinculado | **Não preservado**. Os dados são completamente apagados; no próximo uso, um computador em branco será reinicializado | Desligamento de funcionários, redefinição completa por corrupção de dados |

### Operações no console e solução de problemas

1. Acesse a página e clique em **Manage**, pesquise por nome ou e-mail para filtrar membros, com suporte a seleção individual, seleção múltipla ou **Select all**.
2. No menu suspenso **Manage selected**, escolha a operação desejada e inicie a execução após confirmar o número de pessoas afetadas.
3. Após a conclusão, **é obrigatório clicar no botão Done no cartão**. Cada equipe só pode executar uma operação em lote por vez; se não clicar em Done, os botões subsequentes permanecerão bloqueados.

Se encontrar status ignorados ou com falhas, proceda de acordo com o retorno:
- **Ignorado (Sem VM / Não foi possível concluir a operação)**: não há VM vinculada à conta ou o usuário saiu da equipe durante a fila; nenhuma ação é necessária.
- **Falha (Outra recriação em andamento / Verificação de VM não concluída)**: outra atualização ainda não terminou ou o sistema não conseguiu obter o status temporariamente no back-end; aguarde alguns minutos e tente novamente.
- **Falha (Não foi possível concluir a operação)**: o Bot está executando tarefas intensivas, causando timeout; avise o membro para deixar o Bot ocioso antes de tentar novamente.

### Automação e critérios de aceitação

Ative a opção **Terminate Inactive Computers** acima dos botões de ação. **Os computadores dos membros sem atividade por 30 dias consecutivos serão encerrados automaticamente**, liberando apenas a instância de computação e mantendo o disco, com o sistema realizando a limpeza em ciclos contínuos.

Para operações em lote em várias equipes, é possível chamar a [API de Admin da Organização](https://cursor.com/docs/account/organizations/organization-admin-api.md#grok-bot-computers).

Ao fazer a chamada, forneça uma chave de API da organização com permissão `admin:*`, passe o ID da equipe, o array de e-mails dos membros e o tipo de ação (`recreate` ou `terminate`), monitorando o progresso via polling; isso também está sujeito ao limite de uma concorrência por equipe.

Durante a validação, concentre-se em dois indicadores principais:
- Capacidade de recriar instâncias em lote de forma estável e sem perda de dados.
- Ativação do encerramento automático após 30 dias de inatividade, evitando que VMs zumbis consumam a cota da organização na nuvem.

## Configuração de Linha de Base de Segurança Corporativa e Prompts Práticos

### Configuração do administrador
1. Trave a rede em "apenas lista de permissões da equipe" e desative modelos públicos e canais de e-mail.
2. Ative **Enforce Auto-review** e defina a execução local como **Never allow** para evitar rebaixamentos não autorizados.
3. Qualquer chamada a APIs de produção e alterações em bancos de dados, ou ações envolvendo envio de e-mails externos, assinatura de contratos e merge na branch main, devem ser configuradas obrigatoriamente como **Ask first**; consultas de logs e compilações podem ser liberadas diretamente.

### Diretrizes para colaboradores
1. Use variáveis de ambiente para credenciais; **é terminantemente proibido colar senhas em texto simples na caixa de diálogo**.
2. Para autorizações confidenciais, escolha **Allow once** em vez de permitir sempre, e encerre a sessão assim que concluir.

### Prompts práticos
::: details Prompts práticos
```text
你現在負責對內部服務進行介面與架構調研。
請遵循以下嚴格的安全限制：
1. 本次任務為純唯讀模式，嚴禁對目標服務發起任何 POST、PUT、DELETE 請求。
2. 檢查網路連通性：嘗試向內部端點 http://api-monitor.corp.internal/health 發起 GET 請求並打印狀態碼。
3. 如果遇到證書問題或連線被重定向，記錄錯誤記錄，不要嘗試使用任何提權手段。
4. 將調研結果彙總輸出為 Markdown 表格，包含服務名稱、回應耗時、健康狀態。
5. 完成後暫停執行，等待我的進一步指令，不要擅自讀取其他網段資產。
```
:::

::: details Prompts práticos
```text
請按規範完成本週發版程式碼的對比檢查與 PR 草稿建立：
1. 切換到工作區程式碼目錄，拉取 origin/main 最新分支。
2. 比對 feature/sso-login 分支與 main 分支的改動差異，列出所有變動的文件列表。
3. 檢查是否有硬寫程式的密鑰、密碼或私鑰文件被提交。如果發現任何形如 'AKIA...' 或 'BEGIN PRIVATE KEY' 的文本，立即中斷任務並向我告警。
4. 在本地執行靜態檢查指令碼：npm run lint 和 npm run test。
5. 準備 PR 描述文本草稿，包含變更摘要與測試結果。
6. 注意：嚴禁直接推送到遠端倉庫。把 PR 描述保存為 local-pr-draft.md 後向我申請確認。得到明確授權前不得執行 git push。
```
:::

::: details Prompts práticos
```text
請處理今天未分配的內部支援工單：
1. 打開瀏覽器，訪問內部工單主控台 https://tickets.corp.internal。
2. 過濾出狀態為 'New' 且優先級為 'High' 的所有工單。
3. 逐條提取工單的核心問題，按照以下類別打標記：[帳號登入]、[權限申請]、[網路故障]。
4. 為每條工單生成標準回覆模版，存入草稿區。
5. 涉及權限開通的工單，一律在回覆中註明：'需直屬主管在 OA 提交審批流，當前僅作資訊預審'。
6. 嚴格要求：所有郵件和系統回覆只保留在草稿狀態，嚴禁點選 'Send' 或 'Submit'。生成處理清單供我逐條審查。
```
:::

## Armadilhas Comuns

1. **Esquecer curingas de múltiplos níveis no gateway**: o hostname segue o formato `<vm-id>.<cluster-id>.cursorvm.com`; configurar apenas `*.cursorvm.com` trava o carregamento em 99%, portanto **é necessário adicionar `*.*.cursorvm.com`**.
2. **Buffer ativo no proxy interrompendo o streaming**: ativar o Response Buffering no Zscaler causa desconexões. **É obrigatório desativar o buffer para os domínios do Cursor e permitir a passagem direta de Server-Sent Events**.
3. **Falta de lista de permissões nas políticas de roaming**: não conseguir conectar em casa ocorre porque o Zscaler alternou para a política Off-Network. Lembre-se de sincronizar a lista de domínios permitidos e as isenções de TLS com a política fora da rede.
4. **Ativação acidental do modo de privacidade legado**: ativar "Modo de privacidade (legado)" no painel desativa o Bot completamente; desative essa opção nas configurações da equipe.
5. **IdP exigindo dispositivos em conformidade**: a VM Linux na nuvem não é gerenciada por MDM e não executa o FastPass. **Adicione uma regra de alta prioridade no Okta/Entra ID para Linux (Other Desktop)**, liberando o acesso mediante senha mais autenticação secundária pelo celular.
6. **Armazenamento de segredos em texto simples nos scripts**: o Team Setup é um JSON em texto simples. Armazene os tokens no **Team Secrets** e faça a leitura no script usando `"$TS_AUTHKEY"`.
7. **Instalação com permissão SYSTEM não encontrada**: o aplicativo é instalado em `%LOCALAPPDATA%\Programs`. **Execute o comando de instalação `/S` no contexto do usuário atual**.
8. **Confundir encerramento com revogação de acesso**: Terminate apenas interrompe o processo e preserva o disco; ao enviar uma nova mensagem, a VM será reiniciada. **Para revogar o acesso definitivamente, desatribua o usuário no IdP ou remova-o pelo Manage Group Access**.
9. **Perda de segredos ao participar de várias equipes**: entrar em mais de duas equipes com o Team Setup configurado causará a **rejeição de qualquer Team Secrets**; basta sair das equipes excedentes.
10. **Versão bloqueada abaixo do limite mínimo**: uma versão bloqueada via `apt-mark hold` que fique abaixo do limite do ciclo de vida será bloqueada com a mensagem "Update required"; basta desbloquear e atualizar.

## Como Validar Após a Conclusão

### Rede e Gateway
- No computador de trabalho, execute `curl -v https://api2.cursor.sh |& grep -C1 issuer:` para garantir que o emissor do certificado seja **Amazon RSA**.
- Execute `nslookup test.us9.cursorvm.com` para testar a resolução de domínio de múltiplos níveis; conecte-se ao ponto de acesso móvel e acesse o computador na nuvem para verificar se **não há alertas de certificado**.

### Identidade e SSO
- Faça login no Grok Bot com uma conta de fora da equipe de engenharia e confirme se o Cursor SSO realiza o login com sucesso na primeira tentativa.
- No navegador do Bot, faça login no SSO interno usando "senha + código de verificação no celular", **sem pop-up de bloqueio do FastPass**, enquanto as políticas de conformidade no computador de trabalho continuam funcionando normalmente.

### Rede Privada e Scripts de Ambiente
- No console do Tailscale ou Cloudflare, confirme se as novas máquinas entram automaticamente na rede com as tags corretas.
- Execute ping ou curl no terminal para um host privado para validar a conectividade; verifique se os logs do Team Setup não apresentam timeouts e se **os segredos foram devidamente mascarados**.

### Cliente e Linha de Base de Segurança
- Instalação silenciosa em conta comum do Windows em `%LOCALAPPDATA%\Programs` com criação do atalho na área de trabalho.
- Regras globais em "Configurações > Geral > Revisão Automática" bloqueadas contra alterações; ao testar a exclusão de arquivos no diretório raiz ou chamadas a webhooks não autorizados, o sistema **exige obrigatoriamente um pop-up de aprovação**.

### Ciclo de Vida dos Computadores
- O administrador executa **Recreate VMs** no console e confirma que os arquivos originais e o histórico continuam intactos.
- Após a conclusão das tarefas em lote, clicar em **Done** permite que o sistema inicie normalmente a próxima rodada.

## Leituras Complementares

- Documentação oficial: [Grok Bot para Teams e Enterprise](https://cursor.com/cn/docs/grok-bot/teams)
- Documentação oficial: [Configuração de Identidade e Acesso](https://cursor.com/cn/docs/grok-bot/identity)
- Documentação oficial: [Conectar-se a Redes Privadas](https://cursor.com/cn/docs/grok-bot/private-networks)
- Documentação oficial: [Configurar Proxy com Inspeção TLS](https://cursor.com/cn/docs/grok-bot/proxies)
- Documentação oficial: [Implantar o Grok Bot na sua Organização](https://cursor.com/cn/docs/grok-bot/deployment)
- Documentação oficial: [Gerenciar Computadores Grok Bot](https://cursor.com/cn/docs/grok-bot/computers)
- Ajuda oficial: [Planos e Faturamento](https://cursor.com/cn/help/grok-bot/plans)
- Ajuda oficial: [Bots de Equipe](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- Ajuda oficial: [Conectar Aplicativos](https://cursor.com/cn/help/grok-bot/connect-apps.md)
- Guia oficial: [Visão Geral da Arquitetura de Segurança do Grok Bot](https://cursor.com/cn/docs/grok-bot/security)

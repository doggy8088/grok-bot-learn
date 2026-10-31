# Capítulo 5 Computador em Nuvem Compartilhado: Arquivos, Navegador e Assunção de Controle

Usuários novatos no Grok Bot costumam ter alguns equívocos comuns. Esses mal-entendidos geralmente criam obstáculos no desenvolvimento e na manutenção posteriores:

- Pensar equivocadamente que criar um novo Bot adiciona uma máquina virtual independente.
- Pensar equivocadamente que, ao colocar vários Bots para trabalhar juntos, eles conseguirão ler diretamente o histórico de chat uns dos outros.
- Colar credenciais de login ou até mesmo API Tokens diretamente na janela de chat quando ferramentas de terceiros exigem autenticação.

Quando o computador em nuvem é subitamente limpo devido à manutenção do sistema ou atualizações subjacentes, todos os ambientes e scripts instalados desaparecem. Só então as pessoas percebem que não sabiam nada sobre os mecanismos internos desse computador em nuvem.

Todos os Bots sob a mesma conta trabalham no mesmo computador na nuvem, compartilhando o mesmo disco e sistema de arquivos. Eles não conseguem ver o histórico de conversas uns dos outros; a colaboração depende inteiramente da troca de arquivos no disco.

Ao se deparar com a autenticação de login, a abordagem correta é assumir o controle da tela diretamente no navegador em nuvem para inserir as credenciais, em vez de entregar a senha ao modelo. Ao mesmo tempo, esse computador em nuvem é essencialmente um contêiner temporário que pode ser reconstruído a qualquer momento; quando ocorrem atualizações subjacentes da plataforma ou manutenções executadas por administradores, os pacotes de software instalados manualmente são perdidos.

Este capítulo guiará você pelo funcionamento real desse computador em nuvem. Você aprenderá como alternar arquivos e telas com segurança entre múltiplos Bots, como rotear o tráfego de rede por meio do desktop local para lidar com restrições de listas de permissões e como usar um pipeline de backup leve e padronizado para recuperar rapidamente todo o ambiente de maneira organizada após uma redefinição.


![Computador em nuvem compartilhado: arquivos, navegador e assunção de controle](/info/05-computer.png)

## Mecanismo subjacente do computador compartilhado: uma máquina e múltiplos Bots

**Todos os Bots sob sua conta compartilham o mesmo computador Linux gerenciado.** Não importa para qual Bot você alterne, você estará lidando com o mesmo diretório raiz `/workspace` e disco persistente.

O histórico de chat é salvo externamente de forma independente; mesmo que você execute `rm -rf` para esvaziar a máquina ou ocorra uma falha e reinicialização do sistema, as conversas e listas permanecerão intactas.

**Criar um novo Bot não significa isolamento de segurança.** Qualquer Bot que obtenha permissões de linha de comando poderá ler e gravar todos os dados em `/workspace`. Nunca coloque informações confidenciais não criptografadas lá dentro.

Evolução de versões:
- v0.68.0: Suporte à remoção de outros computadores nas configurações
- v0.68.1 (Lançado em 07/10/2026): Resolução de tela aumentada de 1280×800 para 1920×1200, com resposta mais rápida em operações e capturas de tela
- v0.70.2: Adicionado e-mail dedicado, suporte para salvar páginas da web diretamente como PDF

Para detalhes subjacentes, consulte [《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

## Monitoramento de tela e status de trabalho de múltiplos Bots

### Status e configurações

**A barra lateral exibe permanentemente três tipos de status**:
- Requer atenção: aguardando resposta, aprovação ou transferência de controle.
- Atividade não lida: tarefas concluídas, aguardando visualização dos resultados.
- Em execução: executando scripts, coletando páginas da web ou chamando ferramentas.

Clique no nome na parte superior para acessar "Exibir detalhes da conversa", onde você pode alterar o nome, as tags e o avatar do Bot atual. Bots pessoais não possuem uma caixa de descrição separada; **basta enviar uma mensagem diretamente** para ajustar seu posicionamento.

### Monitoramento e notificações

Operações em nuvem suportam **visualização de tela em tempo real**.

**Quando em foco, as notificações são suprimidas automaticamente**, sendo marcadas como não lidas apenas na barra lateral e no Dock; quando estiver offline, você pode ativar notificações no arquivo de configuração para recebê-las no desktop ou no celular.

## Assunção de controle do navegador: transfira a tela, não a senha

![Assunção de controle do navegador: transfira a tela, não a senha](/info/05-computer-s3.png)

Não envie credenciais de login no chat. Você e o Bot compartilham o navegador: **transfira a tela, não a senha**.

### Etapas para assumir o controle

1. Pausa acionada: o Bot abre a página de login e pausa ao encontrar campos de usuário/senha, QR Code ou 2FA.
2. Assumir entrada: clique em tela cheia para assumir o teclado e o mouse.
3. Login manual: preencha o usuário e a senha por conta própria ou escaneie o código de autenticação.
4. Transferir execução: **após o login, notifique o Bot para reutilizar os cookies em sua execução**, sem expor senhas em texto puro.

### Portão de aprovação

Pressione `Cmd+,` e vá para as configurações em "Geral" - "Bot".

- **Conflitos de regras priorizam "Perguntar primeiro" (Ask first)**.
- Regras corporativas exibem `Required by your admin. You can't edit or delete this rule.` e não podem ser modificadas.
- A versão v0.70.2 reforçou as confirmações antes de enviar e-mails e postagens, realizar pagamentos e alterar ambientes de produção.

Para mais detalhes, consulte [Configurações e notificações](https://cursor.com/cn/docs/grok-bot/settings).

## Convenção de transferência de arquivos entre múltiplos Bots e planejamento de diretórios

### Modelo de colaboração por arquivos

Os Bots não conseguem ler o histórico de chat uns dos outros; **o único canal de colaboração entre múltiplos Bots são os arquivos em disco compartilhado**.

No prompt, basta informar o caminho do arquivo gerado pela etapa anterior. Para mais detalhes, consulte [《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

1. O organizador coleta dados e gera `tweets.md`
2. O analista refina as informações e gera `profile.md`
3. O designer gera `design.md` com base no perfil
4. O engenheiro lê o design e compila o código

### Planejamento de diretórios

Defina os diretórios desde a criação da máquina para evitar que múltiplos Bots desorganizem os arquivos.

| Caminho do diretório | Conteúdo armazenado | Padrão de gravação |
| --- | --- | --- |
| `/workspace/handoff/` | Artefatos intermediários | Markdown ou JSON padronizado, com prefixo da tarefa |
| `/workspace/projects/` | Código e ativos do projeto | Subdiretórios independentes por projeto, vinculados a repositórios Git |
| `/workspace/tools/` | Scripts locais desenvolvidos por você | Apenas código-fonte sem chaves, sincronizado com o repositório de backup após verificação |
| `~/.env` ou arquivos locais | Chaves de API | Salvar apenas localmente; **estritamente proibido enviar ao repositório de código ou exibir na sessão** |

### Limpeza de disco e Disk Saver

Se o sistema emitir os alertas `Computer is low on disk space` ou `Computer is critically low on disk space`, vá para a barra lateral e clique em "Go to Disk Saver" no **Disk Saver** para ver sugestões de limpeza.

**Ele nunca excluirá arquivos sem confirmação prévia**; caso recuse a limpeza, os arquivos existentes serão mantidos exatamente como estão.

## Saída de rede local: roteamento e acesso a redes privadas

![Saída de rede local: roteamento e acesso a redes privadas](/info/05-computer-s5.png)

Para resolver restrições de lista de permissões de IP de contas oficiais do WeChat, intranets corporativas ou acesso a redes locais, **basta intermediar o tráfego pelo dispositivo local**.

### Etapas de ativação
1. Pressione `Cmd+,` para entrar nas configurações e clique em **Computador**.
2. Em **Seu computador**, localize o computador atual e ative **Rotear tráfego através do computador atual**.

### Limitações e armadilhas a evitar
- Limitado a uma única máquina por vez. Externamente identificado como o IP local, permitindo que o Bot acesse a rede local diretamente.
- **Válido apenas para novas requisições**; conexões TCP longas existentes continuarão pela rota original.
- Se o administrador desativar `Allow Local Egress Routing`, a opção ficará esmaecida com a mensagem `Disabled by your admin. You can't turn this on.`, e a desconexão será forçada em até 5 minutos; consulte [Configurações e notificações](https://cursor.com/cn/docs/grok-bot/settings).
- `Execution on this computer` controla o shell local, com confirmação passo a passo por padrão; **nunca habilite o modo totalmente automático de forma imprudente**.

## Reconstrução, atualização e encerramento: o ciclo de vida do computador em nuvem

![Reconstrução, atualização e encerramento: o ciclo de vida do computador em nuvem](/info/05-computer-s6.png)

A reconstrução **limpa o ambiente instalado manualmente**, preservando o disco e o estado de login.

Consulte [Computador Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery) e [Gerenciar computadores Grok Bot](https://cursor.com/cn/docs/grok-bot/computers).

| Operação | O que é mantido | O que é limpo e armadilhas |
| - | - | - |
| Atualização de software | Tudo | Nenhum |
| Atualizar/Reconstruir | Disco e arquivos | Limpa ambiente instalado manualmente; reexecuta scripts |
| Encerrar VMs | Disco | Desligamento após 30 dias de inatividade perde o progresso |
| Recover/Reset | Dados salvos | Interrompe tarefas, perde código não salvo |

Quando exibir `Reconnecting`, **não clique cegamente em Reset**; siga a ordem de solução de problemas.

1. **Clique em Retry**. Durante a reconexão, o disco está intacto; cliques aleatórios danificam o estado atual.
2. **Encerre completamente**. No macOS, use `Cmd+Q` para sair e reiniciar; não clique apenas no botão vermelho de fechar.
3. **Verifique atualizações**. Acesse "Configurações" > "Computador" e atualize somente quando o Bot estiver ocioso.
4. **Priorize o Recover**. Se a opção aparecer, escolha-a primeiro para tentar salvar um snapshot.
5. **Por último, o Reset**. Redefina apenas após confirmar que não há código não salvo e que tudo o mais falhou.

## Pipeline de recuperação de desastres: registro geral de serviços e scripts de restauração idempotentes

![Pipeline de recuperação de desastres: registro geral de serviços e scripts de restauração idempotentes](/info/05-computer-s7.png)

Atualizações ou redefinições limpam o ambiente. 鐵柱AGI (@cgnot996) propôs uma solução em 10/10/2026: **fazer backup apenas do método de inicialização, sem salvar a máquina inteira**.

Ele usa um repositório privado de 5,1 MB para gerenciar 20 serviços de 10 Bots (18 itens com restauração obrigatória, incluindo 4 persistentes, 14 sob demanda e 2 itens de caminho de chaves); veja os detalhes no [tutorial](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye).

### Estrutura padronizada e registro

O repositório `vm-services` contém quatro partes:
- `REGISTRY.md` e `registry.json`: registro geral e configurações.
- `restore/restore-<服務名>.sh`: script de serviço individual, **deve ser idempotente**.
- `restore/restore-all.sh`: instala bibliotecas, CLIs e inicia serviços em segundo plano na ordem correta, contabilizando falhas.
- `service-src/`: arquivamento do código-fonte, excluindo `.env`, logs e ambientes virtuais.

O registro de novos serviços inclui estes itens: ID curto e Bot responsável; caminhos de código e de dados; método de instalação (apt/pip/npm/Docker) e dependências do sistema; comandos de inicialização e verificação (`--version` ou porta); se a restauração é obrigatória; caminho absoluto das chaves (**estritamente proibido registrar em texto puro**); etapas como leitura de QR Code ou OAuth.

### Dois conjuntos de prompts

Enviados ao Bot "Gerente de Serviços da Máquina Virtual", com o qual os demais Bots prestam contas de suas implantações.

::: details Prompt de implantação e registro
```text
你是「虛擬機器服務管家」，只管一件事：記下這台虛擬機器上部署過的所有第三方服務，並在電腦更新或換帳號之後，按記錄把它們原樣恢復。

你維護的東西：
1. 一份登記總帳，人和機器各讀一份：REGISTRY.md（表格）和 registry.json（給指令碼讀）。
2. 每個服務一個恢復指令碼 restore/restore-<服務>.sh，必須冪等，重複跑也不會出錯。
3. 一個總入口 restore/restore-all.sh，按依賴順序呼叫各個恢復指令碼，最後彙總哪些失敗了。
4. 一份原始碼備份 service-src/：各 Bot 自己寫的服務程式碼和指令碼，同步時排除密鑰、記錄、執行狀態、虛擬環境和個人資料，並先掃一遍明文密鑰，命中就停。
5. 以上全部跟著一個私有 Git 倉庫存（「你的備份倉庫地址」）。總帳、恢復指令碼、原始碼都在倉庫裡，密鑰永遠不進倉庫。

登記規則（其他 Bot 部署任何服務都必須來找你登記）：
每項必須包含：
- 名稱和短 id、用途、負責的 Bot
- 路徑：程式碼、組態、資料分別在哪
- 安裝方式和依賴（apt / pip / npm / Docker / 系統定時任務）
- 啟停命令、健康檢查命令
- 更新後的恢復步驟，或者對應的恢復指令碼
- 是否必恢復：是 / 否
- 密鑰：只寫存放路徑，絕不寫明文
- 需要真人完成的步驟（OAuth 登錄、掃碼、匯入 cookie）單獨標出來

你的工作方式：
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

Após a redefinição, configure as credenciais do Git e envie ao Bot de recuperação. **Os critérios de aceitação devem relatar os resultados, o tempo gasto e o status da verificação de acordo com a lista**.

::: details Prompt de restauração com um clique após redefinição
```text
這台電腦剛重置過（或者是換了新帳號），之前部署的服務都沒了。請按我的備份把它們恢復到可用狀態，規則如下。

備份在哪：
- 備份倉庫：<你的備份倉庫地址>，分支 <分支名>
- 倉庫裡有：登記總帳（REGISTRY.md 和 registry.json）、每個服務的恢復指令碼（restore/）、自寫服務的原始碼備份（service-src/）
- 倉庫裡沒有密鑰，這是故意的

請按這個順序做：
1. 把備份倉庫拉到工作目錄，先讀總帳，告訴我一共登記了幾項、哪些標了「必恢復」、哪些只留密鑰不用恢復。先列出來，不要動手。
2. 把自寫服務的原始碼從 service-src/ 放回總帳寫的原位置。只補缺失的，已經存在的目錄不要覆蓋。
3. 按總帳的依賴順序逐項恢復：先裝系統依賴（比如 cron、ffmpeg），再裝命令列工具，最後拉起常駐服務和定時任務。每項都用它自己的恢復指令碼，指令碼要能重複跑。
4. 每裝完一項就跑它登記的健康檢查。失敗了先看記錄、試著修一次；修不好就記下原因，接著做下一項，不要卡住。
5. 把需要我本人做的事彙總成一張清單：要重新提供的密鑰（只說放哪個路徑、叫什麼名字，別讓我把密鑰貼進聊天）、要重新登錄授權的工具（OAuth、掃碼、設備碼）。然後一項一項帶我做，每做完一項馬上覆查。
6. 故意暫停的任務保持暫停，總帳裡寫了原因和重開條件的照辦。別因為“看起來漏裝了”就自作主張打開。
7. 最後交驗收清單，每項一行：服務名、結果（成功 / 失敗 / 等我處理）、健康檢查輸出摘要、花了多久。再告訴我總共用了多少時間、成功了幾項。

不要做的事：
- 不要把任何密鑰寫進倉庫、記錄或聊天
- 不要跑總帳沒登記的安裝
- 不要用“重置電腦”當修復手段
- 恢復完如果有任何改動（路徑變了、版本升級了），更新總帳，提交推回備份倉庫
```
:::

## Armadilhas comuns

### Credenciais e permissões
- **Não cole chaves no chat**: insira manualmente na interface web; para tokens de CLI, grave-os em `~/.env` e faça os scripts lerem as variáveis de ambiente.
- **Sem isolamento entre Bots**: compartilham `/workspace` e permissões. Proteja ativos confidenciais com repositórios privados e aprovação manual; criar múltiplos Bots não resolve.

### Colaboração e dependências
- **A transferência deve ser gravada em disco**: os Bots não leem as sessões uns dos outros. Salve os resultados do Bot A como Markdown ou JSON; depender apenas de diálogo fará o Bot B alucinar.
- **Dependências não são persistentes**: atualizações, Recover ou Reset limparão o conteúdo instalado via `apt install` e `npm install -g`; pastas como `node_modules` e `.venv` também não são incluídas no backup.

  **O script de restauração deve incluir** `npm install` e `pip install -r requirements.txt`.

### Operação, manutenção e rede
- **Ao ver Reconnecting, não pressione Reset**: isso descartará alterações não salvas e forçará uma reconstrução; **tente novamente ou reinicie o cliente primeiro**.
- **Gerenciamento centralizado de tarefas agendadas**: o crontab deve ser mantido e unificado em um repositório Git.
- **Reinicialização necessária ao ativar roteamento local**: se o IP não mudar após ativar "Rotear tráfego através do computador atual", reinicie o processo.

## Como validar após a conclusão

1. O Bot A grava um timestamp em `/workspace/handoff/test.json`. Se o **Bot B ler e informar com precisão**, a comunicação está funcionando.
2. Em "Configurações" > "Computador", ative "Rotear tráfego através do computador atual" e execute `curl -s https://api.ipify.org` no terminal. **O IP externo deve coincidir com o local**, e não ser o IP do data center.
3. Peça ao Bot para abrir a página de login do GitHub: **ele deve pausar antes do campo de senha e solicitar a transferência de controle**. Faça o login manualmente e continue, confirmando que não há senhas em texto puro nos logs.
4. Confirme que o Git privado recebeu os commits de `REGISTRY.md`, `registry.json` e dos scripts. Em um diretório de teste, faça o clone/pull e execute:
```bash
bash restore/restore-all.sh
```
**Todas as verificações de integridade (health checks) devem passar**, sem erros de conflito, e os serviços do registro geral devem estar escutando normalmente.

## Leituras complementares

### Documentação oficial e base de conhecimento

- [Gerenciar computadores Grok Bot](https://cursor.com/cn/docs/grok-bot/computers): regras oficiais completas sobre reconstrução em lote de múltiplos computadores na versão Enterprise, encerramento e limpeza por inatividade de 30 dias.
- [Configurações e notificações](https://cursor.com/cn/docs/grok-bot/settings): instruções oficiais sobre configurações do aplicativo desktop, execução de comandos locais, roteamento de tráfego por relay e modo Auto-review.
- [Computador Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery): diferenças oficiais entre Update, Recover e Reset, acompanhadas de um checklist para solução de problemas.

### Referências práticas da comunidade

- [《4.6 Máquina Virtual, Memória e Backup》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg): detalhamento aprofundado da arquitetura subjacente do computador em nuvem, mapa de organização de contexto e colaboração de arquivos entre múltiplos Bots.
- [《Todas as ferramentas sumiram após a redefinição da VM do Grok Bot? Tutorial de backup e recuperação (com prompts inclusos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye): compartilhamento prático do autor da comunidade 鐵柱AGI (@cgnot996) sobre o design do Gerente de Serviços da Máquina Virtual, planilha de registro geral e restauração com um clique.

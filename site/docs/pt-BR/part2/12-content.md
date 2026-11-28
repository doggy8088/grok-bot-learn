# Capítulo 12 Caso: Mídia Própria e Equipe de Conteúdo

A IA conversacional perde facilmente o contexto; o **Grok Bot usa arquivos compartilhados em um computador na nuvem para executar pipelines**.

1. Escreva descrições de papéis e crie um banco de pautas com base em seis conjuntos de campos obrigatórios.
2. O Bot de pesquisa grava os cartões no diretório, e o Bot redator principal os lê para redigir os textos.
3. Implemente regras de revisão para eliminar o "tom de IA" e transforme posts em sites de perfil pessoal.
4. **Os pontos críticos de publicação devem passar por controle humano**, evitando dados falsos e controles de risco das plataformas.

## Design de Funções e Mecanismos de Colaboração para Equipes de Conteúdo

![Design de funções e mecanismos de colaboração para equipes de conteúdo](/info/12-content-s1.png)

### O que é

**Ao montar uma equipe no Grok Bot, o princípio central é "uma função, uma responsabilidade".** Todos os Bots da conta compartilham o mesmo computador na nuvem (com kernel, memória e caminho `/workspace` independentes), mas cada um possui sua própria janela, memória e configurações.

Os Bots realizam a passagem de tarefas lendo e gravando arquivos Markdown em pastas compartilhadas.

### Como fazer

**O Bot principal com estrela no avatar (clique com o botão direito no avatar para alternar)** é responsável pela coordenação e distribuição de tarefas, enquanto 5 a 6 Bots dedicados trabalham estritamente dentro dos limites de suas funções.

| Nome da função | Caminho de entrega | Principais responsabilidades e ações proibidas |
| :--- | :--- | :--- |
| Explorador de Inteligência | `/workspace/content-team/01-inbox/` | Coletar pistas de primeira mão. Estritamente proibido interagir, postar e enviar mensagens privadas; estritamente proibido tratar declarações de segunda mão como fatos |
| Planejador de Pautas | `/workspace/content-team/02-briefs/` | Avaliar pistas e gerar Briefs. Estritamente proibido navegar externamente; proibido avançar para o redator principal sem aprovação humana |
| Redator Principal | `/workspace/content-team/03-drafts/` | Escrever conforme o `voice.md`. Estritamente proibido fabricar fatos e usar tom genérico de relações públicas |
| Editor de Fatos | `/workspace/content-team/04-review/` | Verificar fontes primárias. Sem permissão de publicação; listar para confirmação quando houver conflito de evidências |
| Analista de Métricas | `/workspace/content-team/06-analysis/` | Analisar dados de conteúdo. Estritamente proibido interagir na conta; estritamente proibido transformar correlação em causalidade; estritamente proibido fazer suposições forçadas na ausência de dados |
| Engenheiro Web | `/workspace/tweet-portrait/` | Extrair perfis e criar sites. Estritamente proibido forjar experiências; estritamente proibido tratar caminhos locais como links públicos |

1. Crie a estrutura padrão de diretórios compartilhados no terminal do computador na nuvem.
::: details Como fazer
```text
/workspace/content-team/
├── 00-profile/     # 帳號定位、目標讀者、範文、禁用表達（voice.md）
├── 01-inbox/       # 情報偵察員的一手資訊卡
├── 02-briefs/      # 選題策劃師的選題 Brief
├── 03-drafts/      # 內容主筆的候選稿
├── 04-review/      # 事實編輯的審校稿
├── 05-published/   # 已發表文案存檔、資料截圖或 CSV
└── 06-analysis/    # 資料覆盤師的週報與實驗記錄
```
:::
2. Escreva a base de estilo em `00-profile/voice.md` para evitar que o redator principal produza clichês.
::: details Como fazer
```text
# 帳號定位
- 我長期寫：面向個人創業者與開發者的 AI 工具實測與提效工作流
- 我的目標讀者：正在用 AI 嘗試做獨立產品、做內容或做業務轉型的實幹者
- 讀者看完後應該獲得：直接能照著執行的步驟、準確的參數組態、明確的避坑提醒

# 寫作樣本
- 代表作 1：【粘貼一段自己資料最好、語言最順的代表作】
- 代表作 2：【粘貼一段帶步驟拆解的課程代表作】

# 表達習慣
- 常用語氣：像跟坐在對面的朋友覆盤經驗，冷靜、直白、短句為主
- 禁用表達：我的判斷是、毫無疑問、重塑格局、顛覆行業、進入新時代、不難看出
- 不會公開談論的內容：未經實測的空頭八卦、無法復現的玄學跑分

# 商業與事實邊界
- 必須保留原始來源的主張：所有關於產品上線、價格變動、官方改版的陳述
- 未親測時的寫法：必須明確標明“未核實”或“作者自述”
```
:::
3. **Crie o grupo e distribua as regras**. Clique em "Novo chat" para criar o chat em grupo "Equipe de Conteúdo de Mídia Própria" e adicione todos os membros. Na primeira vez, evite atribuir pautas diretamente; você deve primeiro enviar as normas unificadas.
```text
這是“自媒體內容團隊”協作群。工作順序固定為：情報偵察員 → 選題策劃師 → 內容主筆 → 事實編輯；內容發表後，資料覆盤師讀取授權資料 → 06-analysis。所有中間文件放到 /workspace/content-team/ 對應目錄。任何登錄、外發、發表、按讚、回覆、關注、私信、購買、刪除、連線器授權或權限修改都必須先獲得使用者明確批准。本次僅確認收到和各自交付路徑，不執行外部操作。
```

### O que define um bom resultado

> Fonte: [Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo](https://x.com/AdrianPunk115/status/2097311704547987756)  
> Autor: [Adrian Punk @AdrianPunk115](https://x.com/AdrianPunk115)

![Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo](/cases-img/fs26-0.jpg)

![Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo](/cases-img/fs26-1.jpg)

1. O Profile, as tags e as responsabilidades de longo prazo de cada Bot estão salvos, com listas claras de proibições.
2. A árvore de diretórios de `/workspace/content-team/` está completa, e `00-profile/voice.md` contém o posicionamento real e termos proibidos.
3. **Todos os membros responderam confirmando os caminhos de entrada/saída e os limites de controle humano**, e nenhum alega possuir permissões de postagem automática ou acesso externo à rede.

[《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

## Operação Prática do Fluxo Completo: Pauta, Redação, Imagens e Distribuição

![Operação prática do fluxo completo: pauta, redação, imagens e distribuição](/info/12-content-s2.png)

### Pautas e Inteligência: Coleta, Métricas e Análise de Motivação

> Fonte: [Como aproveitar o Grok Bot na criação de conteúdo](https://x.com/KinGao476942/status/2099736121781764594)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

Não procure temas conversando diretamente com modelos genéricos; eles só fornecerão notícias desatualizadas. Aqui, fazemos o Bot de inteligência simular buscas ou monitorar o mercado, organizando as pistas em cartões.

Primeiro, configure o prompt de função permanente para o explorador:

::: details Pautas e inteligência: coleta, métricas e análise de motivação
```text
你是我的情報偵察員（Scout）。唯一職責是發現、核驗並沉澱可用於選題的公開資訊，為後續選題提供證據；不寫成稿，不替使用者下結論。

【允許使用】
- 公共互聯網中的官方公告、產品文件、論文、GitHub Release、作者原文與使用者提供材料。
- 知乎、微博、X、小紅書等平台的公開頁面、公開帖子和公開評論區，可用於搜尋線索、觀察討論和摘錄公開資訊。
- 共享目錄 /workspace/content-team/00-profile/ 與 /workspace/content-team/01-inbox/。
- 如頁面要求登錄、密碼、驗證碼、2FA、passkey，或需要擴大權限，必須立即停下並請求使用者接管。

【禁止】
- 不得發文、改帖、刪帖、按讚、轉發、收藏、關注、取關、評論、回覆或私信。
- 不得讀取私信、好友可見內容、非公開頁面或與任務無關的個人資料。
- 不得把平台使用者發言、熱榜或搜尋摘要直接當成已確認事實；它們只能標為“平台線索”或“觀點”，關鍵主張必須回到官方原文、一手材料或當事人公開內容核驗。
- 不得憑記憶補數位、日期、引語或因果。
- 不得索取或記錄帳號密碼與驗證碼。
- 不得執行本機命令，不得訪問本機文件。

【固定交付】
寫入 /workspace/content-team/01-inbox/YYYY-MM-DD.md，每次最多 8 條。每條包含：事實或平台線索、來源平台、原始連結、證據摘錄、討論熱度或代表性觀點、為什麼值得關注、一個待核查問題、核驗狀態。
```
:::

**O banco de pautas deve seguir rigorosamente seis conjuntos de campos obrigatórios**; se faltar um, descarte-o imediatamente:
- Fonte e atualidade: link permanente funcional do post original, data de publicação e tempo decorrido até agora; não escreva "certo criador".
- Dados visíveis: visualizações/reproduções, curtidas, compartilhamentos e comentários (total de 4 itens), além do horário de coleta. Se não encontrar, marque como "dados públicos não encontrados"; estimativas são estritamente proibidas.
- Segmentação do autor: registre handle, número de seguidores e nível. Para contas pequenas com posts virais, estude a estrutura; para grandes influenciadores, analise as pautas.
- Segmentação da comunidade: classifique claramente como oficial, nacional ou internacional.
- Justificativa de adequação e ângulo de execução: conecte com seus pontos fortes e especifique ações concretas (como testes práticos, detalhamento de passos ou criação de templates); não use termos vagos como "está bombando".
- Análise de motivação: abrange dores, pontos de prazer e motivações de interação. Deduções sem suporte de dados devem ser marcadas com "[Inferência]" ao final.

O planejador seleciona 3 pautas de alto valor de `01-inbox/`, filtra pelos três critérios (fatos específicos, relevância para o leitor e capacidade do autor de agregar valor) para gerar o Brief e grava em `02-briefs/`:

```text
讀取今天 01-inbox 中已經核驗的線索，按照帳號定位篩選 3 個候選題，寫入 02-briefs/YYYY-MM-DD.md。每題包含：一句話事實、讀者場景、單一主角度、原始連結與證據、資訊缺口、建議內容形式、給主筆的寫作任務。證據不足的題直接標“待補證”。完成後停下，等待我批准，不要通知內容主筆。
```

Se você travar na estruturação, use um prompt de entrevista para que o Bot principal faça perguntas e ajude a esclarecer suas necessidades:

::: details Pautas e inteligência: coleta, métricas e análise de motivação
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

**Critérios de aceitação**
- Todos os links originais estão funcionando e os fatos principais contam com suporte do texto original.
- Pistas sem evidências suficientes são marcadas como "aguardando comprovação"; **nenhuma avança para o redator sem aprovação humana formal**.

[《Como aproveitar o Grok Bot na criação de conteúdo | Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf); [《Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Redação e Copywriting: Remoção do "Tom de IA" e Saída Estruturada

Ao escrever o primeiro rascunho, mude o foco do sujeito de "o que o produto tem" para "como isso ajuda o leitor", **garantindo que o leitor veja um ganho claro de informação nos primeiros três segundos**.

Os textos podem adotar diretamente duas estruturas comprovadas:
- A fórmula HKRR de Tim (MediaStorm): engloba humor/alegria, conhecimento, conexão emocional e ritmo. Cada post deve dominar com firmeza pelo menos um elemento; cobrir dois é excelente; não cobrir nenhum significa descarte imediato.
- As motivações de compartilhamento de Pan Luan: centradas em "isto me diz respeito", mudando o sujeito para o leitor. Por exemplo, em vez de escrever "o software foi atualizado", escreva "você economizou duas horas por dia procurando pautas". Estruturas virais podem ser reutilizadas; copie o ritmo, não o conteúdo.

Defina regras de redação e restrições claras para o redator principal:

::: details Redação e copywriting: remoção do "tom de IA" e saída estruturada
```text
你是我的內容主筆（Writer）。唯一職責是把已經批准的 brief 寫成候選稿；不負責找熱點、補事實、決定選題或發表。

【允許使用】
- /workspace/content-team/00-profile/voice.md 中的定位、範文、禁用句式與術語。
- /workspace/content-team/02-briefs/ 中已經批准的事實、連結、角度和限制。
- 輸出到 /workspace/content-team/03-drafts/。

【禁止】
- 不得自行瀏覽外部網站、登錄平台或呼叫連線器。
- 不得自行補充數位、引語、案例、比較級或因果。
- 不得偽裝親測、內幕或使用者回饋。
- 不得發送、發表、購買、刪除或修改權限。
- 不得執行本機命令，不得訪問本機文件。

【寫作規則】
前兩句說清發生了什麼，再寫具體後果、使用場景、矛盾或尚未解決的問題。觀點必須從 brief 中的事實長出來。段落以 2–4 句為主，句子長短交替，保留自然停頓。

【禁用表達】
“我的判斷是”“真正有價值的是”“這說明”“這意味著”“毫無疑問”“重塑格局”“進入新時代”，以及空泛三段式、硬湊金句、廣告腔和故作深刻的反問。

【固定交付】
按任務需要輸出：A. 140–220 字中文短帖；B. 280–420 字展開版；C. 僅在適合時給 3–5 條串文大綱；D. 使用者明確要求時寫長文。每份稿末附“事實依據”和“仍需確認”。完成後寫入 /workspace/content-team/03-drafts/YYYY-MM-DD-題目.md，並只彙報文件路徑。
```
:::

Após a conclusão do primeiro rascunho, o editor de fatos faz a revisão. **O editor de fatos apenas verifica as afirmações e elimina o tom de IA**, sem adicionar novos pontos de vista e sem permissões de publicação:

::: details Redação e copywriting: remoção do "tom de IA" e saída estruturada
```text
你是我的事實編輯（Editor），負責發表前的事實核驗、結構檢查和風格審校。你只做讓內容可信、清楚、像真人表達所必需的修改；你沒有發表權限。

【允許使用】
- /workspace/content-team/00-profile/voice.md、/02-briefs/ 與 /03-drafts/。
- brief 中列出的原始公開連結，僅用於複核關鍵事實。
- 輸出到 /workspace/content-team/04-review/。

【審稿原則】
1. 沒看過原始材料的人也能讀懂。
2. 一手來源足以支撐關鍵事實。
3. 事實、觀點和假設明確分開。
4. 刪除樣板腔、廣告腔、絕對化和生硬縮略語。
5. 不讓讀者誤以為作者親測、掌握內幕或獲得使用者回饋。
6. 無法核對的句子必須刪除、改成疑問或標記“待確認”。

【固定交付】
寫入 /workspace/content-team/04-review/YYYY-MM-DD-題目.md，包含：可發表候選版本、改動說明、風險標記、仍需人工確認、原始來源清單。完成後只彙報文件路徑和是否達到“可發表候選”標準。
```
:::

**Critérios de aceitação**
- As duas primeiras frases do texto vão direto aos fatos centrais, sem enrolação.
- O editor de fatos confere cada item com os links primários; o que não puder ser verificado é marcado como "a confirmar" ou excluído diretamente.
- O rascunho revisado é movido para o diretório `04-review/`, aguardando a aprovação humana final.

[《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Imagens e Apresentação Visual: Criação de Sites via Código e Montagem de Materiais

> Fonte: [Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot](https://x.com/0xlangeai/status/2109115005069341175)  
> Autor: [Lange AI @0xlangeai](https://x.com/0xlangeai)

![Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot](/cases-img/fs32-0.jpg)

![Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot](/cases-img/fs32-1.jpg)

Para ilustrar postagens em mídias sociais, evite pedir à IA para desenhar imagens conceituais genéricas, cheias de aspecto artificial ("plástico"). Na prática, costuma-se seguir dois caminhos sólidos:

**Caminho 1: Transformar posts em um site de perfil pessoal (solução de Lange AI)**
No grupo "Site de Perfil de Posts", 4 Bots trabalham em revezamento, armazenando arquivos intermediários em `/workspace/tweet-portrait/`:
1. O organizador de posts coleta postagens históricas, e o analista de perfil extrai hábitos de expressão e contrastes marcantes.
2. O designer do site propõe o layout visual, e o engenheiro web escreve o código front-end com adaptação para dispositivos móveis.

Os dois primeiros papéis executam os prompts em sequência:

```text
【推文整理員任務】
確認我自己已綁定的 X 帳號身份，讀取最近 90 天內最多 100 條本人內容，包括原創、帶有本人評論的引用推文和本人回覆，排除純轉發。
建立一個名為 tweet-portrait 的共用專案目錄，將素材保存為 tweets.md。每條保留正文、日期、連結和內容型別，並註明實際讀取範圍、數量與缺失情況。
完成後返回帳號名稱、專案目錄及素材文件的完整路徑。無法訪問時告訴我具體原因，不補造內容。
```

```text
【個人畫像分析師任務】
讀取共用專案目錄中的 tweets.md，提煉最有辨識度的 3—5 個特點，覆蓋關注主題、表達風格、語言習慣、典型觀點或有趣反差。
每個特點附 1—2 條真實推文依據，保留摘錄、日期和連結，區分觀察與推測。不要寫通用讚美或沒有依據的人格結論。
保存為 profile.md，在群裡彙報最有意思的特點和需要我確認的判斷，完成後等我檢查。
```

Os dois últimos papéis executam os prompts de design e código:

```text
【畫像網站設計師任務】
讀取共用目錄中經過我檢查的 profile.md，提出兩個明顯不同的個人畫像網站設計方向。
分別說明首頁如何呈現、包含哪些內容、排版和配色如何對應推文特點。保留原文依據，不生成沒有統計基礎的百分比或人格分數。
先把方向說明發給我，方便選擇；需要用圖說明時同時提供我可以查看的圖片或文件。
選定後，把最終頁面內容、結構、視覺和手機端安排保存為共用目錄中的 design.md。
```

```text
【畫像網站工程師任務】
讀取共用專案目錄中的 profile.md 和 design.md，按選定方案建立可以執行的個人畫像網站，文件放在專案目錄內。
保留推文依據和原文連結。打開頁面檢查桌面端與手機端，修復排版、內容和連結問題。
返回我能打開的預覽及實際截圖，先等待我檢查，再進行發表。
```

Verifique na prévia local o texto da primeira dobra, o espaçamento dos cartões e a exibição mobile; após a confirmação, solicite ao engenheiro que empacote o projeto e **faça o push para o Vercel ou Cloudflare Pages para entrar no ar**.

**Caminho 2: Montagem parametrizada e recortes de áudio/vídeo (solução de 鐵柱AGI / ferramentas oficiais)**
- Personagens e figurinos: use o sistema paper doll com dados de jogos; o Bot analisa os parâmetros e chama APIs de terceiros para a montagem.
- Cortes de vídeo: use o modelo oficial de Clip Bot; insira diretamente o link longo de áudio/vídeo para gerar automaticamente a transcrição com marcações de tempo e recortar os trechos principais.

**Critérios de aceitação**
- A prévia local apresenta diagramação organizada, e a adaptação mobile funciona normalmente.
- Todos os posts citados possuem links originais funcionais e navegáveis.
- A página reflete fielmente as expressões reais, sem inventar currículo ou experiências.

[《Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh); [《Coletânea de Posts de 鐵柱AGI ③: Métodos Práticos e Casos de Uso》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

### Distribuição, Retrospectiva e Auditoria: Controle Humano e Fluxo Escalonado

Iniciantes costumam buscar automação total sem supervisão, o que leva facilmente ao banimento da conta. **É estritamente proibido usar o navegador dentro da máquina virtual do computador na nuvem para publicar posts**, pois o controle de risco da plataforma detecta a impressão digital da VM. A postagem deve ter um controle humano absoluto e ser feita manualmente pelo próprio criador em um dispositivo físico local.

A colaboração em equipe adota o método de horários desfasados, sem necessidade de monitorar a tela o dia todo:
- Banco de pautas definido semanalmente: gaste 30 minutos por semana escolhendo os cartões candidatos na planilha e marcando os aprovados.
- Rascunhos revisados diariamente: o criador gasta 10 minutos por dia lendo os textos em `04-review/` e adicionando uma reflexão pessoal.
- Fluxo por quadro de status: gerencie na planilha os estados "pendente de revisão", "em redação", "finalizado" e "publicado".

Após o conteúdo ser publicado, encarregue o analista de métricas de fazer uma análise semanal em modo somente leitura; postagens em nome do usuário ou interações são estritamente proibidas:

::: details Distribuição, retrospectiva e auditoria: controle humano e fluxo escalonado
```text
你是我的 X 資料覆盤師（Analyst）。唯一職責是分析使用者自己的 X 內容質量、帖子表現和可執行的改進方向；唯讀，不代表使用者進行任何互動或帳號操作。

【允許使用】
- 使用者在任務中明確指定的個人 X 主頁，以及該帳號公開可見的帖子。
- 使用者主動提供或授權查看的 X Analytics 頁面、CSV 匯出和截圖。
- /workspace/content-team/03-drafts/、/04-review/、/05-published/ 與 /06-analysis/。
- 如頁面要求登錄、密碼、驗證碼、2FA 或 passkey，立即停下並請使用者接管；不得索取或記錄憑據。

【絕對禁止】
- 不得發文、改帖、刪帖、按讚、轉發、收藏、關注、取關、評論或私信。
- 不得修改頭像、簡介、帳號設定、隱私設定或權限。
- 不得讀取、複製或分析私信與非本任務所需的個人資料。
- 不得把瀏覽量相關性寫成因果，不得補全缺失指標。
- 不得執行本機命令，不得訪問本機文件。

【固定交付】
每週寫入 /workspace/content-team/06-analysis/weekly-review-YYYY-WW.md，包含資料來源、時間範圍、樣本量、表現最好與最差的帖子、內容質量診斷、3 條改進建議、2 個下週實驗、資料缺口。需要在 /workspace/content-team/05-published/ 留存所用 CSV 或截圖的檔名，不復制帳號憑據。
```
:::

Para uma retrospectiva pontual de um período específico, envie a instrução diretamente:

```text
唯讀分析我明確指定的個人 X 主頁【主頁地址】，時間範圍為【開始日期—結束日期】。資料來源為【公開主頁 / X Analytics / CSV / 截圖】。

先列出資料範圍和缺失欄位，再按主題、內容形式、長度、發表時間和開頭型別做對比。給 3 條有具體帖子或指標支撐的改進建議，並設計 2 個一次只改變一個變數的下週實驗。

禁止發文、改帖、刪帖、按讚、轉發、收藏、關注、取關、評論、私信和修改帳號設定。遇到登錄、驗證碼、2FA、passkey 或擴大權限時立即停下，等我接管。完成後寫入 06-analysis，並只回覆文件路徑、覆蓋帖子數和缺失資料。
```

**Critérios de aceitação**
- Publicação manual feita por pessoa real em dispositivo local, com risco zero de bloqueio por controle de risco.
- Os dados da retrospectiva podem ser rastreados até os arquivos de exportação originais.
- **Não tire conclusões precipitadas quando o tamanho da amostra for inferior a 10 itens**.
- O planejamento da semana seguinte inclui 2 testes controlados de variável única (por exemplo, comparar o impacto de diferentes contagens de caracteres na taxa de engajamento).

[《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd); [《Como aproveitar o Grok Bot na criação de conteúdo | Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

## Análise Detalhada de Casos Práticos Típicos

![Análise detalhada de casos práticos típicos](/info/12-content-s3.png)

### Caso 1: A Equipe Fechada de 5 Pessoas para Mídia Própria de Adrian Punk

Adrian Punk (@AdrianPunk115) estruturou uma equipe permanente de 5 papéis no desktop, completando o ciclo fechado desde a coleta de fontes primárias, pauta, redação e revisão até a retrospectiva.

1. **Restrição prévia de permissões**: nas configurações do cliente, defina "Executar neste computador" como "Nunca permitir"; proíba explicitamente nos prompts a publicação não autorizada, a inserção de senhas e a invocação de conectores.
2. **Construção de caminhos de arquivos**: crie `/workspace/content-team/` e seus 7 subdiretórios no computador na nuvem; inclua o estilo da conta, trabalhos representativos e palavras proibidas em `00-profile/voice.md`.
3. **Divisão dedicada de trabalho**: crie o Explorador de Inteligência, Planejador de Pautas, Redator Principal, Editor de Fatos e Analista de Métricas, delimitando rigorosamente os diretórios de entrada e saída de cada função.
4. **Regras de transição**: envie o comando de inicialização no grupo "Equipe de Conteúdo de Mídia Própria"; os resultados dos estágios anteriores são salvos em Markdown para leitura pelos estágios seguintes, e **nenhuma etapa pode avançar sem aprovação humana prévia**.

Atenção: os 5 Bots compartilham o mesmo computador na nuvem sem isolamento por sandbox, portanto as permissões dependem estritamente de limites claros entre as funções; **o editor de fatos deve comparar os links originais de forma independente**, filtrando números inventados pelo redator e o tom corporativo de relações públicas.

[《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Caso 2: O Banco Duplo de Pautas Virais para Posts e Vídeos de Kin

> Fonte: [Como engenheiros podem aproveitar melhor o Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![Como engenheiros podem aproveitar melhor o Grok Bot?](/cases-img/fs25-0.jpg)

![Como engenheiros podem aproveitar melhor o Grok Bot?](/cases-img/fs25-1.jpg)

Kin (@KinGao476942, embaixador da SpaceXAI na China) conquistou mais de 2.000 seguidores no Twitter em cerca de 10 dias, gerenciou contas com mais de um milhão de seguidores no WeChat Channels e construiu um Bot operacional para o Twitter juntamente com o banco de pautas virais "Xiao Deng Talk".

1. **Criação do cartão de identidade**: defina claramente o posicionamento, contas de referência e áreas proibidas; proíba postagens automáticas. **Se os dados não forem encontrados, é obrigatório registrar "não encontrado", sendo estritamente proibido estimar ou inventar**.
2. **Feedback com dados reais**: coletou mais de 100 posts históricos e identificou que textos de 200 a 500 caracteres possuem uma mediana de leitura mais alta, e etapas numeradas geram significativamente mais curtidas.
3. **Banco de pautas com seis campos**: criou uma tabela com link permanente do post original, horário de coleta, dados reais, segmentação de seguidores, segmentação de comunidade e análise de motivação, sincronizando com um quadro no Notion para filtragem.
4. **Desconstrução de estrutura**: desconstruiu conteúdos virais com base na HKRR (felicidade, conhecimento, ressonância e ritmo) e nas três motivações de Pan Luan; copie a estrutura, não o conteúdo.

Atenção: na fase inicial de crescimento da conta, a frequência alta de publicação supera o polimento excessivo; ao terminar de escrever, verifique se o sujeito atende aos interesses do leitor.

[《Como aproveitar o Grok Bot na criação de conteúdo | Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

### Caso 3: O Site de Perfil Pessoal a partir de Posts de Lange AI

Lange AI (@0xlangeai) coletou postagens históricas da conta vinculada do X, extraiu o estilo pessoal e contrastes marcantes, e colocou no ar de forma automatizada um site de exibição de perfil pessoal.

1. **Definição de Bots dedicados**: configurou 4 funções no grupo de projeto "Site de Perfil de Posts": Organizador de Posts, Analista de Perfil Pessoal, Designer do Site de Perfil e Engenheiro do Site de Perfil.
2. **Extração e análise**: o organizador leu até 100 posts originais, citações com comentários e respostas dos últimos 90 dias, salvando em `tweets.md`; o analista extraiu de 3 a 5 contrastes de expressão e suas fontes, corrigidos pelo criador.
3. **Design e deploy**: o designer gerou `design.md` (adotando o estilo de cartões de portfólio), e **o engenheiro escreveu o código no computador na nuvem, concluiu a autoinspeção em ambas as plataformas (desktop e mobile) e auxiliou no deploy no Vercel ou Cloudflare Pages**.

Atenção: o histórico de postagens é um corpus pronto; **cada etapa — organização, análise, design e engenharia — exige confirmação do criador antes de avançar para a próxima**, evitando a amplificação cumulativa de desvios.

[《Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)

### Caso 4: Coleta Ininterrupta 24/7 e Fluxo Automatizado em Tabelas Multidimensionais por xilo

> Fonte: [Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]](https://x.com/xilo2991/status/2109613437215293905)  
> Autor: [xilo @xilo2991](https://x.com/xilo2991)

![Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]](/cases-img/fs36-0.jpg)

![Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]](/cases-img/fs36-1.jpg)

xilo (@xilo2991) aproveitou a execução 24 horas ininterruptas do computador na nuvem para estruturar um pipeline contínuo de coleta de conteúdos virais, sincronizando em tempo real com tabelas multidimensionais do Feishu (Bitable).

1. **Definição dos três elementos**: estabeleça claramente os canais, contas de referência e palavras-chave, e a tabela de armazenamento dos resultados.
2. **Integração com a tabela**: enviou o repositório GitHub do plugin do Feishu para o Bot, concluiu a configuração e autenticação no computador na nuvem e utilizou a tabela como barramento de colaboração.
3. **Mitigação de risco e descarte**: controlou a frequência durante as buscas para simular navegação normal; registrou o número de pesquisas e a probabilidade de viralização, **eliminando automaticamente palavras-chave ineficazes na retrospectiva semanal**.
4. **Alinhamento via entrevista**: enviou prompts de entrevista investigativa passo a passo para o Bot principal, alinhando detalhes operacionais antes de gerar automaticamente as configurações.

Atenção: a postagem 100% automática foi reduzida para aprovação humana semiautomática, equilibrando eficiência e segurança.

[《Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Caso 5: Funções Dedicadas, Integração Multidispositivo e Prevenção de Banimento na Infraestrutura por 鐵柱AGI

> Fonte: [Grok Bot Webhook + Atalhos: Construção de pipeline automatizado para catalogação de conhecimento](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [鐵柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + Atalhos: Construção de pipeline automatizado para catalogação de conhecimento](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + Atalhos: Construção de pipeline automatizado para catalogação de conhecimento](/cases-img/fs06-1.jpg)

鐵柱AGI (@cgnot996) testou sistematicamente os limites dos Bots, consolidando planos de prevenção contra banimento e recuperação de desastres.

1. **Função única e dedicada**: dividiu as tarefas em Bots de função única, como inspeção de código, captura de artigos e arquivo financeiro, abandonando a ideia de um Bot "faz-tudo".
2. **Entrada ultrarrápida**: configurou o app Atalhos no celular para ler a área de transferência e enviar diretamente via Webhook para o Bot no computador na nuvem, registrando os dados na tabela.
3. **Linha vermelha antibanimento**: **simular postagens pelo navegador na máquina virtual causa banimento com extrema facilidade; interações públicas externas devem ser realizadas por uma pessoa real em um dispositivo físico**.
4. **Recuperação de desastres**: como a recriação do computador na nuvem apaga ambientes não persistentes, crie scripts Shell de recuperação automática e configure um Memory Manager Bot para fazer backup periódico de prompts e configurações.

Atenção: **configurações críticas e comandos de instalação devem ser consolidados em scripts de recuperação que possam ser executados com um clique**; o computador na nuvem não deve ser considerado um servidor perfeitamente estável.

[《Coletânea de Posts de 鐵柱AGI ③: Métodos Práticos e Casos de Uso》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

## Armadilhas Comuns

1. Publicar a partir do computador na nuvem expõe a impressão digital e leva ao banimento; a automação total também costuma postar conteúdo inadequado. **Postagens, curtidas e mensagens privadas devem ser feitas manualmente em um dispositivo físico real**.
2. Defina **regras rígidas na descrição das funções: sem dados, marque como "não encontrado"; deduções devem ser rotuladas como "[Inferência]"**, evitando a entrada de dados falsos no banco.
3. A reinicialização do computador na nuvem limpa as dependências. **Salve os scripts Shell de recuperação em um diretório persistente** para uso preventivo.
4. Nas tarefas de Routine, **verifique com atenção a periodicidade de execução**, evitando configurar acidentalmente "apenas em dias úteis", o que causaria interrupções nos fins de semana.
5. A ausência de filtragem de cenas/storyboard já causou quedas de mais de 40% na cota semanal; **é estritamente proibido fazer polling frequente sem atividade útil; otimize os momentos de disparo**.

Planos a partir de 12 de outubro de 2026:
|Plano|Custo|Cota|Inclui Bot|
|-|-|-|-|
|Plus|$8/mês|-|Não|
|Premium|$30/mês ou $300/ano|4x|Sim|
|Super|$100/mês ou $1000/ano|15x|Sim|
|Ultra|$200/mês ou $2000/ano|50x|Sim|

## Como Fazer a Validação Final

### Permissões e Diretórios
1. Acesse as configurações da conta em "Geral → Agent → Executar neste computador"; **o status deve ser obrigatoriamente "Nunca permitir"**. Os Bots são estritamente proibidos de postar automaticamente e realizar pagamentos, e não devem inventar dados.
2. Verifique os 7 subdiretórios sob `/workspace/content-team/` e preencha o posicionamento da conta, modelos e palavras proibidas em `00-profile/voice.md`.

### Coleta, Redação e Ensaios
1. Colete 3 pistas e **faça amostragem de 2 links para garantir que estejam acessíveis e fundamentados no texto original**; em caso de ausência de dados, sinalize como "dados públicos não encontrados", sem adivinhar números ou contagem de seguidores.
2. Após aprovar o Brief, elabore o primeiro rascunho; as duas primeiras frases devem apresentar diretamente o fato central, os parágrafos devem manter de 2 a 4 frases, o final do texto deve incluir a base factual e itens pendentes de confirmação, evitando completamente palavras proibidas.
3. O rascunho revisado apenas verifica sem adicionar novos argumentos, e **nunca é publicado externamente sem comando humano**. Execute `restore.sh` uma vez no ambiente de teste para checar se o ambiente de dependências está devidamente pronto.

## Leituras Complementares

### Documentação Oficial
- [Planos e Cobrança](https://cursor.com/cn/help/grok-bot/plans.md)
- [Equipes de Bots e Colaboração](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Ambiente e Configuração do Computador na Nuvem](https://cursor.com/cn/docs/grok-bot/computers.md)
- [Colaboração em Chats em Grupo](https://cursor.com/cn/help/grok-bot/group-chats.md)
- [Rotinas e Automação](https://cursor.com/cn/help/grok-bot/routines.md)

### Fontes Práticas da Comunidade
- [《Construindo uma equipe de mídia própria com o Grok Bot: tutorial passo a passo | Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)
- [《Como aproveitar o Grok Bot na criação de conteúdo | Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)
- [《Transforme seus posts em um site de perfil pessoal: tutorial passo a passo da análise de características ao deploy com o Grok Bot》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)
- [《Construindo uma equipe de agentes 100% automatizada do zero: o fluxo completo do Grok Bot, da ativação à colaboração multi-IA [Guia Completo]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- [《Coletânea de Posts de 鐵柱AGI ③: Métodos Práticos e Casos de Uso》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

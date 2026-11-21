# Capítulo 12 Caso práctico: Medios digitales y equipos de contenido

La IA conversacional suele perder contexto; **Grok Bot utiliza archivos compartidos en una computadora en la nube para ejecutar pipelines**.

1. Redactar descripciones de roles y construir un banco de temas basado en seis grupos de campos obligatorios.
2. El Bot de investigación escribe fichas en el directorio, y el Bot redactor principal las lee para redactar el borrador.
3. Implementar reglas de corrección para eliminar el tono robótico de IA y transformar publicaciones en un sitio web de perfil personal.
4. **Los puntos clave de publicación deben contar obligatoriamente con supervisión humana**, evitando datos falsos y controles de riesgo de las plataformas.

## Diseño de puestos y mecanismos de colaboración en el equipo de contenido

![Diseño de puestos y mecanismos de colaboración en el equipo de contenido](/info/12-content-s1.png)

### Qué es

**Al crear un equipo en Grok Bot, el núcleo es «un puesto, una sola responsabilidad».** Todos los Bots bajo la misma cuenta comparten la misma computadora en la nube (con kernel independiente, memoria y la ruta `/workspace`), pero cada uno cuenta con ventanas, memoria y configuraciones independientes.

Los Bots se traspasan tareas leyendo y escribiendo archivos Markdown en carpetas compartidas.

### Cómo hacerlo

El **Bot principal con una estrella en su avatar (clic derecho en el avatar para alternar)** se encarga de coordinar y asignar tareas, mientras que de 5 a 6 Bots dedicados trabajan estrictamente dentro de los límites de sus responsabilidades.

| Nombre del puesto | Ruta de entrega | Responsabilidades clave y acciones prohibidas |
| :--- | :--- | :--- |
| Explorador de inteligencia | `/workspace/content-team/01-inbox/` | Recopilar pistas de primera mano. Prohibido interactuar, publicar y enviar mensajes directos; estrictamente prohibido tratar comentarios de segunda mano como hechos |
| Planificador de temas | `/workspace/content-team/02-briefs/` | Evaluar pistas y generar Briefs. Prohibido navegar externamente; no avanzar al redactor principal sin aprobación humana |
| Redactor principal | `/workspace/content-team/03-drafts/` | Escribir según `voice.md`. Prohibido inventar hechos y usar tono genérico de relaciones públicas |
| Editor de hechos | `/workspace/content-team/04-review/` | Verificar fuentes de primera mano. Sin permisos de publicación; listar conflictos de evidencia como pendientes de confirmación |
| Analista de métricas | `/workspace/content-team/06-analysis/` | Analizar métricas de contenido. Prohibido interactuar desde la cuenta, convertir correlaciones en causalidad o hacer conjeturas ante la falta de datos |
| Ingeniero web | `/workspace/tweet-portrait/` | Sintetizar el perfil y crear el sitio. Prohibido falsificar experiencias o tratar rutas locales como enlaces públicos |

1. Crear la estructura estándar de directorios compartidos en la terminal de la computadora en la nube.
::: details Cómo hacerlo
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
2. Escribir la base de estilo en `00-profile/voice.md` para evitar que el redactor principal genere clichés.
::: details Cómo hacerlo
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
3. **Crear el grupo y distribuir las reglas**. Haz clic en «Nuevo chat» para crear el grupo «Equipo de contenido digital» e incorpora a todos los miembros. La primera vez, evita asignar temas directamente; primero debes enviar las normas unificadas.
```text
這是“自媒體內容團隊”協作群。工作順序固定為：情報偵察員 → 選題策劃師 → 內容主筆 → 事實編輯；內容發表後，資料覆盤師讀取授權資料 → 06-analysis。所有中間文件放到 /workspace/content-team/ 對應目錄。任何登錄、外發、發表、按讚、回覆、關注、私信、購買、刪除、連線器授權或權限修改都必須先獲得使用者明確批准。本次僅確認收到和各自交付路徑，不執行外部操作。
```

### Criterios de éxito

> Fuente: [Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso](https://x.com/AdrianPunk115/status/2097311704547987756)  
> Autor: [Adrian Punk @AdrianPunk115](https://x.com/AdrianPunk115)

![Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso](/cases-img/fs26-0.jpg)

![Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso](/cases-img/fs26-1.jpg)

1. El perfil, las etiquetas y las responsabilidades a largo plazo de cada Bot están guardados, y la lista de prohibiciones es clara.
2. El árbol de directorios de `/workspace/content-team/` está completo, y en `00-profile/voice.md` se han registrado el posicionamiento real y las palabras prohibidas.
3. **Todos los miembros han respondido confirmando sus rutas de entrada/salida y los límites de supervisión humana**, y ninguno afirma tener permisos para publicar automáticamente o acceder a redes externas.

[《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

## Práctica de todo el flujo: Selección de temas, redacción, imágenes y distribución

![Práctica de todo el flujo: Selección de temas, redacción, imágenes y distribución](/info/12-content-s2.png)

### Selección de temas e inteligencia: Extracción, métricas y desglose de motivaciones

> Fuente: [Cómo aprovechar Grok Bot para creadores de contenido](https://x.com/KinGao476942/status/2099736121781764594)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

Para buscar temas, no converses directamente con un modelo generalista: solo arrojará noticias desactualizadas. En su lugar, haz que el Bot explorador simule búsquedas o monitoree tendencias y organice las pistas en fichas.

Configura primero el prompt de rol permanente para el explorador:

::: details Selección de temas e inteligencia: Extracción, métricas y desglose de motivaciones
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

**El banco de temas debe incluir obligatoriamente seis grupos de campos fijos**; si falta uno, se descarta de inmediato:
- Fuente y frescura: Enlace permanente accesible a la publicación original, hora de publicación y tiempo transcurrido desde entonces; no escribir «cierto blogger».
- Métricas visibles: 4 datos consistentes en visualizaciones/reproducciones, «me gusta», compartidos y comentarios, junto con la hora de extracción. Si no se encuentran, marcar como «datos públicos no encontrados»; estrictamente prohibido estimar.
- Nivel del autor: Registrar handle, recuento de seguidores y categoría. De cuentas pequeñas con publicaciones virales se aprende la estructura; de los grandes referentes se analizan las temáticas.
- Segmento de la comunidad: Clasificar explícitamente en oficial, nacional o internacional.
- Motivo de idoneidad y ángulo de ejecución: Vincular con fortalezas propias y detallar acciones concretas (como hacer pruebas reales, añadir pasos o proporcionar plantillas), evitando adjetivos vacíos como «es muy popular».
- Desglose de motivaciones: Abarcar puntos de dolor, gratificaciones inmediatas e incentivos de interacción. Las deducciones sin respaldo de datos deben marcarse al final como «inferencia».

El planificador selecciona 3 temas de alto valor desde `01-inbox/`, filtrándolos a través de tres filtros: hechos concretos, relevancia para el lector y propuesta de valor del autor, generando un Brief que se guarda en `02-briefs/`:

```text
讀取今天 01-inbox 中已經核驗的線索，按照帳號定位篩選 3 個候選題，寫入 02-briefs/YYYY-MM-DD.md。每題包含：一句話事實、讀者場景、單一主角度、原始連結與證據、資訊缺口、建議內容形式、給主筆的寫作任務。證據不足的題直接標“待補證”。完成後停下，等待我批准，不要通知內容主筆。
```

Si te bloqueas al estructurar las ideas, utiliza un prompt de entrevista para que el Bot principal te haga preguntas y te ayude a aclarar tus necesidades:

::: details Selección de temas e inteligencia: Extracción, métricas y desglose de motivaciones
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

**Criterios de aceptación**
- Todos los enlaces originales son accesibles y los hechos principales están respaldados por el texto original.
- La falta de evidencia se clasifica como «pendiente de verificación»; **sin confirmación y firma humana, jamás pasa a la fase del redactor principal**.

[《Cómo aprovechar Grok Bot para creadores de contenido ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)；[《Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Redacción y textos: Eliminación del tono de IA y salida estructurada

Al redactar el primer borrador, cambia el enfoque de «qué tiene el producto» a «para qué le sirve al lector», **asegurando que el lector perciba un valor informativo claro en los primeros tres segundos**.

Puedes aplicar directamente dos estructuras ampliamente comprobadas:
- La fórmula HKRR de Tim (MediaStorm): abarca felicidad (Happiness), conocimiento (Knowledge), resonancia (Resonance) y ritmo (Rhythm). Cada publicación debe dominar sólidamente al menos un elemento; dos elementos es excelente; si no tiene ninguno, descártala.
- Los motivos de reenvío de Pan Luan: centrados en el «tiene que ver conmigo», situando al lector como protagonista. Por ejemplo, en lugar de «El software se ha actualizado», escribe «Ahorra dos horas al día buscando temas». Las estructuras virales se pueden reutilizar: copia el ritmo, no el contenido.

Configura en el redactor principal reglas de escritura y prohibiciones explícitas:

::: details Redacción y textos: Eliminación del tono de IA y salida estructurada
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

Una vez terminado el borrador, el editor de hechos toma el control. **El editor de hechos solo verifica afirmaciones y elimina el tono robótico de IA**, sin añadir nuevos puntos de vista ni tener permisos de publicación:

::: details Redacción y textos: Eliminación del tono de IA y salida estructurada
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

**Criterios de aceptación**
- Las dos primeras frases van directo al grano con los hechos clave, sin rodeos ni relleno.
- El editor de hechos coteja uno por uno los enlaces de primera mano; lo que no pueda verificarse se marca como «pendiente de confirmación» o se elimina directamente.
- El borrador corregido se traslada al directorio `04-review/` a la espera de la revisión humana final.

[《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Imágenes y presentación visual: Creación de sitios mediante código y ensamblaje de materiales

> Fuente: [Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación](https://x.com/0xlangeai/status/2109115005069341175)  
> Autor: [藍哥AI @0xlangeai](https://x.com/0xlangeai)

![Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación](/cases-img/fs32-0.jpg)

![Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación](/cases-img/fs32-1.jpg)

Al ilustrar contenidos, evita pedirle a la IA ilustraciones conceptuales al azar, que suelen verse genéricas y artificiales. En la práctica se suele optar por dos vías sólidas:

**Vía 1: Convertir publicaciones en un sitio web de perfil personal (solución de 藍哥AI)**
En el grupo «Sitio web de perfil de publicaciones», 4 Bots se turnan en relevos, almacenando los archivos intermedios en `/workspace/tweet-portrait/`:
1. El recopilador de publicaciones extrae publicaciones históricas y el analista de perfil sintetiza los hábitos de expresión y contrastes.
2. El diseñador web propone el diseño visual y el ingeniero web escribe el código frontend adaptándolo para dispositivos móviles.

Los dos primeros roles ejecutan sus prompts en orden:

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

Los dos últimos roles ejecutan los prompts de diseño y código:

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

Comprueba en la vista previa local el texto inicial, el espaciado de las tarjetas y la visualización móvil; tras confirmarlo, haz que el ingeniero empaquete el proyecto y **lo suba a Vercel o Cloudflare Pages para su publicación**.

**Vía 2: Ensamblaje parametrizado y clips de audio/video (solución de 鐵柱 / herramientas oficiales)**
- Personajes y atuendos: utilizando un sistema de muñeca de papel basado en datos de juego, el Bot analiza los parámetros y llama a una API de terceros para el ensamblado.
- Clips de video: utilizando la plantilla oficial Clip Bot, introduce directamente el enlace largo de audio/video para generar automáticamente una transcripción con marcas de tiempo y recortar los segmentos destacados.

**Criterios de aceptación**
- La maquetación en la vista previa local es ordenada y la adaptación móvil responde correctamente.
- Todas las publicaciones citadas incluyen su enlace original y se pueden abrir.
- La página refleja fielmente las expresiones reales sin inventar trayectorias ni historiales.

[《Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)；[《Colección de tweets de 鐵柱 ③: Métodos prácticos y casos》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

### Distribución, revisión y moderación: Control humano y flujo asíncrono

Los principiantes a menudo buscan una automatización total sin intervención humana, lo que conduce fácilmente a la suspensión de cuentas. **Está terminantemente prohibido publicar mediante navegadores dentro de la máquina virtual en la nube**, ya que los sistemas de control de riesgo de las plataformas identifican las huellas digitales de las máquinas virtuales. La publicación debe contar con un control humano absoluto, realizándose de forma manual por el propio creador desde un dispositivo físico local.

La colaboración en equipo utiliza un enfoque asíncrono, evitando tener que estar pegado a la pantalla todo el día:
- Banco de temas semanal: dedica 30 minutos a la semana a seleccionar fichas candidatas en una hoja de cálculo y márcalas como aprobadas.
- Revisión diaria de borradores: el creador dedica 10 minutos al día a revisar los textos en `04-review/` y añadir una reflexión personal.
- Flujo en tablero kanban: gestiona en la tabla los estados de pendiente de revisión, en redacción, finalizado y publicado.

Tras publicar el contenido, asigna al analista de métricas una revisión semanal en modo de solo lectura, prohibiendo estrictamente publicaciones o interacciones en tu nombre:

::: details Distribución, revisión y moderación: Control humano y flujo asíncrono
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

Para revisiones puntuales de periodos específicos, envía una instrucción directa:

```text
唯讀分析我明確指定的個人 X 主頁【主頁地址】，時間範圍為【開始日期—結束日期】。資料來源為【公開主頁 / X Analytics / CSV / 截圖】。

先列出資料範圍和缺失欄位，再按主題、內容形式、長度、發表時間和開頭型別做對比。給 3 條有具體帖子或指標支撐的改進建議，並設計 2 個一次只改變一個變數的下週實驗。

禁止發文、改帖、刪帖、按讚、轉發、收藏、關注、取關、評論、私信和修改帳號設定。遇到登錄、驗證碼、2FA、passkey 或擴大權限時立即停下，等我接管。完成後寫入 06-analysis，並只回覆文件路徑、覆蓋帖子數和缺失資料。
```

**Criterios de aceptación**
- Publicación manual local por parte de una persona real, con riesgo cero de suspensión por controles de seguridad.
- Las métricas de análisis pueden rastrearse hasta los archivos de exportación originales.
- **No sacar conclusiones precipitadas si el tamaño de la muestra es menor a 10 publicaciones**.
- La planificación para la semana siguiente incluye 2 experimentos controlados de variable única (por ejemplo, comparar el impacto de diferentes longitudes de texto en la tasa de interacción).

[《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)；[《Cómo aprovechar Grok Bot para creadores de contenido ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

## Desglose en profundidad de casos prácticos representativos

![Desglose en profundidad de casos prácticos representativos](/info/12-content-s3.png)

### Caso 1: El equipo cerrado de 5 personas para medios de Adrian Punk

Adrian Punk (@AdrianPunk115) configuró en la versión de escritorio un equipo permanente de 5 roles, completando un ciclo cerrado que abarca desde la captura de fuentes primarias, selección de temas, redacción y corrección hasta el análisis posterior.

1. **Restricción preventiva de permisos**: en la configuración del cliente, ajusta «Ejecutar en esta computadora» a «Nunca permitir»; el prompt prohíbe explícitamente publicar por cuenta propia, introducir contraseñas y llamar a conectores.
2. **Configuración de rutas de archivos**: crea `/workspace/content-team/` y sus 7 subdirectorios en la computadora en la nube, y añade en `00-profile/voice.md` el estilo de la cuenta, trabajos representativos y palabras prohibidas.
3. **División especializada del trabajo**: crea los roles de explorador de inteligencia, planificador de temas, redactor principal, editor de hechos y analista de métricas, limitando estrictamente los directorios de entrada y salida de cada puesto.
4. **Transferencia reglamentada**: envía la instrucción de inicio en el grupo «Equipo de contenido digital»; los entregables de las etapas previas se escriben en Markdown para que las etapas posteriores los lean; **queda prohibido avanzar de fase sin aprobación humana**.

Nota: Los 5 Bots comparten la computadora en la nube sin aislamiento sandbox, por lo que los permisos deben apoyarse en límites de roles bien definidos; **el editor de hechos debe cotejar de forma independiente los enlaces originales**, filtrando cifras inventadas por el redactor y el tono de relaciones públicas.

[《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)

### Caso 2: El banco de contenido viral dual de Kin (tweets y videos)

> Fuente: [¿Cómo pueden los ingenieros aprovechar Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![¿Cómo pueden los ingenieros aprovechar Grok Bot?](/cases-img/fs25-0.jpg)

![¿Cómo pueden los ingenieros aprovechar Grok Bot?](/cases-img/fs25-1.jpg)

Kin (@KinGao476942, embajador de SpaceXAI para China) consiguió más de 2000 seguidores en Twitter en unos 10 días y ha gestionado canales de video con más de un millón de seguidores, creando un Bot de operaciones en Twitter y el banco de temas virales para «小鄧Talk».

1. **Ficha de identidad**: define con claridad el enfoque, las cuentas de referencia y las áreas prohibidas, inhabilitando la publicación automática de tweets. **Si no se encuentran datos, debe indicarse «no encontrado», prohibiéndose terminantemente estimar o inventar**.
2. **Retroalimentación con datos reales**: analizó más de 100 publicaciones históricas y comprobó que los textos de entre 200 y 500 caracteres tenían una mediana de lectura superior, y aquellos con pasos numerados recibían muchos más «me gusta».
3. **Banco de temas de seis campos**: diseñó una tabla con enlace permanente original, hora de captura, métricas reales, niveles de seguidores, segmento de comunidad y análisis de motivaciones, sincronizándola con un tablero de Notion para el filtrado.
4. **Desglose de estructuras**: descompone publicaciones virales según HKRR (felicidad, conocimiento, resonancia, ritmo) y las tres motivaciones de Pan Luan, replicando la estructura pero no el contenido.

Nota: Durante la fase inicial de crecimiento de la cuenta, la alta frecuencia de publicación es más efectiva que un perfeccionamiento excesivo; al terminar, revisa siempre que el sujeto apele directamente a los intereses del lector.

[《Cómo aprovechar Grok Bot para creadores de contenido ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)

### Caso 3: El sitio web de perfil de publicaciones de 藍哥AI

藍哥AI (@0xlangeai) extrajo publicaciones históricas de su cuenta vinculada de X, sintetizó su estilo personal y contrastes, y puso en línea de forma automatizada un sitio web de exhibición de perfil personal.

1. **Configurar Bots especializados**: en el grupo del proyecto «Sitio web de perfil de publicaciones», configuró 4 roles: recopilador de publicaciones, analista de perfil personal, diseñador web de perfil e ingeniero web de perfil.
2. **Extracción y análisis**: el recopilador leyó hasta 100 publicaciones originales, citas comentadas y respuestas de los últimos 90 días, guardándolas en `tweets.md`; el analista extrajo de 3 a 5 contrastes expresivos con sus referencias, las cuales fueron revisadas por el creador.
3. **Diseño y despliegue**: el diseñador generó `design.md` (adoptando un formato de tarjetas estilo portafolio), y **el ingeniero redactó el código en la computadora en la nube, realizó pruebas en móvil y escritorio, y colaboró en el despliegue en Vercel o Cloudflare Pages**.

Nota: El historial de publicaciones es un corpus de datos ya disponible; **cada paso (recopilación, análisis, diseño e ingeniería) requiere la confirmación del creador antes de pasar a la siguiente etapa**, evitando que los desvíos se magnifiquen.

[《Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)

### Caso 4: Captura ininterrumpida 24/7 y flujo automatizado con tablas multidimensionales de xilo

> Fuente: [Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]](https://x.com/xilo2991/status/2109613437215293905)  
> Autor: [xilo @xilo2991](https://x.com/xilo2991)

![Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]](/cases-img/fs36-0.jpg)

![Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]](/cases-img/fs36-1.jpg)

xilo (@xilo2991) aprovechó el funcionamiento continuo 24 horas de la computadora en la nube para crear un pipeline de recolección de contenido viral activo en todo momento, sincronizándolo en tiempo real con hojas de cálculo multidimensionales de Feishu.

1. **Definir los tres elementos clave**: precisar los canales, las cuentas de referencia y palabras clave, y la hoja de cálculo de destino para los resultados.
2. **Integrar la tabla**: enviar el repositorio de GitHub del plugin de Feishu al Bot, completar la configuración y autenticación en la computadora en la nube, y utilizar la tabla como bus de colaboración.
3. **Mitigar riesgos y descartar variables**: controlar la frecuencia de búsqueda simulando una navegación normal; registrar el recuento de búsquedas y la probabilidad de viralidad, y **descartar automáticamente las palabras clave ineficaces en la revisión semanal**.
4. **Aclarar mediante entrevista**: enviar un prompt de entrevista con preguntas progresivas al Bot principal para pulir los detalles operativos antes de generar la configuración automáticamente.

Nota: Cambiar la publicación totalmente automática a una semiautomática con aprobación humana para equilibrar la eficiencia con la seguridad.

[《Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

### Caso 5: Especialización de roles, coordinación multidispositivo y prevención de baneos en la base por 鐵柱AGI

> Fuente: [Webhook de Grok Bot + Atajos: Creación de un pipeline automatizado de ingesta de conocimiento](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [鐵柱AGI @cgnot996](https://x.com/cgnot996)

![Webhook de Grok Bot + Atajos: Creación de un pipeline automatizado de ingesta de conocimiento](/cases-img/fs06-0.jpg)

![Webhook de Grok Bot + Atajos: Creación de un pipeline automatizado de ingesta de conocimiento](/cases-img/fs06-1.jpg)

鐵柱AGI (@cgnot996) probó sistemáticamente los límites de los Bots, consolidando soluciones contra bloqueos y para recuperación ante desastres.

1. **Especialización de puesto único**: dividir en Bots con una sola función como inspección de código, captura de artículos y archivo contable, descartando el concepto de un Bot todoterreno.
2. **Ingesta ultra rápida**: configurar Atajos en el móvil para leer el portapapeles y enviarlo directamente mediante Webhook al Bot en la computadora en la nube para consolidarlo en una tabla.
3. **Línea roja contra suspensiones**: **la simulación de publicaciones con navegadores en máquinas virtuales provoca fácilmente el bloqueo de la cuenta; toda interacción externa debe ser realizada por una persona real en un dispositivo físico**.
4. **Recuperación ante desastres**: reconstruir la computadora en la nube borra los entornos no persistentes; redacta scripts de recuperación automática en Shell y utiliza un Bot administrador de memoria para respaldar periódicamente prompts y configuraciones.

Nota: **Las configuraciones y comandos de instalación clave deben estructurarse en scripts de recuperación reproducibles con un solo clic**; la computadora en la nube no debe considerarse un servidor infaliblemente estable.

[《Colección de tweets de 鐵柱 ③: Métodos prácticos y casos》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

## Errores comunes que debes evitar

1. Publicar desde la computadora en la nube expone huellas digitales que provocan bloqueos, y la automatización total suele publicar contenido errático. **Publicar, dar «me gusta» y enviar mensajes directos debe hacerse manualmente en un dispositivo real**.
2. En la descripción de roles, **establece reglas estrictas: marcar «no encontrado» si no hay datos y etiquetar como «inferencia» toda deducción**, evitando la ingesta de datos falsos.
3. El reinicio de la computadora en la nube borra las dependencias. **Guarda scripts de recuperación en Shell dentro de directorios persistentes** como respaldo.
4. En las tareas Routine, **verifica minuciosamente el ciclo de ejecución** para evitar configurar por error «ejecutar solo en días laborables», lo que provocaría desconexiones los fines de semana.
5. No filtrar tomas previamente causó una reducción de cuota de más del 40% en una sola semana; **queda terminantemente prohibido el sondeo frecuente e innecesario, optimiza los momentos de activación**.

Planes a partir del 12 de octubre de 2026:
| Plan | Costo | Cuota | Incluye Bot |
| - | - | - | - |
| Plus | $8/mes | - | No |
| Premium | $30/mes o $300/año | 4x | Sí |
| Super | $100/mes o $1000/año | 15x | Sí |
| Ultra | $200/mes o $2000/año | 50x | Sí |

## Cómo verificar el resultado

### Permisos y directorios
1. Ve a Configuración de la cuenta en «General → Agent → Ejecutar en esta computadora»; **el estado debe ser obligatoriamente «Nunca permitir»**. Se prohíbe terminantemente a los Bots publicar o realizar pagos automáticamente, así como falsear datos.
2. Verifica los 7 subdirectorios bajo `/workspace/content-team/` y asegúrate de haber completado en `00-profile/voice.md` el posicionamiento de la cuenta, los ejemplos y las palabras prohibidas.

### Recopilación, redacción y simulacro
1. Extrae 3 pistas y **comprueba aleatoriamente que 2 de los enlaces sean accesibles y cuenten con respaldo en el texto original**; si faltan datos, marca «datos públicos no encontrados», sin conjeturar cifras ni números de seguidores.
2. Tras confirmar el Brief, genera el borrador inicial: las dos primeras oraciones deben presentar directamente los hechos clave, los párrafos deben mantenerse entre 2 y 4 oraciones, adjuntar al final la base fáctica y los puntos pendientes de confirmación, y evitar por completo las palabras prohibidas.
3. El texto revisado solo verifica sin añadir nuevos argumentos; **jamás se envía al exterior automáticamente sin una instrucción humana**. Ejecuta `restore.sh` una vez en el entorno de prueba para comprobar que las dependencias estén listas con normalidad.

## Lecturas complementarias

### Documentación oficial
- [Planes y facturación](https://cursor.com/cn/help/grok-bot/plans.md)
- [Equipos de Bots y colaboración](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Entorno y configuración de computadoras en la nube](https://cursor.com/cn/docs/grok-bot/computers.md)
- [Colaboración en chats grupales](https://cursor.com/cn/help/grok-bot/group-chats.md)
- [Tareas rutinarias y automatización](https://cursor.com/cn/help/grok-bot/routines.md)

### Fuentes prácticas de la comunidad
- [《Construir un equipo de creadores de contenido con Grok Bot: Tutorial paso a paso ｜ Adrian Punk》](https://jcng5q8n0f3z.feishu.cn/wiki/TGF0wLSNFiL6A8kDHZAcXL2bnGd)
- [《Cómo aprovechar Grok Bot para creadores de contenido ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/FzlswUo4GiBJYuk9xO7cyIIWnRf)
- [《Convierte tus publicaciones en un sitio web de perfil personal con Grok Bot: Tutorial paso a paso desde el análisis hasta la publicación》](https://jcng5q8n0f3z.feishu.cn/wiki/BgFKwIqQSiGyWzk1r5rcsTcTnFh)
- [《Creación desde cero de un equipo de agentes totalmente automatizado: Flujo completo desde la activación de Grok Bot hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- [《Colección de tweets de 鐵柱 ③: Métodos prácticos y casos》](https://jcng5q8n0f3z.feishu.cn/wiki/SMztw0FlBilqx5k1tXzc9kFjndb)

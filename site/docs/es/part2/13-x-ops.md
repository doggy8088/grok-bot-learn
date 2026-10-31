# Capítulo 13 Caso: Creación de contenido y operaciones en X

Escribir scripts directamente para invocar la API de publicación con alta frecuencia activa fácilmente el control de riesgos y bloqueos, consumiendo en pocos días la cuota de toda la semana.

- Construye un pipeline en máquina virtual en la nube: envía una sola frase por WeChat para buscar temas automáticamente y redactar el primer borrador.
- Mantén la regla de **generar solo borradores y hacer clic manual para publicar**, lo que garantiza la seguridad de la cuenta y asume el trabajo mecánico.

## Capacidades nativas de la plataforma X: De la búsqueda de solo lectura a la asignación de tareas en comentarios

![Capacidades nativas de la plataforma X: De la búsqueda de solo lectura a la asignación de tareas en comentarios](/info/13-x-ops-s1.png)

El 08-10-2026 se lanzó la función nativa de solo lectura; la búsqueda de publicaciones y las tendencias de 7 días se descuentan del pool de suscripción.

La v0.70.2 del 11-10-2026 permite buscar publicaciones públicas sin vincular una cuenta; consulta el [registro](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd).

|Tipo|Acción|Reglas y control de riesgos|
|---|---|---|
|Solo lectura nativa|Buscar publicaciones, análisis de publicaciones individuales, tendencias de 7 días|Consume del pool de suscripción, sin riesgo de baneo|
|Activación externa|@bot en comentarios para extracción y archivado|Enrutado al Bot principal marcado con estrella, terminantemente prohibido responder automáticamente en X|
|Escritura en cuenta|Publicar tweets, mensajes directos, leer favoritos, dar me gusta|Pasa por la API oficial, **terminantemente prohibido publicar mediante navegadores headless**|

### Cómo hacerlo
1. **Cuadro de diálogo**: Escribe "Ayúdame a buscar cómo ha valorado la gente el tema XX en los últimos 3 días", o pega un enlace e indica "Extrae los puntos de vista centrales de este tweet y los puntos de controversia en la interacción con los lectores".
2. **Zona de comentarios**: Responde `@bot 提取本帖核心邏輯並存入選題庫`, consulta las [instrucciones](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

### Criterios de aceptación
- **Extracción completa**: Recupera la fuente original, la fecha/hora de publicación y el hilo de la discusión.
- **Límites de respuesta**: Genera registros **en menos de 30 segundos** tras asignar la tarea; solo redacta borradores sin publicar por ti, y jamás da me gusta ni publica automáticamente.

## 5 plantillas de Bot y sistema de colaboración multi-Agent

![5 plantillas de Bot y sistema de colaboración multi-Agent](/info/13-x-ops-s2.png)

**Hacer que un solo Bot se encargue a la vez de la investigación, el copywriting y la retrospectiva genera confusión de contexto fácilmente.** La solución es dejar que cada especialista cumpla su función y comparta archivos dentro de la misma computadora en la nube.

> Fuente: [Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas](https://x.com/Chchenhao0129/status/2109258247790313478)  
> Autor: [Hardy Chen @Chchenhao0129](https://x.com/Chchenhao0129)

![Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas](/cases-img/fs34-0.jpg)

![Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas](/cases-img/fs34-1.jpg)

La base de Grok Bot es una máquina virtual en la nube que incluye un sistema Linux completo. Todos los Bots de una misma cuenta comparten la misma computadora en la nube, con sesiones de escritorio, administradores de archivos y terminales independientes.

El host está equipado con una CPU Xeon de 8 núcleos y 8 hilos, 16 GB de RAM y 128 GB de espacio en disco (declarado por el autor, no verificado); para la corrección de errores de los mecanismos, consulta 《Colección de tweets de 鐵柱 ②: Observaciones de funciones del producto y versiones》[https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd).

**El sistema de archivos y la red de esta máquina están completamente comunicados, y los materiales que el Bot anterior guarda en el directorio de trabajo pueden ser leídos directamente por el siguiente Bot.

** El creador comunitario Hardy Chen ha compartido en código abierto 5 conjuntos de plantillas de especialistas que cubren las distintas etapas de operación en X; los detalles de configuración se encuentran en 《Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye).

| Nombre del especialista | Enlace directo a la plantilla compartida oficial | Responsabilidad central |
|---|---|---|
| Director de Inteligencia | [https://x.ai/bot/s4iMTsbMiTosZ2xm2RISD](https://x.ai/bot/s4iMTsbMiTosZ2xm2RISD) | Rastrear tendencias populares y contenidos virales de alta interacción, buscar fuentes fiables y ángulos de enfoque |
| Radar de Noticias de IA | [https://x.ai/bot/wUbWteZc9NS-RUrJc22nh](https://x.ai/bot/wUbWteZc9NS-RUrJc22nh) | Filtrar noticias técnicas desde AIHOT y verificar sus fuentes, eliminando el ruido |
| Recreación de Tweets | [https://x.ai/bot/VGmfFlKaPO6JUEc3xeg1_](https://x.ai/bot/VGmfFlKaPO6JUEc3xeg1_) | Leer enlaces a publicaciones originales, redactar tweets de cita o respuestas y aportar puntos de vista |
| Redacción de Tweets Cortos | [https://x.ai/bot/F5fO0z2lrcoP5s6JaZ1Z5](https://x.ai/bot/F5fO0z2lrcoP5s6JaZ1Z5) | Convertir materiales factuales en tweets cortos y coloquiales |
| Retrospectiva de Datos de X | [https://x.ai/bot/z1A0pKGOZOUA-v6DNdpYN](https://x.ai/bot/z1A0pKGOZOUA-v6DNdpYN) | Leer datos de publicaciones y archivos CSV, analizar patrones y proponer acciones de prueba posteriores |

### Pasos de configuración del despachador

1. Añade las 5 plantillas a tu propia cuenta.
2. Selecciona un Bot principal como punto de entrada de orquestación.
3. **Envía el prompt de inicialización directamente al Bot principal para registrar el posicionamiento de la cuenta, el enrutamiento de especialistas y las normas de redacción en el contexto persistente.**

El contenido del prompt está citado de 《Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye).

::: details Pasos de configuración de orquestación
```text
我已經新增五個 X 運營專員：情報總監、AI新聞雷達、推文二創、短推成稿、X資料覆盤。請保留你的原有功能，作為這套團隊的統一入口，完成一次初始化。

1. 先檢查能力和連線
確認當前環境能發現 Bot、向 Bot 發任務並接收回執。找到五個專員的實際 Bot ID，核對名稱、職責和來源，遇到同名先消歧。保存持久的“角色—名稱—ID”路由，讓後續聊天和微信入站任務都能讀取。缺 Bot 或缺工具時明確告訴我，不憑名稱宣稱連線成功。

2. 確認我的帳號定位
一次只問一個關鍵問題，瞭解主題、目標讀者、我能提供的價值和不寫的話題。也可以分析我授權提供的主頁和近期帖子，提出建議，等我確認。把已確認定位和表達偏好持久保存，並同步給相關專員。不要繼承樣板作者的個人資訊。

3. 自動理解需求、安排任務
找選題、熱點、爆款拆解交情報總監；AI新聞交AI新聞雷達；原帖回覆、引用、二創交推文二創；短推寫稿、改稿交短推成稿；發文資料分析交X資料覆盤。
多步任務由你安排先後，傳遞來源、我的定位和必要上下文，等真實回執後彙總。日常不要求我指定崗位，也不要求我重複文風。專員失敗就說明卡點，不能悄悄代寫並聲稱是專員成果。

4. 保存預設寫作要求
像跟朋友分享：講清發現、理由和具體用途，允許適量語氣詞，不堆口號。不編我的親歷、數位、測試結果或漲粉成績。原帖保留歸屬，新聞核對來源和日期。預設沿用這些要求，我另有要求時再調整。
你交付前檢查事實、來源、定位和可讀性。來源和說明放在草稿外，方便我看，也方便複製正文。檢查X可發表長度，超出則給短版或說明需要的帳號功能。

5. 真正跑一次
給五個專員各派一個小任務，檢查接收、完成、回傳，再跑“找素材→短推成稿→你檢查→返回草稿”。保留可核對的任務記錄。資料覆盤沒有真實資料就報告缺口，不編數位。彙報通過項、失敗項和恢復辦法，不把發出任務當完成。

6. 根據真實回饋改進
記錄已發表內容和表現，提出下一輪調整。日常選題和寫作規則的小改動留版本、可回退；帳號定位、授權範圍、發表權限、定時安排或新增收費服務變更先問我。小樣本形成試驗建議，不宣稱已驗證漲粉規律。

預設只起草。發文、回覆、按讚、關注和私信由我另行決定，不自動執行。
```
:::

Una vez completada la configuración, el Bot principal recordará los IDs de sus subordinados. En el día a día, cuando surja la necesidad de proponer temas y redactar publicaciones, el Bot principal coordinará automáticamente con el Director de Inteligencia para recopilar material, luego se lo pasará al Redactor de Tweets Cortos y finalmente entregará el primer borrador.

### Criterios de aceptación

Pide al Bot principal en la ventana de chat que realice una prueba de búsqueda de temas y redacción; el resultado satisfactorio debe cumplir dos puntos:
- **Relevo real multi-Agent**: En los registros en segundo plano del Bot principal y los especialistas, debe verse el proceso de asignación de tareas, la ejecución real por parte de los sub-Bots y el retorno de resultados.
- **Calidad del borrador y normas de maquetación**: El borrador devuelto no contiene eslóganes mecánicos, y las fuentes originales y textos explicativos están ordenados limpiamente debajo del cuerpo del texto, sin mezclarse con él.

## Operaciones con una frase en WeChat: Conexión del bucle cerrado de recepción y envío en el móvil

Conecta el Bot principal a WeChat mediante el plugin integrado de WeChat ClawBot (o iLink) estableciendo una conexión persistente con el Routine Webhook de Grok Bot. **Todos los Bots comparten un pool de cuotas unificado y no hay consumo adicional por inactividad al despertar de forma pasiva mediante eventos de Webhook.**

Los niveles de suscripción unificados de The X Subscription lanzados el 12-10-2026 son los siguientes; consulta las reglas en 《4.3 Activadores y automatización: Temporizadores, Webhooks y asignación de tareas en X》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg):

| Plan de suscripción | Costo | Multiplicador de cuota |
|---|---|---|
| Premium | $30/mes o $300/año | 4x uso |
| Super | $100/mes o $1000/año | 15x uso |
| Ultra | $200/mes o $2000/año | 50x uso |

### Cuatro pasos para conectar WeChat

1. En la versión de escritorio, envía los requisitos de configuración al Bot principal para que verifique los programas de escucha y las rutinas en el entorno.

   El prompt está citado de 《Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye):

::: details Cuatro pasos para conectar WeChat
```text
請把你接入我的微信，讓我直接在微信裡說X運營需求，並收到結果。沿用已確認的帳號定位、預設文風和五專員持久路由。

先檢查當前是否已有微信連線器、監聽程式和routine，避免重複。參考課程：
https://x.com/KinGao476942/status/2108132811635032316?s=20
核對當前ClawBot/iLink接法和所需工具。缺工具或需要授權時如實說明；需要我安全填寫、手機掃碼時給出具體步驟，不代替我確認。

準備微信入站Webhook任務和監聽保活。Webhook URL、密鑰及憑據只通過安全輸入保存，不打印到普通聊天、記錄或公開截圖。

只處理我綁定身份的指令，不讀取聯繫人或群聊歷史。入站任務必須讀取我的定位、文風和五專員實際ID，按需求真派單、等回執，再原路返回純文字。預設只起草，寫稿失敗明確報告，不悄悄代寫。

監聽保持單一實例。處理前持久保存待辦，以訊息ID去重；回覆成功才標記完成，失敗保留並有限重試。登錄過期或權限錯誤停止重試並報告。重啟後恢復未完成任務，避免漏回和重複回覆。

完成後實際驗證：掃碼登錄、微信入站、你的回覆、專員接力和微信收到最終稿。再檢查監聽重啟後的恢復。保留脫敏記錄，告訴我哪些通過、哪些未通過，不把組態完成當接通成功。說明監聽執行在哪個環境、何時會停，以及如何恢復。
```
:::

2. En WeChat móvil, pulsa sucesivamente en "Yo → Ajustes → Plugins" y habilita "WeChat ClawBot". Si no encuentras el acceso, indica al Bot principal tu versión actual de WeChat para que te asista en la verificación.
3. Despliega el nombre del Bot en la parte superior de la ventana principal de chat en el escritorio, entra en "Tareas rutinarias / Routines", abre la tarjeta "Activación entrante de WeChat" (微信入站喚醒) y copia la URL del Webhook y la clave secreta.

   Introduce y guarda cada dato por separado en el cuadro de seguridad emergente; **recuerda terminantemente no introducir la cadena larga completa que contiene Authorization en un solo campo de entrada**.
4. En el escritorio, envía al Bot principal: "Plugin habilitado, dirección y clave guardadas; por favor verifica la configuración y genera el enlace de vinculación", y escanea el código QR con WeChat móvil para autorizar. Luego envía "Hola" en WeChat; si recibes respuesta, el canal estará operativo.

Consulta el registro de solución de problemas en 《Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye).

### Criterios de aceptación

Envía al Bot vinculado en WeChat móvil: "Genérame 3 publicaciones de tráfico general". **Si recibes en menos de dos minutos 3 borradores con ángulos de enfoque y fuentes de material, y en los registros en segundo plano se puede comprobar el registro de asignación, el sistema estará listo.**

## Diseño de barrera humana para emitir solo borradores y límites de seguridad

![Diseño de barrera humana para emitir solo borradores y límites de seguridad](/info/13-x-ops-s4.png)

Si la publicación automatizada presenta alucinaciones del modelo, fechas incorrectas o respuestas ofensivas, provocará daños irreversibles. **Al final del pipeline se debe añadir una barrera de seguridad humana para bloquear completamente cinco acciones: publicar, dar me gusta, seguir, enviar mensajes directos y eliminar, permitiendo únicamente que el modelo redacte borradores.**

::: details 只出草稿的人閘設計與安全邊界
```text
[微信一句話 / 定時觸發] 
       │
       ▼
[主 Bot 排程中心] ───► [情報總監 / AI新聞雷達 抓取素材]
       │
       ▼
[推文二創 / 短推成稿 編寫草稿]
       │
       ▼
[主 Bot 事實與長度校驗]
       │
       ▼
[推送到手機微信 / 客戶端對話框] ───► (停住：系統不具備自動發文權限)
       │
       ▼
[人工審閱：修改、定奪] ───► [人工手動複製到 X 發表]
```
:::

### Configuración de protección de doble capa

1. **Orden estricta en el prompt**: Añade de forma fija al final del prompt del Bot principal y de los especialistas:
   "Por defecto solo redacta borradores. Publicar, responder, dar me gusta, seguir y enviar mensajes directos quedan a mi entera discreción y no se ejecutan automáticamente. Las fuentes y textos explicativos deben ubicarse fuera del borrador para facilitar la lectura humana y la copia del cuerpo con un solo clic".
2. **Interceptación a nivel de sistema**: En Settings → Custom Rules (o Auto-review) de Grok Bot, **marca como "Ask first" todas las operaciones que contengan `send`, `post`, `buy`, `transfer`, `delete` y `permissions`**. Sin tu clic explícito, el sistema subyacente jamás las ejecutará.

Consulta las especificaciones de configuración en 《4.3 Activadores y automatización: Temporizadores, Webhooks y asignación de tareas en X》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

### Criterios de aceptación

Durante las pruebas reales, envía la instrucción "Publica este borrador directamente en mi perfil de X"; para ser conforme debe cumplir dos puntos:
- **Interceptación efectiva**: El Bot rechaza explícitamente la ejecución o el sistema subyacente muestra una tarjeta de interceptación de aprobación "Ask first" deteniendo la invocación.
- **Maquetación conforme**: El cuerpo del borrador está separado de los enlaces de referencia y la longitud se ajusta estrictamente al límite de caracteres de la plataforma X.

## Análisis en profundidad de casos prácticos

Para comprender de forma más intuitiva cómo distintos creadores integran este sistema en su trabajo diario, a continuación se analizan tres casos prácticos representativos de la comunidad. Los tres modelos corresponden a flujos operativos de diferente escala y necesidad:

| Caso práctico | Creador | Arquitectura y método central | Puntos clave de referencia |
|---|---|---|---|
| Caso 1 | Hardy Chen (@Chchenhao0129) | 5 plantillas de Bot + plugin ClawBot de WeChat + Webhook | Orquestación unificada desde un único punto de entrada, consolidación de estilo y posicionamiento, entrega de borradores con barrera humana |
| Caso 2 | SCOTTY BEAM (@ScottyBeamIO) | Colaboración de tres Agents + directorio compartido en computadora en la nube + grabación de acciones | Transferencia de datos mediante disco compartido, normalización estética con imágenes de referencia fijas, programación de temporizadores en sesiones independientes |
| Caso 3 | 鐵柱AGI (@cgnot996), AYi (@AYi_AInotes) | Búsqueda nativa de solo lectura + activación por `@bot` en comentarios + almacenamiento local | Cero APIs externas para reducir costos y evitar baneos, asignación de tareas en comentarios sin cambiar de aplicación, persistencia en `/home/box` |

### Caso 1: El pipeline colaborativo de 5 Bots con una frase en WeChat de Hardy Chen

- **Quién**: Hardy Chen (@Chchenhao0129), creador de contenido individual.
- **Qué hizo**: Configuró 5 plantillas de Bot con funciones verticales e integró el plugin ClawBot de WeChat, logrando que con solo enviar una frase de requerimiento por WeChat se complete de forma totalmente automatizada el descubrimiento de temas en X, el filtrado inicial de noticias de IA, la redacción de tweets y la retrospectiva semanal de datos de publicaciones.
- **Cómo lo hizo**:
  1. Primero añadió una a una en la versión web las 5 plantillas de Bot compartidas oficialmente; tras seleccionar el Bot principal, le envió el prompt de inicialización del sistema, inyectando de una sola vez el posicionamiento de la cuenta personal, la audiencia objetivo y el enrutamiento persistente de los 5 especialistas en el Bot principal.
  2. A continuación, configuró el Webhook entrante de WeChat y el proceso de escucha para mantenerlo activo, vinculando el Bot principal a WeChat mediante el escaneo de código QR desde el móvil.
  3. Para las actualizaciones diarias de noticias, programó una tarea periódica a las 7:30 de la mañana todos los días en la zona horaria Asia/Shanghai, haciendo que el Radar de Noticias de IA recopile información de AIHOT, verifique las fuentes originales y la envíe a WeChat.
  4. Para el análisis de datos de publicaciones, proporcionó los archivos CSV del backend según se solicitaba, permitiendo que el especialista de datos analizara el rendimiento de la interacción y guiara las acciones de la semana siguiente.
- **Qué se puede aprender**:
  - Establecer un sistema de orquestación con un único punto de entrada, sin perder energía transmitiendo mensajes a cada especialista por separado.
  - Fijar el posicionamiento de la cuenta con un prompt de inicialización, evitando tener que explicar el estilo de redacción cada vez que se envía una instrucción.
  - Mantener el mecanismo de entrega exclusiva de borradores, maquetando las notas explicativas por separado del texto principal.
  - Cuando WeChat se conecta pero no responde, seguir la ruta estándar de solución de problemas: "proceso de escucha — tarea de mantenimiento activo — deduplicación de mensajes", sin desvincular ni reescanear el código QR a ciegas una y otra vez.
  - Consulta la retrospectiva detallada en 《Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas》[https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye).

### Caso 2: El flujo de contenido totalmente automatizado de tres Bots de SCOTTY BEAM y la comparativa de cuatro soluciones

> Fuente: [Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](https://x.com/ScottyBeamIO/status/2089417013647073753)  
> Autor: [SCOTTY BEAM @ScottyBeamIO](https://x.com/ScottyBeamIO)

![Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](/cases-img/fs41-0.jpg)

![Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot](/cases-img/fs41-1.jpg)

- **Quién**: SCOTTY BEAM (@ScottyBeamIO), creador técnico de redes sociales.
- **Qué hizo**: Construyó un sistema de actualización en la nube de tres Agents compuesto por un especialista en investigación, un especialista en creatividad visual y un especialista en redacción de textos, logrando articular de manera totalmente autónoma la detección de tendencias, el diseño de infografías y la redacción de tweets; asimismo, realizó una comparativa transversal de cuatro arquitecturas de Agent: Grok Bot, Buzz, OpenClaw y Hermes.
- **Cómo lo hizo**:
  1. Aprovechó plenamente la característica de Grok Bot según la cual todos los Agents comparten la computadora en la nube subyacente; el Bot de investigación busca tendencias en X y en repositorios públicos de código en segundo plano y guarda los materiales en disco.
  2. El Bot de creatividad visual aprendió previamente el estilo de las infografías de referencia proporcionadas por el autor, leyendo directamente los materiales de investigación para generar imágenes visuales con una maquetación coherente.
  3. El Bot de redacción sintetizó los resultados de ambos para generar los borradores listos para publicar. Para las operaciones fijas y mecánicas del día a día, utilizó la función de grabación de acciones (Recording) para enseñarle directamente al Bot.
- **Qué se puede aprender**:
  - Al colaborar con múltiples Agents, utilizar el directorio compartido de la computadora en la nube como centro de datos, eliminando el copiado manual y la intermediación de datos.
  - Estandarizar la estética visual suministrando imágenes de referencia fijas al Bot de diseño.
  - Estar alerta ante la limitación de que las sesiones de equipo multi-Bot no pueden guardar tareas programadas, dividiendo las rutinas de orquestación para configurarlas en sesiones independientes de cada Bot.
  - Consulta la comparativa de arquitecturas y los detalles operativos en 《Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot｜SCOTTY BEAM》[https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb](https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb).

### Caso 3: Búsqueda nativa en X y archivado de conocimiento mediante @bot en comentarios de 鐵柱 y AYi

- **Quién**: 鐵柱AGI (@cgnot996) y AYi (@AYi_AInotes), investigadores técnicos de alta frecuencia.
- **Qué hicieron**: Aprovecharon la capacidad nativa de solo lectura lanzada el 08-10-2026 y el mecanismo de interacción con @bot en la sección de comentarios de la v0.70.2 del 11-10-2026 para construir un flujo de monitoreo de inteligencia de la industria y almacenamiento de conocimiento de tweets en un clic desde el móvil, sin necesidad de APIs externas.
- **Cómo lo hicieron**:
  1. En el día a día, envían instrucciones en lenguaje natural en el cuadro de diálogo para extraer la curva de evolución de tendencias de cualquier palabra clave en X durante los últimos 7 días y las publicaciones clave de debate, sin habilitar ningún conector de pago.
  2. Al leer tweets en el móvil, cuando encuentran hilos largos o soluciones técnicas, responden directamente en la sección de comentarios con `@bot` indicando los requisitos de archivado.
  3. Tras recibir el evento del sistema, el Bot principal marcado con estrella extrae automáticamente el texto completo del tweet, invoca la base de conocimiento para limpiar el formato y lo guarda como un archivo Markdown persistente en el directorio `/home/box` de la máquina virtual.
- **Qué se puede aprender**:
  - Aprovechar bien los permisos oficiales de solo lectura en lugar de scrapers de terceros, reduciendo significativamente la complejidad de mantenimiento y el riesgo de baneo.
  - Sin necesidad de cambiar de aplicación en el móvil, lograr una activación ligera mediante @bot.
  - Gestionar rigurosamente el almacenamiento local de datos, concentrando las rutas clave en la computadora en la nube y previniendo pérdidas por reinicios.
  - Consulta los puntos clave de la práctica en 《Colección de tweets de 鐵柱 ②: Observaciones de funciones del producto y versiones》[https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd) y 《4.3 Activadores y automatización: Temporizadores, Webhooks y asignación de tareas en X》[https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg).

## Errores comunes y precauciones

### Tareas programadas y consumo de cuota
1. Al agregar varios Bots al mismo Team Chat no se puede guardar una Routine unificada (comprobado por SCOTTY BEAM); **es obligatorio volver a una conversación individual independiente para configurarlo por separado**.
2. Algunas versiones se ejecutan por defecto solo en días laborables; en la instrucción de creación se debe especificar "incluyendo sábados y domingos, ejecutar puntualmente todos los días" (comprobado por 鐵柱).
3. Verifica en la configuración del sistema que la zona horaria local sea Asia/Shanghai para evitar que las 7:30 de la mañana en hora de Pekín se ejecuten de madrugada.
4. La cuota de Bot se comparte con Grok y Cursor; el sondeo cada 5 minutos lee todo el contexto incluso si no hay actualizaciones. **Es indispensable cambiar a una comprobación en dos fases o activación incremental (Wake on Done)** para el filtrado inicial; melvindvivas, quien opera 29 Bots, también recomienda limpiar periódicamente las rutinas de bajo rendimiento.

Fuente: [《4.3 Activadores y automatización: Temporizadores, Webhooks y asignación de tareas en X》](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)

### Solución de problemas de conexión entre WeChat y Webhook
1. La falta de respuesta tras escanear el código QR en WeChat suele deberse a que el proceso de escucha se ha colgado o a que la Routine de mantenimiento activo se ha pausado; **no vuelvas a escanear repetidamente para revincular la cuenta**. La experiencia de Hardy Chen indica que se deben enviar comandos de diagnóstico desde el escritorio para revisar procesos y colas, y enviar un nuevo mensaje de prueba para restablecer el flujo.
2. Hasta la v0.68.1, si la tarjeta de detalles del cliente no se abre, pide al Bot que envíe el enlace directo al activador en el cuadro de chat para visualizarlo.

Fuente: [《Colección de tweets de 鐵柱 ②: Observaciones de funciones del producto y versiones》](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

### Restricciones de interacción de la plataforma y entorno del host
1. La asignación de tareas en comentarios no admite videos puros; no responde cuando se menciona a @grok y a @bot al mismo tiempo; **está terminantemente prohibido conceder permisos de publicación externa a la asignación de tareas en comentarios**, para evitar inyecciones maliciosas de prompts.
2. El mantenimiento de la máquina virtual restablece las rutas temporales; **los scripts, documentos y datos de copia de seguridad deben guardarse de forma unificada en `/home/box`**, preparando además scripts de autorreparación.

Especificación de rutas: [《Colección de tweets de 鐵柱 ②: Observaciones de funciones del producto y versiones》](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)

## Cómo verificar tras completar la configuración

1. El Bot principal busca 3 tweets con muchos likes, comprueba el ID del autor, las opiniones y la hora, sin errores.
2. Envía la instrucción para consultar los registros y **confirma el relevo de los 5 especialistas para completar el borrador**, evitando estrictamente que un solo bot escriba en su lugar.
3. Envía a ClawBot en WeChat: "Escribe un tweet corto sobre herramientas de modelos de lenguaje desde la perspectiva de un principiante"; devuelve un borrador en 2 minutos.
4. Envía "Publica el borrador recién generado directamente en mi cuenta de X"; **debe aparecer la ventana Ask first** y no publicar externamente sin confirmación.
5. Alinea los horarios de las Routines; suministra un archivo vacío y confirma que el especialista de retrospectiva reporte con veracidad los datos faltantes sin inventar cifras.

## Lecturas complementarias

### Documentación oficial y anuncios de lanzamientos
- [x.ai Changelog](https://x.ai/changelog/bot)
- [Anuncio oficial y documento de precios de The X Subscription (12-10-2026)](https://docs.x.ai/x-subscription/pricing)

### Artículos originales de prácticas comunitarias

> Fuente: [Grok Bot Webhook + Atajos: Creación de un pipeline automatizado para almacenamiento de conocimiento](https://x.com/cgnot996/status/2097487429104197688)  
> Autor: [鐵柱AGI @cgnot996](https://x.com/cgnot996)

![Grok Bot Webhook + Atajos: Creación de un pipeline automatizado para almacenamiento de conocimiento](/cases-img/fs06-0.jpg)

![Grok Bot Webhook + Atajos: Creación de un pipeline automatizado para almacenamiento de conocimiento](/cases-img/fs06-1.jpg)
- [Con una frase en WeChat puedes gestionar X: mis 5 plantillas de Bot publicadas](https://jcng5q8n0f3z.feishu.cn/wiki/DJwawbQxeiUcIjkKbekcVkHRnye)
- [Grok Bot vs Hermes vs OpenClaw vs Buzz + How I fully automated my X content with Grok Bot｜SCOTTY BEAM](https://jcng5q8n0f3z.feishu.cn/wiki/RuhbwzhViiB3FwkYaylc8Uv7nLb)
- [4.3 Activadores y automatización: Temporizadores, Webhooks y asignación de tareas en X](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [Colección de tweets de 鐵柱 ②: Observaciones de funciones del producto y versiones](https://jcng5q8n0f3z.feishu.cn/wiki/ZRFQwIlNgiuJTVkGcJgcrZhsnKd)
- [Grok Bot Webhook + Atajos: Creación de un pipeline automatizado para almacenamiento de conocimiento](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)
- [Ahorra aún más cuota de Grok Bot: Optimización extrema de tareas programadas](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)

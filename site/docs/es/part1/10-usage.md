# Capítulo 10 Cuota y costes: cómo hacer que el uso semanal dure toda la semana

Quedarse sin cuota un martes y recibir cargos de cientos de dólares suele deberse a ciclos de computación en vacío. **Cada vez que el Bot se reactiva, relee el historial completo**, inflando el contexto a cientos de miles de tokens en pocas horas.

Para aguantar toda la semana sin problemas, sigue estos tres pasos:
1. Desactiva el pago bajo demanda en segundo plano.
2. Reduce los sondeos frecuentes y las conversaciones entre múltiples Bots.
3. Ajusta las sesiones y evita enviar archivos grandes en la ventana de chat.


![Cuota y costes: cómo hacer que el uso semanal dure toda la semana](/info/10-usage.png)

## ¿Cómo funciona el cobro de la cuota en Grok Bot? {#扣費原理-額度是怎麼被花掉的}

**Grok Bot factura por tokens consumidos en cada llamada. Su mecanismo central se basa en sesiones largas individuales: cada respuesta o reactivación vuelve a leer el contexto histórico completo, y el consumo total equivale al número de reactivaciones multiplicado por la longitud del contexto releído en cada ocasión.**

![Principio de cobro: cómo se consume la cuota](/info/10-usage-s1.png)

Grok Bot factura según los tokens que el modelo realmente consume. **Su mecanismo principal es la conversación larga única: cada respuesta o reactivación programada vuelve a leer todo el historial desde el principio.**

```
每週總消耗 = Bot 喚醒的總次數 × 每次喚醒時重讀的上下文長度
```

Cuando una conversación acumula gran cantidad de registros o páginas web, una sola relectura puede alcanzar cientos de miles de tokens; responder una sola frase implicará procesarlo todo por completo.

Para ver un desglose de la comunidad, consulta [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi).

A partir del 12 de octubre de 2026, se implementa el plan de suscripción unificado The X Subscription. Los estándares para cada nivel son los siguientes:

| Nivel del plan | Precio suscripción individual | Precio por plaza de equipo | Multiplicador de cuota y permisos de Grok Bot |
| :--- | :--- | :--- | :--- |
| **Free** | $0 | No aplicable | Limited, sin Bot completo |
| **Plus** | $8/mes ($80/año) | No aplicable | Base, **explícitamente sin Grok Bot** |
| **Premium** | $30/mes ($300/año) | $30/plaza/mes | 4x, incluye Grok Bot |
| **Super** | $100/mes ($1000/año) | $100/plaza/mes | 15x, incluye Grok Bot |
| **Ultra** | $200/mes ($2000/año) | $200/plaza/mes | 50x, incluye Grok Bot |

Para más detalles sobre las reglas de cuota, consulta la [Guía oficial de Cursor: Planes y facturación](https://cursor.com/cn/help/grok-bot/plans). Existen varias limitaciones estrictas en el uso diario:

- **Los fondos de cuota no se acumulan**: con múltiples suscripciones solo se toma la cuota semanal más alta, no se suman ni combinan.
- **Alcance del fondo compartido**: la cuota semanal cubre Grok Bot y Grok dentro de Cursor, además de la versión web, móvil, Imagine y Voice, y se restablece periódicamente en una fecha fija.
- **Los modelos de terceros se facturan por separado**: invocar modelos que no sean Grok dentro de Cursor se factura directamente según el consumo.
- **Pago bajo demanda y límite mensual**: tras agotar la cuota semanal, activar On-demand se cargará al límite mensual (Monthly Limit); una vez superado el límite, las tareas en curso terminarán de ejecutarse; si se desactiva, dejará de responder a la espera del restablecimiento.

**Oficialmente se especifica que no hay selector de modelos (there is no model picker), por lo que no es posible cambiar a un modelo inferior.** Para controlar los costes solo queda reducir la frecuencia de reactivación, recortar la longitud del contexto o desviar los cálculos de alto consumo hacia el exterior.

## ¿Cuáles son las trampas habituales de alto consumo de cuota en Grok Bot? {#高耗操作清單-堅決避開的六大陷阱}

**Es imprescindible evitar los chats grupales con múltiples Bots, enviar imágenes y vídeos en la conversación, los sondeos de alta frecuencia durante todo el día, mantener una conversación larga de principio a fin, los bucles infinitos de reintentos sin protección y activar a ciegas el pago bajo demanda sin fijar un límite mensual.**

![Lista de operaciones de alto consumo: seis trampas que debes evitar a toda costa](/info/10-usage-s2.png)

Referencias: [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h), [《Guía para principiantes paso a paso para maximizar la autonomía de la cuota de Grok Bot (¡envíala directamente al Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf).

| Operación de alto consumo | Razón del gasto excesivo | Cómo evitar la trampa |
| :--- | :--- | :--- |
| Chats grupales con múltiples Bots | La reactivación mutua duplica los tokens en vacío | Un único Bot principal con Subagents asignados, o chats individuales humanos |
| Enviar imágenes y vídeos directamente en la conversación | Los fotogramas permanecen en el historial, pagando una relectura completa en cada turno | Procesar en la línea de comandos del terminal; el Bot solo recibe texto estructurado de menos de 100 palabras |
| Sondeos de alta frecuencia todo el día | Cada 15 minutos supone 672 veces por semana, la mayoría para confirmar que no hay cambios | Limitar al horario laboral o cambiar a scripts del sistema con Webhooks |
| Usar una sola conversación de principio a fin | Tras decenas de turnos, cada relectura consume cientos de miles de tokens | Una sola tarea por conversación; resumir periódicamente y reiniciar con Duplicate |
| Bucle infinito de reintentos sin protección | Decenas de auto-reintentos continuos tras un error | **Limitar obligatoriamente a un máximo de 2 reintentos en el prompt**; si falla, bloquear de inmediato y consultar a un humano |
| Activar a ciegas el pago por uso | Un bucle infinito puede generar facturas astronómicas de la noche a la mañana | **Mantener desactivado el pago bajo demanda habitualmente**; si se activa, establecer un límite mensual bajo y estricto |

## Flujo de trabajo en cuatro pasos para ahorrar cuota: del control de pérdidas a la derivación

![Flujo de trabajo en cuatro pasos para ahorrar cuota: del control de pérdidas a la derivación](/info/10-usage-s3.png)

### Asegurar la facturación y la línea de seguridad
1. Ve a Settings > Usage & Billing para comprobar tu plan (Premium $30/mes o Super $100/mes), el consumo y la cuenta atrás; si se queda bloqueado, haz clic en Stop para forzar la finalización.
2. **Desactiva Additional Usage / On-demand durante la depuración**; si lo activas, ve a cursor.com/dashboard > Gastos > Monthly Limit y fija un límite mensual ($10-$20).
3. Ve a Settings > General > Auto-review y **configura send, post, buy, transfer, delete y permissions en Ask first para aprobación manual**.

### Estandarizar sesiones e interacciones
- **Una sola tarea por sesión**; archívala inmediatamente al terminar.
- Guarda registros y textos largos en `/workspace/`, respondiendo únicamente con conclusiones y rutas; queda terminantemente prohibido pegarlos de vuelta en el chat.
- Las búsquedas en X están limitadas a 30 por minuto y 1000 al día (no descuentan de la cuota semanal); **indica al Bot que «extraiga los hechos clave y los presente en 3 a 5 puntos principales»**.
- Cuando una sesión se vuelva demasiado pesada, usa Duplicate para reiniciarla: primero haz que el Bot antiguo redacte un resumen de menos de 10 líneas, cópialo y envíaselo al nuevo Bot para que tome el relevo, y oculta el Bot antiguo.

### Enrutamiento de capacidades y derivación
- El Bot principal solo se encarga de desglosar, asignar y resumir tareas; no debe escribir código extenso ni convertir archivos grandes.
- **Para escribir código, utiliza el Agent en la nube de Cursor** (consume la cuota de Cursor y no descuenta de la cuota semanal), o ejecuta de forma headless Grok Build CLI / Codex CLI en una máquina virtual.
- Procesa capturas de pantalla, audio y vídeo desde la línea de comandos del ordenador en la nube, o utiliza modelos gratuitos para transcribirlos a texto antes de pasárselos al Bot.

### Reestructuración de tareas programadas
1. En Details > Routines, **pausa o elimina aquellas rutinas que hayan estado notificando «sin cambios» a diario durante la última semana**.
2. Cámbialas por scripts de Linux para sondeos de bajo coste y envía un Webhook para reactivar al Bot solo cuando haya cambios.
3. **Añade una instrucción de silencio a las rutinas conservadas**: «Tras la comprobación, si no hay cambios, finaliza la tarea inmediatamente y abstente estrictamente de generar cualquier texto».

Referencia: [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)

## Optimización profunda de rutinas y sondeos: adiós a las ejecuciones en vacío

Las rutinas son un agujero negro de cuota oculto: un sondeo de alta frecuencia **puede consumir la cuota de toda una semana en un solo día**.

### Reducción de frecuencia y control de ventanas de ejecución

Comprueba primero en el cliente si la Timezone del Bot coincide con la local. El consumo según las distintas configuraciones de programación es el siguiente:

| Configuración de programación | Ejecuciones semanales | Escenarios de aplicación |
| :--- | :--- | :--- |
| Cada 15 minutos (24/7) | 672 veces | Muy propenso a agotar la cuota en 1 o 2 días; rara vez necesario |
| Cada hora (24/7) | 168 veces | Monitorización de fallos en infraestructuras críticas |
| Cada hora de 9:00 a 17:00 en días laborables | 45 veces | Seguimiento de paneles Kanban, gestión de incidencias y triaje de correo |
| 3 veces por día laborable | 15 veces | Filtrado de bandeja de entrada por la mañana, mediodía y tarde; seguimiento del progreso |
| 1 vez por semana | 1 vez | Informes semanales del sector, resúmenes tecnológicos y archivado de documentación |

Para restringir al horario laboral, puedes usar el formato estándar de cron:

```text
CRON_TZ=Asia/Shanghai 0 9-17 * * 1-5
```

**Esta regla reduce las reactivaciones en un 93%**. Al ejecutarse a las horas en punto de 9:00 a 17:00 en días laborables en la zona horaria de Shanghái, solo se activa 45 veces por semana.

### Apuntar a habilidades y aplicar estrictamente la regla de silencio

Los prompts de las rutinas deben apuntar únicamente a las habilidades, sin entrar en detalles:
- Usa comandos de barra para especificar el nombre concreto de la habilidad y el objeto de inspección
- Define umbrales de decisión, condiciones de parada y límites de reintento único
- **Mantén un silencio absoluto cuando no haya cambios, sin enviar ningún mensaje**

El silencio total puede ocultar fallos imprevistos. Para una estrategia combinada, consulta la [Guía oficial de Cursor: Rutinas](https://cursor.com/cn/help/grok-bot/routines): mantén silencio en las rutinas de alta frecuencia y, en las de baja frecuencia, envía un registro de latido de una sola línea a las 18:00 todos los días para confirmar que la ejecución del día transcurrió con normalidad.

### Separación de doble rol: inspección con scripts cron de Linux y reactivación mediante Webhook

Mientras el Bot está suspendido, el ordenador en la nube Linux subyacente sigue funcionando: **no utilices grandes modelos para hacer comparaciones mecánicas**.
- Rol de comprobación: el cron del propio sistema programa scripts de Python o Shell para comparar datos; tarda pocos segundos y consume cero cuota.
- Rol de decisión: solo cuando el script detecta un cambio envía un Webhook para reactivar al Bot, permitiéndole realizar el análisis lógico y generar el informe.

Pasos de reactivación por Webhook y criterios de aceptación:
1. Obtén la dirección `POST to` y la `key` en la sección de Webhook de la rutina.
2. Envía una petición POST a dicha URL incluyendo el encabezado `Authorization: Bearer <key>`.
3. Comprueba el código de estado de la respuesta: un código 200 indica que la reactivación se realizó con éxito.

### Casos prácticos y trampas a evitar

- **Reestructuración de 6 rutinas del Bot Director de Marketing por 鐵柱**: se mantuvieron sin cambios 4 rutinas orientadas a entregas; 2 tareas en vacío que solo esperaban respuestas y revisiones de PR se sustituyeron por scripts cron del sistema con Webhook. El script realiza comprobaciones cada media hora durante el horario laboral diurno y reactiva al Bot solo si hay cambios.

  **La reestructuración tomó unos 23 minutos y redujo de 8 a 10 reactivaciones innecesarias a la semana**, logrando detectar novedades en menos de media hora.

  Origen del caso: [《Ahorrar un poco más de cuota en Grok Bot: optimización extrema de tareas programadas》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned).
- **Craig Hewitt consumió toda la cuota semanal de Ultra en 24 horas**: con una suscripción al plan Cursor Ultra de $200/mes, agotó la cuota de toda una semana en un solo día el 23 de agosto de 2026.

  Archivó 10 años de correos antiguos en el Bot supervisor con el que chateaba a diario; la API recuperaba el cuerpo de los mensajes y los añadía continuamente a la sesión, inflando el contexto a cientos de miles de tokens y provocando una tormenta de relectura masiva.

  Origen del caso: [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi).
- **Claves para evitar problemas con cargas pesadas**: **las tareas puntuales de alta carga nunca deben ejecutarse en el Bot principal con el que interactúas a diario**; es obligatorio crear un Bot dedicado o generar una copia mediante Duplicate; filtra el correo no deseado con reglas del buzón antes de procesar; y para tareas por lotes, valida siempre primero con 1 o 2 muestras antes del lanzamiento masivo.

## Control de chats grupales y múltiples Bots: erradicar las reactivaciones mutuas

**Bajo ninguna circunstancia incluyas varios Bots en un mismo chat grupal.** Cada mensaje nuevo se difunde a todos los integrantes, obligando a cada Bot a releer todo el historial para responder. 鐵柱 relató que 4 Bots conversando entre sí consumieron rápidamente el 25% de la cuota semanal (sin verificar).

La colaboración entre múltiples Bots debe regirse por una arquitectura en **estrella (hub-and-spoke), prohibiendo las conexiones horizontales**.

- Líder único: conserva un único Bot principal como punto de entrada de la interacción.
- Asignación unidireccional: el Bot principal inicia Subagents o transferencias punto a punto (A2A); los subagentes finalizan su ejecución y se cierran automáticamente, sin responder en el chat.
- Persistencia de resultados: la tarea ascendente escribe los datos en archivos bajo `/workspace/` y la descendente los lee directamente, sin debatir ni procesar en la ventana de chat.
- Limpieza de inactivos: elimina a tiempo los Bots inactivos tras confirmar que no tienen rutinas asociadas, evitando así reactivaciones accidentales.

Origen: [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)

## ¿Cómo realizar auditorías de uso y gestionar emergencias por agotamiento en Grok Bot? {#用量審計與應急機制-守住每週節奏}

**Dedica 15 minutos el día anterior al reinicio semanal para revisar los registros de las rutinas y la facturación; si la cuota se agota y la interfaz se bloquea, el ordenador en la nube Linux subyacente no se destruirá: puedes abrir el terminal directamente para tomar el control del código y hacer commits y pushes manualmente.**

### Proceso de auditoría semanal de 15 minutos

Se recomienda dedicar 15 minutos el día anterior al restablecimiento semanal para verificar lo siguiente:
1. Abre Settings > Usage & Billing para ver el porcentaje consumido. Si el consumo va por delante de lo previsto, revisa las tareas de días anteriores para localizar las fechas anómalas.
2. Accede a Details > Routines para examinar los últimos 20 registros de ejecución (Running, Succeeded o Failed), identificando rutinas con reintentos por error o ejecuciones frecuentes en vacío.
3. En cuanto al Bot principal marcado como favorito a partir de la v0.66.0, **prohíbe expresamente en su descripción que asuma tareas por iniciativa propia**, evitando que se encargue de tareas secundarias de forma autónoma.
4. Visita cursor.com/dashboard, revisa el Monthly Limit y el cobro real bajo demanda para confirmar que no haya cargos anómalos.

### Puntos ciegos de monitorización y cómo afrontarlos

El sistema no proporciona un desglose detallado del consumo por Bot, rutina, conversación o modelo, y el historial de 20 ejecuciones tampoco registra tokens ni importes económicos. **Para probar nuevos flujos es obligatorio utilizar el método de control de variables**:
1. Crea o modifica únicamente un Bot o una rutina cada vez.
2. Consulta el porcentaje en Usage & Billing antes y después de la ejecución para comparar el incremento; evita bajo cualquier circunstancia desplegar varias rutinas nuevas al mismo tiempo.

### Respuesta de emergencia: toma de control del ordenador en la nube al agotarse la cuota

Cuando la cuota semanal se agota al 100% y el chat de la interfaz se bloquea, el ordenador en la nube Linux subyacente no se destruye; puedes tomar el control abriendo el escritorio o el terminal del sistema desde el cliente:
1. Revisa el código y los archivos no entregados en el directorio `/workspace/`.
2. Ejecuta manualmente `git commit` y `git push` para subir los cambios al repositorio remoto.
3. Utiliza herramientas de línea de comandos locales en el terminal para continuar con la depuración, **sin necesidad alguna de gastar dinero comprando uso adicional**.

Origen: [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h), [《Guía para principiantes paso a paso para maximizar la autonomía de la cuota de Grok Bot (¡envíala directamente al Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Biblioteca de prompts para ahorrar cuota listos para enviar al Bot

### Prevención de la sobrecarga del contexto
- Haz que el Bot sintetice y memorice las reglas para **evitar repetir instrucciones continuamente en el chat**; en Bots compartidos, puedes añadirlas en el campo About de los detalles.
```text
請回顧我們至今的協作流程，執行兩項沉澱工作：
1. 把你需要長期遵守的行為邊界、彙報格式與約束規矩，提煉成一段不超過 300 字的精簡文本，我將直接粘貼到你的描述（Description）中；
2. 把我們剛才已經跑通的標準操作流程，封裝為一個可複用的技能（Skill），供後續例程直接呼叫。
完成提取後直接在對話中給出文本，不要展開多餘閒聊。
```
- Fuerza el guardado en disco de registros originales y documentación extensa en lugar de pegarlos directamente en la conversación.
```text
從現在起執行上下文瘦身規則：
所有抓取的長篇網頁、介面除錯記錄、大批原始資料和階段性中間產物，一律直接保存為 /workspace/ 目錄下的文本文件。在聊天視窗中回覆我時，嚴格只提供核心結論、關鍵變動要點以及對應的文件絕對路徑。嚴禁將大段原始文本或記錄程式碼貼回對話。
```
- Convierte imágenes multimodales para analizarlas desde la línea de comandos, **evitando el alto consumo en la ventana de chat**.
```text
遇到查看多張截圖、分析影片畫面、逐幀拉片、音訊轉寫或處理長掃描件的任務時，嚴禁在當前對話框中直接讀取原始多模態文件。
你應當在雲端電腦終端中呼叫系統已組態的命令列工具（如 Grok Build 或相關轉錄 CLI）在後台執行，並輸出簡明的結構化文字摘要；你只需閱讀生成的文字結論。如果當前環境無法執行命令列解析，請停下提醒我先在網頁端轉換成文字後再發給你。
```

### Derivación de tareas y código
- Las rutinas de monitorización deben cerrarse en silencio si no hay cambios.
```text
請列出當前你名下的全部例行任務（Routines），註明每條任務的觸發頻率、每週預計執行次數以及沒有變化時的處理邏輯。
找出其中執行最頻繁、消耗最大的任務，向我提出降低頻率的具體建議；同時為所有監控類例程新增硬性約束：執行檢查後若目標無實質變動，立刻靜默退出，嚴禁向我發送「一切正常」或「沒有新訊息」等無有效資訊的通報。
```
- Las tareas deben asignarse mediante chats individuales, **prohibiendo estrictamente que los Bots creen grupos o conversen entre sí por su cuenta**.
```text
嚴格執行獨立單聊工作模式：
只接收並執行我本人下達的直接指令。嚴禁在沒有得到我明確授權的情況下，主動在會話中喚醒、提及或聯絡其他 Bot 開展群聊協同；如果任務涉及多個專業環節，請將結果寫成文件並由我來負責跨 Bot 排程，或者將其派發給雲端電腦內的後台 CLI 工具獨立執行。
```
- El Bot se enfoca en la orquestación; la redacción y depuración de código extenso **se delega a la CLI en segundo plano de Grok Build**.
```text
明確你的角色定位是任務排程主管，核心職責是理解目標、拆解方案、組織邏輯和驗收結果。
不要在聊天視窗中直接編寫整段的長篇程式碼，也不要通讀整個大型倉庫做全量重構。涉及程式碼編寫、項目除錯和環境排查的工作，統一在後台呼叫雲端電腦內已經授權的 Grok Build 命令列工具執行。執行完畢後，你僅需檢查其退出狀態碼並將最終結論同步給我。
```

### Búsqueda, control de riesgos y relevo
- Guarda en disco los resultados de búsqueda en la plataforma X y reporta solo puntos clave simplificados en la conversación.
```text
在檢索 X 平台的推文、觀點或動態時，使用你自帶的免費搜尋能力。
搜尋到的批量推文原文，請直接寫入 /workspace/ 下的對應 markdown 文件中保存。在聊天框中向我彙報時，嚴格限制為 3 到 5 條提煉後的核心事實與推文對應連結，嚴禁把多條推文的大段原文搬運回聊天中。
```
- La automatización y las llamadas a API deben contar con un límite de reintentos, **interrumpiendo de forma obligatoria para aprobación humana en caso de anomalía**.
```text
在執行自動化任務、網路請求或文件排查時，嚴格執行防死循環規則：
同一操作或相似介面呼叫的重試上限為 2 次。如果連續 2 次重試均未成功，或者對下一步執行動作存在疑問，立刻中斷自動化流程並向我發起提問，詳細說明遇到的錯誤原因，嚴禁自行無限重試或在後台空轉。
```
- Antes de duplicar con Duplicate, haz que el Bot antiguo elabore una ficha de traspaso **estrictamente limitada a menos de 10 líneas**.
::: details Búsqueda, control de riesgos y relevo
```text
當前會話歷史較長，需要進行交接重置。請為我梳理一份 10 行以內的結構化交接總結，嚴格包含以下五項內容：
1. 你的角色設定與核心職責；
2. 當前正在進行的任務目標；
3. 已經達成的關鍵結論與做過的核心決定；
4. 下一步必須立刻執行的動作；
5. 新會話需要優先讀取的關鍵文件絕對路徑。
輸出完畢後不要執行任何新任務，等待我啟動新會話。
```
:::
- Rellena la clave gratuita de OpenRouter en el cuadro de claves para desviar directamente las tareas ligeras.
```text
請協助組態 OpenRouter 免費模型呼叫環境，嚴格遵循以下安全執行流程：
1. 在聊天框中調出系統的密鑰輸入彈窗向我收取 API Key，嚴禁讓我把密鑰明文發送在普通對話中；
2. 將獲取到的 Key 保存到 ~/.agents/secrets/openrouter.env 文件中，環境變數名指定為 OPENROUTER_API_KEY；
3. 對該密鑰文件執行 chmod 600 設定安全權限；
4. 執行全程嚴禁在終端標準輸出或聊天訊息中打印該 Key 的明文內容；
5. 使用 curl 呼叫一個以 :free 結尾的免費模型進行一次最小文本測試，確認呼叫成功且費用為 0，並將測試結果告訴我。
```

Referencia del prototipo: [《Guía para principiantes paso a paso para maximizar la autonomía de la cuota de Grok Bot (¡envíala directamente al Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)

## Errores comunes

- En Details > Routines, hacer clic en Test ejecuta el flujo real en la máquina, **descontando cuota real en cada ocasión**.
- Las cuotas de Cursor y SuperGrok **no se acumulan**: solo se toma en cuenta la que tenga mayor uso semanal y la otra queda inactiva.
- La facturación de grok.com y Grok Bot es independiente; las recargas de la versión web **no son deducibles ni reembolsables**.
- Pegar una API Key o Webhook en la ventana de chat consume tokens y es peligroso: **debes usar la ventana emergente segura para definir variables de entorno**.
- Hacer clic en «Actualizar ordenador» borrará el cron de Linux, conservando `/workspace/`; **tras actualizar, deberás reinstalar cron**.
- Duplicate descarta la conversación, la learned memory y los archivos adjuntos: **tendrás que proporcionar el contexto manualmente al nuevo Bot**.
- Al alcanzarse el Monthly Limit no se eliminan los procesos en curso: **las tareas largas seguirán ejecutándose hasta el final**, por lo que un bucle infinito podría generar costes excesivos.

## Cómo verificar y validar los resultados

1. Ve a Settings > Usage & Billing y a cursor.com/dashboard para revisar la facturación, asegurándote de ver el porcentaje consumido y la cuenta atrás de reinicio; **desactiva Additional Usage o fija el Monthly Limit en un valor bajo y seguro**.
2. Haz que el Bot simule borrar archivos o enviar peticiones de red hacia el exterior; debe mostrar obligatoriamente la tarjeta de aprobación **Ask first** y quedar en pausa a la espera, sin ejecutarse nunca en silencio.
3. Revisa la conversación actual y lanza una búsqueda en X de múltiples publicaciones: la barra lateral no debe acumular conversaciones largas de decenas de turnos, debe devolver solo de 3 a 5 puntos de resumen, guardar los textos largos en `/workspace/` y no volcar el texto original en el chat.
4. Dirígete a Details > Routines y haz clic en Test en una rutina de monitorización sin cambios; tras la comprobación debe cerrarse en silencio de inmediato, sin enviar mensajes innecesarios de «sin actualizaciones».
5. Pide al Bot que escriba código con dependencias multifichero y comprueba que invoque Grok Build en segundo plano o el Agent en la nube, **mostrando únicamente el estado final y el resumen de ejecución**, sin pegar pantallas enteras de código en el chat.

## Lecturas complementarias

### Capítulos relacionados

- [Capítulo 2 Planes y suscripciones: elige el nivel adecuado](/part1/02-plans)
- [Capítulo 8 Habilidades y rutinas: convierte un éxito puntual en una ejecución automática diaria](/part1/08-skills-routines)
- [Capítulo 20 Automatización fiable: programación, Webhooks y disparadores de eventos](/part3/20-automation)
- [Capítulo 25 Preguntas frecuentes y resolución de problemas](/part4/25-faq)

### Documentación oficial y centro de ayuda
- [Guía oficial de Cursor: Planes y facturación](https://cursor.com/cn/help/grok-bot/plans)
- [Guía oficial de Cursor: Rutinas](https://cursor.com/cn/help/grok-bot/routines)

### Casos prácticos de la comunidad y resúmenes de optimización
- [《4.1 Cuota y costes: lista para ahorrar cuota》](https://jcng5q8n0f3z.feishu.cn/wiki/KFbzwPhAliezlBkkvIuc1Abgn4h)
- [《Resumen del evento presencial de Hangzhou: cómo hice que la cuota de Grok Bot durara más》](https://jcng5q8n0f3z.feishu.cn/wiki/D04JwEvL7iss9UkDBvLcLuvyncf)
- [《Ahorrar un poco más de cuota en Grok Bot: optimización extrema de tareas programadas》](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [《Guía para principiantes paso a paso para maximizar la autonomía de la cuota de Grok Bot (¡envíala directamente al Bot!)》](https://jcng5q8n0f3z.feishu.cn/wiki/OPMJw2EgtiWMiJkcrzFc6gJ8nlf)
- [《How to Stop Your Grok Bot From Eating a Week of Usage in a Day｜Fan Grok Bot Radar》](https://jcng5q8n0f3z.feishu.cn/wiki/HO20w5OQQiNtNuk92mhcdQEynOi)

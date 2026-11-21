# Capítulo 4 Asignar tareas: mensajes, archivos adjuntos y un traspaso efectivo

Si los requisitos son demasiado breves, es fácil que busque docenas de páginas web irrelevantes y altere archivos. **Enviar un mensaje es hacer el traspaso de trabajo a una computadora en la nube**.

- **Establece límites estrictos de la tarea** y explica el propósito de los archivos adjuntos para evitar que tome decisiones por su cuenta
- Proporciona instrucciones claras a cambio de entregables listos para su aceptación directa
- Intervén en cualquier momento durante la ejecución para corregir desviaciones o usa la voz para complementar el contexto


![Asignar tareas: mensajes, archivos adjuntos y un traspaso efectivo](/info/04-handoff.png)

## Los cinco elementos de una buena solicitud

![Los cinco elementos de una buena solicitud](/info/04-handoff-s1.png)

Al asignar tareas a Grok Bot, **las instrucciones deben definir claramente los objetivos y el alcance de las herramientas**; consulta las especificaciones en la documentación de [《Grok Bot》](https://cursor.com/cn/docs/grok-bot).

1. **Acciones específicas y únicas**. Especifica «rastrear y comparar» o «redactar correo externo», no uses «investiga un poco»; cuanto más corta sea la ruta, más pasos se ahorran.
2. **Limitar las fuentes de datos**. Especifica páginas de Notion, canales de Slack como #sales-leads o URLs para evitar búsquedas descontroladas en toda la web.
3. **Trazar líneas rojas de aprobación**. La lectura y comparación se ejecutan automáticamente; **si implica enviar correos externos, pagos en línea o modificar/eliminar datos, debe pausarse y esperar aprobación**.
4. **Fijar el formato de entrega**. **Rechaza informes verbales** y exige generar informes en Markdown con enlaces o tablas CSV en `/workspace/leads/`.
5. **Establecer reglas de error y límites de hechos**. Distingue entre especulaciones y hechos objetivos; si la sesión expira, omite y registra, **prohibiendo bucles infinitos de reintento**.

## Especificaciones de archivos adjuntos y lista de restricciones

Consulta las reglas de subida en [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work).

### Restricciones de especificaciones

- En la versión de escritorio hay un **límite de 6 por mensaje** (el exceso debe colocarse en el espacio de trabajo); imágenes, texto y audio tienen un límite de 25MB, y video de 200MB.
- Si encuentras bloqueos o errores, conviértelo localmente a PDF, CSV o imagen antes de subirlo.

### Traspaso y chats grupales

1. **No presiones Enter inmediatamente después de arrastrar**, explica claramente la identidad de cada archivo, la lógica de correlación y las declaraciones de protección.

```text
上傳的 PDF 是已經簽署的標準採購合同樣板。上傳的 Excel 是本月供應商提交的實際報價清單。
請對照合同樣板中第 4 條關於各類物料的基準單價，逐行核驗 Excel 裡的實際報價。
標出單價超出基準價的所有條目，在附帶的備忘中引用合同中的對應條款編號。
將核驗結果另存為一份新的 Excel 表格，並輸出一份簡短的例外摘要。
請勿改動原始上傳文件。
```

2. Entre Bots en chats grupales **solo se admite texto plano**. Si un Bot posterior necesita ver los archivos adjuntos, deben enviársele por chat privado.

## Biblioteca de prompts prácticos para entrega de tareas

Para escenarios comunes, **usa directamente las plantillas**; solo modifícalas un poco y estarán listas.

1. **Investigación y contacto externo**: buscar pistas y preparar material, sin enviar directamente.
```text
從我們的 CRM 系統中獲取本週銷售管道的重點評審列表。
請跳過當前已經處於活躍跟進序列中的聯繫人。
在指定公開網頁和已授權的 Slack 相關頻道中，深入調研排名前五的重點帳戶，找出負責採購或技術的對口聯繫人。
參考我在系統中歷史郵件的口吻，為這五位聯繫人分別起草個性化的初次外聯郵件。
將草稿保存在系統草稿箱中，並在明天上午 9 點前在此對話中列出清單供我審批。未經我的明確確認，絕不向外發送任何郵件。
```
2. **Verificación de archivos adjuntos**: alinear múltiples tablas y auditar ingresos y gastos.
```text
附件中的 PDF 為《2026 年度差旅與報銷政策細則》，CSV 表格為本月部門提交的待審批費用報銷流水。
請逐項核對 CSV 中的每一筆申報項目：
1. 檢查報銷金額是否超過對應城市級別的住宿與餐飲標準。
2. 檢查單筆超過 500 元的支出是否有對應的發票類別標記。
3. 提取所有不符合政策規定的例外申報，列明行號、申報人、金額、超標原因及違背的政策條款。
最後生成一份 Markdown 格式的核查報告，並列出通過與未通過的統計彙總。保持原始 CSV 文件不被改動。
```
3. **Inspección de sitios web**: inspeccionar páginas y conservar evidencia.
::: details Biblioteca de prompts prácticos para entrega de tareas
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
4. **Revisión de planes**: revisar la lógica antes de operaciones complejas para evitar desviaciones.
::: details Biblioteca de prompts prácticos para entrega de tareas
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
5. **Notificación de mensajes entrantes**: extraer puntos clave y clasificar para su derivación.
::: details Biblioteca de prompts prácticos para entrega de tareas
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

## Reglas permanentes y tareas puntuales: no confundas las reglas de la casa con los quehaceres

![Reglas permanentes y tareas puntuales: no confundas las reglas de la casa con los quehaceres](/info/04-handoff-s4.png)

**Distingue claramente entre reglas permanentes y tareas puntuales** (consulta [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work)), no escribas parámetros temporales en configuraciones a largo plazo, ni vuelvas a definir las líneas rojas cada vez.

| Tipo | Ciclo y configuración | Ejemplos y restricciones |
| --- | --- | --- |
| Reglas permanentes | Efectivas en todas las sesiones; configurar en Bot Details o ingresar «Por favor, guarda esto en tu memoria como una regla permanente» | Líneas rojas de permisos, fecha YYYY-MM-DD |
| Tareas puntuales | Efectivas solo en la ronda actual sin persistencia; ordenar directamente | Procesar 12 cuentas o 3 audios, extraer la lista de la reunión de las diez en punto |

Todos los Bots comparten `/workspace` (consulta [《10 consejos esenciales para que tu Grok Bot funcione mejor》](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)).

**La memoria no puede reemplazar a los sistemas de negocio**; los saldos y el inventario deben consultarse en la fuente original, quedando estrictamente prohibido inventarlos.

## Intervención durante la ejecución de la tarea: detener, interrumpir y aprobar

![Intervención durante la ejecución de la tarea: detener, interrumpir y aprobar](/info/04-handoff-s5.png)

### Interrumpir y detener
Cuando el Bot se desvíe del objetivo, enviar un mensaje normal permite **interrumpir de inmediato**, por ejemplo enviando «cambia a la versión de especificaciones actualizada en octubre de 2026 y vuelve a verificar».

Si ocurre un error en la operación o una llamada de alto riesgo, envía cuatro caracteres en el cuadro de entrada para detenerlo.
```text
立即停止
```

**Detener solo bloquea acciones no ejecutadas; nunca revierte archivos ya guardados ni solicitudes de API ya enviadas**. Tras detenerlo, sigue tres pasos para la resolución de problemas.
1. Abre el panel de vista previa de la computadora en la nube para ver el estado.
2. Limpia los archivos a medio terminar o las escrituras incorrectas.
3. Reduce el alcance y define claramente los límites antes de reiniciar.

### Aprobación y tiempo de espera agotado
Al activar Auto-review o activar operaciones de alto riesgo, aparecerá una tarjeta de «Revisión de acción» (consulta la [《Guía de operaciones de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to)), que contiene tres opciones.
- Permitir una vez: solo aprueba esta vez; se seguirá preguntando en ocasiones similares posteriores.
- Permitir siempre: añadir a la lista blanca y no volver a avisar.
- Rechazar: bloquear completamente dicha operación.

| Escenario | Mecanismo de espera | Resultado por tiempo agotado |
| --- | --- | --- |
| Interacción en tiempo real | Suspensión en espera | Espera continua hasta que se haga clic para procesar |
| Desatendido en segundo plano | Expira automáticamente en unos 10 minutos (Expired) | **No se ejecuta la operación y finaliza la tarea** |

### Tomar el control de credenciales (Action needed)
Cuando involucre contraseñas, 2FA, así como CAPTCHA o pagos reales, aparecerá una tarjeta de toma de control; sigue estos tres pasos.
1. Haz clic en **Take over** e ingresa manualmente en la computadora en la nube.
2. Una vez completado, haz clic en **I'm done** para devolver el control.
3. **Nunca introduzcas contraseñas en texto plano en el cuadro de chat normal**.

## Interacción por voz: uso diferenciado entre llamadas de voz en tiempo real y dictado por voz

Grok Bot incluye **dos funciones de voz distintas**: dictado y llamadas; para más detalles, consulta [《Chat de voz con Bot》](https://cursor.com/cn/help/grok-bot/voice-chat) y la [《Guía de operaciones de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to).

### Comparación de los dos modos

| Modo | Activación y atajos | Salida y escenarios |
| --- | --- | --- |
| Entrada de voz (dictado) | En escritorio haz clic en «Iniciar entrada de voz», en Mac presiona Cmd+D, en Win/Linux presiona Ctrl+D, en el móvil toca «Iniciar dictado» | El texto se inserta en el cuadro de entrada, adecuado para ajustar prompts o añadir parámetros |
| Chat de voz en tiempo real | **Vacía el cuadro de entrada** y haz clic en el icono de onda (Start voice chat) | Llamada bidireccional en tiempo real, adecuada para ordenar ideas o realizar traspasos rápidos |

### Pasos para iniciar y errores a evitar

1. Abre una conversación individual con un Bot.
2. **El cuadro de entrada debe vaciarse por completo**; cualquier espacio o borrador residual ocultará el icono de onda.
3. Haz clic en el icono de onda; en el primer uso se deben conceder permisos de micrófono.
4. Aparecerá Connecting… (en móviles Calling…); cuando el Bot comience a hablar, la conexión estará establecida.

### Controles y restricciones estrictas

- Durante la llamada es posible silenciar, ver subtítulos desplazables y ajustar la velocidad y el timbre de voz; al cambiar de pantalla para consultar información, haz clic en la barra superior en «Volver al chat de voz» para regresar.
- **Solo admite chats individuales uno a uno**; no se puede iniciar en chats grupales, grupos de múltiples Bots ni con «Bots de equipo».
- **Solo se puede mantener una llamada al mismo tiempo**; para cambiar a un nuevo Bot es necesario confirmar «Finalizar y chatear».
- Al colgar, se genera automáticamente una tarjeta de Voice chat que registra la duración total; haz clic para consultar el texto completo y las tareas posteriores continuarán en el flujo de texto.

## Ejemplos comunes de errores y comparación con versiones optimizadas

1. **Restringir rutas**: si no se definen el alcance y el método, el Bot hará clics aleatorios en la consola, **e incluso modificará código en entornos de producción**.
```text
  幫我維護一下網站，看看有沒有什麼 Bug。
  ```
Cámbialo para delimitar páginas y pasos de inspección:
```text
  對站點清單（/workspace/sites.txt）中的三個靜態展示頁進行巡檢。
  用雲端瀏覽器打開每個頁面，檢查主控台是否有 404 或 500 報錯，檢查頂部導覽欄連結是否全部有效。
  將報錯資訊、對應頁面 URL 及當時的螢幕截圖寫入 /workspace/logs/err-20261014.md。
  全程僅做唯讀檢查，嚴禁點選任何帶有提交或刪除性質的表單按鈕。
  ```

2. **Límites de aprobación**: no otorgues permisos de envío externo; si hay un malentendido, **es fácil enviar contenido incorrecto a clientes importantes**.
```text
  讀取 Gmail 裡的未讀郵件，重要的直接幫我回一下。
  ```
Deja los puntos clave para la aprobación humana:
```text
  讀取 Gmail 中過去 12 小時的未讀郵件。
  僅篩選出發件人屬於我們現有企業客戶、且正文包含售後或諮詢訴求的郵件。
  根據產品常見問題手冊，為每封郵件起草回覆草稿並存入 Gmail 草稿箱。
  在當前對話中列出客戶名稱、郵件摘要與草稿正文，等待我的審批。未經我的明確確認，絕不點選發送。
  ```

3. **Separación de hechos**: no incluyas sesgos en los prompts, **para evitar que el Bot se adapte a suposiciones y confunda una pequeña promoción con una guerra de precios**.
```text
  去看看競品今天的動態，總結一下他們是不是要跟我們打價格戰。
  ```
Separa los datos objetivos de las conjeturas:
```text
  訪問競品官網的公開定價頁與首頁橫幅，獲取他們當下的方案價格表。
  對照我們在 /workspace/competitor/last-month-price.json 中記錄的舊價格：
  1. 事實列：標出哪些 SKU 的標價發生了變動，變動金額是多少，附帶頁面截圖與訪問時間。
  2. 推測列：基於該降價是限時促銷還是永久調價，給出你的分析理由。
  兩部分內容必須分開分欄呈現，不得將分析推論當作已知事實。
  ```

4. **Protección de solo lectura**: sin especificar las tablas principales/secundarias y los campos a conservar, **los datos originales pueden sobrescribirse y dañarse con facilidad**.
```text
  （直接拖入三個 Excel 表格）把這幾個表整理一下。
  ```
Debe aclararse qué tabla sirve de referencia y establecerse como de solo lectura:
```text
  上傳的三個表格分別是 7 月、8 月和 9 月的銷售明細。
  以「訂單編號」為唯一主鍵進行資料去重合並：
  1. 欄位統一保留：訂單號、成交日期、客戶名稱、銷售代表、成交金額。
  2. 生成一份全新的 Q3_sales_summary.csv 文件，保存在當前工作區。
  3. 保持我上傳的原始 7、8、9 月表格內容與檔名完全不變。
  ```

5. **Misión única**: no acumules múltiples tareas en un solo Bot; no solo desordenará la memoria, **sino que también agotará rápidamente la cuota semanal**.
```text
  你幫我寫一篇關於新產品的推文，順便把昨天的帳目算了，然後再幫我看看競品推特。
  ```
Divídelo en flujos de trabajo de tareas individuales:
```text
  遵循一個 Bot 負責一項核心任務的原則。當前 Bot 僅承擔社媒文案起草職責：
  依據 /workspace/product/spec.md 中的新功能說明，為 X 平台起草三條不同風格的發表文案。
  要求突出效能提升資料，字數控制在 280 字元以內。
  帳目核算與競品調研交由對應的專用 Bot 負責，不要在此會話中處理。
  ```

## Casos reales de traspaso en negocios

### Inspección diaria de sitios web y conservación de evidencia
El webmaster yishan redactó los requisitos de inspección directamente como especificaciones de aceptación. El directorio de trabajo está estrictamente limitado a `/workspace/site-check/`, permitiendo únicamente inspeccionar la página de inicio, los artículos más recientes y los accesos de suscripción, prohibiendo estrictamente el rastreo exploratorio.
- El informe debe conservar los enlaces completos, marcas de tiempo y capturas de pantalla de ese momento. **Los errores observados directamente se consideran hechos, mientras que las causas investigadas se consideran conjeturas; deben registrarse por separado.**
- Al encontrar una sesión expirada o enlaces rotos, se registra la incidencia y se omite directamente, prohibiendo insistir repetidamente. Para el método específico, consulta [《Cómo profundizar en el uso de Grok Bot en una hora》](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg).

### Intermediación de la bandeja de entrada y distribución de operaciones
一澤Eze configuró especialmente un Bot de bandeja de entrada para hacerse cargo de Gmail, sin conceder permisos de correo electrónico individualmente a cada Bot posterior.
- Al recibir correos de comentarios, los reenvía por chat privado al «Bot de comentarios de productos», y las facturas al «Bot de gestión de suscripciones».
- La comparación puramente numérica se delega directamente a scripts de línea de comandos. **Sincronizar solo datos incrementales con el Bot permite ahorrar cuota de uso semanal.**
- No vincules herramientas de altos permisos en todas partes; usar un punto de entrada dedicado para el filtrado inicial es lo más seguro.

  Para un resumen de experiencias, consulta [《10 consejos esenciales para que tu Grok Bot funcione mejor》](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc).

### Evaluación inicial del jefe de gabinete y creación de Bots
CyrilXBT hizo primero que el Bot jefe de gabinete leyera el Notion y Slack del equipo para detectar las tres tareas que más tiempo consumían, más se repetían y presentaban mayores bloqueos, avanzando en tres pasos.
1. El Bot jefe de gabinete las ejecuta manualmente guiado, con supervisión humana de la calidad de los resultados.
2. Tras confirmar que no hay errores, se consolida como una habilidad y se crea un Bot dedicado independiente.
3. Finalmente, se configura para que se ejecute automáticamente de forma programada.
**Los puntos que involucren envíos, compras, publicaciones o modificaciones en sistemas en línea deben conservar estrictamente la aprobación manual.

** Tutorial completo en [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)。

## Errores comunes que debes evitar

1. **Adjuntar archivos con descripción**: al subir varias imágenes o dos o más hojas de cálculo, **asegúrate de especificar su propósito**, de lo contrario es fácil confundir la relación principal-secundaria.
2. **Guardar reglas permanentes en la memoria**: las instrucciones individuales se pierden al cambiar de sesión; las normas y líneas rojas deben **escribirse en Acerca de / Responsabilidades en los detalles del Bot** o guardarse en la memoria.
3. **Prevenir la suspensión en la vinculación local**: en la nube pura sigue funcionando al cerrar la tapa, pero al vincularse con la computadora local, entrar en suspensión cortará la conexión; recuerda **verificar la configuración de energía y suspensión**.
4. **Compartir imágenes entre Bots mediante rutas**: entre Bots en grupos solo se admite texto plano; para compartir imágenes debes **guardarlas en la ruta compartida `/workspace/`** para que el otro Bot las lea.
5. **Si el botón de voz desaparece, vacía primero**: si quedan textos o espacios no eliminados en el cuadro de entrada, el botón de onda se ocultará; **vacía completamente el cuadro de entrada** para restaurarlo.
6. **Seleccionar permitir una vez para operaciones de alto riesgo**: no elijas «Permitir siempre» al enviar correos o modificar/eliminar datos; antes de que funcione de forma estable durante varias semanas, **insiste en elegir «Permitir una vez»**.

## Cómo realizar la aceptación al terminar

1. Ve a `/workspace/` o al directorio especificado para verificar los archivos; **confirma que se puedan previsualizar normalmente y sin caracteres extraños**, no te limites a mirar el texto temporal.
2. Revisa al azar 2 o 3 datos clave abriendo los enlaces o capturas de pantalla para evitar que el modelo invente información.
3. Revisa los registros de llamadas para **confirmar que no haya enviado comunicaciones no autorizadas, ni modificado configuraciones o sobrescrito archivos originales**.
4. Distingue hechos de conjeturas: coloca las citas textuales de las páginas en el área de hechos y las inferencias o sugerencias en el área de notas, corrigiendo de inmediato cualquier confusión.
5. Revisa la lista de excepciones: **si encuentras páginas web no válidas o campos faltantes, registra el motivo y completa la ejecución**, sin interrumpirla al primer error.

## Lecturas recomendadas

- Documentación oficial: [《Grok Bot》](https://cursor.com/cn/docs/grok-bot)
- Documentación oficial: [《Uso de Grok Bot》](https://cursor.com/cn/docs/grok-bot/work)
- Soporte oficial: [《Guía de operaciones de Grok Bot》](https://cursor.com/cn/help/grok-bot/how-to)
- Soporte oficial: [《Chat de voz con Bot》](https://cursor.com/cn/help/grok-bot/voice-chat)
- Artículo de la comunidad: [《Cómo profundizar en el uso de Grok Bot en una hora》](https://jcng5q8n0f3z.feishu.cn/wiki/GBV8wdZOaijukikjO0pcYFWKnbg)
- Artículo de la comunidad: [《10 consejos esenciales para que tu Grok Bot funcione mejor》](https://jcng5q8n0f3z.feishu.cn/wiki/Hfqxwy3zQiWkRPkVjRZcVCuHnbc)
- Artículo de la comunidad: [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

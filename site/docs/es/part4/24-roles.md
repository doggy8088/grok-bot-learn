# Capítulo 24: Estructura tu equipo de IA por puestos de trabajo

**No trates a Grok Bot como una simple ventana de chat o un asistente para todo.** Meter todas las tareas diversas en la misma sesión provoca saturación de contexto, lentitud y desperdicio de cuota, y por la noche, sin supervisión, es fácil enviar correos por error, modificar código de producción o realizar cobros y transferencias indebidas.

En el fondo, Grok Bot es una computadora en la nube equipada con un navegador independiente y un sistema de archivos local; **aprovecharlo al máximo requiere establecer una plantilla clara organizada por puestos**.

1. **Establece líneas rojas estrictas de aprobación**. Divide las responsabilidades de cada puesto según 5 señales concretas; los correos no revisados, el código de producción y las deducciones o transferencias de fondos deben detenerse invariablemente antes de la aprobación humana.
2. **Valida la transición de rutinas**. Configura la primera tarea de validación y las rutinas programadas para los 7 puestos clave, consolidando los criterios de aceptación en las revisiones rutinarias.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)


![Estructura tu equipo de IA por puestos](/info/24-roles.png)

## Cinco señales y principios organizativos para la división de puestos

![Cinco señales y principios organizativos para la división de puestos](/info/24-roles-s1.png)

### Delimitación de límites y aislamiento de entornos

Todos los bots bajo una misma cuenta comparten la misma computadora en la nube: los archivos, las sesiones web activas y los conectores son comunes. Sin embargo, la memoria y los hilos de conversación de cada bot son independientes; **mezclar diferentes tareas saturará la memoria con información irrelevante, provocando desviaciones en las instrucciones**.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Cinco señales para la división de puestos

**Siempre que el trabajo presente cualquiera de las siguientes características, se debe crear un bot dedicado e independiente.**

- Objetivos distintos: por ejemplo, encargarse de descubrir fallos del sistema frente a optimizar la tasa de conversión de un texto.
- Herramientas distintas: por ejemplo, conectarse principalmente a un repositorio de código frente a conectarse a hojas de cálculo de CRM.
- Estilos de trabajo distintos: por ejemplo, atención al cliente prudente y comedida frente a análisis de datos riguroso y objetivo que solo presenta cifras.
- Límites de aprobación distintos: por ejemplo, redactar memorandos internos debe estar separado de tener permisos para enviar correos externos.
- Horarios distintos: por ejemplo, revisar tickets cada hora frente a consolidar informes financieros todos los lunes.

### Comparación entre asistente generalista y equipo dedicado

**En comparación con un asistente generalista, un equipo dedicado aísla eficazmente el contexto y los riesgos de permisos.**

| Dimensión de comparación | Asistente generalista (propenso a problemas) | Equipo de bots dedicados |
| :--- | :--- | :--- |
| Contexto | Mezcla múltiples tareas comerciales, proclive a confusión de memoria y alucinaciones | Hilos independientes mantienen una memoria exclusiva, funcionando de forma estable |
| Permisos y depuración | El exceso de permisos aumenta el riesgo de acciones peligrosas; los conflictos son difíciles de localizar | Aprobación granular; la atribución de fallos es directa |
| Expansión de rutinas | Las tareas programadas interfieren entre sí, congestionando fácilmente el calendario | Ejecución asíncrona mediante cronogramas independientes o disparadores de eventos |

### Barreras humanas de aprobación y el principio de reversibilidad

La gestión de permisos debe adherirse firmemente a la **regla de barrera humana centrada en la reversibilidad**.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

| Categoría de operación | Ejemplos de comportamiento típico | Principio de tratamiento y mecanismo de aprobación |
| :--- | :--- | :--- |
| Operaciones reversibles | Redactar documentos, conciliar cuentas, etiquetar o extraer resúmenes | Permitir que el bot las complete de forma autónoma y registre logs |
| Operaciones irreversibles | Enviar correos externos, publicar abiertamente, fusionar código o debitar fondos | **Antes de ejecutarse, debe detenerse para generar un borrador o una comparación de diferencias, quedando en espera de que un humano haga clic en aprobar dentro de la interfaz** |

## De la validación en siete pasos a la implementación de bots persistentes

![De la validación en siete pasos a la implementación de bots persistentes](/info/24-roles-s2.png)

**No te apresures a programar tareas automáticas nada más crear el bot**; primero ejecútalo manualmente siguiendo la ruta oficial: [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases).

1. Establece reglas en el campo de descripción (Description): especifica con claridad las responsabilidades, las fuentes de datos y las líneas rojas. **Las reglas del campo de descripción tienen efecto permanente en todas las tareas**, mientras que las instrucciones en la ventana de chat solo aplican a una única sesión.
2. Ejecuta una prueba única en un entorno seguro: limita las fuentes de entrada y ejecuta manualmente un flujo de negocio real.
3. Ajusta hasta que sea revisable: realiza correcciones mediante el diálogo hasta que alcance el estándar de revisión sin intervención.
4. Guárdalo como habilidad (Skill): guarda los pasos directamente. Para páginas web complejas, utiliza la demostración «Teach a task» (límite de 10 minutos, no graba audio del micrófono) y completa las aprobaciones de ramificaciones.
5. Validación con un segundo conjunto de entradas independientes: prueba con datos diferentes para descartar el sobreajuste al ejemplo inicial.
6. Define la estrategia de rutina (Routine): antes de crear un Schedule o Trigger, define los reintentos por tiempo de espera y el manejo de errores; **ante la pérdida de red o datos faltantes, jamás debe inventar información de la nada**.
7. Mantén compuertas de aprobación para operaciones críticas: reserva la confirmación humana (Allow once/Deny) para envíos y pagos; solo asigna Auto Review a operaciones de riesgo extremadamente bajo.

## Dotación, rutinas y prompts para 7 puestos clave

Siguiendo estos principios, dividimos el equipo digital según las necesidades del negocio en siete puestos estandarizados: contenido, ingeniería, ventas, investigación, operaciones, asistente personal y gestión. Cada puesto cuenta con límites claros de dotación, una primera tarea ligera de validación, lógica de rutinas automatizadas y prompts listos para copiar y usar.

### 1. Puesto de contenido: Bot de comparación de posicionamiento y pipeline de contenido

Este bot se ejecuta **todos los lunes a las 08:00**, recopilando 3 páginas de competidores para compararlas con nuestra pantalla principal. Si hay cambios, abre una rama de PR; si no hay cambios, permanece en silencio.

- Permisos: solo abre PR o borradores de calendarios; **queda estrictamente prohibido fusionar directamente o publicar abiertamente**.
- Criterio de aceptación: el resultado se limita a 1 tabla y 1 párrafo de texto, verificable en menos de 30 segundos.
- Errores comunes: si falla el análisis, notifica inmediatamente un enlace roto sin hacer suposiciones.

::: details 1. Puesto de contenido: Bot de comparación de posicionamiento y pipeline de contenido
```text
每週一上午 08:00，對比我們產品定位頁 <our_landing_url> 與以下三個競品頁面：
1. <competitor_url_1>
2. <competitor_url_2>
3. <competitor_url_3>

產出以下內容：
- 主張對比表格：我方主張、對方主張、哪一方表述更直接明確。
- 競品提到但我們未提及的三項內容，需附帶原句引用。
- 我們提及但競品均未提及的三項獨有優勢。
- 改寫我方定位頁前兩段文案的草稿，使其更具針對性。

在程式碼倉庫 <repo_name> 中針對文案修改開啟一個 Pull Request，僅允許改動定位頁文案文件。
嚴禁合併該 Pull Request。嚴禁觸碰定位頁以外的程式碼或文件。
執行結束時彙報：自上週以來競品側發生的主要文字變化；若無變化則明確註明。
```
:::

### 2. Puesto de ingeniería: Bot de reproducción y diagnóstico de defectos

[Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

1. **Líneas rojas de permisos**: es obligatorio utilizar una cuenta de prueba dedicada; **queda estrictamente prohibido usar datos reales de clientes en el entorno de preproducción** y modificar alertas o parámetros de producción. Las credenciales sensibles deben gestionarse mediante Safe handoff, quedando prohibido su envío en texto plano.
2. **Pasos de depuración**: monitorea los issues etiquetados con `needs-repro` e inicia un navegador aislado en Staging para ejecutar la reproducción.
3. **Criterios de aceptación**: **rellena los comentarios del issue con un borrador que incluya el comportamiento esperado frente al real, códigos de estado de red y capturas de pantalla**, y luego elimina la etiqueta a la espera de la revisión de un ingeniero.

::: details 2. Puesto de ingeniería: Bot de reproducción y diagnóstico de defectos
```text
閱讀工單 <issue_url> 中的缺陷報告，並在預發表環境 <staging_url> 中嘗試復現該問題。

執行規則：
- 必須使用全新分配的測試帳號登入，嚴禁呼叫或匯入正式環境客戶資料。
- 詳細記錄完整的復現操作步驟、預期行為與實際出現的不一致表現。
- 捕獲例外發生時的主控台報錯記錄、網路請求狀態以及頁面截圖。
- 嘗試提取導致該問題的最小復現步驟。

輸出規範：
將整理好的復現包整理為 Markdown 文本附在下方。
嚴禁修改系統的報警規則，嚴禁更改預發表或正式環境組態。
若嘗試三次仍無法復現，詳細說明每次嘗試的輸入參數並標記為“未能穩定復現”，不要偽造成功的結論。
```
:::

### 3. Puesto de ventas: Bot de prospección y contacto con clientes potenciales

1. Cada día laborable a las 07:00, lee las primeras 20 filas de clientes potenciales no contactados en la hoja de cálculo y evalúalos según 3 criterios clave de ICP.
2. Selecciona a los 3 contactos más compatibles y redacta para cada uno un borrador de correo de no más de 4 frases, insertándolo en la hoja de cálculo.
3. **Queda estrictamente prohibido enviar correos reales a los clientes o añadirlos a secuencias automatizadas de contacto**. Cada afirmación personalizada debe incluir un enlace a la fuente; si el acceso está restringido, detén la tarea de inmediato y repórtala a un humano.

::: details 3. Puesto de ventas: Bot de prospección y contacto con clientes potenciales
```text
每個工作日早晨 07:00，處理表格 <sheet_url> 中最早未觸達的 20 行銷售線索。

針對每一行資料執行以下操作：
1. 訪問該公司官網及其公開社交帳號，提取過去 30 天內的實質性變動（如產品發表、高管變動、業務調整或受關注動態）。
2. 根據以下三條 ICP 標準逐一判定：
   - 目標團隊規模在 20 至 200 人之間；
   - 核心業務包含多工具協同流程；
   - 過去一個季度內有公開擴張動態。
   若不符合標準，在狀態欄標記“不匹配”並跳過後續步驟。
3. 為符合條件的線索撰寫一段不超過 4 句話的首觸郵件草稿。必須直接引用第一步中查到的具體變動事實，禁止使用任何寒暄客套套話。
4. 將郵件草稿填入表格的“首觸草稿”列，並在相鄰列貼上佐證該事實的公開連結。

安全要求：
嚴禁向任何郵箱發送真實郵件。嚴禁將聯繫人匯入自動發送佇列。嚴禁呼叫未授權的個人帳號。
執行結束時彙報：已處理行數、排除行數，以及如果你是銷售代表會優先發送的前三位名單。
```
:::

### 4. Puesto de investigación: Bot de verificación de hechos y cálculo de datos

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

Se conecta a la web pública, bases de conocimiento y archivos CSV de uso. **Si faltan datos, debe reportar un error e indicar los campos ausentes; queda estrictamente prohibido hacer estimaciones empíricas o dar sugerencias sin fundamento.**

- **Primera tarea**: buscar información sobre la consulta de negocio y generar una lista de verificación, clasificando las afirmaciones en «respaldada por pruebas», «contradice las pruebas» o «no confirmada por pruebas», enumerando las lagunas de información.
- **Rutina de ejecución**: **se ejecuta todos los lunes a las 09:00**, leyendo el CSV de facturación de la semana anterior para responder 4 preguntas cuantitativas fijas y **generando un informe de datos puros de no más de una página**.

::: details 4. Puesto de investigación: Bot de verificación de hechos y cálculo de datos
```text
研究課題：<research_topic_or_question>
閱讀並分析知識庫及公開檢索信源，生成一份可供直接發表的簡報。

執行規則：
- 打開每一個引用來源頁面，嚴禁僅憑模型內部記憶作答。
- 針對報告中的每一個核心結論，摘錄支援該結論的原文章節段落。
- 對每一個主張進行事實狀態標註：分為“有證據支援”、“與證據矛盾”或“證據未證實”三類別。
- 當不同信源存在分歧時，同時列出雙方原文，並註明發表時間先後。
- 整理在調研過程中未能找到確證資訊的內容列表，將其作為正式結論的一部分列在文末。

輸出規範：
輸出一份精簡報告、一張事實來源對比表、以及尚未解決的疑問清單。
嚴禁使用似是而非的推測性陳述式填充資訊空白。如果資料源完全未提及某事，直接記錄“未找到相關記錄”。
```
:::

### 5. Puesto de operaciones: Bot de soporte de tickets y conciliación contable

1. Gestión de tickets: redacta respuestas automáticamente cada hora; **las respuestas solo pueden escribirse en Internal Note, quedando estrictamente prohibido enviarlas al usuario**.
2. Conciliación de facturas: los días laborables a las 17:00, recopila las 10 facturas más recientes para cotejarlas con la tabla de órdenes de compra (PO), señalando coincidencias, excesos y partidas faltantes; las anomalías quedan suspendidas a la espera de revisión humana.
3. Líneas rojas de permisos: **debe emitir una alerta si la desviación del importe supera el 2% o si aparece un nuevo proveedor**; queda estrictamente prohibido aprobar transacciones o iniciar transferencias sin autorización.

::: details 5. Puesto de operaciones: Bot de soporte de tickets y conciliación contable
```text
每天下午 17:00，讀取財務收件箱 <finance_inbox> 中的新增發票，與採購訂單表格 <po_sheet_url> 進行逐筆核對。

針對每張發票執行以下比對：
- 提取金額、幣種、開票日期、採購訂單號（PO Number）與供應商全稱。
- 在採購表格中查找對應的 PO 記錄。若無匹配記錄，在備註欄標明“無對應訂單”。
- 比對發票金額與 PO 批准金額。若偏差絕對值超過 2%，立即將其標記為“金額例外偏差”，並記錄具體差額。
- 檢查供應商名稱是否屬於本季度首次出現的新供應商，若是，打上“新供應商待核實”標記。

結果寫入規範：
將比對明細寫入表格 <po_sheet_url> 的“對帳結果”工作表中，並附帶該發票的原件查看連結。
嚴禁執行任何批准報銷、發起付款或向供應商發送郵件的操作。
執行結束時彙報：成功匹配筆數、例外待查筆數，以及所有存在例外的發票總金額。
```
:::

### 6. Puesto de asistente personal: Bot de gestión de bandeja de entrada y agenda

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

1. **Operación diaria**: los días laborables a las 07:30, escanea los correos y calendarios de las últimas 24 horas y genera un informe matutino de una sola página.
2. **Primera tarea**: limpiar notificaciones irrelevantes y redactar para 2 correos importantes sendos borradores de no más de 4 frases cada uno, colocándolos en «Pendiente de revisión» y deteniéndose a la espera de la confirmación humana.
3. **Líneas rojas de permisos**: solo archivar correo no deseado y notificaciones; **queda estrictamente prohibido eliminar o modificar correos de contabilidad, legales, clientes clave o directivos**; **las respuestas solo se guardan como borradores sin enviarse jamás por iniciativa propia, y el calendario no se modifica**.

::: details 6. Puesto de asistente personal: Bot de gestión de bandeja de entrada y agenda
```text
每個工作日早晨 07:30，掃描我的工作郵箱 <email_account> 與日曆 <calendar_url>。

處理規則：
1. 自動歸檔系統通知、行銷推廣與電子發票。若郵件發件人包含會計師、法務顧問或核心客戶，嚴禁自動歸檔。
2. 提取需要我親自處理的事項，按緊急程度列出，註明發件人、主要訴求與截止期限。
3. 針對其中最需要緊急回覆的 2 封郵件，以我的口吻起草回覆方案：
   - 語言簡短直接，不使用套話與客套感謝語；
   - 整體控制在 4 句話以內，明確給出下一步行動建議；
   - 若涉及約定會議時間，主動從我日曆中調取明天下午的 2 個空閒時段供對方選擇。
4. 彙總今天必須參加的會議日程，標出準備資料缺失的場次。

安全邊界：
所有生成的回覆只能存入郵箱的“待審核草稿”資料夾中，嚴禁點選發送。
嚴禁拒絕、更改或新建任何日曆日程。
文末以一頁紙以內的篇幅彙報：今日概覽、已歸檔數量、待審草稿列表，以及今天唯一一件必須由我做決定的事項。
```
:::

### 7. Puesto de gestión: Bot de jefe de gabinete y coordinación interdepartamental

Como centro neurálgico del equipo, se encarga de revisar el panorama general, detectar cuellos de botella y organizar la inspección semanal.

**Líneas rojas de permisos**
- Mantenerse en silencio si no hay avances en el negocio.
- **Queda estrictamente prohibido enviar mensajes en nombre de otros o mover tarjetas de tableros**, solo proporciona sugerencias y **jamás toma decisiones en lugar de los humanos**.

**Tareas y rutinas**
1. Primera tarea: revisar a fondo los registros de las últimas 24 horas en tableros y Slack, elaborando una **lista dinámica de atención** que incluya bloqueos, estancamientos y elementos pendientes de decisión.
2. Días laborables a las 18:00: compilar el informe vespertino.
3. Viernes a las 16:30: comparar los registros y resultados de cada bot dedicado, marcar tareas ineficientes y proponer optimizaciones o sugerencias de eliminación.

[《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)

::: details 7. Puesto de gestión: Bot de jefe de gabinete y coordinación interdepartamental
```text
每個工作日傍晚 18:00，審閱過去 24 小時內已批准的通訊頻道 <slack_channels>、收件箱與項目看板 <board_url>。

提煉並輸出以下四部分內容，篇幅嚴格控制在一頁以內：
- 今日實質進展：提煉 5 行關鍵動態，說明關聯繫統與具體推進事項。
- 潛在風險預警：列出 3 項如果不做干預明天可能會惡化或延期的事情，說明阻礙人與卡阻天數。
- 待辦決議選項：對於必須由我決策的事項，給出選項 A 與選項 B 的利弊對比，並附帶你推薦的選項及一句理由。
- 日程減負建議：檢查我明天的日曆，挑出 1 個可以被取消或改為非同步跟進的會議，並說明原因。

輸出要求：
不發送任何外部訊息，不修改任何會議日程，不挪動看板卡片。
若全天各項指標平穩且無例外阻塞，直接輸出“今日執行平穩，無需要升級的決策事項”，不要為了湊字數生成冗餘報告。
```
:::

## Colaboración entre puestos y casos prácticos de orquestación multibot

![Colaboración entre puestos y casos prácticos de orquestación multibot](/info/24-roles-s4.png)

El núcleo de la colaboración multibot se basa en el flujo de tickets de trabajo; **los humanos solo actúan aprobando en los nodos críticos**, sin convertirse en transportistas de copiar y pegar manualmente.

### Coordinación multipuesto en el equipo de producto de SpaceXAI

Movez detalló 9 puestos dedicados en SpaceXAI, incluyendo un jefe de gabinete, un supervisor, análisis de datos, reclutamiento y 5 bots de desarrollo.
[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

1. **Desacoplamiento de objetivos**: los humanos definen los grandes objetivos, mientras que el bot supervisor se encarga de desglosarlos y distribuirlos a los bots de desarrollo modular.
2. **Transferencia en cadena**: el bot de reproducción genera el paquete de validación y lo transfiere directamente; el bot de resolución implementa la corrección y abre un PR, **deteniéndose en el nodo de revisión de código (Code Review) humana a la espera de aprobación**.
3. **Alineación de estado**: el bot de jefe de gabinete mantiene una lista dinámica y, si detecta tarjetas sin commits durante varios días consecutivos, avisa al supervisor para que las revise.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Operaciones ligeras de expansión global para equipos independientes

CyrilXBT y Codez articularon un pipeline operativo diario con solo 3 bots.
[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

| Bot por puesto | Responsabilidades colaborativas | Supervisión humana |
|---|---|---|
| Bot de contenido | Monitorear dinámicas del sector y competidores, redactar artículos de blog y preparar borradores para distribución multicanal | - |
| Bot de prospección de ventas | Buscar clientes potenciales y puntuarlos, generando 20 borradores de correo cada mañana de un día laborable | **El responsable dedica 10 minutos por la mañana a revisarlos y aprobarlos** |
| Bot de soporte al cliente | Monitorear tickets y redactar sugerencias internas consultando la base de conocimiento | **Tras verificar que son correctas, se convierten en respuestas públicas con un solo clic** |

## Errores comunes a evitar

- No crees un bot comodín para tareas diversas: hacer que un solo bot gestione tanto reembolsos como publicaciones en redes provoca saturación de memoria y dificulta la resolución de problemas; **apégate al principio de asignar un bot específico para cada tarea**.

  [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- No actives tareas programadas antes del paso 6: ejecutar tareas programadas antes de afinar los mecanismos de reintento y reporte de errores solo generará bucles infinitos de fallos durante la noche.
- No confundas compartir una cuenta con aislamiento de sandbox: los bots bajo una misma cuenta comparten la computadora en la nube y el navegador; se deben configurar correos independientes, ramas dedicadas y tarjetas de compra, **quedando estrictamente prohibido vincular cuentas personales privadas críticas**.

  [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- No escribas normas a largo plazo en la ventana de chat: una vez finalizada la conversación, las reglas se desvanecen; los flujos y los límites deben especificarse en el campo de descripción (Description) del bot.
- No definas reglas de escucha demasiado laxas: configurarlo para que se active ante «cualquier mensaje nuevo» consumirá enormes cantidades de cuota en vano y provocará acciones erróneas fácilmente.

  [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- No omitas las alertas por datos faltantes: ante un error de API o campos ausentes, el bot tenderá a inventar o falsificar datos; debe quedar estipulado de forma rígida en sus normas: **si la fuente de datos falta o está desactualizada, debe reportar el fallo con total veracidad de inmediato, quedando estrictamente prohibido improvisar o hacer adaptaciones por cuenta propia**.

  [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

## Cómo evaluar y verificar los resultados

### Verificación instantánea en 30 segundos
En la primera tarea entregada por un nuevo bot, **la verificación humana debe poder completarse en un plazo de entre 30 segundos y 1 minuto**. Por ejemplo, pedirle al bot financiero que busque elementos faltantes en las primeras 5 filas de facturas, o al bot de ventas que evalúe 3 empresas designadas. Si requiere media hora para cotejar los datos originales, significa que el alcance de entrada es demasiado amplio o que los criterios de aceptación no son claros; descártalo y reestructúralo directamente.

[《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

### Pruebas de estrés y barreras humanas
Antes de habilitarlo formalmente, introduce a propósito una instrucción de alto riesgo para realizar una prueba de estrés (por ejemplo, pedirle que gestione un correo de cobro y exigirle que pague de inmediato):
1. Observa si es capaz de **detenerse en estado de borrador y generar una tarjeta de aprobación**.
2. Si envía, fusiona o debita fondos por su cuenta sin haber obtenido aprobación, **revoca de inmediato los permisos de las herramientas y reescribe las restricciones de límites**.

### Verificación de los seis elementos antes de la activación
Antes de hacer clic en activar en la interfaz, verifica con claridad estas seis configuraciones básicas:
- Bot responsable asignado (Owning bot)
- Horario de activación y configuración de zona horaria (Schedule and time zone)
- Ruta de la fuente de entrada (Input source)
- Formato estructurado de salida esperada (Expected result)
- **Línea roja innegociable de aprobación humana (Approval boundary)**
- Política de reporte de errores ante cortes de red o datos faltantes (Missing data policy)

### Mecanismo de revisión semanal y recorte de puestos
Los cambios en el diseño web o en los campos pueden provocar que las rutinas fallen silenciosamente en segundo plano. **Dedica 15 minutos cada viernes por la tarde** a ejecutar el prompt de revisión semanal para que todos los bots del equipo informen de su estado:

[《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

::: details Mecanismo de revisión semanal y recorte de puestos
```text
全體 Bot 成員，請按各自崗位彙報本週的執行情況：
1. 本週累計觸發執行多少次，其中發生失敗或報錯的次數是多少？
2. 在執行過程中，有哪些步驟因資料缺失而跳過、重試或進行了推測？
3. 有哪些掛起等待審批的事項，我一直沒有給出答覆？
4. 本週生成的哪些文件或表格，我從未打開查閱過？

最後回答兩個核心問題：
- 在本週的執行中，哪兩個崗位之間存在明顯的重複勞動？
- 綜合目前的業務價值，你認為團隊中哪一個例程或席位最應該被精簡裁撤，理由是什麼？
```
:::

Evalúa de forma continua tres métricas a largo plazo según los informes:
- **Horas de trabajo ahorradas reales**: compara con las operaciones manuales y calcula el tiempo efectivo realmente ahorrado.
- **Magnitud de modificaciones en los resultados**: si el volumen de correcciones humanas a los borradores sigue aumentando, indica una desviación de las reglas y requiere recalibración.
- **Determinación de la trayectoria de confianza**: para los puestos que, tras múltiples ajustes, sigan sin producir resultados estables, ciérralos o elimínalos con firmeza.

[《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)

## Lecturas recomendadas

### Documentación oficial
- [Casos de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/use-cases)

### Casos prácticos de la comunidad
- [《Top 10 Grok Bot Prompts That Replace an Entire Team｜maestro》](https://jcng5q8n0f3z.feishu.cn/wiki/MKHywsPUNinwvEkIF9icQgj2nJg)
- [《How to master Grok Bot in 16 minutes - Full Course｜CyrilXBT》](https://jcng5q8n0f3z.feishu.cn/wiki/WGaCwZU71iHAGPkzjkLcahN2nHd)
- [《Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial)｜Codez》](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)
- [《GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)｜Movez》](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)

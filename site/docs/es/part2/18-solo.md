# Capítulo 18 Caso de estudio: Empresa unipersonal y equipo de IA

**Todos los Bots bajo la misma cuenta comparten la misma computadora en la nube**, equipada con su propio navegador, sistema de archivos y terminal.

Crear una docena de Bots de golpe y entregarles todas las cuentas es una receta para caer en trampas:
- Rutas equivocadas en páginas web externas y sobreescritura silenciosa de datos.
- Aprobaciones frecuentes en mitad de la noche que agotan al revisor.

Al aclarar los límites del puesto, el aislamiento de credenciales y las líneas rojas de aprobación, es posible **evolucionar desde la configuración del primer empleado de IA hasta la gestión de 29 Agents**.

## El primer empleado de IA: definir puestos y permisos como en una contratación

![El primer empleado de IA: definir puestos y permisos como en una contratación](/info/18-solo-s1.png)

Tratar a un Bot como una herramienta o como un empleado depende de si estás escribiendo un prompt puntual o estableciendo responsabilidades de un puesto. Un prompt puntual solo se ocupa de una tarea inmediata; una vez que se cierra la ventana, el contexto desaparece. Las responsabilidades del puesto constituyen un archivo fijo que determina la línea base de comportamiento y el modelo de pensamiento del Bot al procesar asuntos cotidianos.

### Definición del puesto y pruebas de admisión

**No otorgues permisos irreversibles al principio**; comienza con tareas monótonas, frecuentes y fáciles de revertir.

Antes de poner al Bot a trabajar, ejecuta dos pruebas de admisión para detectar errores con anticipación:
1. **Prueba de responsabilidad en una sola frase**: explica en una sola frase qué debe entregar. Meter cuatro o cinco verbos no relacionados equivale a que una sola persona haga el trabajo de tres, y si algo sale mal, no podrás localizar la causa raíz.
2. **Simulación en texto puro (Trial in text)**: toma menos de dos minutos; primero reporta los pasos, las URL que prevé visitar y los juicios dudosos.

La descripción del puesto se desglosa en cinco campos para delimitar claramente las fronteras:
- Owns: Entregables fijos.
- Inputs: Canales cuya lectura está permitida.
- May: Operaciones que puede gestionar de forma autónoma.
- Must ask before: Acciones de alto riesgo como gastar dinero o modificar configuraciones; **deben esperar aprobación humana**.
- Done when: Lista de verificación de aceptación objetiva.

```text
先不要執行任何實際操作。請逐步向我推演你的完整執行方案：
1. 列出你準備依次打開的工具、網址與呼叫的外掛。
2. 列出你在過程中需要做出的業務判斷。
3. 標出你目前資訊不足、存在疑慮或拿不準的決策點。
推演完畢後等待我的指令，嚴禁自行操作。
```

::: details Definición del puesto y pruebas de admisión
```text
崗位名稱：收件箱管理員（Inbox Manager）
Owns：
每天上午梳理工作郵箱，歸檔垃圾郵件與訂閱通訊，起草客戶諮詢的回覆草稿，標出需要我決策的緊急郵件。
Inputs：
僅限於 Gmail 中收件箱的未讀郵件與公司提供的常見問題回覆模版。
May：
閱讀郵件、按標記分類、打上處理標記、撰寫回復草稿、歸檔無回覆價值的宣傳郵件。
Must ask before：
嚴禁直接點選發送任何郵件；嚴禁歸檔來自財務、法務或房東的郵件；如果郵件涉及轉帳、退款、重置密碼或修改憑證，立即停下向我確認。
Done when：
工作日上午 9:00 前收件箱所有未讀郵件分類完畢；生成的草稿不超過四句話，語氣平實直接，不使用任何客套空話；所有待辦事項單獨列出截止日期。遇到不確定如何處理的郵件，保持未讀並掛起詢問，嚴禁自行猜測意圖。
```
:::

La configuración del puesto es completamente diferente a los prompts temporales.

| Dimensión | Prompt temporal | Configuración del puesto |
|---|---|---|
| **Objetivo y forma** | Conversación única, enfocada en una sola acción | Configuración a largo plazo, entrega resultados de negocio |
| **Límites y permisos** | Las instrucciones verbales facilitan extralimitarse; si hay error se reinicia | Tareas reversibles autónomas; irreversibles esperan aprobación; barrera humana obligatoria |

### Período de prueba de tres ejecuciones y escala de promoción

> Fuente: [Grok Bot: How to Hire Your First AI Employee (Full Guide)](https://x.com/distortgeekin/status/2105275395901726845)  
> Autor: [distort @distortgeekin](https://x.com/distortgeekin)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-0.png)

![Grok Bot: How to Hire Your First AI Employee (Full Guide)](/cases-img/fs55-1.jpg)

Cuando un nuevo Bot funcione por primera vez, **nunca lo dejes desatendido en segundo plano de inmediato**; pruébalo primero según la «regla de las tres ejecuciones» de distort.

1. 1.ª vez (observación total): mira la pantalla en cada paso y anota malinterpretaciones de instrucciones, pérdidas de contexto y conjeturas a ciegas.
2. 2.ª vez (corrección de reglas): cambia a una tarea de dificultad similar sin recordarle los errores anteriores. Enfócate en si los cambios en las reglas del puesto y permisos surtieron efecto, sin corregir los resultados por él.
3. 3.ª vez (prueba real sin intervención): no intervengas en todo el proceso; actúa solo ante aprobaciones o al alcanzar el límite de reintentos, verificando el nivel de completitud, número de intervenciones, tiempo consumido y cuota.

**Tras superar las tres pruebas, ingresa en la escala de promoción**, dividida en cinco niveles de permisos.

| Nivel | Mecanismo | Límite |
| :--- | :--- | :--- |
| Level 0 | Solo observación | No modifica ningún dato |
| Level 1 | Solo preparación | Tareas reversibles como búsqueda, resumen y maquetación |
| Level 2 | Aprobación humana | Pasos críticos suspendidos a la espera de confirmación |
| Level 3 | Ejecución independiente | Ejecución programada o por disparador, generando reportes periódicos con cadena de evidencias |
| Level 4 | Colaboración multi-Bot | Actúa como nodo de distribución y control de calidad |

Para ascender al siguiente nivel, se deben cumplir cuatro **indicadores estrictos**:
- 5 ejecuciones reales consecutivas sin fallos
- Todos los pasos de verificación superados
- Sin efectos secundarios no resueltos
- Mecanismo de reversión (rollback) verificado y operativo

Para prácticas relacionadas, consulta [«Grok Bot: How to Hire Your First AI Employee (Full Guide) | distort»](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc) y [«Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial) | Codez»](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg).

## De cero a una empresa operativa: Jefe de Gabinete y orquestación de equipos dedicados

Cuando una sola persona utiliza Grok Bot para construir un sistema operativo empresarial completo, el callejón sin salida más común es sobrecargar a un único Bot con demasiadas capacidades. Un Bot que gestiona clientes potenciales de ventas, redacta contenido, concilia cuentas y además modifica código verá su ventana de contexto rápidamente saturada de preferencias irrelevantes, lo que no solo confunde el contexto de negocio, sino que acelera el consumo de cuota.

### Arquitectura de Jefe de Gabinete y división departamental

Al crear un equipo, comienza construyendo un Bot Jefe de Gabinete (Chief of Staff). En el día a día, **solo interactúas con el Jefe de Gabinete**, y este se encarga de desglosar tareas, coordinar puestos dedicados y consolidar las entregas.

::: details Arquitectura de Jefe de Gabinete y división departamental
```text
你是一人公司的幕僚長（Chief of Staff），也是我日常溝通的唯一入口。
你的核心職責：
1. 接收我的業務目標，拆解為明確的工作階段，派發給對應的專職 Bot（調研、內容、程式碼、運維）。
2. 在群聊中排程各崗位接力，追蹤各任務交付狀態。
3. 檢查專職 Bot 提交的產物是否符合完成標準，核對資料來源與執行螢幕錄影。
4. 每天晚上彙總團隊進展，用不超過五行文字向我彙報核心結果、阻塞問題與需要我決策的審批項。
行為底線：
若無任何新進展或例外，保持靜默；嚴禁越權代替專職 Bot 編寫業務交付內容；嚴禁繞過人工審批直接執行外發、扣款或修改正式環境。
```
:::

- Bot de investigación: Las afirmaciones deben incluir fecha y URL; marcar dudas de forma proactiva; no inventar a la fuerza.
- Bot de contenido: Dar formato según plantilla; **queda estrictamente prohibido publicar directamente al exterior**.
- Bot de ventas: Guardar todos los correos de prospección en la bandeja de borradores; esperar aprobación humana antes de enviar.
- Bot técnico: Todo PR de GitHub debe adjuntar capturas de pantalla de pruebas superadas.
- Bot de finanzas: Cualquier ajuste de fondos debe listarse por separado para confirmación.

::: details Arquitectura de Jefe de Gabinete y división departamental
```text
團隊總體目標：
在兩週內針對新上線的知識庫產品，完成競品定價調研，產出一份對比簡報，並根據簡報結構生成 3 篇官網更新草稿。

協作規則：
1. 調研 Bot 先行檢索 5 家競品公開定價，生成包含引用網址的 Markdown 表格。
2. 調研完成後在群內移交給內容 Bot，內容 Bot 根據資料起草 3 篇文案，放入指定 Notion 頁面。
3. 幕僚長全程跟進看板狀態，若遇到資料缺失，要求責任 Bot 重新抓取或報錯，不得擅自編造。
4. 全流程中所有涉及對外發表的操作全部掛起，等待我在看板中勾選通過。
```
:::

| Arquitectura | Todoterreno individual | Línea de producción con Jefe de Gabinete |
|---|---|---|
| Colaboración | Memoria mezclada difícil de rastrear | **Memoria independiente por puesto**, atribución precisa de responsabilidades |

### Revisión de la cadena de evidencias y transferencia de confianza en cuatro semanas

> Fuente: [From Zero to a Running Company: The Grok Bot Agent Team Playbook](https://x.com/N01ennn/status/2091534159088959967)  
> Autor: [NO1ennn @N01ennn](https://x.com/N01ennn)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-0.jpg)

![From Zero to a Running Company: The Grok Bot Agent Team Playbook](/cases-img/fs44-1.jpg)

**Para poder cerrar la laptop con tranquilidad, el requisito previo es ver las pruebas (Show the tape).** Las entregas del Bot deben incluir tres credenciales/evidencias:

- Grabación de pantalla o registros de invocación de operaciones: mostrar la trayectoria web completa o la secuencia de llamadas a herramientas.
- Fuente original de datos y cifras: prohibidas las citas sin procedencia.
- Explicación de elementos omitidos por error y conclusiones deducidas.

**La confianza se transfiere gradualmente a lo largo de cuatro semanas:**

1. Semana 1 (fase de borrador): El Bot solo redacta; el humano lee todo y ejecuta manualmente.
2. Semana 2 (fase de aprobación): El Bot se detiene en los pasos clave; el humano solo verifica las acciones y aprueba.
3. Semana 3 (fase de reporte de anomalías): Las tareas de bajo riesgo se ejecutan de forma autónoma; solo solicita ayuda si hay anomalías o intento de extralimitación.
4. Semana 4 (fase de inspección de rutinas): Ejecución totalmente autónoma según rutinas; los fines de semana solo se revisa el informe de auditoría.

Para prácticas relacionadas, consulta [«From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn»](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd) y [«Grok Bot: How to Build Your First AI Team (Full Guide)»](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Práctica de empresa unipersonal: límites y operación independiente en una sola computadora en la nube

### Límites físicos

**Todos los Bots bajo la misma cuenta comparten una sola computadora**, utilizando los mismos directorios y sesiones. Oficialmente se especifica no considerar al Bot como una frontera de aislamiento: los prompts no evitan inyecciones y ejecutar comandos por error puede filtrar cookies y sesiones.

Respeta tres reglas básicas en todo momento:
- No inicies sesión en la banca electrónica principal ni en repositorios centrales, ni almacenes datos confidenciales en discos en la nube.
- En plataformas externas, utiliza únicamente subcuentas con privilegios mínimos.
- Los inicios de sesión externos deben realizarse mediante Handoff: el humano introduce la contraseña y el Bot solo hereda la Session.

### Automatización de sistemas sin API

**Los sistemas sin API dependen de las capacidades informáticas para hacer clics y rellenar formularios**; cuatro tipos de trabajo son idóneos para delegar primero:
- Prospección de clientes: Explorar directorios de comunidades y redactar correos.
- Seguimiento de entregas: Verificar desabastecimientos y rastrear envíos retrasados.
- Programación de contenido: Rellenar textos en la bandeja de borradores.
- Mantenimiento de código: Diagnosticar errores en sitios web independientes y generar parches.

::: details Automatización de sistemas sin API
```text
崗位名稱：供應鏈履約追蹤員（Supplier Logistics Bot）
Owns：
每天上午 10:00 登錄供應商門戶，核對昨天未發貨訂單狀態，提取物流單號，更新至運營表格。
Inputs：
供應商訂貨後台會話、本地待處理訂單表格。
May：
在供應商後台查詢訂單狀態、下載發貨清單 CSV、更新本地表格對應列的運單號與發貨時間。
Must ask before：
嚴禁點選「重新下單」或「取消訂單」；嚴禁修改收貨地址；若供應商後台提示帳戶欠款或商品缺貨，停止處理並立即向我報警。
Done when：
所有處理過的運單在表格中均標註狀態與回填時間；遇到後台頁面改版導致按鈕無法識別時，截取當前螢幕報錯並退出，不得盲目重試。
```
:::

### Umbrales y puntuación

> Fuente: [One-Computer Company: A Real Playbook For Running Solo On Grok Bot](https://x.com/zerqfer/status/2093299037705236540)  
> Autor: [ZER @zerqfer](https://x.com/zerqfer)

Solo cuando la **revisión humana se reduzca de forma estable a menos de 15 minutos al día** se deben añadir nuevos Bots, evitando multiplicar la carga. Completa una tarjeta de puntuación una vez al mes para prevenir el deterioro silencioso.

::: details Umbrales y puntuación
```text
Bot 月度執行評分卡
評估週期：2026 年 10 月
崗位名稱：[例如：訂單跟進助理]
1. 實際工時節省：本月相比純手工操作，實際節省了約多少小時？
2. 人工介入程度：產出草稿中，需要人工手動大幅修改的比例是多少（低於 10% 算達標）？
3. 信任度變化趨勢：對該崗位的自主執行信任度處於上升、持平還是下滑？
4. 例外與回滾記錄：本月出現過幾次頁面識別錯誤或越權報警？
5. 處置結論：[保留繼續執行 / 降級為人工審批執行 / 徹底停用刪除]
```
:::

Consulta [«One-Computer Company: A Real Playbook For Running Solo On Grok Bot | ZER»](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg).

## Sistema de entrega para AI Agency: línea de entrega mensual y barrera humana de control de calidad

![Sistema de entrega para AI Agency: línea de entrega mensual y barrera humana de control de calidad](/info/18-solo-s4.png)

Para una agencia de IA (AI Agency) que entrega a múltiples clientes, la principal dificultad radica en la estabilidad de la calidad y el control de costes de cuota ante la concurrencia de clientes.

El autor comunitario maestro compartió la arquitectura del sistema con la que una sola persona atiende a 5 clientes con cuota de retención (retainer) y mantiene la operativa mensual (el autor comunitario maestro afirma facturar 18 000 USD mensuales atendiendo a 5 clientes, no verificado).

### Las «tres pruebas de admisión» del menú de servicios

No aceptes proyectos totalmente a medida para no caer en la subcontratación manual; **para que un servicio entre en el menú de entrega automática, debe superar tres filtros**:

1. El brief se puede redactar como una lista estructurada.
2. El entregable cuenta con criterios objetivos de aceptación por parte de terceros.
3. **Haberlo entregado manualmente al menos 10 veces con anterioridad**. Sin haberlo hecho 10 veces no se conocen las líneas rojas, y delegarlo a un agente solo generará palabrería inútil.

Los servicios conformes incluyen comparar 40 documentos con un contexto de 500K para elaborar informes de investigación, redactar textos en lote a partir de archivos de muestra de voz (Voice File), o crear paneles de control y herramientas ligeras de extracción (scraping).

### Enrutamiento de modelos e intercepción del abismo de facturación de 195 000 Tokens

Asigna los modelos según la tarea; no recurras siempre al modelo insignia:
- Grok 4.1 Fast: Contexto de 2M, ejecuta limpieza y filtrado inicial.
- Grok Build 0.1: Responsable del 80 % de los materiales de desarrollo.
- Grok 4.6: 500K, ejecuta Agents de largo recorrido y razonamiento.

**Si la entrada supera los 200 000 Tokens, la tarifa se duplica de inmediato**. La pasarela debe **codificar un umbral estricto de 195 000 Tokens**, truncando o podando con error al excederlo.

### Revisor de solo lectura independiente y barrera humana tras tres reintentos

> Fuente: [How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](https://x.com/maestrooth/status/2092658066714177657)  
> Autor: [maestro @maestrooth](https://x.com/maestrooth)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-0.png)

![How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside)](/cases-img/fs47-1.png)

Cuando un Bot de producción revisa su propio producto tiende a la autovalidación, lo que oculta fácilmente fallos en los prompts. **La revisión debe dividirse en un circuito independiente de solo lectura**.

- Contexto independiente: introducir únicamente el brief original, las especificaciones del cliente y el producto final, sin proporcionar el razonamiento intermedio.
- Estrictamente de solo lectura: **al detectar defectos solo reporta FAIL y nunca reescribe**, evitando parches no autorizados que encubran problemas.
- Crítica adversarial: enfocada en detectar fallos graves; cualquier cifra no respaldada por datos se califica automáticamente como reprobada.

::: details Revisor de solo lectura independiente y barrera humana tras tres reintentos
```text
# 獨立審查者審核準則（reviewer.md）
你是一名獨立質量審查員，負責評估一份並非由你生產的交付產物。
你的唯一任務是找出交付物不符合客戶要求的地方。你絕不需要去讚美它的優點。

輸入物料：
原始需求 Brief、服務核對清單、客戶品牌聲音規範文件、最終交付草稿。
你未被提供、也嚴禁索取生產 Bot 的思考草稿。

審查規則（按順序嚴格執行）：
1. 逐條核對需求 Brief 中的清單項。指出任何未被完全覆蓋的要點。
2. 檢查全文，嚴禁殘留任何佔位符文字、TODO 標記或括號說明文本。
3. 全文中的每一個具體數位、引文、統計百分比與人名，必須能在客戶資料庫中找到對應出處。發現任何未註明來源的數位，必須直接判定為 FAIL。
4. 語言風格是否符合客戶過往已批准作品的語氣標準。

輸出格式：
第一行必須且只能輸出一個詞：PASS 或 FAIL。
如果判定為 FAIL，按以下格式列出所有缺陷：[清單條款] - [出現位置] - [具體問題及修正要求]。第一行後嚴禁輸出任何空洞的總結段落。
若因上下文缺少憑據導致無法核驗某一項，直接判定為 FAIL。
```
:::

```text
單任務自動化生產循環規則：
1. 生產 Bot 基於需求與聲音規範生成第 1 版草稿。
2. 獨立審核 Bot 執行審查。若返回 PASS，記錄記錄並進入待交付佇列。
3. 若返回 FAIL，系統將審查不通過的具體原因拼接入下一輪 Brief，由生產 Bot 進行針對性修復重試。
4. 重試上限（MAX_ATTEMPTS）嚴格設定為 3 次。
5. 若連續 3 次均無法通過審查，系統立即終止自動重試，觸發報警將原始 Brief、草稿與審查報錯完整推送到人工桌面由人工兜底接管。
```

**El traspaso admite como máximo 3 reintentos**, evitando bucles infinitos que disparen elevadas facturas de Tokens. Si la máquina no cumple con los estándares tras tres intentos, indica un conflicto en los requisitos y un humano debe intervenir para decidir.

Consulta [«How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside) | maestro»](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf).

## Práctica con 29 Agents: cómo expandirse sin fricciones desde un operador individual hasta una legión

![Práctica con 29 Agents: cómo expandirse sin fricciones desde un operador individual hasta una legión](/info/18-solo-s5.png)

Una vez familiarizado con la configuración de un solo empleado y el bucle cerrado de control de calidad con dos Bots, las demandas del negocio te impulsarán naturalmente a expandir el equipo.

El autor comunitario Melvin Vivas documentó su experiencia completa expandiendo gradualmente Grok Bot a 29 agentes dedicados (el autor comunitario Melvin Vivas afirma tener 29 Bots, no verificado).

### Distribución funcional y evolución progresiva de 29 Agents

**Estos 29 Bots surgieron orgánicamente según la necesidad**: al encontrar tareas repetitivas en el día a día, se creaba un rol dedicado, y cuando hubo muchos roles, la Jefa de Gabinete Emma pasó a coordinarlos. El negocio se divide en siete áreas clave:

- Centro de despacho: Emma se encarga de la gestión global y la distribución de tareas.
- I+D técnica: El CTO gestiona la arquitectura; **Coder coordina Cursor para escribir código automáticamente, crear PR y corregir errores**, todo sin necesidad de abrir un editor local.
- Investigación de vanguardia: Escanea las novedades de código abierto en la plataforma X durante todo el día y elabora resúmenes.
- Matriz de contenido: Responsable de la redacción de textos y análisis posteriores en varios canales.
- Desarrollo de negocio: Búsqueda de oportunidades comerciales y prospectos de colaboración.
- Operaciones y seguridad: Gestión de correos, copias de seguridad y revisiones de seguridad.
- Crecimiento personal: Registro de hábitos, seguimiento del mercado y fundamentación de decisiones.

### Línea de producción colaborativa multi-Agent: caso de conversión de prototipo técnico a contenido

Cada Bot toma el relevo apoyándose en la computadora en la nube compartida y en referencias de sesión.

::: details Línea de producción colaborativa multi-Agent: caso de conversión de prototipo técnico a contenido
```text
端到端跨團隊協同案例：
1. 【情報捕獲】：X 調研員監控到某大模型最新發表，抓取官方文件與程式碼倉庫地址，整理為技術要點。
2. 【任務排程】：幕僚長 Emma 捕獲該報告，根據設定規則判定該模型具備測試價值，自動將任務下發給技術團隊。
3. 【工程交付】：寫程式員 Coder 接收技術說明，調起 Cursor Cloud coding agent 在雲端編寫 Google Colab 示範筆記本，推送到 GitHub 倉庫並自動建立 Pull Request。
4. 【排錯閉環】：執行測試出現相依套件版本衝突，終端 Traceback 自動返回 Coder，Coder 修復程式碼再次提交 PR 通過測試。
5. 【內容物料轉譯】：PR 合併後，Emma 將成功程式碼倉庫與技術參數推送給內容創作團隊，YouTube 指令碼助手與 X 內容經理在半小時內完成多平台發表草稿，存入指定待審目錄。
6. 【人閘閉環】：創始人全程不介入程式碼編寫與格式排版，僅在最後核驗 Colab 實際執行效果，並點選確認對外發表推文。
```
:::

**Para hacer cambios no es necesario abrir las 29 ventanas una por una**; una sola instrucción emitida por el supervisor se sincroniza en cuestión de segundos.

### Cinco señales para la división de roles y el método de automatización en siete pasos

Cuando los objetivos de evaluación, las herramientas invocadas, el estilo de trabajo, los límites de aprobación (los borradores y la comunicación externa jamás deben mezclarse) o los ciclos de programación difieren, es imprescindible **separar en un Bot independiente**.

1. Envía los objetivos, fuentes de datos, formatos y límites de parada al Bot para que los memorice; para Bots compartidos, escríbelo en el About de los detalles.
2. Elige una tarea real controlada para una sola ejecución.
3. Ajuste manual hasta alcanzar la exención de inspección.
4. Consolidar en una Skill reutilizable.
5. Reevaluar la generalización con nuevos datos.
6. **Activa la Routine solo tras definir el límite de reintentos y las alertas por omisión**.
7. Para enviar correos, realizar pagos o aplicar cambios, vincula obligatoriamente la barrera humana Require Approval.

| Fase | Escala | Arquitectura y cuello de botella |
| :-- | :-- | :-- |
| 1 Operador individual | 1 Bot | Bucle cerrado de verificación con barrera humana completa; requiere supervisión continua |
| 2 Grupo | 2-3 Bots | Separación de producción y revisión; mantenimiento diario reducido a 15 minutos |
| 3 Jefe de Gabinete | 4-6 Bots | Distribución y panel de control; **evitar que el Jefe de Gabinete realice tareas menores** |
| 4 Legión | 10-30 Bots | Standups multilínea; poda periódica de rutinas ineficaces |

### Sistema de paneles de control y mecanismo de reuniones diarias (standups)

> Fuente: [How I use Grok Bot: My team of 29 AI agents](https://x.com/melvindvivas/status/2109480575421808962)  
> Autor: [Melvin Vivas @melvindvivas](https://x.com/melvindvivas)

Cuando los Bots superan los 5, olvídate de usar múltiples ventanas de chat; es imposible seguirles el ritmo. **La colaboración multi-Bot depende principalmente de dos aspectos: paneles de control e inspecciones periódicas**:

- **Panel de estado compartido**: No dejes las tareas dispersas en el historial de chat; consolídalas en un panel de Notion o de base de datos con cinco estados definidos: `Todo`, `Working`, `Blocked`, `Ready for Review`, `Done`.

  Si el Bot encuentra un error desconocido o carece de permisos, cambia directamente la etiqueta a `Blocked` y solicita asistencia humana; en el día a día basta con observar el flujo de las tarjetas.
- **Inspección periódica y conciliación**: Cada Bot admite como máximo 50 Routines, ejecutándose a lo sumo cada 5 minutos.

  **A las 3:00 a. m. se revisan automáticamente enlaces rotos en el código y el tamaño de los paquetes, y a las 5:00 a. m. un Bot supervisor (como Jenny) revisa uno a uno el Playbook de los Bots dedicados**, lo que previene eficazmente que el modelo olvide con el paso del tiempo.

```text
全體專職 Bot，開始進行本週團隊回顧審計。請各崗位彙報：
1. 本週你實際執行了多少次任務，其中失敗或例外的中斷有多少次？
2. 在執行過程中，有哪些步驟存在推測行為、跳過行為或由於資料缺失強行拼湊的情況？
3. 有哪些掛起的審批事項我一直沒有回應？有哪些生成的物料我從來沒有打開查看過？
4. 請指出：在當前的工作流中，你發現哪兩個 Bot 存在職責重疊或重複工作？
5. 給出客觀建議：為了節省整體用量額度，我們下週最應該裁撤哪一個無效的 Routine 或崗位？
```

Para prácticas relacionadas, consulta [«How I use Grok Bot: My team of 29 AI agents»](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh), [«GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course) | Movez»](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54) y [«Grok Bot: How to Build Your First AI Team (Full Guide)»](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe).

## Errores comunes

### Permisos y aprobaciones
1. Las computadoras en la nube compartidas utilizan la misma Session sin aislamiento: **jamás inicies sesión en cuentas principales ni en sistemas sensibles**.
2. Require Approval solo bloquea operaciones no ejecutadas y no puede revertir daños: **establece una barrera humana estricta desde el primer momento para acciones de alto riesgo**.
3. Las solicitudes de aprobación expiran tras unos 10 minutos sin respuesta (Lapse): durante la noche **es imprescindible configurar listas blancas Allow rule o detenerse en fase de borrador**.

### Costes y arquitectura
4. Si la entrada supera los 200 000 Tokens, el precio unitario se duplica: **la capa de enrutamiento debe establecer una intercepción estricta y poda en 195 000 Tokens**.
5. No intentes que un solo Bot se encargue de todo ni clones 5 Bots genéricos: **una división poco clara del trabajo solo contaminará el contexto y desperdiciará cuota**.
6. No configures sondeos (polling) cada 5 minutos ni escuches todos los mensajes: **ante la falta de una No-data policy, las caídas de red facilitan la invención de datos y agotan la cuota**.

### Reglas y traspaso
7. Las indicaciones en la ventana de chat pierden efecto al refrescar: **las disciplinas inter-tareas deben quedar memorizadas por el Bot**; en Bots compartidos, escríbelas en el About de los detalles; los Bots personales ya no cuentan con Description.
8. Entre distintos Bots, no transfieras todo el historial: **el paquete de traspaso solo debe conservar el objetivo y la ruta de los entregables, junto con las conclusiones y los requisitos para el siguiente paso**.

## Cómo verificar una vez completado

1. **Verificar credenciales**: Elimina las credenciales bancarias y principales de Plugins y del navegador, sustituyéndolas por subcuentas o Sessions; **jamás almacenes contraseñas en texto plano en el historial de chat**.
2. **Validar puestos**: El Bot debe incluir Owns/Inputs/May/Must ask before/Done when, añadiendo una declaración contra la desviación al final; **ante la falta de datos, reportar error de inmediato y prohibir estrictamente inventar información**.
3. **Probar la barrera humana**: Envía instrucciones de cargo o eliminación; deben **activar al 100 % la suspensión por Require Approval**.
4. **Resistencia a auditorías**: Alimentar con un borrador de datos falsos; el Bot de control de calidad debe **devolver FAIL en la primera línea** sin realizar cambios por su cuenta; tras 3 fallos consecutivos, detenerse y lanzar alarma.
5. **Estabilidad de rutinas**: El estado del panel debe actualizarse en tiempo real; antes de activarlo, pulsa Test run para comprobar que funcione; **las tareas programadas no deben depender de aprobaciones nocturnas que tarden más de 10 minutos**.

## Lecturas complementarias

### Documentación oficial

- [Organizar negocios y trabajo en Grok Bot](https://cursor.com/cn/docs/grok-bot/work.md)
- [Colaboración y gestión de permisos de Bots para equipos](https://cursor.com/cn/docs/grok-bot/teams.md)
- [Arquitectura de seguridad y entorno de ejecución de Grok Bot](https://cursor.com/cn/docs/grok-bot/security.md)
- [Planes, cuotas y detalles de facturación](https://cursor.com/cn/help/grok-bot/plans.md)
- [Configurar tareas programadas y rutinas de activación](https://cursor.com/cn/help/grok-bot/routines.md)
- [Conectar aplicaciones](https://cursor.com/cn/help/grok-bot/connect-apps.md)

### Fuentes prácticas de la comunidad

> Fuente: [GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](https://x.com/0xMovez/status/2100261918896169259)  
> Autor: [Movez @0xMovez](https://x.com/0xMovez)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-0.png)

![GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course)](/cases-img/fs52-1.jpg)

- [«From Zero to a Running Company: The Grok Bot Agent Team Playbook | NO1ennn»](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)
- [«How to Build an $18K/Month AI Agency on Grok (Exact Setup Inside) | maestro»](https://jcng5q8n0f3z.feishu.cn/wiki/MtKDwMe0FiNf4wkxwj7cgnnAndf)
- [«One-Computer Company: A Real Playbook For Running Solo On Grok Bot | ZER»](https://jcng5q8n0f3z.feishu.cn/wiki/VcevwDlGGimAvjkEGGPceItanNg)
- [«GrokBot Agents: build a team that works for you 24/7 in 10 steps (Full-Course) | Movez»](https://jcng5q8n0f3z.feishu.cn/wiki/LSfqwAew5i4h3mkuQT9cgw3jn54)
- [«Grok Bot: How to Hire Your First AI Employee (Full Guide) | distort»](https://jcng5q8n0f3z.feishu.cn/wiki/KGhnwWY0QiQrhgkKy2FcgECtnnc)
- [«Grok Bot: How to Build Your First AI Team (Full Guide)»](https://jcng5q8n0f3z.feishu.cn/wiki/MRhNwTEH8i0PrDkSp5uce2V7nKe)
- [«How I use Grok Bot: My team of 29 AI agents»](https://jcng5q8n0f3z.feishu.cn/wiki/YBjswa1rnivPkjk5BpscN6mcnDh)
- [«Grok Bot Agents: how to automate your life in 10 Steps (Full-tutorial) | Codez»](https://jcng5q8n0f3z.feishu.cn/wiki/PPKGwdkOkiGsxRkSInucbrNgnAg)

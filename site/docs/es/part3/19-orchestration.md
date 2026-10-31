# Capítulo 19 Orquestación de equipos: estatutos, puestos y delegación

Crear varios Bot especializados de golpe suele provocar que se citen datos falsos entre sí y que termines transfiriendo datos manualmente entre 5 ventanas. **Todos los Bot de una misma cuenta se ejecutan en la misma máquina virtual de ordenador en la nube**, compartiendo disco, sesiones de navegador y el fondo de cuota, sin aislamiento de datos.

1. **Configura un nodo central 1+N marcado con estrella**, donde el Bot principal se encarga del enrutamiento.
2. Delimita las responsabilidades con un contrato de seis líneas y diez reglas límite, añadiendo compuertas de aprobación humana.
3. Realiza la entrega de tareas mediante archivos en el directorio compartido del ordenador en la nube, coordinado con un ritmo de delegación de cuatro semanas y cinco rutinas estándar.

[《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)


![Orquestación de equipos: estatutos, puestos y delegación](/info/19-orchestration.png)

## 1. Bot principal y Bot especializados: arquitectura de nodo central 1+N marcado con estrella

![1. Bot principal y Bot especializados: arquitectura de nodo central 1+N marcado con estrella](/info/19-orchestration-s1.png)

Para múltiples Bot, utiliza una arquitectura 1+N, **haciendo que el Bot principal monopolice el punto de entrada de la conversación**, mientras que los Bot especializados solo se encargan de la ejecución.

- Comparten la máquina virtual, `/workspace`, conectores (Settings → Plugins / Connect Apps) y Skill; los chats privados y las Routine son independientes.

1. En el lateral izquierdo, crea un «Jefe de Gabinete» (Chief of Staff) y márcalo con estrella (clic derecho para cambiar); v0.66.0 (2026-10-02) admite sugerencias proactivas.
2. **Está estrictamente prohibido que el Bot principal escriba código de negocio**; solo debe encargarse de desglosar y asignar tareas, ya que si el despachador interviene directamente en la ejecución perderá el enfoque.
3. Los requerimientos solo se envían al Jefe de Gabinete; los procesos descendentes devuelven un informe de no más de cinco líneas y permanecen en silencio el resto del tiempo.

| Dimensión | Bot principal (marcado con estrella) | Bot especializado |
|---|---|---|
| Rol | Centro de tareas, no escribe código de negocio | Ejecución especializada, puede escribir código con pruebas |
| Interacción | Envía proactivamente un informe diario | No inicia chats privados con el usuario |

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 2. Plantilla de estatuto: redactar la descripción del puesto como un contrato de cumplimiento

### Qué es
**Un estatuto es un contrato a largo plazo**. Para un Bot personal, envíalo en la conversación y pídele que lo recuerde; para un Bot compartido, escríbelo en la Description de About en detalles. La barra lateral ya no incluye Edit Profile.

- No uses adjetivos como "maestro del copywriting"; la falta de límites claros propicia alucinaciones.
- **Debe redactarse como un contrato**, definiendo con verbos las responsabilidades, formatos de entrega, compuertas humanas y criterios de parada.

### Cómo implementarlo
1. **Rellena el acuerdo de seis líneas**: Para un Bot personal, envía el acuerdo en la conversación y haz que lo recuerde; para un Bot compartido, escríbelo en la Description de About en detalles.

```text
Own: 負責需求的統一拆解、分派、彙總與五行簡報彙報。
Sources: 人工下發的指令、項目看板文件。
Output: 純文字狀態摘要，超出五行時輸出為指定文件路徑。
Approval: 任何對外通信、採購、刪除操作必須暫停等待確認。
Failure: 下游專職 Bot 報錯時如實上報，不使用過期資料假裝完成。
Never: 永遠不直接編寫業務程式碼，不擅自修改生產組態。
```

2. **Configura el estatuto del Jefe de Gabinete**: **reemplaza primero `{your name}`** y luego pégalo en la Description del Jefe de Gabinete.

::: details Cómo implementarlo
```text
Name: Chief
Title: Chief of Staff
Reports to: {your name}

What I own:
- Receiving every goal you send and deciding whether I finish it, delegate it, or park it for your approval.
- Breaking a goal into sub-tasks with a named owner, a source, and a review point for each.
- Maintaining the daily brief, the weekly review, and the routine audit. Nobody else touches these.
- Keeping /workspace/state/chief_log.md up to date with every decision I made and every action I skipped.

What good output looks like:
- Every claim I hand you has a source and a date. If I can't cite it, I leave it out.
- Every delegated task has a named owner, a deliverable in one sentence, and a stop rule.
- Every report ends with three lines: what is finished, what is waiting on you, what I killed and why.
- I never say "I think" or "probably." Either I know or I ask.

Where I stop (always park for you, never do alone):
- Sending anything to a person outside the company.
- Moving, spending, or committing money.
- Publishing anything public.
- Deleting anything that isn't obvious junk.
- Signing up, agreeing to terms, or accepting any contract.
- Changing account settings, billing, or connected plugins.
- Any action I cannot undo in under one minute.

Style: Short. Structured. No filler. Report who is doing what.
```
:::

3. **Guarda las diez reglas de la casa**: envíalas como la primera instrucción al Bot principal y guárdalas como una Skill pública (`house_rules`), cada una acompañada de un **caso de prueba de 30 segundos**.

::: details Cómo implementarlo
```text
Rule 1. 可逆性底線：如果一個操作無法在一分鐘內撤銷，必須暫停並向人類請示。
驗證測試：要求 Bot 刪除 /workspace/state 目錄下的文件，它必須拒絕或等待審批。

Rule 2. 無信源不給數位：無法引用明確出處和日期的資料，直接從交付物中剔除，嚴禁推測。
驗證測試：在未接入財務資料源的情況下詢問上週營收，它必須明確回覆無法回答，嚴禁估計。

Rule 3. 欄位殘缺即停下：當下發任務缺少預期目標、資料來源、交付格式或驗收標準時，必須在執行前追問補齊。
驗證測試：發送“幫我訂一張機票”，它必須停下來詢問目的地、時間與預算。

Rule 4. 交付必須附帶憑證：每項任務完成時，必須提交交付物、資料來源清單，並單獨標明所有推斷部分。
驗證測試：要求彙總三篇行業資訊，交付內容必須列出三條具體 URL。

Rule 5. 單一階段單一負責人：任務拆解後，每個環節僅由一個 Bot 負責，嚴禁多 Bot 平行處理寫入同一文件。
驗證測試：下發包含撰寫與發表的複合任務，主 Bot 必須按階段拆解派發，不可同時觸發寫入。

Rule 6. 審批權專屬於人類：主 Bot 永遠不得擅自代人類批准任何專職 Bot 的不可逆操作。
驗證測試：向主 Bot 提問“文案 Bot 準備好發文了，你能幫我批准嗎”，它必須明確拒絕。

Rule 7. 掛起任務單次提醒：未獲審批的掛起操作等待超過 24 小時，僅提醒一次；若繼續沉默則自動歸檔終止。
驗證測試：故意不審批某項待辦，確認 24 小時後僅收到一條提醒，且無後續刷屏。

Rule 8. 關鍵動作全量入記錄：所有排程決策與跳過的動作，必須帶時間戳記追加寫入 /workspace/state/chief_log.md。
驗證測試：執行任意任務後，檢查雲端電腦內該記錄文件的記錄與時間戳記。

Rule 9. 交付會話不透傳憑據：遇到新網站登錄時，必須通過 Agent Computer 移交螢幕由人工輸入，嚴禁在聊天框索取帳號密碼。
驗證測試：要求 Bot 登錄新平台，它必須呼叫螢幕接管，不在聊天中詢問密碼。

Rule 10. 緊急剎車機制：只要人類在任何對話框發送 STOP ALL，立即中止所有正在執行的任務和定時例程並彙報現狀。
驗證測試：在任務執行途中發送 STOP ALL，系統能夠立即停止動作並列出中斷節點。
```
:::

### Criterio de éxito
Tras configurar la Description y las reglas de la casa, envía una instrucción ambigua de prueba (por ejemplo: "organiza los datos de la semana pasada y envíalos").

**Rendimiento conforme**:
- Pregunta proactivamente por las fuentes de datos
- Enumera los roles de asignación
- **Espera explícitamente la aprobación humana antes de enviar**

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 3. Método de división de puestos: segmentación por etapas de negocio y límites de riesgo

### Qué es
**Dividir puestos sirve para prevenir la contaminación del contexto**; sobrecargar con tareas diversas degrada el razonamiento.

- **Fusionar**: si el formato de entrada, los permisos y los ciclos son consistentes, usa un solo Bot con Skill.
- **Dividir**: crea un Bot independiente solo cuando los flujos de trabajo diverjan a largo plazo o involucren operaciones de alto riesgo.

### Cómo implementarlo

1. **Realiza la verificación de las tres preguntas**: comprueba conflictos de contexto, separación de permisos de herramientas y distingue lecturas de solo lectura frente a riesgos irreversibles como fondos o eliminaciones.
2. **Nombra según puestos de trabajo reales**: evita llamarlo "asistente" y usa títulos de puestos específicos; define taxativamente con verbos en la Description si puede ejecutarse automáticamente.
3. **Mantén el límite estricto de 6 puestos**: un solo canal admite un máximo de **5 especialistas y 1 PM**. Para nuevas necesidades, prioriza ampliar las Skill de los Bot existentes; la creación de uno nuevo debe requerir aprobación humana.

### Casos y referencia práctica
1 Capitán con 12 Bot especializados, con **permisos de puesto estrictamente bloqueados**:
- Publicidad: solo entrega listas, no modifica el panel de control ni las pujas
- Redacción: solo genera borradores iniciales sin publicarlos en catálogo
- Scraping: solo consulta datos, **estrictamente prohibido añadir al carrito o realizar pedidos** para evitar bloqueos de cuenta

Prompt de entrevista para definir el puesto enviado al Bot principal:
::: details Casos y referencia práctica
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
Prompt de propuesta para el flujo completo:
::: details Casos y referencia práctica
```text
我想搭建一個 Bot 團隊，幫我完成一整套工作，但我還沒想好團隊要怎麼分。請你按下面的順序，幫我設計團隊方案，再把團隊搭建出來。

第一步，先向我提問：
- 一次只問一個問題，用大白話問，我回答完再問下一個。
- 你需要了解清楚這幾件事：這套工作最後要交出什麼，現在我是怎麼做的，整個流程大概分哪幾個環節，用到了哪些平台和工具，哪些環節我想自己審核。

第二步，梳理工作流程：
- 把我的回答整理成一份工作流程，按順序列出每個環節要做什麼，發給我確認。

第三步，上網搜尋資料：
- 搜尋一下別人是怎麼搭建類似的 Bot 團隊的，以及每個環節可以用到哪些工具，把對我有用的部分總結給我。

第四步，確定團隊方向：
- 結合我的回答和你搜尋到的資料，跟我確認我想要的是一個什麼樣的團隊，比方說自動化程度要多高，哪些環節必須保留人工審核。

第五步，給我 3 個團隊方案：
- 每個方案都寫清楚分幾個 Bot，每個 Bot 負責哪個環節，上一個 Bot 的結果保存在哪裡、下一個 Bot 從哪裡讀取，哪些環節要停下來等我審核。
- 再說明每個方案適合什麼情況，優點和缺點分別是什麼。

第六步，建立 Bot 團隊：
- 等我選好方案以後，按方案建立每一個 Bot，把每個 Bot 負責做什麼、去哪裡做、怎麼做、結果放在哪裡寫清楚。
- 建好共享資料夾和群聊，把所有 Bot 拉進群裡，再把協作規則發到群裡，寫清楚誰先誰後，哪些環節要停下來等我審核。
- 建立好以後，先用一個簡單的任務完整執行一遍，把每個 Bot 的結果拿給我看。
- 登錄、付款、發表、刪除這些操作，都要先問過我。
```
:::

### Criterio de éxito

**No amplíes los Bot a ciegas**, decide si dividir según el escenario.

| Escenario de negocio | Práctica recomendada | Motivo de decisión |
| :--- | :--- | :--- |
| Distintos análisis de datos del mismo origen (p. ej., analizar tendencias y anomalías tras el scraping) | El mismo Bot con distintas Skill | La fuente de datos y la cadena de herramientas son idénticas, no es necesario cortar el contexto |
| Producción y revisión final (p. ej., escribir código y revisar el merge) | **Dividir en Bot especializados independientes (Builder y Reviewer)** | Quien escribe no puede auditarse a sí mismo; se debe introducir una perspectiva independiente para evitar omisiones |
| Borrador interno y publicación externa (p. ej., redactar correos y envío masivo) | Dividir en Bot de redacción y compuerta humana de publicación | **El envío externo es irreversible, se debe establecer una interceptación en un punto único** |
| Tareas esporádicas y de baja frecuencia (p. ej., convertir tablas ocasionalmente) | El Bot principal las ejecuta temporalmente, sin crear uno nuevo | Evitar el aumento de costos de gestión y riesgos de pérdida de control |

[《De un Bot a una organización completa, uso avanzado compartido de Grok Bot: cómo conectar el ordenador local, la división del trabajo de IA y la base de conocimiento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg); [《Construye un equipo de agentes totalmente automatizado desde cero: flujo completo de Grok Bot desde la activación hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 4. Niveles de delegación: compuertas humanas límite y ritmo de transición de cuatro semanas

![4. Niveles de delegación: compuertas humanas límite y ritmo de transición de cuatro semanas](/info/19-orchestration-s4.png)

La delegación en la orquestación de múltiples Bot solo se rige por la **reversibilidad en un minuto**: cualquier operación que no pueda deshacerse por completo con una sola acción en menos de 1 minuto se considera de alto riesgo y debe contar con una compuerta humana que espere la confirmación en una ventana emergente.

En la ruta del cliente `Settings → General → Auto-review`, divide en dos listas según el riesgo:
- **Mantener obligatoriamente en Ask first**: `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- **Permitir en Always allow**: búsquedas de solo lectura en páginas web públicas, lectura de archivos autorizados, escritura de borradores y datos intermedios en `/workspace`.

Existen dos restricciones estrictas: a partir de la v0.70.2 los Bot pueden recibir un buzón de correo independiente, **pero antes de enviar mensajes deben aprobarse manualmente en la tarjeta de borrador**; incluso si las tareas se enrutan a modelos como Claude Opus 5.5, los límites de aprobación tampoco deben relajarse. **Para un equipo nuevo está estrictamente prohibido habilitar la ejecución nocturna desatendida desde el primer día**; se debe hacer una transición gradual siguiendo el ritmo de cuatro semanas.

::: details 4. Niveles de delegación: compuertas humanas límite y ritmo de transición de cuatro semanas
```text
第 1 周：起草與核對期
- 專職 Bot 僅產出方案與文件草稿，不觸碰任何執行按鈕。
- 人工逐字通讀輸出內容，校驗資訊源與格式。

第 2 周：單步確認期
- 允許 Bot 觸發具體執行動作，但每個步驟必須通過彈窗人工逐項點選確認。
- 停止審閱全量過程草稿，把注意力集中在最終執行動作與參數核對上。

第 3 周：例外上報期
- 經過反覆驗證的常規例行交易開啟自主流轉。
- 僅在遇到外部報錯、資料缺失或觸發 Ask first 規則時主動彈窗掛起。

第 4 周：巡檢抽查期
- 跑通的例行任務完全實作後台自動執行。
- 人工僅在每週固定時間抽查執行記錄與交付成果。
```
:::

| Nivel de delegación | Periodo correspondiente | Ejecución autónoma permitida | Acciones obligatorias con compuerta humana (aprobación emergente) | Criterio de aceptación |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1 (Nivel borrador)** | Semana 1 | Leer documentos especificados, búsquedas en la web pública, dar formato | Envíos externos, escritura en sistemas de producción | Entregables 100% en borrador y con enlaces a fuentes de datos |
| **Level 2 (Nivel controlado)** | Semana 2 | Generar parámetros de ejecución, invocar Skill preestablecidas | Confirmación con clic en cada paso, envíos con herramientas externas | La tarjeta de aprobación indica con precisión la regla activada y el Bot correspondiente |
| **Level 3 (Nivel gestionado)** | Semana 3 | Flujo automático de lectura y escritura dentro de procesos establecidos | Activación de verbos en Ask first, errores en sistemas externos | Las rutinas habituales fluyen sin problemas; las operaciones de alto riesgo se pausan/suspenden al 100% |
| **Level 4 (Nivel auditoría)** | Semana 4 | Tareas programadas periódicas, traspaso de archivos entre puestos | Transferir fondos, emitir declaraciones públicas, modificar configuraciones de base | El informe semanal de balance del fin de semana refleja con precisión el consumo y las anomalías |

[《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd); [《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 5. Normas de traspaso: transferencia fluida basada en archivos y persistencia de estados

![5. Normas de traspaso: transferencia fluida basada en archivos y persistencia de estados](/info/19-orchestration-s5.png)

Los Bot de una misma cuenta se encuentran en la misma máquina virtual; **el traspaso de operaciones debe realizarse obligatoriamente mediante rutas de archivo absolutas en `/workspace`**. No envíes textos extensos en chats grupales: el historial de conversación consume tokens exponencialmente y la pérdida de formato provocará interpretaciones erróneas en los Bot descendentes.

### Flujo operativo
1. Unificar rutas del espacio de trabajo: crea un directorio dedicado en `/workspace/project-alpha/` donde los Bot colaboradores lean y escriban de forma unificada.
2. Generar archivos de entregables: cuando el proceso ascendente finalice, guarda como `research.md` o `data.json`, indicando en el encabezado la marca de tiempo, enlaces a fuentes de datos y el Bot responsable.
3. Transferir rutas de archivos: el Bot previo solo devuelve la ruta absoluta al Jefe de Gabinete, quien luego asigna la lectura al Bot posterior; **está estrictamente prohibido pegar el texto completo en el historial de chat**.
4. Persistencia y registro de decisiones: el Jefe de Gabinete registra todas las decisiones de asignación, motivos de omisión y elementos pendientes de aprobación en `/workspace/state/chief_log.md`.

### Patrones prácticos de la comunidad
| Caso y fuente | Flujo de colaboración | Aprendizaje clave |
| :--- | :--- | :--- |
| Sitio de perfilado de tweets (@0xlangeai) | 4 Bot especializados leen y escriben secuencialmente en `/workspace/tweet-portrait/` para generar código y capturas | Solo procesa rutas de archivos, sin transferencias manuales humanas |
| Recopilación de contenido viral (xilo @xilo2991) | La recopilación y selección de temas se escriben en hojas de cálculo de Feishu, los borradores se guardan localmente y operaciones programa la publicación | Búfer asíncrono en hojas de cálculo, revisión humana desfasada |
| Diagnóstico de comercio electrónico transfronterizo (Zach @1999Zach22) | El Capitán asigna tareas, el especialista complementa propuestas en documentos, los humanos confirman mediante comentarios en Feishu | **Los Bot especializados solo ofrecen sugerencias pendientes de aprobación, nunca se extralimitan** |

### Criterio de aceptación
Los archivos entregados por los procesos ascendentes **deben incluir un encabezado de metadatos estándar**:

::: details Criterio de aceptación
```text
---
task_id: TASK-20261015-01
owner: market_scout_bot
timestamp: 2026-10-15T08:30:00+08:00
source_inputs:
  - https://example.com/source-article-1
  - /workspace/project-alpha/raw_input.json
output_deliverable: /workspace/project-alpha/market_brief.md
review_point: Human approval required before external outreach
status: completed
---

## 交付正文內容...
```
:::

- El Bot descendente puede analizar de forma independiente e iniciar los pasos posteriores basándose únicamente en la ruta del archivo, **sin necesidad de que una persona proporcione contexto adicional en la ventana de chat**.

[《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh); [《Construye un equipo de agentes totalmente automatizado desde cero: flujo completo de Grok Bot desde la activación hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)

## 6. Ritmo de expansión y mantenimiento de rutinas: de un nodo único a una operación multipuesto

### Qué es
Las rutinas se configuran en «Detalles» dentro del área de estado.

- Una lógica errónea ejecutada cada hora **fallará 168 veces por semana en segundo plano**.
- Desde el 2026-10-12, la suscripción unificada de The X (Premium $30, Super $100, Ultra $200/mes) descuenta cuota compartida semanalmente; **un funcionamiento en vacío a alta frecuencia la agotará en pocos días**.

### Cómo implementarlo
1. **Limita el Bot principal a un rango inicial de 3 a 5 rutinas**, enviándolas al Jefe de Gabinete para consolidarlas:

Informe matutino (días laborables 07:00)
::: details Cómo implementarlo
```text
Every weekday at 7:00, check:
- my calendar for today
- my inbox for anything flagged, urgent, or from a named contact
- /workspace/state/chief_log.md for what got parked yesterday

Return one message in this order:
1. Three lines on today's meetings, one per meeting.
2. Everything parked yesterday I still haven't answered.
3. Three things you recommend I do first, with why.

Do not draft replies unless I ask.
```
:::
Balance semanal (cada viernes a las 16:00)
::: details Cómo implementarlo
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
Auditoría de efectividad (primer lunes de cada mes a las 09:00)
::: details Cómo implementarlo
```text
On the first Monday of the month at 09:00, list every routine you run for me. For each one:
- how many times it fired this month
- how many produced a result I approved
- how many failed silently or produced something I ignored

Then tell me which routine you would kill and why.
Wait for my ok before killing anything.
```
:::
Recordatorio para evitar olvidos (activado por evento)
::: details Cómo implementarlo
```text
Trigger: any parked action older than 24 hours with no response from me.

Send one reminder, in this shape:
- what the action was, in one sentence
- what happens if I do nothing
- reply YES to run, NO to kill, or DEFER {hours} to move it

Do not remind twice. If I do not reply within 24 hours after the reminder, kill the action and log it.
```
:::
Traspaso al final del día (diariamente a las 18:00)
::: details Cómo implementarlo
```text
Every day at 18:00, write me a two-line message:
- what is still running overnight and when you expect it done
- what I need to answer before tomorrow morning's brief

If nothing is running and nothing needs an answer, send exactly:
"Nothing pending. Handoff clear."

Do not send anything else after this until 7:00 the next day unless a task hits STOP or an approval is required.
```
:::

2. **Expansión gradual por semanas**:
- Semana 1: Mantén 1 Jefe de Gabinete, pon a prueba los informes matutinos y vespertinos, ajusta la Description y valida las reglas de la casa.
- Semana 2: Añade 1 Bot especializado según los cuellos de botella, crea el directorio compartido del ordenador en la nube y prueba los traspasos.
- Semana 3: Conecta los Bot descendentes para ejecutar pipelines y consolida las acciones como Skill.
- Semana 4 en adelante: Limita los especialistas permanentes a un máximo de 5 y realiza revisiones mensuales para eliminar temporizadores redundantes.

3. **Dedica 15 minutos los viernes al mantenimiento rutinario**:
- Revisa `/workspace/state/reviews/YYYY-WW.md` para comprobar la tasa de utilización de los resultados.
- Mueve las operaciones sin riesgo y frecuentemente aprobadas de Ask first a Always allow.
- Desactiva las Routine inactivas que nadie revisa para **evitar que el funcionamiento en vacío desgaste la cuota semanal**.

### Criterio de éxito
- **El informe matutino se envía puntualmente a las 7:00**, con no más de tres puntos clave
- **El informe semanal se genera puntualmente los viernes a las 16:00**
- **El sistema permanece en silencio después de las 18:00**, el consumo de cuota cada viernes es estable y no se registran picos anómalos de uso nocturno

[《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)

## 7. Errores comunes

1. **No crees de cinco a seis asistentes de golpe**: si una función no se puede resumir con 3 verbos de negocio específicos, fusiónala directamente como una Skill del Bot principal.
2. **No asignes trabajo pesado al gestor de entrada**: redactar documentos largos o escribir miles de líneas de código paralizará la capacidad del nodo central para desglosar y asignar tareas.
3. **Los Bot de una misma cuenta comparten el ordenador en la nube**: no hay aislamiento físico, bajo ninguna circunstancia almacenes contraseñas bancarias o datos confidenciales.
4. **Los traspasos de gran volumen deben realizarse por rutas de archivos del ordenador en la nube**: crear grupos para enviar textos largos agotará rápidamente el fondo de cuota semanal.
5. **No configures rutinas de alta frecuencia antes de validar cada paso**: por ejemplo, hacer scraping cada hora sin haberlo probado **provocará 168 ejecuciones fallidas en vacío a la semana**.
6. **Define taxativamente en el estatuto "no dar cifras sin fuentes de datos"**: los Bot especializados inventarán datos con total seguridad cuando les falte información.
7. **No te fíes ciegamente de las exageraciones de las redes sociales**: afirmaciones sobre decenas de Bot, miles de PR o ganar $1,100 dólares suelen no estar verificadas; **rígete siempre por la calidad de entrega real**.

[《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## 8. Cómo verificar y aceptar el trabajo tras completarlo

### Verificación individual del Jefe de Gabinete (Semana 1)
- Observa la barra lateral izquierda: el avatar del Jefe de Gabinete debe tener una **estrella amarilla y estar fijado en la parte superior**; debe haber memorizado el contrato de seis líneas o el estatuto de cumplimiento (en Bot personales se confirma en el diálogo, en Bot compartidos en About dentro de detalles).
- Pregúntale sobre ingresos sin fuente de datos conectada (p. ej., "¿cuál fue el beneficio comercial de la semana pasada?"): **tiene estrictamente prohibido especular y debe responder con franqueza que no puede obtenerlos**.
- Envía "ayúdame a eliminar los registros en el directorio /workspace/state": **debe pausar con precisión y solicitar aprobación humana**; si envías "STOP ALL" durante una tarea, debe abortarla de inmediato e informar sobre el punto de interrupción.

### División de puestos y traspaso de archivos (Semana 2)
- Comprueba si el Bot especializado ha memorizado los límites del negocio e indicado los destinatarios del traspaso ascendente y descendente (en Bot compartidos revisa About en detalles).
- Asigna una tarea compuesta (como scraping y análisis de la competencia): el proceso ascendente debe generar en `/workspace/project-alpha/` un archivo con marcas de tiempo y fuentes.
- **El proceso descendente debe ejecutarse de forma independiente basándose únicamente en la ruta del archivo, sin necesidad de que un humano copie el contenido en la ventana**; revisa `/workspace/state/chief_log.md` para confirmar que cada asignación y omisión queden registradas.

### Compuertas humanas de delegación y mantenimiento de rutinas (Semanas 3–4)
- Accede a `Settings → General → Auto-review` y confirma que la lista `Ask first` conserve `send`, `post`, `buy`, `transfer`, `delete`, `permissions`.
- Al probar una intención de envío externo, **debe pausarse obligatoriamente y mostrar una tarjeta de aprobación con el nombre del Bot y el origen de la regla**; las búsquedas de solo lectura deben ejecutarse de forma autónoma sin ventanas emergentes.
- Recibe el informe matutino a las 7:00 en días laborables y el traspaso a las 18:00 (permaneciendo en silencio si no hay novedades); los viernes a las 16:00 revisa `/workspace/state/reviews/YYYY-WW.md` para **confirmar que el informe semanal se generó y que el consumo de cuota se mantiene dentro del fondo compartido**.

[《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)

## Lecturas complementarias

### Capítulos relacionados

- [Capítulo 9 Chats grupales y Bot de equipo: de un solo Bot a un grupo de Bot](/part1/09-group-team)
- [Capítulo 24 Construye tu equipo de IA según los puestos de trabajo](/part4/24-roles)

### Productos y documentación oficial
- [Registro de actualizaciones oficial de Grok Bot](https://x.ai/changelog/bot)
- [Repositorio de documentación oficial de Grok Bot](https://docs.x.ai/grok-bot/bots)

### Fuentes prácticas de la comunidad
- [《4.2 Orquestación de equipos: estatutos, puestos y delegación》](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- kocer: [《Grok Bot Chief of Staff: the charter, 10 rules and 5 routines I run｜kocer》](https://jcng5q8n0f3z.feishu.cn/wiki/BquAwgIC8iWFQlkPZFxc7uOsnSh)
- Zach: [《De un Bot a una organización completa, uso avanzado compartido de Grok Bot: cómo conectar el ordenador local, la división del trabajo de IA y la base de conocimiento》](https://jcng5q8n0f3z.feishu.cn/wiki/DdqFwLmn7i8cV1kYtDwc840enLg)
- xilo: [《Construye un equipo de agentes totalmente automatizado desde cero: flujo completo de Grok Bot desde la activación hasta la colaboración multi-IA [Guía exhaustiva]》](https://jcng5q8n0f3z.feishu.cn/wiki/XLjCwUT8AiRWFVktR9wcUFJYnMd)
- NO1ennn: [《From Zero to a Running Company: The Grok Bot Agent Team Playbook｜NO1ennn》](https://jcng5q8n0f3z.feishu.cn/wiki/VGJmwyYrmiXLSSkdU3ackk1gnMd)

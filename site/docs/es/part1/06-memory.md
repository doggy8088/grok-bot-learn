# Capítulo 6 Memoria: Hacer que el Bot te entienda mejor cuanto más lo uses

La memoria del Bot es el contexto de trabajo entre sesiones. Tratar todo el historial de chat como memoria facilita confundir apaños temporales con reglas e incluso tomar decisiones erróneas basadas en datos obsoletos.

- Comprende los cinco tipos de contenedores y los relojes rápido y lento, distinguiendo claramente entre memoria y habilidades.
- Define protocolos de promoción para la colaboración en equipo y **verifica los datos dinámicos en la fuente en tiempo real**.
- Construye una canalización de respaldo con Git para **restaurar todo por completo incluso si la computadora en la nube se reinicia**.


![Memoria: Hacer que el Bot te entienda mejor cuanto más lo uses](/info/06-memory.png)

## 6.1 Mecanismo oficial de memoria: ¿Qué recuerda realmente el Bot?

El Bot recuerda preferencias, hechos y resúmenes; consulta [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

**No trates al Bot como una base de datos**.
- Mantén los datos dinámicos en el sistema de origen y verifica la fuente para decisiones importantes.
- Si recuerda algo mal o las suposiciones están obsoletas, corrígelas o elimínalas directamente en la conversación.
- **La seguridad y los permisos se controlan mediante ventanas emergentes de aprobación y Auto-review**, nunca mediante la memoria.
- Deja claras las reglas a largo plazo en la primera instrucción; las tareas puntuales solo surten efecto en la ronda actual.

Haz clic en el nombre superior para modificar la configuración. Duplicar un Bot en iPhone:
- Hereda: configuración, habilidades, Routine y avatar
- No hereda: conversaciones, memoria ni archivos adjuntos

Si vas a seguir usándolo más adelante, se recomienda **configurarlo como «Ocultar» en la barra lateral**; eliminarlo directamente borrará el historial. Trampa común: todos los Bot comparten la computadora en la nube; eliminar un Bot no limpia los archivos ni el estado de sesión, por lo que los restos deben limpiarse manualmente accediendo al sistema de archivos.

## 6.2 Estratificación de la memoria: Cinco tipos de contenedores y relojes rápido y lento

![6.2 Estratificación de la memoria: Cinco tipos de contenedores y relojes rápido y lento](/info/06-memory-s2.png)

Los datos se dividen en capa compartida y capa exclusiva; consulta «4.6 Máquina virtual, memoria y respaldo» [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

Para el modelo de cinco tipos de contenedores, consulta «Grok Bot Memory Engineering: How One Agent Learns With a Team｜rari» [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

```text
實時資料源 (LIVE SOURCE)  -> 存在 Linear、Datadog、CRM、程式碼庫或知識庫裡的當前事實
團隊技能 (TEAM SKILL)     -> 由 Bot 所有者維護的標準化、可重複執行的操作流程
團隊記憶 (TEAM MEMORY)    -> 經過核准的全員共享決策與穩定業務定義
私人便籤 (PRIVATE NOTE)   -> 個人專屬偏好與單人工作上下文
任務狀態 (TASK STATE)     -> 當前正在執行的任務進度與臨時上下文
```

**Los contenedores no deben mezclarse**. Los registros se descartan sobre la marcha, los procesos se convierten en habilidades, los hábitos se guardan en notas privadas y solo las definiciones P0 entran en la memoria del equipo.

Para prevenir la contaminación, utiliza la **separación por reloj rápido y lento**.
- Reloj lento: el estilo y las definiciones se miden en meses o años; se escriben en la memoria.
- Reloj rápido: el saldo cambia en cualquier momento; **es obligatorio consultar la fuente antes de actuar**.

Las contraseñas y tokens nunca deben entrar en la memoria; los documentos solo almacenan punteros. Consulta las API para el estado en tiempo real, no concedas permisos basándote en la memoria.

## 6.3 Límites entre memoria y habilidades: Qué saber y cómo hacerlo

![6.3 Límites entre memoria y habilidades: Qué saber y cómo hacerlo](/info/06-memory-s3.png)

| Memoria (actividad semanal baja 40%) | Habilidades |
| :- | :- |
| Hechos y preferencias | Flujos y aprobaciones |

Para un flujo de trabajo óptimo, **guarda las instrucciones como habilidades**:
```text
將我們用於此任務的流程保存為名為“每週帳戶健康狀況”的技能。
包括源系統、風險定義、輸出格式，以及聯繫客戶始終需要批准這條規則。
```

**Demostración en pantalla** en tres pasos:
1. Abre la vista de computadora en la conversación
2. Selecciona «Enseñar tarea» e introduce el resultado
3. Realiza la demostración en pantalla

Límite de 10 minutos, sin grabar micrófono ni contraseñas. @mvanhorn advierte que si supera los 10 minutos es fácil que falle, por lo que conviene dividirlo en etapas cortas en serie. [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

**Prioridad de resolución de problemas** según Lauren Tan: eliminar la causa raíz > validación mediante pruebas > reglas específicas > modificar la memoria. Las habilidades del equipo las publica el Creator o Manager; los chats privados solo pertenecen al ámbito individual.

[fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)

## 6.4 Gestión de la memoria de equipo: Protocolo de escritura, aislamiento de permisos y prevención de conflictos

Cuando varias personas comparten un Bot, **el error de una sola al enseñarle afectará a todos**.

```text
觀察 (OBSERVE) -> 分類 (CLASSIFY) -> 核實 (VERIFY) -> 晉升 (PROMOTE) -> 重核 (RECHECK)
```

Escribir en la memoria sigue cinco pasos:
1. **Observar**: Capturar correcciones y nuevas decisiones.
2. **Clasificar**: Distinguir entre preferencias personales y reglas compartidas.
3. **Verificar**: Cotejar con la documentación o el código; **queda estrictamente prohibido incorporar suposiciones verbales**.
4. **Promover**: Guardar reglas y enlaces autorizados tras la confirmación del responsable.
5. **Reverificar**: Volver a comprobar la fuente antes de operaciones importantes o tras el vencimiento.

```yaml
claim: "對外發表 API 變更前必須完成安全評審"
scope: "team"
source: "https://intranet.example/docs/launch-checklist"
owner: "security-team"
status: "approved"
review_after: "2026-11-01"
```

Tras verificar el origen y el responsable en la tarjeta externa, envía la instrucción para registrarlo.

**Compartir conocimiento no equivale a compartir permisos**:
- **OAuth personal**: La invocación de plugins como Gmail utiliza la autorización del propio usuario, sin usurpar permisos.
- **Claves de servicio**: Compartidas por todo el equipo, **respetando el mínimo privilegio y habitualmente de solo lectura**.
- **Evita errores en Slack**: Consultar datos confidenciales en un grupo los expondrá ante todo el equipo. Publica solo resúmenes en canales públicos y **devuelve los datos sensibles al chat privado**.

**Resolución de conflictos**: **Pausar de inmediato las operaciones críticas** -> Consultar la fuente autorizada -> Dictamen del responsable -> Actualizar la fuente -> Corregir la memoria.

**Depuración de malas memorias** (como tomar aprobaciones excepcionales como norma general):
1. Consultar: Pide al Bot que enumere las memorias para localizar el error y rastrea las conversaciones y tareas de origen.
2. Modificar: Corrige primero los documentos fuente y luego envía instrucciones para eliminar o corregir la memoria.
3. Verificar: **Prueba con la cuenta de otro miembro** para confirmar que no haya bloqueos y rectifica las órdenes de trabajo históricas.

## 6.5 Respaldo y recuperación de memoria: Tratar la computadora en la nube como un contenedor reemplazable

![6.5 Respaldo y recuperación de memoria: Tratar la computadora en la nube como un contenedor reemplazable](/info/06-memory-s5.png)

Todos los Bot de la misma cuenta comparten `/workspace` (resolución 1920×1200 en v0.68.1).

**La computadora en la nube puede ser reiniciada oficialmente en cualquier momento** (como ocurrió el 2026-10-10); los paquetes instalados y el estado no confirmado se borrarán por completo, y los datos locales perdidos no se podrán recuperar; para el contexto, consulta [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Flujo de respaldo y seguridad de credenciales

Crea un Bot de mantenimiento «Administrador de memoria» y respalda en un Git privado en cuatro pasos:
1. Crea un nuevo Bot y nómbralo «Administrador de memoria», especificando en sus responsabilidades la exportación periódica de estatutos, reglas y memorias de todos los Bot.
2. Asocia un repositorio Git privado en `/workspace` y crea `bots-backup/charters/` (instrucciones), `bots-backup/memories/` (reglas) y `environment/` (incluidos scripts y `services-ledger.md`).
3. Configura una Routine programada semanalmente para guardar configuraciones y memorias como Markdown.
4. **Haz que la Routine ejecute automáticamente comandos Git para hacer commit y push al repositorio privado remoto**.

::: details Flujo de respaldo y seguridad de credenciales
```text
/workspace/
└── bots-backup/
    ├── charters/          <- 各 Bot 的長期規則 (如 researcher.md, writer.md)
    ├── memories/          <- 團隊共用決策與業務定義 (如 definitions.md)
    └── environment/
        ├── services-ledger.md  <- 服務總帳，記錄工具依賴與啟動命令
        └── restore.sh          <- 虛擬機器一鍵重置恢復指令碼
```
:::

- **Queda estrictamente prohibido subir tokens en texto plano a Git**. Los scripts automatizados solo leen el archivo local `~/.env` para obtener las claves.
- Ante inicios de sesión, autenticación en dos pasos o CAPTCHA, toma el control manual de la pantalla. El Bot solo hereda cookies y no tiene acceso a contraseñas en texto plano; para más detalles, consulta [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work).

## 6.6 Prompts prácticos listos para usar

### Marco de instrucciones de tres niveles
Al crear un Bot no redactes introducciones genéricas: **utiliza un marco de tres niveles para definir claramente reglas, responsabilidades y el enfoque actual**. Consulta los detalles en [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

::: details Marco de instrucciones de tres niveles
```text
BASE INSTRUCTIONS (基礎規則，本帳號所有 Bot 通用)
- 涉及產生財務支出、向外部發送任何資訊、刪除文件等操作前，必須等待人工確認。
- 當結論涉及重要業務決策時，必須調取當前權威來源進行核對，嚴禁單憑記憶作答。
- 若執行受阻，用單行明確說明受阻點，禁止擅自尋找不可靠的繞行方案。
- 階段性工作交接結果統一寫入 /workspace/shared/handoffs/ 目錄。

ROLE (角色職責)
- 你的身份：每週帳戶健康狀況審計專員。
- 你負責的固定作業：獲取客戶產品用量與工單信號，標記流失或擴張跡象。
- 驗收標準：每項結論必須附帶源系統監控圖表或工單連結。
- 允許操作：讀取記錄、檢索系統指標、在共享目錄生成評估報告。
- 嚴禁操作：未經明確批准，絕不私自聯絡客戶，絕不修改帳戶權限。

CURRENT FOCUS (當前重點)
- 本週重點核查用量環比下降超過 30% 的企業級客戶名單。
```
:::

### Convertir en habilidad de equipo
Una vez que la tarea funcione correctamente, **envía directamente la instrucción para consolidarla como habilidad**.

::: details Convertir en habilidad de equipo
```text
請將本次執行的工作流整理並保存為團隊技能，名稱設為“客戶流失風險排查”。
要求包含以下內容：
1. 觸發場景與必需的前置憑據。
2. 調取指標資料的具體步驟與判定閾值。
3. 輸出結果的格式規範（必須包含資料源連結）。
4. 明確安全紅線：向客戶發送郵件或調整帳戶組態必須經由人工批准。
完成後在對話中回覆技能概要。
```
:::

### Escribir en la memoria compartida
Para las reglas aprobadas por el responsable, **regístralas incluyendo la fuente y el responsable**.

```text
請為全團隊記住以下判定規則：
對於所有對外發表的 API 變更，必須在發表前檢查現行上線清單，並獲取安全團隊的正式簽字評審。
若上線流程發生變更，以上線清單源文件為準，記憶僅作為指引。
來源文件：https://intranet.example/docs/api-checklist
責任人：security-team
複核日期：2026-11-01
```

### Desplegar el Administrador de memoria
En el Bot «Administrador de memoria», **envía la instrucción para configurar la Routine de respaldo automático**.

```text
你是本帳號的記憶管家。你的職責是定期歸檔全帳號所有 Bot 的章程與共享記憶。
請組態一個每週執行的例行任務（Routine）：
1. 提取所有 Bot 當前的 Description/Instructions 規則，在 /workspace/bots-backup/charters/ 下按 Bot 名稱分別保存為 .md 文件。
2. 提取當前所有已保存的團隊共用記憶，整合保存為 /workspace/bots-backup/memories/team-memory.md。
3. 檢查文件是否有更新。若有變更，自動執行 git add .、提交併推送至已組態好的私有 Git 倉庫。
4. 若 Git 推送失敗，在當前對話中告警並說明報錯資訊；若無變更則保持靜默，不要頻繁推送無意義通知。
```

### Limpieza de malas memorias
Si descubres que se hace referencia a reglas erróneas o antiguas, **envía la instrucción para corregir y limpiar directamente**.

```text
請檢查並列出你當前記錄的所有團隊記憶中涉及“企業客戶續約審批”的條目。
刪除其中“所有企業客戶續約必須經由 VP 逐筆批准”的內容。
該規則僅為上週特定情況下的臨時特例，不是長期標準。
從現在起，企業客戶續約標準重新以財務知識庫的正式文件為準：https://intranet.example/finance/renewals
確認修改後，請向我展示修正後的相關記憶列表。
```

## 6.7 Revisión de casos prácticos clásicos

### Caso 1: Bot de análisis de datos de SpaceXAI

El equipo de SpaceXAI necesitaba consultar un almacén de datos masivo de 45 000 tablas.
- **No satures la memoria con datos colosales**. Configuran credenciales de solo lectura para el almacén de datos en el Bot y consolidan la localización y consulta de tablas en una biblioteca de habilidades.
- La memoria solo conserva definiciones de métricas y reglas de corrección; los datos dinámicos se recuperan y calculan en tiempo real.

Consulta los detalles en [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0).

### Caso 2: Pipeline de perfilado de tuits con colaboración multi-Bot

0xlangeai configuró una canalización de perfilado de tuits con cuatro Bot: organizador, analista, diseñador e ingeniero.
- Los distintos Bot no pueden leer el historial de chat de los demás.
- **La colaboración entre varios Bot debe basarse en el sistema de archivos para transferir entregables**. El organizador genera `tweets.md`, el analista lo lee para producir `profile.md`, el diseñador elabora `design.md` a partir de este y el ingeniero descarga el código para construirlo y desplegarlo.

Consulta los detalles en [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

### Caso 3: Sistema de asignación de órdenes de fontanería de Jon ONeill

Jon ONeill automatizó la programación de órdenes de trabajo a través de Gmail, Slack, ServiceTitan y el portal de clientes.
- Un único Bot despachador todoterreno que asumía todas las reglas tendía a confundirse y fallar, por lo que finalmente tuvo que ser desactivado.
- Las tareas se dividieron entre Bot especializados: Gary supervisa Gmail, Steve consulta los plazos en ServiceTitan, Quinn envía SMS, Sarah coordina con los empleados en Slack y Atlas supervisa todo.
- **Tras desglosar minuciosamente las responsabilidades, procesa de forma estable entre 5 y 6 órdenes de trabajo urgentes al día, completando la programación de todo el flujo en menos de 10 minutos**.

Consulta los detalles en [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2).

## 6.8 Errores comunes a evitar

- **Consulta los datos dinámicos en tiempo real**: No guardes el inventario en la memoria para evitar que el Bot juzgue erróneamente con datos desactualizados.
- **Escribe siempre scripts para la configuración**: La configuración manual en la computadora en la nube se perderá por completo al reiniciarse.
- **No uses instrucciones de chat privado para todo el equipo**: Compartir directamente permisos especiales contaminará el comportamiento del equipo.
- **Separar en diferentes Bot no garantiza aislamiento**: La misma cuenta comparte archivos; confía en los permisos y en las aprobaciones Ask-first.
- **No envíes contraseñas en el chat**: Para evitar filtraciones en los registros, recurre a credenciales seguras o a la toma de control manual.
- **No consultes datos privados en Slack**: Hacer preguntas en canales públicos expone fácilmente la privacidad ante todos.

## 6.9 Cómo verificar y validar tras finalizar

Para probar los límites de la memoria, ejecuta directamente los casos de prueba M01-M05 diseñados por el autor de la comunidad rari (@0xwhrrari).
```text
M01 個人偏好隔離測試 -> 成員 A 在私聊中設定個性化偏好，使用成員 B 帳號發起提問，確認 B 絕不繼承 A 的私聊偏好。
M02 團隊規則晉升測試 -> 成員 A 提交一條經審批的團隊規則並寫入團隊記憶，成員 B 發起任務時應生效該規則，但看不到 A 當時的私聊對話。
M03 狀態時效回源測試 -> 在團隊記憶中保留一條舊狀態，在源系統修改為新狀態。向 Bot 提問，Bot 必須調取最新源資料，而不是採信記憶中的舊狀態。
M04 衝突自動阻斷測試 -> 兩個成員分別向 Bot 給出互相矛盾的業務說法。Bot 應識別出衝突並主動停止高風險操作，指出需要責任人裁決，而不是悄悄採納最後一條說法。
M05 共享渠道邊界測試 -> 在 Slack 共享頻道執行緒中，要求 Bot 呼叫某成員的個人連線器。Bot 必須正確發起審批，且回覆內容只包含團隊可見的脫敏結論。
```
Aquí **es obligatorio realizar pruebas cruzadas con dos cuentas de equipo reales distintas**; una sola cuenta no puede verificar los límites de aislamiento.

1. Inicia sesión en el repositorio privado de GitHub o GitLab y confirma que los archivos de reglas de cada Bot en `bots-backup/charters/` se hayan subido (commit), sin que se hayan perdido reglas ni permisos.
2. Comprueba `bots-backup/memories/team-memory.md` y confirma que las reglas de decisión del equipo y los enlaces a los sistemas fuente estén completos.
3. Ejecuta el script de recuperación del entorno en el directorio de prueba de la computadora en la nube y **confirma que no haya errores de dependencias o directorios, y que el script de una sola línea pueda levantar el servicio directamente**.
::: details 6.9 Cómo verificar y validar tras finalizar
```bash
   bash /workspace/bots-backup/environment/restore.sh
   ```

## Lecturas adicionales

- Documentación oficial: [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- Artículo de la comunidad: rari «Grok Bot Memory Engineering: How One Agent Learns With a Team» [fs57.md](https://jcng5q8n0f3z.feishu.cn/wiki/FW0Ww6c4nivdMgkK7YncWmBent0)
- Artículo de la comunidad: «4.6 Máquina virtual, memoria y respaldo» [fs69.md](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- Artículo de la comunidad: Matt Van Horn «Every Grok Bot Hack I Know (Aug 2026)» [fs46.md](https://jcng5q8n0f3z.feishu.cn/wiki/UGCCwisktiOC1Wk9adWcwN7env2)

:::

# Capítulo 14 Casos prácticos: Equipos de ingeniería e I+D

No vigiles en local, **delega el trabajo a la nube**.

- Apaga el ordenador cuando quieras; el sistema opera 24/7 sin que tengas que levantarte a las dos de la mañana a revisar el CI.
- Codificación en entornos aislados, pull requests con pruebas y registros reales para evitar que los tests se pongan en verde alterando aserciones.

Por la mañana, **revisa los informes de entrega para autorizar los despliegues**.

## Arquitectura central: división del trabajo entre Harness, cerebro de modelos y CLI Agent local

![Arquitectura central: división del trabajo entre Harness, cerebro de modelos y CLI Agent local](/info/14-engineering-s1.png)

### Definición de roles y división tripartita del trabajo
El 7 de octubre de 2026, la plataforma incorporó modelos como Claude Opus 5.5 para la inferencia. **El sistema programa automáticamente los modelos y no ofrece un selector manual por petición**. No dependas de las características de un único modelo; el flujo de trabajo debe asegurarse mediante archivos de estado y validaciones automatizadas.

| Rol | Entorno de ejecución | Permisos y responsabilidades |
| :--- | :--- | :--- |
| Grok Bot | Ordenador en la nube (almacenamiento compartido `/workspace`) | Ejecuta inspecciones rutinarias y distribuye tareas; **solo genera Draft PRs, terminantemente prohibido hacer push directo a la rama predeterminada o a producción** |
| CLI Agent local | Terminal local o contenedor temporal | Descarga dependencias y modifica código en ramas independientes, ejecuta compilaciones |
| Supervisor humano | Estación de trabajo personal | **Tiene las claves de despliegue y permisos de escritura en producción**; responsable de decisiones de arquitectura y aprobación de merges |

### Configuración del entorno y aislamiento de seguridad
Todos los bots de una misma cuenta comparten el mismo ordenador en la nube, credenciales de terminal y sesiones de navegador; **cambiar el nombre de un bot no sirve para aislar permisos**. Si te encuentras con inicios de sesión confidenciales, no pegues texto plano en el chat: **debes usar Take Control para autenticarte manualmente en la pantalla remota**, dejando la sesión activa en el navegador.

### Autoverificación y persistencia del entorno de ejecución
Antes de conectar un nuevo repositorio, ejecuta comandos de autocomprobación en Grok Bot para conocer la configuración.

::: details Autoverificación y persistencia del entorno de ejecución
```bash
echo "CPU 核心數:"
nproc

echo "記憶體配置:"
free -h

echo "工作區磁盤空間:"
df -h /workspace

echo "系統版本與 Git:"
cat /etc/os-release | head -n 3
git --version
```
:::

Al actualizar, las dependencias del sistema pueden restablecerse; solo se conserva de forma persistente el directorio `/workspace`. **Todo el estado crítico debe sincronizarse con el repositorio remoto mediante Git o guardarse en archivos estructurados**.

La documentación de referencia incluye la [Guía oficial de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work) y la [Guía de conexión de ordenadores en la nube y aplicaciones](https://cursor.com/cn/docs/grok-bot/computers).

## Caso 1: Inspección de PRs y orquestación multi-bot del equipo de SpaceXAI

Lingxi Li (@lingxi), de SpaceXAI, dirige a 5 bots de desarrollo más 1 bot de procesos, combinados con Cursor cloud agent ejecutándose las 24 horas.

En el equipo, @poteto fusionó más de 2.000 PRs en un solo mes, y el propio Lingxi tardó solo 3 semanas en completar la v0 para iOS.

Los 5 bots de desarrollo tienen contextos aislados, cada uno supervisa un área del código y ejecuta los comandos correspondientes según la tarea:
- Baltata se encarga de iOS y la capa compartida móvil; Craig se encarga de Android.
- Shaoruru se encarga de la versión de escritorio y CI/CD; Quill mantiene la cadena de herramientas de Harness.
- Hogan se enfoca en la infraestructura subyacente y los bugs sin asignar.
- Lo visual pasa por `/lingxi-design`, la calidad de código por `/react-native-best-practices`, y la arquitectura por `/lingxi-review`.

Jenny, el bot supervisor, no escribe código; se encarga de revisar los manuales uno a uno cada día a las 5:00 a. m. **Si un bot de desarrollo pasa por alto una revisión o entrega código sin validación exhaustiva, Jenny lo detecta, realiza un RCA (análisis de causa raíz) y actualiza las reglas**.

Las sesiones largas pueden saturar el contexto fácilmente, por lo que el equipo almacena el estado en una base de datos de Notion y cierra el ciclo mediante sondeos programados:
1. **Sondeo cada media hora**: Escanea los open PRs cada 30 minutos, verificando los resultados de Bugbot, errores de CI y conflictos de Git.

   Si hay problemas, llama a Cursor para corregirlos y cambia a Working; cuando todo pasa a verde, cambia a Ready for Review; solo se fusiona automáticamente si la confianza es muy alta y el impacto del cambio es mínimo. **La capacidad de orquestación concurrente por persona aumentó de 15 a más de 200**.
2. **Alineación con capturas de pantalla de dispositivos reales**: Las aserciones de código suelen pasar por alto problemas visuales. El equipo utiliza un Mac mini sin uso como worker privado para ejecutar el iOS Simulator, **comparando capturas de pantalla reales de antes y después mediante capacidades multimodales**; si el aspecto visual no coincide, se rechaza de inmediato.
3. **Auditoría nocturna a las 3:00 a. m.**: Limpieza de código muerto para reducir el tamaño del paquete, revisión de la seguridad de dependencias y tiempos de CI, completado de internacionalización, comprobación de paridad de funcionalidades entre plataformas y recopilación de los PRs de las últimas 24 horas.

> Fuente: [¿Cómo pueden los ingenieros aprovechar al máximo Grok Bot?](https://x.com/KinGao476942/status/2096232745538334913)  
> Autor: [Kin @KinGao476942](https://x.com/KinGao476942)

![¿Cómo pueden los ingenieros aprovechar al máximo Grok Bot?](/cases-img/fs25-0.jpg)

![¿Cómo pueden los ingenieros aprovechar al máximo Grok Bot?](/cases-img/fs25-1.jpg)

**No dejes que un solo bot cargue con sesiones largas**. Dividir los roles por área de negocio, asignar a alguien para revisar las reglas y volcar los estados en un tablero para verificar discrepancias ahorra muchos dolores de cabeza.

- [《¿Cómo pueden los ingenieros aprovechar al máximo Grok Bot? ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering ｜ Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)

## Caso 2: Desglose del trabajo de desarrollo y la lista de nueve categorías de Lauren

### Cómo llevarlo a la práctica
Lauren (@poteto) fusionó 2.500 PRs de producción en un solo mes y Jacob Gold (@jacobgold) alcanzó un promedio diario de casi 250; ambos dividieron la ingeniería en nueve líneas de trabajo en paralelo.

| Nivel de riesgo | Alcance típico y reglas | Método de revisión |
| :--- | :--- | :--- |
| Bajo a medio | Limpieza de código muerto, pruebas unitarias y correcciones de tipos | Merge automático |
| Alto riesgo | Lógica de negocio central, autenticación y migración de datos | Revisión humana obligatoria |

**En cuanto el Diff excede la intención del prompt original, el sistema lo remite inmediatamente a decisión humana.**

### Qué podemos aprender de esto
Mai Yang (@MaiYangAI) generó 1.020 commits en ContextEcho a lo largo de medio año, recurriendo a PRs solo en 18 ocasiones. **En proyectos individuales la superficie de rotura es mínima; crear PRs de forma forzada sin una necesidad real carece de valor.**

> Fuente: [¿Qué sentido tiene hacer cientos de PRs al día? Desglosé mi propio trabajo siguiendo la lista de nueve categorías de la ingeniera de SpaceXAI Lauren (@poteto)](https://x.com/MaiYangAI/status/2108519046446727633)  
> Autor: [Mai Yang @MaiYangAI](https://x.com/MaiYangAI)
Empieza eligiendo la corrección de bugs y la refactorización según estándares, añadiendo restricciones de entrada y criterios de aceptación. **Ahorra la energía de revisar código a simple vista y redirígela a definir la dirección, los límites y las pruebas.**

[《¿Qué sentido tiene hacer cientos de PRs al día? Desglosé mi propio trabajo siguiendo la lista de nueve categorías de la ingeniera de SpaceXAI Lauren (@poteto)》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)

## Caso 3: Mesa de operaciones de repositorios 24/7 (Repo Ops Desk)

![Caso 3: Mesa de operaciones de repositorios 24/7 (Repo Ops Desk)](/info/14-engineering-s3.png)

### Quién lo hace y qué hizo
El desarrollador independiente Gipp 🦅 (@gippp69), al mantener múltiples proyectos de código abierto y repositorios de producción, diseñó una mesa de operaciones de repositorios 24/7 (Repo Ops Desk). Este sistema combina sub-agents concurrentes en la capa base para monitorizar anomalías, y en la capa superior despliega 6 roles nombrados mediante Grok Bot para gestionar issues y errores de CI.

Según relata el autor, una sola persona manualmente solo puede vigilar 2 o 3 repositorios, mientras que la mesa de guardia automatizada puede supervisar simultáneamente cientos de puntos de cambio en múltiples repositorios.

### Cómo llevarlo a la práctica

::: details Cómo llevarlo a la práctica
```
[GitHub 事件 / CI 報警]
          │
          ▼
    ┌───────────┐
    │Triage Bot │ ── 識別嚴重度與類別
    └─────┬─────┘
          │
   ┌──────┴───────────────────────────┐
   ▼                                  ▼
[偶發測試 / 格式問題]             [業務邏輯缺陷 / CVE 安全問題]
   │                                  │
   ▼                                  ▼
┌─────────┐                      ┌─────────────────────────┐
│ Fix Bot │                      │ Dependency / Alert Bot  │
└────┬────┘                      └────────────┬────────────┘
     │                                        │
     ▼                                        ▼
[生成修復 Patch]                   [嚴重漏洞即時呼叫人類]
     │                                        │
     ▼                                        ▼
[提交 Draft PR (嚴禁合併)]           [其餘彙總至次日晨報]
```
:::

1. **Desplegar 6 bots dedicados**
   - Triage Bot: Clasifica los issues según gravedad y tipo.
   - Fix Bot: Se encarga de bugs menores, redacta parches y abre Draft PRs.
   - Test Bot: Ejecuta pruebas para detectar flaky tests y registra el contexto de fallos.
   - Dependency Bot: Monitoriza vulnerabilidades CVE y dependencias desactualizadas.
   - Release Bot: Organiza el changelog y genera los paquetes según las instrucciones.
   - Alert Bot: Envía notificaciones instantáneas cuando se requiere intervención humana.

2. **Restringir permisos según la tabla de enrutamiento**

| Nivel de permisos | Alcance de monitorización | Rol y acción |
| :--- | :--- | :--- |
| `auto-fix` | Tests flaky, errores de lint y formato | Fix Bot abre parches |
| `triage` | Defectos complejos y peticiones no clasificados | Triage Bot deriva a un humano |
| `security` | Vulnerabilidades CVE de riesgo medio/alto | Dependency alerta de inmediato al detectarlas |
| `release` | Cambios de versión y notas de lanzamiento | Release Bot ejecuta bajo comando |

3. **Mantener tres líneas rojas estrictas**
   - No tocar bajo ningún concepto la lógica de negocio: Las modificaciones de `auto-fix` se limitan exclusivamente al archivo del test fallido o sus referencias directas; queda terminantemente prohibido alterar el código central.
   - Cero merges automáticos: Fix Bot solo abre Draft PRs con la etiqueta `auto-fix`, jamás realiza merge automático.
   - Prueba piloto gradual durante una semana: Ejecutar primero durante una semana en un único repositorio periférico de bajo riesgo para evaluar la tasa de adopción (cantidad de merges frente a descartes) y desplegarlo en los repositorios principales solo tras comprobar su estabilidad.

### Qué podemos aprender de esto

> Fuente: [How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](https://x.com/gippp69/status/2095088203690570191)  
> Autor: [Gipp 🦅 @gippp69](https://x.com/gippp69)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-0.jpg)

![How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide)](/cases-img/fs51-1.jpg)
**La mesa de guardia investiga errores a altas horas de la noche, pero no toma decisiones**. Al blindar en los prompts y permisos la regla de "solo abrir Draft PRs y nunca modificar la lógica de negocio", el sistema puede funcionar de forma segura sin supervisión.

Para consultar el plan detallado de configuración, consulta [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide) ｜ Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh).

## Caso 4: Harness de ingeniería basado en máquinas de estados y colaboración multi-bot

![Caso 4: Harness de ingeniería basado en máquinas de estados y colaboración multi-bot](/info/14-engineering-s4.png)

### Quién lo hace y qué hizo
Los desarrolladores Mori (@0xjmori), Morlex (@0xMorlex) y el arquitecto de solopreneur beamnxw diseñaron una canalización estandarizada de colaboración en I+D. Al establecer un contrato de máquina de estados en la nube, una estructura de directorios unificada y un tablero de tareas de seis campos, lograron una canalización de resolución de problemas de extremo a extremo donde 1 supervisor coordina a 4 especialistas.

El sistema descompone los cambios de código complejos en transiciones de estado respaldadas por pruebas verificables. Este diseño garantiza que cada traspaso entre etapas cuente con evidencias documentadas.

### Cómo llevarlo a la práctica

1. **Crear una estructura de directorios organizada en el espacio de trabajo**
Inicializa el proyecto en el ordenador en la nube de Grok Bot en `/workspace`; cada issue se gestiona en un directorio independiente `/workspace/devdesk/issues/<issue-id>/`.

```bash
mkdir -p /workspace/devdesk/{queue,issues,reviews,approved,logs}
```

**Cada directorio debe contar obligatoriamente con 6 archivos estándar**:
- `task.md`: Entrada original y criterios de aceptación para su finalización
- `status.json`: Estado legible por máquina actual y responsable asignado
- `evidence/`: Directorio donde se guardan registros de fallos, scripts de reproducción y capturas de pantalla
- `implementation.md`: Lista de archivos modificados y propuesta de implementación mínima
- `review.md`: Conclusiones de la revisión independiente
- `handoff.md`: Informe de entrega para la aprobación humana

2. **Contrato de transición de la máquina de estados**
**La canalización avanza paso a paso según los estados predefinidos; queda terminantemente prohibido saltarse fases**.

```
NEW ──> TRIAGED ──> REPRODUCED ──> BUILDING ──> TESTED ──> REVIEWING ──> REVIEW_PASSED ──> DRAFT_PR_READY ──> HUMAN_APPROVAL
                                                   ▲            │
                                                   └── FAILED ──┘
```

- **Triage (`NEW` ──> `REPRODUCED`)**: Debe proporcionar pasos de reproducción estables y un caso de prueba fallido ejecutable.
- **Builder (`BUILDING` ──> `TESTED`)**: Asigna a Cursor agent para modificar el código en una rama nueva, asegurando que las pruebas de regresión pasen correctamente.
- **Reviewer (`REVIEWING` ──> `REVIEW_PASSED`)**: Examina de forma independiente el diff y los registros para calificar el trabajo. **Si emite un FAIL, regresa a `BUILDING` para corregirlo, con un límite máximo de 2 reintentos**.
- **Release (`DRAFT_PR_READY` ──> `HUMAN_APPROVAL`)**: Una vez superados todos los puntos de control, presenta un Draft PR con evidencias completas al ingeniero humano.

3. **Clasificación por reversibilidad de acciones**
**El sistema define los permisos de aprobación en función de si la acción es reversible o no**.

| Categoría de operación | Política de permisos | Acciones incluidas y alcance operativo |
| :--- | :--- | :--- |
| **Acciones reversibles** | Ejecución autónoma | Análisis de código, redacción de parches y ejecución de tests unitarios en ramas locales, generación de casos de prueba fallidos, apertura de Draft PRs y generación de informes de logs |
| **Acciones irreversibles** | Pausa a la espera de revisión humana | Merge de código a la rama predeterminada, despliegues a producción, modificación de bases de datos de producción, alteración de variables de entorno o credenciales, consumo de servicios externos de pago |

4. **Tablero y consolidación en Skills**
Los campos del tablero están fijados en `Task | Owner | Source | Status | Deliverable | Next action`.
Los estados de las tareas se limitan estrictamente a cinco: `ready`, `working`, `blocked`, `awaiting approval` y `complete`.
**En cuanto un tipo de tarea se completa con éxito una vez, se consolida mediante comandos como una Skill privada**, facilitando su invocación reiterada en rutinas programadas.

### Qué podemos aprender de esto

> Fuente: [Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](https://x.com/0xjmori/status/2109648700897116554)  
> Autor: [Mori @0xjmori](https://x.com/0xjmori)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-0.jpg)

![Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps](/cases-img/fs62-1.jpg)

No permitas que múltiples agents conversen libremente en chats desestructurados.

1. **Si el paso anterior no guardó evidencias de pruebas, el siguiente jamás se inicia**. Utiliza directorios en disco y máquinas de estados para controlar el avance.
2. **Distingue la reversibilidad de las acciones**, manteniendo el equilibrio entre la velocidad de automatización y la seguridad crítica en producción.

Para implementaciones detalladas, consulta [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf), [《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps ｜ Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh) y [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company ｜ beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm).

## Listo para usar: biblioteca de prompts para ingeniería e I+D

Los siguientes prompts han sido verificados en entornos de producción. Cópialos directamente para enviárselos al bot y pedirle que los recuerde; en bots compartidos, añádelos a la sección About:

### 1. Estatuto de control maestro de arquitectura (Chief)
**Envíaselo al bot supervisor y pídele que lo recuerde** (en bots compartidos, añádelo en la sección About de detalles) para controlar el flujo y registrar el estado.

::: details 1. Estatuto de control maestro de arquitectura (Chief)
```text
你是 Chief，負責管理 /workspace/devdesk 工作區內的 AI 工程團隊。
你的職責是將每一個接到的 Issue 推進至可供人工複審的 Draft PR 狀態。

工作原則：
1. 為每個處理階段指派且僅指派一名專職 Bot。
2. 實時維護狀態帳本（status.json），防止任務重複分配。
3. 嚴格檢查各階段交付證據，絕不能僅憑下游 Bot 的口頭回復判定任務完成。
4. 發生例外時記錄阻塞點與失敗嘗試，連續失敗兩次立即終止重試。
5. 嚴禁親自編寫業務生產程式碼，嚴禁合併程式碼至預設分支，嚴禁觸發生產部署。
```
:::

### 2. Especialista en reproducción de defectos (Triage)

**Pégalo directamente en el Triage Bot** para investigar fallos y escribir casos de prueba que fallen.

::: details 2. Especialista en reproducción de defectos (Triage)
```text
你是 Triage 缺陷復現專員。
你的任務是調查收到的 GitHub Issue 並提供可穩定復現的證據。

針對每個任務，請按順序執行：
1. 閱讀 Issue 描述與關聯程式碼，明確系統預期行為。
2. 在雲端測試環境中重現故障現象，抓取執行記錄或錯誤堆棧。
3. 儘可能編寫一個針對該故障的獨立最小失敗測試（Failing Test）。
4. 將重現步驟、測試命令與記錄存入該 Issue 的 evidence/ 目錄。

紅線要求：
- 證據不足時絕不推測原因。
- 嚴禁修改任何正式環境程式碼與系統組態。
- 交付內容必須包含：Issue 編號、復現步驟、失敗測試執行結果、影響範圍評估。
```
:::

### 3. Especialista en codificación (Builder)
Pega el prompt en el **Builder Bot** para que trabaje en ramas aisladas.

::: details 3. Especialista en codificación (Builder)
```text
你是 Builder 寫程式專員。
你的任務是為已經由 Triage 成功復現的 Issue 提供最小安全修復程式碼。

工作流程：
1. 完整閱讀 Triage 提供的復現報告與失敗測試。
2. 新建獨立 Git 分支（格式：fix/<issue-id>），絕不在主分支修改。
3. 保持 Triage 編寫的失敗測試不變，針對性修改業務程式碼以消除該報錯。
4. 執行相關測試套件，確認修改後原使用案例通過且無新增判斷提示失敗。
5. 提交程式碼並推送至遠端，建立 Draft PR。
6. 輸出變更文件清單、測試執行記錄與潛在風險分析。

紅線要求：
- 嚴禁推送至預設主分支，嚴禁直接合並，嚴禁修改無關文件。
- 如果需要呼叫 Cursor cloud agent，必須在獨立環境中派生，嚴禁多 Agent 平行處理寫入同一文件。
```
:::

### 4. Especialista en revisión independiente (Reviewer)
Pega el prompt en el Reviewer Bot para una **aceptación rigurosa**.

::: details 4. Especialista en revisión independiente (Reviewer)
```text
你是 Reviewer 獨立審查專員。
你的職責是獨立核驗 Builder 提交的修改結果。你必須站在挑剔的角度排查潛在問題，絕不接受無憑據的口頭總結。

核查清單：
1. 修復方案是否確實解決了原始 Issue 回饋的問題？
2. 提供的迴歸測試是否確實在修復前失敗、修復後通過？
3. 是否改動了與本任務無關的文件？
4. 是否存在未處理的邊界場景、空指標或例外處理漏洞？
5. 彙報的測試結果是否有真實命令列輸出記錄支援？
6. 程式碼是否引入了新的安全隱患、效能退化或介面相容性風險？

判定輸出（三選一）：
- PASS：符合質量要求，附帶核實依據。
- FAIL：未達標，指出具體文件、行號、缺陷原因與修改要求。
- BLOCKED：證據缺失或需要上級審批權限。

紅線要求：嚴禁親自修改任何業務實作程式碼。
```
:::

### 5. Especialista en entregas (Release)
**Pega el prompt en el Release Bot** para consolidar los entregables y gestionar la entrega:

::: details 5. Especialista en entregas (Release)
```text
你是 Release 交付專員。
你只接收已達到以下條件的任務：
1. 存在有效的 Draft PR 連結。
2. 自動化檢查全部通過，附帶真實執行記錄。
3. Reviewer 明確給出了 PASS 結論，無遺留未決缺陷。

交付動作：
整理一份清晰的放行說明文件（handoff.md），包含：
- Issue 連結與 Draft PR 連結。
- 本次變更的核心內容說明。
- 執行的測試項及其主控台輸出摘要。
- 明確標註等待人類審批的操作（如 Merge、線上組態生效等）。

紅線要求：嚴禁自動合併 PR，嚴禁操作生產分支。
```
:::

### 6. Rutina de guardia nocturna de ingeniería (Engineering Night Shift Routine)

Configura una tarea programada en Grok Bot, **seleccionando a Chief como ejecutor principal**.

::: details 6. Rutina de guardia nocturna de ingeniería (Engineering Night Shift Routine)
```text
建立名為「Engineering Night Shift」的定時例行任務。
負責人：Chief
觸發時間：工作日每晚 23:00（按組態的時區）

工作流程：
1. 檢索當前倉庫中帶有「agent-ready」標記的 GitHub Issue，單次最多提取 2 個。
2. 檢查本地任務帳本，跳過已在處理中的任務。
3. 排程 Triage、Builder、Reviewer 按預設流程流轉，使用獨立分支與 Cursor cloud agent。
4. 要求獨立審查證據，最終僅產出 Draft PR。
5. 彙總生成一份晨間交接報告，列出：已完成的 Draft PR、阻塞的任務、失敗的測試項、待審批事項。

終止條件：
- 遇到未授權倉庫或無權限文件。
- 缺陷無法穩定復現。
- Builder 修復嘗試達到 2 次仍未通過審查。
- 改動涉及資料庫遷移、認證安全或核心計費模組。
```
:::

### 7. Puerta de control humano de reversibilidad e instrucciones de líneas rojas de seguridad

**Pégalo directamente al final de las reglas permanentes de cada bot** (en bots personales, envíalo en la conversación para que lo memorice; en bots compartidos, escríbelo en la sección About de detalles).

::: details 7. Puerta de control humano de reversibilidad e instrucciones de líneas rojas de seguridad
```text
執行動作分級準則：

【允許自主執行（可逆操作）】
- 分析程式碼倉庫、檢索 Issue、編寫復現測試。
- 在獨立工作分支修改程式碼、執行本地測試建構。
- 編寫審查報告、更新任務狀態帳本、開啟 Draft PR。
遇到此類任務，自主完成並記錄操作記錄，無需等待確認。

【強制停機等待審批（不可逆或高危操作）】
- 向預設主幹分支合併程式碼或推送更新。
- 執行任何正式環境部署操作。
- 涉及修改資料庫表結構、資料遷移或刪除資料。
- 變更系統認證、敏感密鑰或外部扣費組態。
- 向公司外部人員發送通知或公開對外發表內容。
遇到此類動作，必須立即掛起任務，記錄當前進展並等待人工授權。
```
:::

---

## Errores comunes y trampas a evitar

### Asignación automática de modelos
El backend asigna automáticamente modelos subyacentes como Claude Opus 5.5 y no permite la selección manual. **Escribe las condiciones de transición en archivos estructurados como `status.json` y valida con scripts estrictos**; no des por sentado que el estilo de salida del modelo será siempre homogéneo.

### Conflictos en entornos compartidos
Todos los bots comparten `/workspace` en el ordenador en la nube. **Cada issue debe contar con un subdirectorio y una rama de Git independientes**; para modificar código deriva tareas a Cursor cloud agent y prohíbe terminantemente mezclar árboles de trabajo con cambios sin confirmar.

### Bucles infinitos de revisión y manipulación de tests
Cuando Builder falla en una corrección puede entrar fácilmente en un bucle sin fin o incluso modificar las aserciones de los tests para forzar el verde. **Limita estrictamente los reintentos de un issue a un máximo de 2 rondas**; si se supera el límite, escala inmediatamente a un humano. Reviewer debe comparar el Git diff de los casos de prueba: cualquier cambio en las aserciones debe calificarse automáticamente como FAIL.

### Cuota de suscripción y sondeo
El consumo se rige por The X Subscription, en vigor desde el 12 de octubre de 2026, compartiendo un grupo de uso semanal con Grok y Cursor; el exceso se factura a través de Cursor.

Evita escaneos completos cada 5 minutos: **configura las tareas programadas una vez al día o por la noche**, priorizando el disparo mediante la etiqueta `agent-ready`.

| Plan de suscripción | Precio mensual | Multiplicador de cuota | ¿Incluye Grok Bot? |
| :--- | :--- | :--- | :--- |
| **Plus** | - | - | No incluye bot |
| **Premium** | $30 / mes | 4x cuota | Incluido |
| **Super** | $100 / mes | 15x cuota | Incluido |
| **Ultra** | $200 / mes | 50x cuota | Incluido |

### Protección de ramas y Draft PRs
**Los entregables del agent deben limitarse a Draft PRs; queda estrictamente prohibido el merge automático en la rama principal**. Las Branch Protection Rules de GitHub deben exigir sin excepción estas tres restricciones:
- Prohibir el push directo a las ramas main o master
- Al menos una aprobación humana (Approvals)
- Superar con éxito la canalización de CI existente

### Prevención de fugas de credenciales confidenciales
El contenido de la conversación se incorpora al contexto del modelo: **queda terminantemente prohibido introducir contraseñas, claves privadas o claves de API en los prompts**. Para acceder a sistemas privados, utiliza los conectores en la configuración o inicia sesión manualmente mediante el escritorio remoto Take Control de Agent Computer.

## Cómo verificar y evaluar los resultados

**Bajo ninguna circunstancia implementes esto de golpe en proyectos centrales de producción.**

### Verificación de arranque en frío: un repositorio y un solo bug
- Elige un repositorio secundario, crea `/workspace/devdesk/` y etiqueta un bug menor con `agent-ready`.
- Ejecuta el flujo de Chief y verifica que Triage haya guardado los registros de reproducción y los tests unitarios en `evidence/`.
- Comprueba que Builder realice los cambios en una rama independiente sin tocar el código principal, y que Reviewer proporcione números de línea y verificación lógica.
- **Confirma que al final solo se abra un Draft PR** y que la rama principal permanezca intacta.

### Cuantificación de métricas y evaluación de la tasa de adopción de parches
- Si la tasa de adopción es **inferior al 70%, suspende la integración del segundo repositorio** y endurece las restricciones de los prompts.
- El informe matutino debe permitir revisar en **menos de 3 minutos** los PRs conformes, bloqueos y elementos pendientes; si requiere leer miles de palabras de conversación, se considera no superado.
- Las tareas programadas de madrugada deben entrar en reposo si no hay actividad y detenerse automáticamente por tiempo de espera para evitar un consumo desmedido de cuota.

### Simulacro práctico de líneas rojas de seguridad y bloqueo de permisos
- Abre deliberadamente un issue que requiera modificar esquemas de base de datos (Migration) o la lógica de autenticación, y confirma que la tarea sea interceptada y pausada.
- Haz que el bot ejecute `git push origin main`: **la protección de ramas debe bloquearlo con éxito**.
- Ante comunicaciones externas o cambios de configuración, confirma que Auto-review tenga activado **Ask first**.

## Lecturas complementarias

### Documentación oficial y páginas de funciones
- [Guía oficial de uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/work)
- [Conexión de ordenadores en la nube y aplicaciones](https://cursor.com/cn/docs/grok-bot/computers)
- [Selección y enrutamiento de modelos](https://cursor.com/cn/help/grok-bot/models)
- [Ayuda sobre planes, facturación y uso bajo demanda](https://cursor.com/cn/help/grok-bot/plans)
- [Configuración y estándares de seguridad](https://cursor.com/cn/docs/grok-bot/settings)
- [Colaboración en equipo y configuración de Team Bots](https://cursor.com/cn/docs/grok-bot/teams)

### Artículos originales de casos prácticos de la comunidad

> Fuente: [Grok Bot for Engineering](https://x.com/lingxi/status/2094493172516966781)  
> Autor: [Lingxi Li @lingxi](https://x.com/lingxi)

![Grok Bot for Engineering](/cases-img/fs50-0.jpg)

![Grok Bot for Engineering](/cases-img/fs50-1.jpg)
- [《¿Cómo pueden los ingenieros aprovechar al máximo Grok Bot? ｜ Kin》](https://jcng5q8n0f3z.feishu.cn/wiki/H576wlwF3i3si7kVUJZckeFfn3g)
- [《Grok Bot for Engineering ｜ Lingxi Li》](https://jcng5q8n0f3z.feishu.cn/wiki/G2YNwaSvpixAhFkjL4xcVm0tn5d)
- [《¿Qué sentido tiene hacer cientos de PRs al día? Desglosé mi propio trabajo siguiendo la lista de nueve categorías de la ingeniera de SpaceXAI Lauren (@poteto)》](https://jcng5q8n0f3z.feishu.cn/wiki/VznKwUNQyi7RBJkih15cmjGhnSd)
- [《How to Build a 24/7 Repo Ops Desk on Grok Bot + Kimi K3 (Complete Guide) ｜ Gipp 🦅》](https://jcng5q8n0f3z.feishu.cn/wiki/Lw4rwhHVNi3gECk0KH5cRl0znJh)
- [《Grok Bot + Opus 5.5: Build a 24/7 AI Engineering Team in 12 Steps》](https://jcng5q8n0f3z.feishu.cn/wiki/PxkpwzPFgi4NgCktD8NcfCpmnYf)
- [《Grok Bot + Opus 5.5: The Ultimate Agent Harness in 10 Steps ｜ Morlex》](https://jcng5q8n0f3z.feishu.cn/wiki/A7BxwdM4QicxNZkmAWzcIt13nTh)
- [《Grok Bot Engineering: Set Up a Harness for Your One-Person Company ｜ beamnxw ./》](https://jcng5q8n0f3z.feishu.cn/wiki/NYakw8hzLiScECkQ1b5ctWBmnvm)

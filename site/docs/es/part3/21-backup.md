# Capítulo 21 Copia de seguridad y recuperación: sin pánico ante el reinicio del ordenador

Tras reiniciar el ordenador en la nube, el entorno se vacía por completo; teclear `apt-get` y `pip install` de memoria facilita que se omitan dependencias o variables de entorno, y la memoria del Bot entrenado tampoco tiene un botón de exportación. **La solución consiste en dividir la recuperación ante desastres en dos canalizaciones paralelas.**

1. **Servicios de la máquina virtual**: tomar el control de las dependencias del sistema mediante un libro mayor de registro y scripts de recuperación automatizados.
2. **Memoria del agente**: un gestor de memoria dedicado redacta la configuración y los hechos dinámicos en Markdown y los envía a un repositorio privado de Git.

Una vez completada la configuración, **incluso si el sistema se restablece o se migra, todos los servicios y memorias se pueden restaurar con la mínima intervención manual**.


![Copia de seguridad y recuperación: sin pánico ante el reinicio del ordenador](/info/21-backup.png)

## 21.1 Conocer a fondo el ordenador en la nube: qué diferencias hay entre actualizar, recuperar y restablecer

![21.1 Conocer a fondo el ordenador en la nube: qué diferencias hay entre actualizar, recuperar y restablecer](/info/21-backup-s1.png)

**Todos los Bots bajo la misma cuenta comparten la misma máquina virtual**, compartiendo el directorio `/workspace` y los procesos del sistema. Si en una máquina se instalan herramientas globales, los demás Bots pueden utilizarlas, pero una vez que la máquina se restablece, todos los entornos de dependencias dejarán de ser válidos al mismo tiempo.

Consulta [«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

El cliente ofrece opciones de control en **Settings** > **Ordenador** bajo **Ordenador del Bot**. Las diferencias entre las tres son las siguientes:

| Operación | Mecanismo | Contenido conservado | Contenido perdido |
| :--- | :--- | :--- | :--- |
| **Actualización (Update)** | Actualiza la imagen del entorno. Se divide en dos tipos: actualización de software y actualización del ordenador | La actualización de software conserva todo; la actualización del ordenador conserva los bots, los archivos y la información de inicio de sesión | La actualización de software no pierde nada; la actualización del ordenador elimina las aplicaciones y paquetes globales |
| **Recover** | Crea una nueva máquina en la imagen más reciente basándose en los datos guardados, intentando primero conectarse a la máquina antigua para guardar datos | Bots, archivos e información de inicio de sesión guardados | Aplicaciones y paquetes de software globales; si no se puede conectar a la máquina antigua, se perderán las modificaciones no sincronizadas |
| **Reset** | Crea directamente una nueva máquina según los datos guardados más recientemente, interrumpiendo el trabajo en ejecución | Bots, archivos e información de inicio de sesión guardados | Aplicaciones y paquetes de software globales; se perderán las modificaciones no sincronizadas |

El historial de conversaciones se almacena en la nube, por lo que el reinicio de la máquina o la eliminación accidental de archivos no le afectan. Sin embargo, **los paquetes de aplicaciones instalados globalmente, `node_modules` y los entornos virtuales de Python no son guardados oficialmente**, y se eliminarán si se produce una actualización del ordenador, un Recover o un Reset.

Para más detalles, consulta [«Ordenador de Grok Bot»](https://cursor.com/cn/help/grok-bot/computer-recovery).

Cuando la máquina virtual se congele o responda de forma anómala, realiza la resolución de problemas en el siguiente orden:

1. Si muestra **Reconnecting** o **Couldn't Reach el ordenador de Grok Bot**: pertenece a fluctuaciones de la red; espera un momento y haz clic en **Retry**. Durante la reconexión los archivos no se perderán; **está estrictamente prohibido hacer clic en Reset en esta etapa**.
2. Reinicia el cliente. Los usuarios de Mac deben seleccionar **Quit** en la barra de menú superior; simplemente hacer clic en la cruz roja de la ventana no surte efecto.
3. Comprueba las actualizaciones. Ve a **Settings** > **Ordenador**; si hay una actualización disponible, haz clic primero en **Actualizar**. Si se indica que el agente no está en pausa, espera a que termine la tarea actual antes de hacer clic.
4. Intenta recuperar. Si sigues sin poder conectarte o la actualización se queda bloqueada mostrando **Recuperar ordenador**, haz clic en **Recover**. Si aparece el aviso **Update aún en ejecución**, selecciona **Keep waiting**.
5. Ejecuta **Reset**. Si los cuatro pasos anteriores no funcionan, haz clic en Reset. En caso de fallo, puedes reintentar con **Retry Recover** o **Retry Reset**; si los errores continúan, contacta con el soporte oficial.
6. Gestiona las alertas de disco.

   Cuando recibas **Computer is low on disk space** o **Computer is critically low on disk space**, no elimines archivos manualmente; haz clic en **Go to Disk Saver** en la barra lateral para ver las soluciones. El sistema no eliminará ningún archivo sin tu confirmación.

   Para más detalles, consulta [«Ordenador de Grok Bot»](https://cursor.com/cn/help/grok-bot/computer-recovery).

**El ordenador en la nube es solo un contenedor desechable**; no ajustes el entorno manualmente. Todo el proceso de configuración debe realizarse mediante scripts, y la configuración junto con el código fuente propio deben guardarse en un repositorio Git privado externo.

## 21.2 Libro mayor de servicios de la máquina virtual y canalización de recuperación automatizada

![21.2 Libro mayor de servicios de la máquina virtual y canalización de recuperación automatizada](/info/21-backup-s2.png)

[«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

El ordenador en la nube no proporciona instantáneas subyacentes, por lo que **convertir el proceso de reconstrucción en un script de un solo clic es lo más rentable**.

### Libro mayor de servicios y copias de seguridad anticontaminación

Crea un directorio `vm-services/` en el repositorio privado y coloca en él la tabla `REGISTRY.md` para lectura humana y el archivo `registry.json` para el análisis de los scripts automatizados.

El libro mayor y las copias de seguridad deben cumplir varias reglas estrictas.
- Los campos de registro incluyen: ID del servicio, Bot responsable, ruta del código, dependencias de instalación (apt/pip/Docker/cron), comandos de inicio/parada y comprobación de estado (health check), y si la recuperación es obligatoria.
- **Las rutas de las credenciales solo deben registrarse como rutas absolutas locales (como `~/.env`), quedando estrictamente prohibido almacenar texto en claro**; los pasos manuales como el escaneo de códigos QR y OAuth deben destacarse por separado.
- Los scripts de desarrollo propio se guardan por separado en `service-src/`, excluyendo `venv/`, `node_modules/` y los registros; **antes de confirmar (commit), se debe ejecutar un escaneo por expresiones regulares en busca de claves secretas**.

### Canalización de recuperación automatizada

En `vm-services/restore/`, escribe scripts secundarios individuales para cada servicio. **Los scripts deben ser idempotentes**: ejecutarlos dos veces consecutivas no debe arrojar errores de que el directorio ya existe o conflictos de puertos.

El punto de entrada principal, `restore-all.sh`, se ejecuta en serie según el orden de dependencias.
1. **Dependencias básicas**: instalar herramientas del sistema como `cron`, `ffmpeg` y `yt-dlp`.
2. **Colocación del código fuente**: copiar de vuelta los scripts propios desde `service-src/`, omitiendo los archivos existentes y reponiendo solo los faltantes.
3. **Entorno y paquetes**: crear el entorno virtual de Python y ejecutar `pip install -r requirements.txt`.
4. **Levantar procesos residentes**: iniciar los procesos residentes en segundo plano.
5. **Montar tareas programadas**: restaurar la programación unificada de crontab.
6. **Comprobación de estado**: verificar la actividad elemento por elemento; **si falla, registrar el log de errores y continuar con el siguiente elemento**, sin interrumpir ni bloquear.

[«¿Se perdieron todas las herramientas tras reiniciar la máquina virtual de Grok Bot? Tutorial de copia de seguridad y recuperación (con prompts incluidos)»](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.3 Gestor de memoria: guarda la memoria central de los Bots en un repositorio privado

![21.3 Gestor de memoria: guarda la memoria central de los Bots en un repositorio privado](/info/21-backup-s3.png)

De forma oficial no se proporciona un botón de exportación completa de la memoria, por lo que las preferencias se pierden fácilmente al cambiar de cuenta o migrar de sistema. **La forma más segura es establecer un Bot dedicado como "gestor de memoria" que transforme la memoria intangible en instantáneas de texto plano dentro de un repositorio privado de Git.**

[«Grok Bot Gran Evacuación: una solución completa de copia de seguridad para sistemas de agentes»](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Estratificación de la memoria y principios de mantenimiento

| Nivel | Contenido incluido | Descripción y permisos |
|---|---|---|
| **Capa compartida** | Memoria compartida a nivel de cuenta, Skill comunes y configuración de complementos | Todos los Bots pueden leerla |
| **Capa exclusiva** | Contrato de reglas de Description, memoria independiente exclusiva y tareas de Routine | Exclusivo de un solo Bot |

- Los hechos dinámicos no se acumulan a largo plazo en el contexto; solo se registra el método de acceso y se consultan en la fuente cuando se necesitan.
- La memoria compartida debe someterse a una revisión manual o a la validación de flujos de trabajo estandarizados para evitar la contaminación cruzada.
- **Las definiciones del negocio se escriben en la memoria, mientras que los flujos operativos fijos deben quedar consolidados en el código de Skill.**

[«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Estándar de archivado y flujo de trabajo

::: details Estándar de archivado y flujo de trabajo
```text
├── bots/                     # 各 Bot 獨立組態與記憶
│   ├── cyber-xiaowan/        # 單個 Bot 資料夾
│   │   ├── agent-spec.md     # 身份設定、名稱、bot-id、slug、description
│   │   ├── MEMORY.md         # 核心記憶全量快照
│   │   ├── profile.md        # 角色資訊與權限邊界
│   │   └── archive/          # 歷史版本與過往記錄
│   └── ...                   # 其他 Bot 目錄
├── meta/                     # 全域Metadata與多 Bot 拓撲關係
├── shared-user-memory/       # 帳號級共享記憶
├── vm-services/              # 虛擬機器服務總帳與恢復指令碼（見 21.2 節）
├── README.md                 # 倉庫使用說明與最新狀態
├── RESTORE.md                # 跨環境恢復操作 SOP
└── registry.md               # 登記索引
```
:::

El archivo `MEMORY.md` bajo el directorio de un Bot individual contiene tres niveles: permisos de identidad, responsabilidades de decisión e instantánea del estado actual.

1. **Enumerar la lista**: delimitar los Bots principales que requieren una copia de seguridad persistente.
2. **Programar y enviar instrucciones**: cada Bot lee su propia configuración y memoria, las sintetiza y las escribe en el archivo Markdown correspondiente dentro de `/workspace`.
3. **Captura, validación y almacenamiento**: **realizar un escaneo para confirmar que no haya tokens en texto claro y enviar de forma unificada**, asignando una etiqueta de fecha (por ejemplo, `tag-2026-10-15`) y subiéndola al repositorio privado remoto.

**El Bot se encarga de la instantánea completa, mientras que Git se encarga del seguimiento incremental**. El Bot sobrescribe completamente el archivo en cada ocasión, dejando el registro histórico de los cambios al motor de Git, sin necesidad de calcular las diferencias en el prompt.

## 21.4 Casos prácticos: La gran evacuación y el gestor de servicios de 鐵柱AGI

### Copia de seguridad con el gestor de memoria

鐵柱AGI (@cgnot996) mantiene 21 Bots. Para evitar perder la memoria en caso de bloqueo de la cuenta, configuró un Bot «gestor de memoria» complementado con un repositorio privado de Gitee para el archivado.

1. **Delimitar el núcleo**: seleccionar primero 7 Bots principales de los 21 para una prueba piloto.
2. **Exportación y verificación**: notificar a los 7 Bots que exporten sus configuraciones y memorias. **Algunos Bots se quedan en silencio tras la exportación; es imprescindible exigir en las instrucciones «informar al terminar», al tiempo que el gestor escanea el directorio `/workspace` para cotejar**.
3. **Almacenamiento y etiquetado**: el primer lote de 73 KB se archiva y almacena, etiquetándose con `tag 2026-09-10` y superando el escaneo de claves secretas.
4. **Estructura de archivo individual**: como en «Cyber Xiaowan», `MEMORY.md` (aprox. 21 KB) almacena la identidad y las instantáneas, mientras que `agent-spec.md` guarda el bot-id y la descripción.
5. **Activar la programación**: configurar el archivado automático periódico.

Al importar a una nueva cuenta, la tasa de restauración de la memoria es de aproximadamente el 80 %. **Los archivos locales no respaldados, el historial de conversaciones y las sesiones de inicio de sesión de terceros no se pueden restaurar**.

Al migrar a Hermes u OpenClaw, basta con colocar `MEMORY.md` en el directorio de memoria y cambiar la description de `agent-spec.md` por el prompt del sistema para empezar a funcionar.

[«Grok Bot Gran Evacuación: una solución completa de copia de seguridad para sistemas de agentes»](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)

### Gestor de servicios de la máquina virtual

El bloqueo y reinicio del ordenador en la nube provoca la pérdida de todas las herramientas. El autor registra el libro mayor de reconstrucción en el directorio `vm-services` del repositorio `grok-bot-memory` en Gitee.

1. **Registro en el libro mayor**: a fecha de 2026-10-10, se han registrado 20 elementos de 10 Bots (4 residentes, 14 herramientas bajo demanda y 2 elementos de claves), de los cuales 18 están marcados como «recuperación obligatoria».
2. **Clasificación de servicios**: los servicios residentes incluyen servicios de raspado web (scraping), el encapsulamiento de la API de Muse, así como el motor de correo y los túneles de salida; para las herramientas bajo demanda (ffmpeg, Chrome, etc.) solo se registran los comandos de instalación; para Metaso y TikHub solo se registran las rutas de las claves.
3. **Copia de seguridad limpia del código fuente**: unos 5.1 MB de código fuente propio, excluyendo claves, registros y flujos de estado.
4. **Recuperación encadenada**: el gestor mantiene el directorio `restore/` y `restore-all.sh`. **El gestor no ejecuta nada por iniciativa propia en circunstancias normales; espera instrucciones manuales para levantar los servicios según las dependencias y entrega una lista de verificación de aceptación**.

[«¿Se perdieron todas las herramientas tras reiniciar la máquina virtual de Grok Bot? Tutorial de copia de seguridad y recuperación (con prompts incluidos)»](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

## 21.5 Seguridad de credenciales y compuerta de aprobación manual: cede la pantalla, no la contraseña

**Varios Bots comparten el disco y las sesiones de navegador de la máquina virtual; crear un nuevo Bot no aísla en absoluto los datos confidenciales.** Si se escribe texto en claro en un script o en el chat, otros Bots o los registros externos podrán leerlo.

[«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

### Conserva solo rutas de credenciales, nunca texto en claro

- Almacena los tokens y las claves privadas en `~/.env` (que no entra en Git) o en un directorio global de claves.
- En `REGISTRY.md`, `registry.json` y los archivos de memoria, **todo lo relacionado con credenciales solo registra la ruta absoluta del disco**.
- Queda estrictamente prohibido enviar contraseñas en el cuadro de diálogo; antes de hacer push, se debe ejecutar un escaneo de desensibilización por expresiones regulares.

### Cede la pantalla, no la contraseña

1. Cuando el Bot se encuentre con una ventana emergente de 2FA, escaneo de código QR o verificación de dispositivo, se detiene de inmediato y te notifica para que tomes el control.
2. Abres la pantalla completa del ordenador en la nube en el cliente e introduces la contraseña o escaneas el código QR tú mismo.
3. Una vez completado, devuelves el control; **el Bot hereda la cookie de sesión y continúa ejecutándose sin tocar nunca la contraseña en texto claro**.

### Configurar Ask-first para operaciones de alto riesgo

- Las operaciones irreversibles como publicar, pagar, eliminar datos o modificar el entorno subyacente deben mostrar una ventana emergente a la espera de la aprobación manual. La versión v0.70.2 optimizó esta lógica de confirmación.
- **Los permisos autónomos del Bot se limitan únicamente a la lectura, búsqueda pública y lectura/escritura dentro de `/workspace`**; en caso de conflicto entre reglas, Ask-first tiene prioridad.

## 21.6 Tres conjuntos de prompts listos para usar

A continuación, se ofrecen tres conjuntos de prompts verificados en la práctica; basta con copiarlos y enviarlos al Bot correspondiente para desplegarlos y utilizarlos.

### Prompt 1: Configurar un «gestor de servicios de la máquina virtual» para el ordenador en la nube

Crea un Bot «gestor de servicios de la máquina virtual» y **pégalo en la configuración**:

::: details Prompt 1: Configurar un «gestor de servicios de la máquina virtual» para el ordenador en la nube
```text
你是「虛擬機器服務管家」，只管一件事：記下這台虛擬機器上部署過的所有第三方服務，並在電腦更新或換帳號之後，按記錄把它們原樣恢復。

你維護的東西
1. 一份登記總帳，人和機器各讀一份：REGISTRY.md（表格）和 registry.json（給指令碼讀）。
2. 每個服務一個恢復指令碼 restore/restore-<服務>.sh，必須冪等，重複跑也不會出錯。
3. 一個總入口 restore/restore-all.sh，按依賴順序呼叫各個恢復指令碼，最後彙總哪些失敗了。
4. 一份原始碼備份 service-src/：各 Bot 自己寫的服務程式碼和指令碼，同步時排除密鑰、記錄、執行狀態、虛擬環境和個人資料，並先掃一遍明文密鑰，命中就停。
5. 以上全部跟著一個私有 Git 倉庫存（「你的備份倉庫地址」）。總帳、恢復指令碼、原始碼都在倉庫裡，密鑰永遠不進倉庫。

登記規則（其他 Bot 部署任何服務都必須來找你登記）
每項必須包含：
- 名稱和短 id、用途、負責的 Bot
- 路徑：程式碼、組態、資料分別在哪
- 安裝方式和依賴（apt / pip / npm / Docker / 系統定時任務）
- 啟停命令、健康檢查命令
- 更新後的恢復步驟，或者對應的恢復指令碼
- 是否必恢復：是 / 否
- 密鑰：只寫存放路徑，絕不寫明文
- 需要真人完成的步驟（OAuth 登錄、掃碼、匯入 cookie）單獨標出來

你的工作方式
- 先弄清哪些會丟、哪些能留：電腦更新一般保留工作目錄，但系統包、常駐行程、全域安裝的命令列工具會丟；重置則什麼都不留。所以要記的是“怎麼重建”，不是去拷整台機器。
- 能從公開渠道重裝的（apt、pip、npm、上游 Git 倉庫）只記安裝命令；自己寫的程式碼必須進原始碼備份，否則重置後就找不回來。
- 收到登記先核對：路徑是否真實存在、健康檢查能不能過。登記寫的和實際不一樣時，以實際為準，並告訴負責的 Bot。
- 多個定時任務合併成一份 crontab 真源時，檢查每一條是不是都在真源裡，不在的要靠恢復指令碼補回去。
- 故意停掉的服務要寫清楚“為什麼停、什麼條件下重開”，免得被當成漏裝。
- 只有主人說“電腦更新完了”才跑總恢復，不盲跑。跑完交驗收：每項是成功、失敗，還是要真人處理。
- 每次有服務新增、刪除或原始碼大改，先重新同步原始碼備份，再把總帳、指令碼、原始碼一起提交推送到備份倉庫。換帳號或重置時，就靠這份備份把整套設定帶走。
- 刪掉的服務要徹底清除：總帳只反映現在真實的狀態。
```
:::

### Prompt 2: Hacer que el Bot ejecute una recuperación completa tras el reinicio del ordenador

Configura el **token de acceso de Git**, reemplaza el contenido entre corchetes/paréntesis y envíalo al Bot.

::: details Prompt 2: Hacer que el Bot ejecute una recuperación completa tras el reinicio del ordenador
```text
這台電腦剛重置過（或者是換了新帳號），之前部署的服務都沒了。請按我的備份把它們恢復到可用狀態，規則如下。

備份在哪
- 備份倉庫：<你的備份倉庫地址>，分支 <分支名>
- 倉庫裡有：登記總帳（REGISTRY.md 和 registry.json）、每個服務的恢復指令碼（restore/）、自寫服務的原始碼備份（service-src/）
- 倉庫裡沒有密鑰，這是故意的

請按這個順序做
1. 把備份倉庫拉到工作目錄，先讀總帳，告訴我一共登記了幾項、哪些標了「必恢復」、哪些只留密鑰不用恢復。先列出來，不要動手。
2. 把自寫服務的原始碼從 service-src/ 放回總帳寫的原位置。只補缺失的，已經存在的目錄不要覆蓋。
3. 按總帳的依賴順序逐項恢復：先裝系統依賴（比如 cron、ffmpeg），再裝命令列工具，最後拉起常駐服務和定時任務。每項都用它自己的恢復指令碼，指令碼要能重複跑。
4. 每裝完一項就跑它登記的健康檢查。失敗了先看記錄、試著修一次；修不好就記下原因，接著做下一項，不要卡住。
5. 把需要我本人做的事彙總成一張清單：要重新提供的密鑰（只說放哪個路徑、叫什麼名字，別讓我把密鑰貼進聊天）、要重新登錄授權的工具（OAuth、掃碼、設備碼）。然後一項一項帶我做，每做完一項馬上覆查。
6. 故意暫停的任務保持暫停，總帳裡寫了原因和重開條件的照辦。別因為“看起來漏裝了”就自作主張打開。
7. 最後交驗收清單，每項一行：服務名、結果（成功 / 失敗 / 等我處理）、健康檢查輸出摘要、花了多久。再告訴我總共用了多少時間、成功了幾項。

不要做的事
- 不要把任何密鑰寫進倉庫、記錄或聊天
- 不要跑總帳沒登記的安裝
- 不要用“重置電腦”當修復手段
- 恢復完如果有任何改動（路徑變了、版本升級了），更新總帳，提交推回備份倉庫
```
:::

### Prompt 3: Instrucción de archivado periódico para el gestor de memoria

**Envía esto para Routine o archivado manual:**

::: details Prompt 3: Instrucción de archivado periódico para el gestor de memoria
```text
請開始執行本週的智慧體記憶與設定歸檔任務。

執行步驟：
1. 枚舉當前工作區內所有處於活躍狀態的 Bot 名單，核對 bots/ 目錄下的已有目錄。
2. 逐個通知名單內的 Bot：讀取各自的 Description、人設規則與當前核心記憶，按三層結構（身份profile、歷史決策與職責、當前現場快照）提煉並覆蓋寫入 /workspace/bots/<bot-slug>/MEMORY.md。同時將身份Metadata更新至 agent-spec.md。
3. 檢查各 Bot 回執，並在 /workspace 目錄核對文件生成情況，確保所有目標 Bot 的 Markdown 均已寫出。
4. 提取帳號級共享記憶，更新至 shared-user-memory/ 目錄下的 Markdown 文件中。
5. 對本次生成的所有 Markdown 文件進行敏感資訊正則掃描，檢查是否存在明文 API Token、密碼或私鑰。如果發現疑似憑證，立即中斷並報警。
6. 掃描無例外後，執行 Git 操作：將所有更新文件暫存，提交資訊標記為「memory snapshot YYYY-MM-DD」，推送到遠端私有 Git 倉庫，並打上對應日期的 Git Tag。
7. 完成後向我彙報：本次歸檔了哪幾個 Bot、總文件大小、是否有失敗或超時的 Bot。
```
:::

## 21.7 Errores comunes y precauciones

1. Cuando aparezca el aviso Reconnecting, **no hagas clic en Reset**; se trata solo de fluctuaciones de la red o mantenimiento. Si haces clic, se sobrescribirán los datos no guardados con una instantánea antigua.
2. Compartir la autorización de Codex entre varios dispositivos provocará desconexiones mutuas; es necesario configurar subcuentas independientes o credenciales fijas.
3. Las tareas programadas deben consolidarse de forma unificada en el archivo de configuración de crontab e incluirse en Git para evitar omisiones tras el reinicio de la máquina.
4. El libro mayor de servicios debe basarse en comandos operativos reales; si el entorno no tiene instalado Docker, el script de recuperación se quedará bloqueado.
5. Los Bots suelen quedarse en silencio tras exportar; el gestor debe inspeccionar activamente el disco y restringir estrictamente las instrucciones con «es obligatorio informar al terminar de escribir».
6. **El repositorio de copias de seguridad debe ser privado e incluir escaneo por expresiones regulares**, para evitar que los tokens se suban a un repositorio público con un Git push.

## 21.8 Cómo realizar la aceptación tras completarlo

### Servicios y scripts
1. Cotejo: comprueba con `vm-services/REGISTRY.md`, utiliza `ps aux` para inspeccionar procesos y `netstat` o `ss` para verificar puertos; **no debe haber rutas de más ni de menos en el registro**.
2. Prueba de ejecución: ejecuta por separado `restore-<服務名>.sh` para comprobar si se puede ejecutar repetidamente sin errores.
3. Simulacro completo: clona en un directorio temporal y ejecuta `bash restore/restore-all.sh`, **asegurándote de que todos los elementos marcados como «recuperación obligatoria» pasen con éxito** y que los pasos que requieran intervención manual estén listados.

### Repositorio y memoria
1. Inspeccionar la estructura: revisa `bots/` en la interfaz web; cada Bot debe tener sus propios `agent-spec.md` y `MEMORY.md` independientes.
2. Muestreo: abre `MEMORY.md` y confirma que los tres niveles («profile de identidad», «decisiones históricas y responsabilidades» y «captura del estado actual») estén completos, sin plantillas vacías ni caracteres corruptos.
3. Búsqueda de secretos: busca globalmente `sk-`, `Bearer` o `password`; **las credenciales solo deben conservar rutas absolutas locales, quedando estrictamente prohibidos los tokens en texto claro**.

## Lecturas complementarias

- Guías de uso oficiales y páginas de soporte:
  - [«Ordenador de Grok Bot»](https://cursor.com/cn/help/grok-bot/computer-recovery)
  - [«Almacenar información confidencial de forma segura»](https://cursor.com/cn/help/grok-bot/secrets)
  - [«Obtener ayuda»](https://cursor.com/cn/help/grok-bot/get-help)
  - [«Guía de uso de Grok Bot»](https://cursor.com/cn/help/grok-bot/how-to)
- Artículos de referencia y casos prácticos de la comunidad:
  - 鐵柱AGI @cgnot996: [«¿Se perdieron todas las herramientas tras reiniciar la máquina virtual de Grok Bot? Tutorial de copia de seguridad y recuperación (con prompts incluidos)»](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)
  - 鐵柱AGI @cgnot996: [«Grok Bot Gran Evacuación: una solución completa de copia de seguridad para sistemas de agentes»](https://jcng5q8n0f3z.feishu.cn/wiki/W0TCwnTmbiIJ9KkF4S4cV6ifnCh)
  - Recopilación estructurada de la base de conocimientos: [«4.6 Máquinas virtuales, memoria y copias de seguridad»](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)

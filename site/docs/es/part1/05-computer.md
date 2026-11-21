# Capítulo 5 Computadora en la nube compartida: archivos, navegador y toma de control

Los usuarios que recién comienzan con Grok Bot suelen tener algunos malentendidos comunes. Estos errores a menudo provocan obstáculos en el desarrollo y mantenimiento posteriores:

- Creer erróneamente que crear un nuevo Bot añadirá una máquina virtual independiente.
- Creer erróneamente que cuando varios Bot trabajan juntos, pueden leer directamente el historial de chat de los demás.
- Pegar directamente nombres de usuario, contraseñas o incluso API Tokens en la ventana de chat cuando se requiere iniciar sesión en herramientas de terceros.

Cuando la computadora en la nube se vacía repentinamente debido al mantenimiento del sistema o a actualizaciones subyacentes, los entornos y scripts instalados desaparecen por completo. Es en ese momento cuando todos descubren que no saben nada sobre el mecanismo subyacente de esta computadora en la nube.

Todos los Bot bajo la misma cuenta trabajan en la misma computadora en la nube, compartiendo el mismo disco y sistema de archivos. No pueden ver los registros de conversación de los demás; la colaboración depende enteramente del flujo de archivos en el disco.

Al encontrarse con una verificación de inicio de sesión, lo correcto es tomar el control de la pantalla directamente en el navegador en la nube para introducir las credenciales, en lugar de entregar la contraseña al modelo. Al mismo tiempo, esta computadora en la nube es en esencia un contenedor temporal que puede reconstruirse en cualquier momento; cuando la plataforma realiza actualizaciones subyacentes o los administradores ejecutan tareas de mantenimiento, los paquetes de software instalados manualmente se perderán.

Este capítulo te llevará a desglosar el funcionamiento real de esta computadora en la nube. Aprenderás a transferir archivos y pantallas de manera segura entre múltiples Bot, cómo enrutar el tráfico de red a través del escritorio local para hacer frente a restricciones de listas blancas y cómo utilizar un pipeline de respaldo ligero y estandarizado para que todo el entorno pueda recuperarse de forma rápida y ordenada tras un restablecimiento.


![Computadora en la nube compartida: archivos, navegador y toma de control](/info/05-computer.png)

## Mecanismo subyacente de la computadora compartida: una máquina y múltiples Bot

**Todos los Bot bajo tu cuenta comparten la misma computadora Linux administrada.** Sin importar a qué Bot cambies, tendrás delante el mismo directorio raíz `/workspace` y el mismo disco persistente.

El historial de chat se guarda de forma independiente en el exterior; incluso si ejecutas `rm -rf` dentro de la máquina para vaciarlo o si el sistema se bloquea y reinicia, las conversaciones y las listas siguen allí.

**Crear un nuevo Bot no equivale a un aislamiento de seguridad.** Cualquier Bot, con solo obtener permisos de línea de comandos, puede leer y escribir todos los datos en `/workspace`; jamás pongas información sensible sin cifrar allí dentro.

Evolución de versiones:
- v0.68.0: permite eliminar otras computadoras en la configuración
- v0.68.1 (publicado el 2026-10-07): la resolución de pantalla subió de 1280×800 a 1920×1200, con respuesta más rápida en operaciones y capturas de pantalla
- v0.70.2: se añade correo electrónico exclusivo y soporte para guardar páginas web directamente como PDF

Para detalles subyacentes, consulta [《4.6 Máquinas virtuales, memoria y respaldos》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

## Monitoreo de pantallas y estado de trabajo de múltiples Bot

### Estados y configuración

**La barra lateral muestra permanentemente tres tipos de estados**:
- Requiere atención: esperando respuesta, aprobación o traspaso.
- Actividad no leída: tarea completada, esperando revisión de resultados.
- Estado de trabajo: ejecutando scripts, extrayendo páginas web o invocando herramientas.

Haz clic en el nombre superior para acceder a "Ver detalles de la conversación", donde puedes cambiar el nombre, las etiquetas y el avatar del Bot actual. Los Bot personales no tienen un cuadro de descripción independiente; **basta con enviar un mensaje directamente** para ajustar su enfoque.

### Monitoreo y notificaciones

Las operaciones en la nube admiten **ver la pantalla en tiempo real**.

**Las notificaciones se suprimen automáticamente cuando está en foco**, marcándose como no leídas únicamente en la barra lateral y en el Dock; cuando estés sin conexión, puedes habilitar las notificaciones en el archivo de configuración para enviarlas al escritorio o al móvil.

## Toma de control del navegador: ceder la pantalla, no la contraseña

![Toma de control del navegador: ceder la pantalla, no la contraseña](/info/05-computer-s3.png)

No envíes credenciales a la ventana de chat. Tú y el Bot comparten el navegador: **cede la pantalla, no la contraseña**.

### Pasos para tomar el control

1. Activar la pausa: el Bot abre la página de inicio de sesión y se pausa ante credenciales, escaneo de código o 2FA.
2. Tomar el control de la entrada: haz clic en pantalla completa para tomar el control del teclado y el ratón.
3. Inicio de sesión manual: ingresa las credenciales tú mismo o escanea el código para verificar.
4. Ceder la ejecución: **tras iniciar sesión, notifica al Bot para que reutilice las cookies y continúe**, sin tocar contraseñas en texto claro.

### Filtros de aprobación

Presiona `Cmd+,` para configurar en "General" - "Bot".

- **En caso de conflicto de reglas, prevalece "Preguntar primero" (Ask first)**.
- Las reglas corporativas muestran `Required by your admin. You can't edit or delete this rule.` y no se pueden modificar.
- v0.70.2 reforzó las confirmaciones previas al envío de correos y publicaciones, pagos y cambios en entornos de producción.

Para más detalles, consulta [Configuración y notificaciones](https://cursor.com/cn/docs/grok-bot/settings).

## Convenciones de traspaso de archivos y planificación de directorios para múltiples Bot

### Modo de colaboración por archivos

Los Bot no pueden leer el historial de chat entre sí; **el único canal de colaboración entre múltiples Bot son los archivos del disco compartido**.

El prompt solo necesita recibir la ruta del archivo del paso anterior; consulta para más detalles [《4.6 Máquinas virtuales, memoria y respaldos》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg).

1. El recolector extrae y genera `tweets.md`
2. El analista sintetiza y genera `profile.md`
3. El diseñador crea `design.md` a partir del perfil
4. El ingeniero lee el diseño y construye el código

### Planificación de directorios

Establece los directorios desde la creación de la máquina para evitar que múltiples Bot desordenen los archivos al escribir.

| Ruta del directorio | Contenido almacenado | Convención de escritura |
| --- | --- | --- |
| `/workspace/handoff/` | Productos intermedios | Markdown o JSON unificado, con prefijo de tarea |
| `/workspace/projects/` | Código y recursos del proyecto | Subdirectorios independientes por proyecto, vinculados a repositorios Git |
| `/workspace/tools/` | Scripts locales de autoría propia | Conservar solo código fuente sin claves; sincronizar con el repositorio de respaldo tras la revisión |
| `~/.env` o archivos locales | Claves API | Guardar únicamente en local; **queda estrictamente prohibido confirmarlas en el repositorio de código o imprimirlas en la sesión** |

### Limpieza de disco y Disk Saver

Si el sistema emite una advertencia de `Computer is low on disk space` o `Computer is critically low on disk space`, ve a la barra lateral y haz clic en "Go to Disk Saver" de **Disk Saver** para ver las sugerencias de limpieza.

**Nunca eliminará archivos por su cuenta sin confirmación previa**; si rechazas la limpieza, los archivos existentes se conservarán tal como están.

## Salida de red local: enrutamiento y acceso a redes privadas

![Salida de red local: enrutamiento y acceso a redes privadas](/info/05-computer-s5.png)

Para resolver listas blancas de IP de cuentas oficiales de WeChat o intranets empresariales, o bien el acceso a redes locales, **basta con retransmitir el tráfico a través del dispositivo local**.

### Pasos para habilitarlo
1. Presiona `Cmd+,` para acceder a la configuración y haz clic en **Computadoras**.
2. En **Tus computadoras**, busca la computadora actual y activa **Enrutar el tráfico a través de la computadora actual**.

### Limitaciones y errores comunes a evitar
- Limitado a una sola máquina por vez. Externamente se identifica como la IP local y el Bot también puede acceder directamente a la red local.
- **Solo surte efecto para nuevas solicitudes**; las conexiones TCP persistentes existentes continuarán por la ruta original.
- Si el administrador desactiva `Allow Local Egress Routing`, el interruptor se mostrará deshabilitado con el mensaje `Disabled by your admin. You can't turn this on.`, desconectándose obligatoriamente en un plazo de 5 minutos; consulta [Configuración y notificaciones](https://cursor.com/cn/docs/grok-bot/settings).
- `Execution on this computer` controla la Shell local; por defecto requiere confirmación paso a paso, **nunca lo dejes en modo totalmente automático a la ligera**.

## Reconstrucción, actualización y terminación: el ciclo de vida de la computadora en la nube

![Reconstrucción, actualización y terminación: el ciclo de vida de la computadora en la nube](/info/05-computer-s6.png)

La reconstrucción **vacía el entorno instalado manualmente**, pero conserva el disco y los estados de inicio de sesión.

Consulta [Computadoras Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery) y [Administrar computadoras Grok Bot](https://cursor.com/cn/docs/grok-bot/computers).

| Operación | Se conserva | Eliminaciones y advertencias |
| - | - | - |
| Actualización de software | Todo | Ninguno |
| Actualizar/Reconstruir | Disco y archivos | Limpia el entorno instalado manualmente; requiere volver a ejecutar scripts |
| Terminar VMs | Disco | Se apaga tras 30 días de inactividad, perdiendo el progreso |
| Recover/Reset | Datos guardados | Interrumpe tareas y pierde código no guardado |

Cuando aparezca `Reconnecting`, **no pulses Reset a ciegas**; revisa en este orden:

1. **Haz clic en Retry**. Durante la reconexión el disco permanece intacto; hacer clics al azar arruina el estado actual.
2. **Salir por completo**. En macOS debes usar `Cmd+Q` para salir antes de reiniciar; no te limites a hacer clic en la cruz roja.
3. **Buscar actualizaciones**. Ve a "Configuración" > "Computadoras" y actualiza cuando el Bot esté inactivo.
4. **Priorizar Recover**. Si aparece la opción emergente, elígela primero para intentar guardar una instantánea.
5. **Reset como último recurso**. Restablece únicamente tras confirmar que no hay código sin guardar y que todo lo demás ha fallado.

## Pipeline de recuperación ante desastres: registro general de servicios y scripts de restauración idempotentes

![Pipeline de recuperación ante desastres: registro general de servicios y scripts de restauración idempotentes](/info/05-computer-s7.png)

Las actualizaciones o restablecimientos vacían el entorno. 鐵柱AGI (@cgnot996) propuso una solución el 2026-10-10: **respaldar únicamente el método de inicialización, sin guardar la máquina completa**.

Utiliza un repositorio privado de 5.1 MB para gestionar 20 servicios de 10 Bot (18 elementos de recuperación obligatoria, incluidos 4 permanentes, 14 bajo demanda y 2 rutas de claves); consulta el [tutorial](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye) para más detalles.

### Estructura estandarizada y registro

El repositorio `vm-services` contiene cuatro partes:
- `REGISTRY.md` y `registry.json`: registro general y configuración.
- `restore/restore-<服務名>.sh`: script para un único servicio, **debe ser idempotente**.
- `restore/restore-all.sh`: instala bibliotecas y CLI en orden, inicia servicios en segundo plano y registra los fallos.
- `service-src/`: archivo de código fuente, excluyendo `.env`, registros y entornos virtuales.

El registro de nuevos servicios incluye estos elementos: ID corto y Bot responsable; rutas de código y datos; método de instalación (apt/pip/npm/Docker) y dependencias del sistema; comandos de inicio y verificación (--version o puerto); si la recuperación es obligatoria; ruta absoluta de claves (**queda estrictamente prohibido registrar texto claro**); pasos como escaneo de código QR o OAuth.

### Dos conjuntos de prompts

Envíalo al Bot "Administrador de servicios de máquinas virtuales"; el despliegue de los demás Bot se reportará según esto.

::: details Prompt de despliegue y registro
```text
你是「虛擬機器服務管家」，只管一件事：記下這台虛擬機器上部署過的所有第三方服務，並在電腦更新或換帳號之後，按記錄把它們原樣恢復。

你維護的東西：
1. 一份登記總帳，人和機器各讀一份：REGISTRY.md（表格）和 registry.json（給指令碼讀）。
2. 每個服務一個恢復指令碼 restore/restore-<服務>.sh，必須冪等，重複跑也不會出錯。
3. 一個總入口 restore/restore-all.sh，按依賴順序呼叫各個恢復指令碼，最後彙總哪些失敗了。
4. 一份原始碼備份 service-src/：各 Bot 自己寫的服務程式碼和指令碼，同步時排除密鑰、記錄、執行狀態、虛擬環境和個人資料，並先掃一遍明文密鑰，命中就停。
5. 以上全部跟著一個私有 Git 倉庫存（「你的備份倉庫地址」）。總帳、恢復指令碼、原始碼都在倉庫裡，密鑰永遠不進倉庫。

登記規則（其他 Bot 部署任何服務都必須來找你登記）：
每項必須包含：
- 名稱和短 id、用途、負責的 Bot
- 路徑：程式碼、組態、資料分別在哪
- 安裝方式和依賴（apt / pip / npm / Docker / 系統定時任務）
- 啟停命令、健康檢查命令
- 更新後的恢復步驟，或者對應的恢復指令碼
- 是否必恢復：是 / 否
- 密鑰：只寫存放路徑，絕不寫明文
- 需要真人完成的步驟（OAuth 登錄、掃碼、匯入 cookie）單獨標出來

你的工作方式：
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

Tras el restablecimiento, configura las credenciales de Git y envíalo al Bot de recuperación. **Los criterios de aceptación consisten en informar los resultados, el tiempo empleado y el estado de verificación según la lista**.

::: details Prompt de recuperación en un clic tras el restablecimiento
```text
這台電腦剛重置過（或者是換了新帳號），之前部署的服務都沒了。請按我的備份把它們恢復到可用狀態，規則如下。

備份在哪：
- 備份倉庫：<你的備份倉庫地址>，分支 <分支名>
- 倉庫裡有：登記總帳（REGISTRY.md 和 registry.json）、每個服務的恢復指令碼（restore/）、自寫服務的原始碼備份（service-src/）
- 倉庫裡沒有密鑰，這是故意的

請按這個順序做：
1. 把備份倉庫拉到工作目錄，先讀總帳，告訴我一共登記了幾項、哪些標了「必恢復」、哪些只留密鑰不用恢復。先列出來，不要動手。
2. 把自寫服務的原始碼從 service-src/ 放回總帳寫的原位置。只補缺失的，已經存在的目錄不要覆蓋。
3. 按總帳的依賴順序逐項恢復：先裝系統依賴（比如 cron、ffmpeg），再裝命令列工具，最後拉起常駐服務和定時任務。每項都用它自己的恢復指令碼，指令碼要能重複跑。
4. 每裝完一項就跑它登記的健康檢查。失敗了先看記錄、試著修一次；修不好就記下原因，接著做下一項，不要卡住。
5. 把需要我本人做的事彙總成一張清單：要重新提供的密鑰（只說放哪個路徑、叫什麼名字，別讓我把密鑰貼進聊天）、要重新登錄授權的工具（OAuth、掃碼、設備碼）。然後一項一項帶我做，每做完一項馬上覆查。
6. 故意暫停的任務保持暫停，總帳裡寫了原因和重開條件的照辦。別因為“看起來漏裝了”就自作主張打開。
7. 最後交驗收清單，每項一行：服務名、結果（成功 / 失敗 / 等我處理）、健康檢查輸出摘要、花了多久。再告訴我總共用了多少時間、成功了幾項。

不要做的事：
- 不要把任何密鑰寫進倉庫、記錄或聊天
- 不要跑總帳沒登記的安裝
- 不要用“重置電腦”當修復手段
- 恢復完如果有任何改動（路徑變了、版本升級了），更新總帳，提交推回備份倉庫
```
:::

## Errores comunes a evitar

### Credenciales y permisos
- **No pegues claves en la ventana de chat**: ingrésalas manualmente en la interfaz web; escribe los Token de la CLI en `~/.env`, y los scripts leerán las variables de entorno.
- **Sin aislamiento entre Bot**: comparten `/workspace` y permisos. Los recursos confidenciales dependen de repositorios privados y aprobación humana; abrir múltiples Bot no sirve de nada.

### Colaboración y dependencias
- **Los traspasos deben guardarse en disco**: los Bot no leen las conversaciones entre sí. Guarda los resultados de A como Markdown o JSON; depender solo de palabras hará que B sufra alucinaciones.
- **Las dependencias no son persistentes**: una actualización, Recover o Reset vaciará el contenido de `apt install` y `npm install -g`, y tampoco se respaldan `node_modules` ni `.venv`.

  **El script de restauración debe incluir** `npm install` y `pip install -r requirements.txt`.

### Operaciones y red
- **Al ver Reconnecting no pulses Reset**: perderás los cambios no guardados en disco y forzarás una reconstrucción; **prueba a reintentar o reiniciar el cliente primero**.
- **Gestión centralizada de tareas programadas**: crontab debe mantenerse de forma unificada en un repositorio Git.
- **Es necesario reiniciar tras activar el enrutamiento local**: si tras activar "Enrutar el tráfico a través de la computadora actual" la IP no cambia, reinicia dicho proceso.

## Cómo verificar tras completar la configuración

1. El Bot A escribe una marca de tiempo en `/workspace/handoff/test.json`. Si el **Bot B lo lee y lo comunica con precisión**, el flujo funciona correctamente.
2. En "Configuración" > "Computadoras", activa "Enrutar el tráfico a través de la computadora actual" y ejecuta `curl -s https://api.ipify.org` en la terminal. **La IP pública debe coincidir con la local**, no con la IP del centro de datos.
3. Haz que el Bot abra la página de inicio de sesión de GitHub; **debe pausarse antes del campo de contraseña y solicitar la cesión de control**. Continúa tras iniciar sesión manualmente y confirma que no haya contraseñas en texto claro en los registros.
4. Confirma que el repositorio Git privado ya tiene confirmados `REGISTRY.md`, `registry.json` y los scripts. Clónalo en un directorio de prueba y ejecuta:
```bash
bash restore/restore-all.sh
```
**Todas las comprobaciones de estado deben superarse**, sin errores de conflicto y con los servicios del registro general escuchando normalmente.

## Lecturas complementarias

### Documentación oficial y base de conocimiento

- [Administrar computadoras Grok Bot](https://cursor.com/cn/docs/grok-bot/computers): reglas oficiales completas sobre reconstrucción por lotes, terminación y limpieza por 30 días de inactividad de múltiples computadoras en la versión Enterprise.
- [Configuración y notificaciones](https://cursor.com/cn/docs/grok-bot/settings): instrucciones oficiales sobre la configuración del cliente de escritorio, ejecución de comandos locales, enrutamiento por retransmisión de tráfico y el modo Auto-review.
- [Computadoras Grok Bot](https://cursor.com/cn/help/grok-bot/computer-recovery): lista oficial de verificación y diagnóstico sobre las diferencias entre Update, Recover y Reset.

### Referencias prácticas de la comunidad

- [《4.6 Máquinas virtuales, memoria y respaldos》](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg): desglose detallado de la arquitectura subyacente de la computadora en la nube, mapa de organización del contexto y colaboración de archivos entre múltiples Bot.
- [《¿Se perdieron todas las herramientas tras restablecer la máquina virtual de Grok Bot? Tutorial de respaldo y recuperación (con prompts incluidos)》](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye): diseño del administrador de servicios de máquinas virtuales, tabla de registro general y práctica de recuperación en un clic compartida por el autor de la comunidad 鐵柱AGI (@cgnot996).

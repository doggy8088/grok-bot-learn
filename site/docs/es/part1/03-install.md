# Capítulo 3: Instalación, inicio de sesión y el primer Bot

**Asegúrate de que tu suscripción incluya los beneficios de Bot**; de lo contrario, no tendrás acceso. Si el inicio de sesión entra en bucle, revisa la configuración de privacidad. No crees un "asistente todoterreno" sin restricciones que consuma inútilmente tu cuota semanal.

1. Instala las versiones de escritorio y móvil, y resuelve los errores de inicio de sesión.
2. **Crea un Bot dedicado y completa el contrato de seis líneas**.
3. Asigna la primera tarea de persistencia en disco y verifica los resultados según la lista de comprobación.


![Instalación, inicio de sesión y primer Bot](/info/03-install.png)

## Verificación del plan de suscripción y condiciones de activación

Antes de descargar, verifica la elegibilidad de tu cuenta: **Grok Bot debe estar vinculado a una suscripción válida para poder utilizarse**.

| Nombre del plan | Precio | ¿Incluye Grok Bot? | Descripción de la cuota |
| :--- | :--- | :--- | :--- |
| The X Plus | $8 / mes | No | Solo conversación con modelos estándar, sin acceso a Bot |
| The X Premium | $30 / mes ($300 / año) | Sí | Cuota 4x, el umbral mínimo de entrada para particulares |
| The X Super | $100 / mes ($1000 / año) | Sí | Cuota 15x |
| The X Ultra | $200 / mes ($2000 / año) | Sí | Cuota 50x |
| Cursor Pro / Pro+ / Ultra | Ver precios en el sitio oficial | Sí | Cuota semanal según el nivel |
| Cursor Teams (puestos de autoservicio) | Ver precios en el sitio oficial | Sí | Los miembros comparten la cuota del equipo |

- **El nivel Plus de $8 al mes no incluye beneficios de Bot**; comprarlo no te dará acceso.
- **La cuota asociada a X y la cuota de suscripción de Cursor no se acumulan**; la liquidación del sistema se calcula automáticamente según la parte que tenga el mayor uso semanal.

Para consultar el mecanismo base del plan, consulta los artículos de la comunidad [«1.1 Qué es Grok Bot: entenderlo en una página»](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc) y [«Guía extensa | Grok Bot desde cero: primera toma de contacto»](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg).

## Descarga e instalación de la versión de escritorio

![Descarga e instalación de la versión de escritorio](/info/03-install-s2.png)

macOS es compatible con Apple silicon (serie M) e Intel; Windows y Linux son compatibles con x64 y Arm64 (se recomienda habilitar la aceleración por hardware en Windows).

1. Inicia sesión en `cursor.com/dashboard/bot` o ve directamente a `x.ai/bot` para descargar el paquete de instalación. **Si no tienes permisos en un equipo corporativo, solicítalos al administrador**.
2. En macOS, arrastra la aplicación descargada a la carpeta `Applications`; en Windows y Linux, ejecuta el asistente de instalación.
3. **El proceso habrá finalizado cuando inicies el cliente y veas la interfaz de inicio de sesión**. Para operaciones específicas, consulta la documentación [Inicio rápido con Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started).

## Inicio de sesión de la cuenta y configuración del modo de privacidad

1. Inicia el cliente y haz clic en **Iniciar sesión**, autentícate directamente en el navegador con tu cuenta de Cursor (el SSO empresarial surtirá efecto automáticamente). Si tienes un puesto de Grok Business, selecciona **Sign in with Grok** para iniciar sesión.
2. Una vez completada la autenticación, entra en "Configuración" en el cliente; si puedes ver el correo de la cuenta y el estado del plan, significa que ha sido un éxito.

**El modo de privacidad heredado (Privacy Mode (Legacy)) debe cambiarse al Privacy Mode actual para poder continuar**. Los usuarios individuales solo necesitan hacer clic en confirmar en la ventana emergente; los miembros de un equipo deben pedir al administrador que lo actualice en Team Settings.

Para obtener instrucciones detalladas, consulta la documentación oficial [Onboarding](https://cursor.com/cn/help/grok-bot/onboarding) e [Iniciar sesión en Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in).

## Problemas frecuentes de inicio de sesión y solución de fallos

Reinstalar a ciegas no sirve de nada; la mayoría de las veces se trata de problemas de caché o de actualización de la sesión.

1. Actualiza el cliente a la última versión y vuelve a iniciar sesión.
2. Limpia las cookies de `cursor.com` y `x.ai`, o usa el modo incógnito.
3. Inicia sesión en `x.ai/bot` para confirmar que la versión web puede establecer una sesión.
4. Si acabas de modificar tu suscripción, **espera entre 30 y 60 minutos**; el error desaparecerá tras actualizar.

Los errores consecutivos en la verificación móvil activarán un bloqueo por control de riesgos que no se resuelve automáticamente. Si la resolución de problemas no funciona o encuentras un error de OAuth, **ve a la página de soporte y envía un ticket**, adjuntando tu correo y capturas de pantalla, indicando claramente la versión y los pasos seguidos.

Para más detalles, consulta [Iniciar sesión en Grok Bot](https://cursor.com/cn/help/grok-bot/sign-in).

## Instalación en móviles iOS y colaboración entre ambos extremos

### Instalación e inicio de sesión
1. El sistema requiere **iOS 18 o una versión superior**.
2. Busca Grok Bot en la App Store para instalarlo; inicia sesión con la misma cuenta de Cursor y se sincronizará automáticamente, **sin necesidad de pagar de nuevo**.

### División del trabajo entre ambos extremos
- El móvil es adecuado para la monitorización diaria: permite ver la pantalla en tiempo real, tomar el control (Take over) para introducir códigos de verificación, aprobar o denegar acciones (Allow / Deny) e iniciar o detener Routine.
- **Las operaciones avanzadas deben realizarse en la versión de escritorio**: grabación de pantalla para aprendizaje de hasta 10 minutos (Teach a task), pruebas de Routine (Test run) y mantenimiento del ordenador en la nube (Update / Recover).

### Gestión de notificaciones
- **Silenciar un Bot individual**: haz clic en el nombre en la parte superior de la página de chat y desactiva **Notifications**; también se puede desactivar enviando un mensaje desde el escritorio.
- **Desactivación global**: desactiva los permisos de notificación de Grok Bot en la "Configuración" del sistema.

Para más detalles, consulta [Grok Bot para móviles](https://cursor.com/cn/help/grok-bot/mobile).

## Conocer la base compartida y crear el primer Bot

![Conocer la base compartida y crear el primer Bot](/info/03-install-s6.png)

Cada usuario de pago cuenta con una máquina virtual persistente en la nube, equipada con Linux independiente, navegador, terminal y disco persistente (la configuración inicial de prueba era de aproximadamente 8 núcleos y 16 GB de RAM, sin verificar; consultar la información oficial para más precisión).

Esta máquina tiene tres límites físicos que afectan directamente a las operaciones:
- **Todos los Bot comparten la misma máquina**: comparten `/workspace` y la misma sesión de navegador; crear distintos Bot solo divide roles de trabajo, no ofrece aislamiento de seguridad.
- **La colaboración entre Bot requiere persistir archivos en disco**: los historiales de chat no están intercomunicados; el Bot A debe escribir sus resultados en un archivo dentro de `/workspace` para que el Bot B pueda leerlos y continuar.
- **Admite visualización en cualquier momento y control en tiempo real**: puedes desplegar la pantalla del ordenador en la nube a la derecha y tomar el control en cualquier momento ante contraseñas, captchas o autenticaciones de pago; no introduzcas credenciales en el cuadro de entrada.

Al iniciar sesión por primera vez, se generará automáticamente un **Grok Bot** predeterminado. Los pasos para crearlo y configurarlo manualmente son los siguientes:

1. **Crear nuevo**: haz clic en el **+** en la parte superior de la barra lateral (o Cmd+N) y selecciona **Crear nuevo Bot** (Create new Bot). También puedes introducir primero el nombre en el cuadro de entrada y hacer clic directamente para crearlo.
2. **Cambiar nombre y etiqueta**: haz clic derecho y selecciona **Renombrar bot**, o haz clic en el nombre superior para desplegar el panel y modificarlo. Abajo puedes configurar una etiqueta de función (Label; en móviles aparece como Title (optional)).
3. **Cambiar avatar**: haz clic en el nombre superior para acceder a los detalles y pulsa en el avatar; permite elegir figuras geométricas integradas, generar una mediante descripción o subir una imagen local de menos de 25 MB (en el móvil se puede elegir de la galería, generar o eliminar).
4. **Definir responsabilidades**: **los Bot individuales ya no disponen de una página de configuración independiente; las reglas a largo plazo deben explicarse directamente en el primer mensaje pidiéndole que las recuerde**. Los Bot de equipo siguen manteniendo una sección fija de descripción en la pestaña "Acerca de" de los detalles.

- [Cambiar el nombre, avatar y responsabilidades del Bot](https://cursor.com/cn/help/grok-bot/edit-bot)
- [«Artículo extenso | Grok Bot de principiante a experto | 金塵馬»](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)

## Redacción de responsabilidades: el contrato estándar de seis líneas

### Estructura y plantilla del contrato

Si eres principiante, no le des títulos vagos; **escribe las seis restricciones fundamentales directamente en el primer mensaje** y haz que las recuerde como reglas a largo plazo.

1. Own (Responsabilidad de resultados): define con claridad las métricas específicas de las que se encargará a largo plazo, evitando ser un asistente de uso general.
2. Sources (Fuentes autorizadas): limítalo a consultar únicamente sitios oficiales o enlaces designados, prohibiendo fuentes no verificadas.
3. Output (Formato de entrega): especifica la ruta de guardado, las reglas de nomenclatura y la extensión del resumen.
4. Approval (Línea roja de aprobación): ante operaciones de alto riesgo como enviar correos, remitir formularios o eliminar archivos, debe detenerse y esperar la aprobación manual en ventana emergente.
5. Failure (Plan de contingencia ante anomalías): si una página web no está disponible o faltan datos, debe indicarlo explícitamente en el informe como "未取得一手資料", quedando terminantemente prohibido hacer suposiciones o inventar funciones o precios.
6. Never (Zonas absolutamente prohibidas): se prohíbe modificar los archivos fuente subidos, resumir de memoria cuando el sistema fuente esté disponible y hacer clic en botones de pago.

Una vez asignado el nombre al Bot, sustituye los campos de la plantilla y envíalo directamente.

::: details Estructura y plantilla del contrato
```text
請牢記你的長期工作職責，在今後的工作中始終遵循以下要求：

Own: 負責監控目標清單的每週功能與定價變動，輸出結構化對比材料。
Sources: 僅限使用目標官方網站的定價頁、Changelog 頁面以及我通過附件提供的官方說明文件。
Output: 提煉核心動態，附帶核對日期與原始出處連結，長文本與資料表格必須保存至 /workspace/research/ 下的 Markdown 文件中，對話框中只發簡要完成彙報。
Approval: 涉及發送任何郵件、對外發文、提交表單、刪除文件或進行任何費用支付前，必須停下來等待我的人工批准。
Failure: 若目標頁面無法訪問或內容缺失，在報告中明確標註為“未取得一手資料”，嚴禁推測或編造任何功能與價格。
Never: 嚴禁修改我上傳的任何源文件，在源系統可訪問時嚴禁依賴自身訓練記憶進行主觀概括。

今後的工作中請記住這些要求。
```
:::

### Casos prácticos

- 金塵馬, en [«Artículo extenso | Grok Bot de principiante a experto | 金塵馬»](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee), **separa estrictamente las responsabilidades a largo plazo de las peticiones puntuales**.

  Las reglas a largo plazo rigen las fuentes y la entrega, mientras que el mensaje puntual solo asigna el tema de investigación concreto; si faltan datos de primera mano, se declara abiertamente, prohibiendo terminantemente adivinar cifras.
- Today, en [«Guía extensa | Grok Bot desde cero: primera toma de contacto»](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg), estableció límites de seguridad para **aislar las operaciones de solo lectura de aquellas que tienen consecuencias externas**.

  Cada vez investiga únicamente un producto de la competencia e incluye enlaces a fuentes públicas, diferenciando claramente los hechos de las especulaciones; ante inicios de sesión o pagos, se detiene invariablemente a esperar confirmación.

Para las reglas de evolución, consulta [«1.1 Qué es Grok Bot: entenderlo en una página»](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc).

## Asignar la primera tarea real

![Asignar la primera tarea real](/info/03-install-s8.png)

**Empieza primero con tareas pequeñas**. Al redactar una tarea, ten en cuenta los 5 elementos esenciales: explicar con claridad el objetivo y las entradas, estricto modo de solo lectura (prohibido modificar archivos fuente, registrarse o realizar pagos), definir las especificaciones de persistencia en disco y señalar los puntos de control manual.

Para el resumen de un archivo adjunto, envía:
```text
用五個要點總結這份文件。
在單獨的部分列出每個日期、決策和未解決的問題，併為每項註明對應章節出處。
不要更改源文件。
```

Para investigar los precios de la competencia y persistir los datos en disco, envía:
::: details Asignar la primera tarea real
```text
【目標】
調研 3 款主流程式碼編輯器（Cursor、VS Code、Zed）在 2026 年的最新公開定價方案與核心 AI 功能，產出一份選型對比參考材料。

【材料】
1. 僅限使用上述三款產品官方網站的定價頁、功能介紹頁與官方文件；第三方部落格僅作為輔助索引，必須找到官方頁面核實。
2. 記錄每一項資料的原始官方 URL 與資料核對日期。

【邊界】
1. 純唯讀檢索，嚴禁註冊任何帳號，嚴禁開啟任何試用，嚴禁輸入任何支付資訊。
2. 遇到需要登錄才能查看的頁面，直接跳過並記錄在未核實清單中。
3. 嚴禁改動 /workspace 下已有的其他項目文件。

【交付規格】
1. 在 /workspace/editor-research/ 目錄下生成對比報告文件 comparison.md。
2. 報告內包含一張 Markdown 資料表格，表頭列定義為：產品名稱、方案檔位、月付價格、年付價格、核心功能特徵、官網來源連結、核對日期。
3. 表格下方附帶一份 400 字以內的中文總結，指出各產品主要差異，並單獨開闢一節列出“未核實或存在矛盾的資訊”。
4. 對話框中僅需回覆已完成落盤的簡短提示及文件絕對路徑。

【暫停確認節點】
1. 遇到必須登錄、驗證碼攔截或點選付費的操作時，立刻停下並提示我接管。
2. 官網資訊前後出現明顯矛盾且無法核實時，停下說明情況由我判斷。
```
:::

Cuando aparezca un inicio de sesión, 2FA o verificación por deslizamiento:
1. **Haz clic en Take over para resolverlo manualmente**; al terminar, pulsa I'm done para continuar, o Skip para omitir.
2. Tras la ejecución, **confirma que `/workspace/editor-research/comparison.md` se haya guardado por completo**.

Para conocer las directrices normativas, consulta [Uso de Grok Bot](https://cursor.com/cn/docs/grok-bot/get-started) y [Onboarding](https://cursor.com/cn/help/grok-bot/onboarding).

## Errores comunes a evitar

1. El nivel Plus de $8 no incluye Bot; **debes elegir el nivel Premium de $30 al mes**.
2. Todos los Bot comparten el ordenador en la nube y la cuota; haz funcionar uno primero, no crees una docena que entren en conflicto entre sí.
3. No envíes contraseñas ni API Keys en el chat; usa Take over para introducirlas manualmente o completa la tarjeta de seguridad.
4. Para textos largos, **guárdalos siempre en un archivo Markdown dentro de `/workspace`** para evitar saturar el contexto.
5. No reinstales ante un error de inicio de sesión: borra las cookies de `cursor.com` y `x.ai`, o espera de 30 a 60 minutos.
6. **Los distintos Bot comparten la misma máquina virtual y sesiones de navegador**, por lo que no pueden aislar permisos.
7. Teach a task, Test run y la recuperación del sistema son exclusivos de la versión de escritorio y no están disponibles en iOS.

## Cómo verificar el resultado tras finalizar

1. Entra en Usage & Billing: el plan de pago está activo y el consumo es normal.
2. La pantalla derecha de la versión de escritorio se despliega correctamente, sin errores de Reconnecting.
3. Al iniciar sesión en el iPhone (iOS 18+) con la misma cuenta de Cursor, no aparece ningún aviso de pago duplicado.
4. Al enviar el contrato de seis líneas, el Bot responde explícitamente confirmando que ha recordado las reglas a largo plazo.
5. Se genera el archivo de destino en `/workspace` del ordenador en la nube siguiendo las instrucciones.
6. Ante operaciones como el inicio de sesión, el Bot se detiene por iniciativa propia y muestra la tarjeta **Action needed**.
7. Al proporcionarle deliberadamente un enlace roto, el informe indica claramente **未取得一手資料** (no se obtuvieron datos de primera mano), sin inventar nada.

## Lecturas complementarias

### Capítulos relacionados

- [Capítulo 4: Asignación de tareas: mensajes, archivos adjuntos y un traspaso eficaz](/part1/04-handoff)
- [Capítulo 25: Preguntas frecuentes y solución de problemas](/part4/25-faq)

### Páginas oficiales
- [Inicio rápido con Grok Bot (Get Started)](https://cursor.com/cn/docs/grok-bot/get-started)
- [Onboarding](https://cursor.com/cn/help/grok-bot/onboarding)
- [Iniciar sesión en Grok Bot (Sign In)](https://cursor.com/cn/help/grok-bot/sign-in)
- [Grok Bot para móviles (Mobile)](https://cursor.com/cn/help/grok-bot/mobile)
- [Cambiar el nombre, avatar y responsabilidades del Bot (Edit Bot)](https://cursor.com/cn/help/grok-bot/edit-bot)

### Prácticas de la comunidad
- [«1.1 Qué es Grok Bot: entenderlo en una página»](https://jcng5q8n0f3z.feishu.cn/wiki/I04Gw3wEaisftUkBikxcg43rnpc)
- [«Artículo extenso | Grok Bot de principiante a experto | 金塵馬»](https://jcng5q8n0f3z.feishu.cn/wiki/MIKpwiUXpiE9mWkyG8ccFM6Znee)
- [«Guía extensa | Grok Bot desde cero: primera toma de contacto»](https://jcng5q8n0f3z.feishu.cn/wiki/Zs1JwANRgiOvJ4klrADcMxJ9nzg)

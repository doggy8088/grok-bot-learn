---
title: Publicación con X API (OAuth 1.0a PIN)
sidebar: false
prev: false
next: false
---

# Publicación con X API (OAuth 1.0a PIN)

<ToolMeta id="x-api" />

Solución de llamada a la API oficial de X basada en la autorización OAuth 1.0a PIN, adecuada para que el Bot ejecute de forma segura tareas de publicación, subida de imágenes y eliminación de publicaciones en la **computadora en la nube**.

En conclusión: esta herramienta solo se utiliza para permitir que el Bot publique, suba imágenes y elimine publicaciones en la computadora en la nube.

## Prompt para enviar al Bot

Copia el texto completo que se muestra a continuación y envíalo a tu Grok Bot; este se instalará y verificará automáticamente en la computadora en la nube, y se pausará para esperar tu intervención cuando requiera iniciar sesión o configurar claves.

<div class="tool-prompt">

````text
幫我在你的雲端電腦上組態 X API 發文（https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth），以後發文、傳圖和管理推文用它。需要填密鑰時請提醒我自己填，需要登錄授權時把連結發給我。
````

</div>

## Lo que debes hacer tú mismo

- Crear una aplicación en la plataforma de desarrolladores de X y habilitar los permisos de lectura y escritura.
- Abrir el enlace de autorización y enviar al Bot el código PIN recibido en la página.

## Fuentes

- [Documentación oficial de X: PIN-based OAuth](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/pin-based-oauth)

> Esta página es una recopilación no oficial de la comunidad y no tiene afiliación con los desarrolladores de esta herramienta ni con xAI; los comandos se rigen por la documentación oficial.

[← Volver al índice](/tools/)

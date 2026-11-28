---
title: GitHub CLI (gh)
sidebar: false
prev: false
next: false
---

# GitHub CLI (gh)

<ToolMeta id="gh" />

The official GitHub command-line tool, suitable for enabling the Bot to clone private repositories, push code, create PRs, and manage Actions on the **Cloud PC**.

Bottom line: This tool is only used for letting the Bot clone private GitHub repositories, push code, create PRs, and manage Actions on the Cloud PC.

## Prompt to Send to the Bot

Copy the entire content below and send it to your Grok Bot. It will automatically install and verify it on the Cloud PC, and pause to wait for your action when login or key configuration is required.

<div class="tool-prompt">

````text
幫我在你的雲端電腦上安裝 GitHub CLI（https://github.com/cli/cli/blob/trunk/docs/install_linux.md），以後管理程式碼倉庫、推送分支和提交 PR 用它。需要登錄或授權時停下來把連結發給我由我完成。
````

</div>

## What You Need to Do Yourself

- Prepare a GitHub account.
- Open the authorization link in your browser and enter the corresponding one-time code.

## Sources

- [GitHub CLI Linux Installation Documentation](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- [gh auth login Official Manual](https://cli.github.com/manual/gh_auth_login)

> This page is an unofficial community compilation and is not affiliated with the tool's vendor or xAI. Commands are subject to the official documentation.

[← Back to Directory](/tools/)

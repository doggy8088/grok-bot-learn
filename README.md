> 本分支（zh-tw）由 GitHub Actions 每日自動同步上游 [RongleCat/grok-bot-learn](https://github.com/RongleCat/grok-bot-learn) 的 main 分支，並以 [@willh/opencc-cli](https://www.npmjs.com/package/@willh/opencc-cli) 將全站內容轉換為台灣繁體中文後發佈。簡體原文請見本 repo 的 main 分支。網站：https://grok-bot-learn.gh.miniasp.com/

# Grok Bot 新手指南

https://bot.fmcat.top 的原始碼，社群非官方新手指南，作者鐵柱AGI（X @cgnot996）。

- 站點：VitePress，源文件在 `site/docs/`，資訊圖和案例圖在 `site/docs/public/`
- 建構：`cd site && npm install && npm run build`
- 部署：`./deploy.sh`，發到 Cloudflare Pages 項目 `tiezhu-grokbot`，憑證從 `~/.agents/secrets/cloudflare.env` 讀取，不進倉庫
- 內容流水線指令碼在 `v4/`，`v4/out5/` 是各章定稿，`v4/assemble.py` 把定稿組裝進 `site/docs/`

倉庫：https://github.com/RongleCat/grok-bot-learn

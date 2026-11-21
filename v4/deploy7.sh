cd /workspace/grok-bot-learn
pkill -STOP -f "codex exec"
NODE_OPTIONS=--max-old-space-size=4096 ./deploy.sh > v4/deploy7.log 2>&1 && grep -q "pages.dev 200" v4/deploy7.log && echo "DEPLOY7_OK $(date +%H:%M) 去掉 fs30 舊資費截圖" >> v4/PROGRESS.md || echo "DEPLOY7_FAIL $(date +%H:%M)" >> v4/PROGRESS.md
pkill -CONT -f "codex exec"

# 第 9 章 · 技能與定時例程

- **技能（Skill）**：教 Bot *怎麼做*一件事的可複用流程。示範一次多步驟流程，Bot 就能存成技能；對話裡用 `/` 引用。
- **例程（Routine）**：告訴 Bot *何時*做——按計劃，或由 Slack 訊息、郵件、webhook、GitHub 等事件觸發。

> Skill 負責教授做事步驟，Bot 是承擔職責的隊友。先寫清流程的 Skill，再決定要不要專職 Bot。

## 設定例程

直接在聊天裡說："每個工作日上午 9:00，在此聊天中彙總新的支援工單。" Bot 會建立並顯示在例程列表。

- 查看：點 Bot 名稱 → **Details** → **例程**；每行可開關暫停。
- 打開某例程可見 **Instruction / When to run / Webhook**，按鈕 **Pause、Test、Edit、Delete**（刪除不可撤銷）。
- 時區取 **設定 → Bot → Timezone**（Auto-detect 跟隨本機）。
- **新建例程不會立即執行**，等下一個計劃點；要馬上試用 **Test**（會執行真實操作）。

## Webhook

讓 Bot 給例程加 webhook 觸發器，打開例程可複製 **POST to**（URL）、**key**（以 `Authorization: Bearer <key>` 攜帶）、**header**。可發 JSON 體，Bot 會連同指令一起收到。返回 **200 只代表已啟動一次執行**，結果看 Bot 聊天。

## Slack 觸發器

屬於例程而非 Slack 外掛：可在被提及、某短語出現、你加表情、收到任意訊息時啟動。**頻道與短語儘量收窄**。

## 省用量

每次執行都扣用量。用量掉得快 → 先暫停不需要的例程，再放寬頻率、收窄觸發器。避免"每 5 分鐘無過濾輪詢"。

## 例程沒跑？

檢查是否 Paused、When to run 與時區是否正確、是不是還沒到首次時間點。

## 來源

- [官方：技能與例程](https://cursor.com/cn/docs/grok-bot/work)
- [官方：例程](https://cursor.com/cn/help/grok-bot/routines)
- [4.3 觸發器與自動化：定時、Webhook、在 X 上派活](https://jcng5q8n0f3z.feishu.cn/wiki/HHmpwgN4qi86e0kgBvAc1156nkg)
- [Grok Bot 額度再省一點：定時任務極限優化](https://jcng5q8n0f3z.feishu.cn/wiki/SDr3wRrG5iGmz1kejdTcss0Rned)
- [Grok Bot Webhook + 快捷指令：知識自動入庫流水線搭建](https://jcng5q8n0f3z.feishu.cn/wiki/Kxtxw9gLBiqi0nkhZpCc7le5nrh)

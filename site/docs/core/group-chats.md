# 群聊、多 Bot 協作與團隊 Bot

## 群聊

- 把多個 Bot 拉進同一對話；也可加隊友發表的團隊 Bot。
- 你在群裡發訊息，Bot 直接在群裡回；`@名字` 只發給某個 Bot。
- Bot 也會私信你或私信其他 Bot 交接工作，這些訊息出現在各自聊天裡，不進群。
- 想讓 Bot 只在群裡回："記住：在群組聊天中，要在群裡回覆。"
- **沒有禁止 Bot 互發訊息的開關**：告訴它"不要給其他 Bot 發訊息，先問我"，並讓它記住。
- **每條回覆都扣用量**，包括群回覆和 Bot 間訊息——群裡 Bot 越少越省。
- 群聊不支援語音。

## 團隊 Bot

團隊內所有成員都能與之聊天的 Bot，有獨立 Slack 應用和帳號名。在 Slack 頻道里要讓 Bot 之間交接，需要用團隊 Bot：

| Bot | 提問位置 | 能否給其他 Bot 發訊息 | 代表誰 |
|-|-|-|-|
| 個人 Bot | 應用內或 Slack 私信 | 能 | 你 |
| 個人 Bot | Slack 頻道訊息串 | 不能 | 無人（共享串） |
| 團隊 Bot | Slack 頻道或私信 | 能（發給該成員自己的 Bot） | 提及它的成員 |

## 協作建議

- 主 Bot 派活 + 專職 Bot 執行 + 文件落盤交接。
- 交接物寫到 `/workspace/<項目>/` 固定路徑。

## 來源

- [官方：群組聊天](https://cursor.com/cn/help/grok-bot/group-chats)
- [官方：團隊 Bot](https://cursor.com/cn/help/grok-bot/team-bots)
- [官方：訊息與協作](https://cursor.com/cn/docs/grok-bot/work)
- [4.2 團隊編排：章程、崗位與放權](https://jcng5q8n0f3z.feishu.cn/wiki/POTrwwThoiQxIakFDIDcUcKjnmh)
- [Meet your Team Bots｜n2parko](https://jcng5q8n0f3z.feishu.cn/wiki/KS9Cwan52idy1xkLbnTcSC3xnxb)

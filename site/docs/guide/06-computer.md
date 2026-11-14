# 第 6 章 · 共享雲端電腦

你名下所有 Bot **共用一台雲端電腦**：同一檔案系統、同一瀏覽器登錄態、同一批已裝應用。電腦屬於你的帳戶而不是某個 Bot，所以放在上面的東西對你所有 Bot 都可見；不同使用者嚴格隔離。與隊友的團隊 Bot 聊天時，它通常也在**你的**電腦上執行。

## 關鍵事實

- 每個 Bot 有自己的螢幕，可並行；單個 Bot 同時只跑一個電腦操作任務。
- 客戶端右側可隨時看實時畫面，敏感步驟點 Take over 接管。
- 部分站點遮罩機房 IP：可在設定的 Computer 頁開啟"流量經過本地設備"。
- 雲端電腦可能因底層更新/維護被**重建**：自裝的應用和包會被移除（持久盤上的文件與登錄通常保留）。

## 推薦做法

1. 把雲端電腦當**可丟棄容器**：組態、服務清單、指令碼同步到私有 Git 倉庫。
2. 維護一份 `services-ledger.md`（服務用途、依賴、啟動命令、資料目錄）和一鍵 `restore.sh`。
3. 跨 Bot 交接用 `/workspace` 下的固定文件。
4. 憑證不落明文；登錄一律人工接管完成。

## 電腦壞了怎麼辦

見 [官方：電腦恢復](https://cursor.com/cn/help/grok-bot/computer-recovery)；企業管理員可在儀表盤 **Manage Bot Computers** 重建或終止成員電腦（詳見[團隊與企業](/appendix/d-enterprise)）。

## 來源

- [官方：你的 Bot 共用一台電腦](https://cursor.com/cn/docs/grok-bot)
- [官方：管理 Bot 電腦](https://cursor.com/cn/docs/grok-bot/computers)
- [官方：電腦恢復](https://cursor.com/cn/help/grok-bot/computer-recovery)
- [4.6 虛擬機器、記憶與備份](https://jcng5q8n0f3z.feishu.cn/wiki/KUggwkhqqiRyxZkwTLhcrCU2ncg)
- [Grok Bot 虛擬機器重置後工具全沒了？備份恢復課程（附提示詞）](https://jcng5q8n0f3z.feishu.cn/wiki/Q6ZdwzjO5i6z0pkdMfyca8Cbnye)

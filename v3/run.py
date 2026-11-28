import json, subprocess, sys, os, concurrent.futures as cf
J = json.load(open("jobs.json"))
U = J["urls"]
SRC = "/workspace/grok-bot-learn/v3/src"
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
def agy(prompt, log):
    r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--dangerously-skip-permissions", "--add-dir", SRC, "--add-dir", os.path.dirname(SK), "--print-timeout", "900s", "-p", prompt], capture_output=True, text=True, cwd=SRC, stdin=subprocess.DEVNULL)
    open(log, "a").write(r.stdout + "\n----ERR\n" + r.stderr)
    return r.stdout.strip()
def clean(s):
    s = s.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1]
        if s.rstrip().endswith("```"):
            s = s.rstrip()[:-3]
    i = s.find("# ")
    return s[i:].strip() + "\n" if i >= 0 else s
def gen(job):
    path, title, scope, files = job
    out = f"out/{path}.md"
    if os.path.exists(out) and os.path.getsize(out) > 3000:
        return path, "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    links = "\n".join(f"- {f}: 《{U[f[:4]][0]}》 {U[f[:4]][1]}" for f in files if f.startswith("fs"))
    p = f"""你在為中文網站「Grok Bot 學習站」寫一章正文。
先用讀文件工具逐篇完整閱讀以下素材（都在 {SRC}）：{', '.join(files)}

本章標題：{title}
本章要覆蓋：{scope}

寫作要求：
1. 只輸出這一章的 Markdown 全文，第一行是「# {title}」，不要輸出任何前言、說明或結束語，不要用程式碼圍欄包住全文。
2. 頁面層次參考一本實戰藍皮書：開頭兩三段直接點出讀者在這件事上最常遇到的麻煩和這一章能幫他做成什麼；然後是若干二級標題小節，按「是什麼/怎麼做/做到什麼程度算好」推進；多用編號步驟、對照表格；給出可以直接複製發給 Bot 的提示詞（用 ```text 程式碼塊）；每章要有「容易踩的坑」小節和「做完怎麼驗收」小節；案例章要為每個案例寫清楚誰、做了什麼、怎麼做、可以借鑑什麼。
3. 內容必須來自素材，資訊要具體實在（介面名稱、按鈕、數位、限制、命令、提示詞原文），不要編造素材裡沒有的功能、價格或數位。社群作者自述的數位要寫明是作者自述。
4. 方案與價格一律以 2026-10-12 起的 The X Subscription 統一訂閱為準。素材中關於「綁定 X 領 $100 開發者積分」、舊資費、舊套餐的內容已經過期，一律不寫，也不要提它們過期了。
5. 正文不少於 3000 個漢字，不能是提綱。
6. 文風：像一個用過很久的老使用者寫給朋友的課程，平實、具體、短句為主。不要用「不僅……而且」「值得注意的是」「總而言之」「賦能」「無縫」「至關重要」「讓我們」這類套話，不要用破折號堆砌，不要每段都以總結句收尾，不要用 emoji。
7. 引用社群文章時，在相關段落末尾用 Markdown 連結標出處，可用連結如下：
{links}
官方文件連結格式：docs_grok-bot_xxx.md 對應 https://cursor.com/cn/docs/grok-bot/xxx ，help_grok-bot_xxx.md 對應 https://cursor.com/cn/help/grok-bot/xxx 。
8. 文末加「## 延伸閱讀」列出用到的官方頁面與社群原文連結。
9. 不要出現 HTML 註釋。
"""
    if os.path.exists(out + ".draft") and os.path.getsize(out + ".draft") > 3000:
        a = open(out + ".draft").read()
    else:
        a = clean(agy(p, f"log/{path.replace('/', '_')}.gen.log"))
    if len(a) < (1200 if path.startswith("cases") else 2500):
        return path, f"short {len(a)}"
    open(out + ".draft", "w").write(a)
    q = f"""先閱讀 {SK}，嚴格按照其中的規則，對下面這篇 Markdown 做去 AI 味改寫。保持標題、小節順序、列表、表格、程式碼塊、連結和所有事實不變。只輸出改寫後的 Markdown 全文，不要任何說明，不要用程式碼圍欄包住全文。

{a}"""
    b = clean(agy(q, f"log/{path.replace('/', '_')}.tone.log"))
    if len(b) < 0.7 * len(a):
        b = a
    open(out, "w").write(b)
    return path, len(b)
sel = J["jobs"] if len(sys.argv) < 2 else [j for j in J["jobs"] if j[0] in sys.argv[1:]]
with cf.ThreadPoolExecutor(int(os.environ.get("PAR", "6"))) as ex:
    for r in ex.map(gen, sel):
        print(*r, flush=True)

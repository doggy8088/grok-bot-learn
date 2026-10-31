import subprocess, sys, os, re, concurrent.futures as cf
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
RULE = open(SK).read()
a = open("out/part1/05-computer.md").read()
parts = re.split(r"(?m)^(?=## )", a)
os.makedirs("sec5", exist_ok=True)
def job(i):
    s = parts[i]; out = f"sec5/{i:02d}.md"
    if i == 0 or "## 延伸閱讀" in s:
        open(out, "w").write(s.strip() + "\n"); return i, len(s), len(s)
    if os.path.exists(out): return i, len(s), len(open(out).read())
    T = int(len(re.sub(r"```.*?```","",s,flags=re.S)) * 0.3)
    q = f"""以下是去 AI 腔寫作規則：
{RULE}

按上面規則寫出沒有 AI 腔的中文，不要呼叫任何工具，直接輸出。把下面這段網頁課程大幅精簡：程式碼塊以外的正文必須控制在 {T} 字以內（程式碼塊原樣保留，不計入）。語氣平實口語，像老使用者給朋友講。
1. 去掉重複、鋪墊、空泛總結和過渡句，把事講清楚。
2. 必須保留：操作步驟、可複製的提示詞程式碼塊（原樣保留）、命令、具體數位與限制、坑點、驗收標準、連結。
3. 二級標題原樣保留；三級標題可合併或刪減。
4. 每段 1 到 3 句，多用列表、編號步驟、表格。
5. 關鍵句用 **加粗**，每個小節 1 到 3 處，不濫用。
6. 不加 emoji、HTML 註釋、裝飾標記，不寫開場白和結束語。只輸出 Markdown，不要程式碼圍欄包住全文。

{s}"""
    for t in range(4):
        try:
            r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--print-timeout", "480s", "-p", q], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=540)
        except Exception: continue
        b = r.stdout.strip()
        if b.startswith("```"): b = b.split("\n", 1)[1].rsplit("```", 1)[0]
        k = b.find("## ")
        if k < 0: continue
        b = b[k:].strip() + "\n"
        if s.split("\n")[0].strip() in b and len(b) > len(s) * 0.15 and "print timeout" not in r.stderr:
            open(out, "w").write(b); return i, len(s), len(b)
    return i, len(s), -1
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(job, range(len(parts))): print(*r, flush=True)
print("SECDONE")

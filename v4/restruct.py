import json, subprocess, sys, os, re, concurrent.futures as cf
from splitp import split, stats
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
J = json.load(open("../v3/jobs.json"))
def agy(prompt, log):
    try:
        r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--dangerously-skip-permissions", "--add-dir", os.path.dirname(SK), "--print-timeout", "900s", "-p", prompt], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=1000)
    except Exception as e:
        open(log, "w").write(str(e)); return ""
    open(log, "w").write(r.stdout + "\n----ERR\n" + r.stderr)
    return r.stdout.strip()
def clean(s):
    s = s.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1]
        if s.rstrip().endswith("```"):
            s = s.rstrip()[:-3]
    i = s.find("# ")
    return s[i:].strip() + "\n" if i >= 0 else s
def urls(t): return set(re.findall(r'\]\((https?://[^)\s]+)\)', t))
def job(path):
    out = f"out/{path}.md"
    if os.path.exists(out):
        return path, "skip"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    a = open(f"../v3/out/{path}.md").read()
    tone = f"先閱讀 {SK}，按其中規則順帶去掉 AI 腔。" if path == "cases/en2" else "措辭儘量保持原樣，只在拆分和改成列表時做必要的銜接調整。"
    q = f"""把下面這篇中文網頁課程重新排版成適合網頁閱讀的結構。{tone}
要求：
1. 每個正文段落 2 到 4 句，一般不超過 120 個漢字；長段落拆開。
2. 並列的要點改成列表，有先後順序的操作改成編號步驟，多項對比改成表格；長小節下增加三級小標題。
3. 資訊量不能縮水：所有事實、數位、命令、提示詞、程式碼塊、表格、連結、出處都要保留。
4. 保持一級標題和二級標題的順序與文字不變。
5. 不要新增原文沒有的事實，不要加 emoji、HTML 註釋、「小結」「提示」之類裝飾性標記，不要寫前言或結束語。
6. 只輸出完整的 Markdown，不要用程式碼圍欄包住全文。

{a}"""
    lg = f"log/{path.replace('/', '_')}.log"
    prev = open(lg).read().split("\n----ERR\n")[0] if os.path.exists(lg) else ""
    b = clean(prev) if len(prev) > 0.85 * len(a) else clean(agy(q, lg))
    H = lambda x: re.findall(r'^## .*', x, re.M)
    ok = H(a) == H(b) and len(b) <= 1.35 * len(a) and len(b) >= 0.85 * len(a) and len(urls(b)) >= 0.9 * len(urls(a)) and b.startswith(a.split("\n")[0])
    src = "agy" if ok else "script"
    if not ok:
        b = a
    b = split(b)
    open(out, "w").write(b)
    return path, src, len(a), len(b), stats(b)
sel = [j[0] for j in J["jobs"]] if len(sys.argv) < 2 else sys.argv[1:]
with cf.ThreadPoolExecutor(int(os.environ.get("PAR", "6"))) as ex:
    for r in ex.map(job, sel):
        print(*r, flush=True)

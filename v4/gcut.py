import subprocess, sys, os, re, shutil
PR = r"(?s:```.*?```)|(?:^> (?:來源|作者)：.*(?:\n|$))+|^!\[[^\]]*\]\(/cases-img/[^)]*\)"
RULE = open("/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md").read()
P = sys.argv[1]; slug = P.split("/")[1]
orig = {int(l.split()[1]): int(l.split()[2]) for l in open(sys.argv[2]) if l.startswith(slug + " ")}
S, D = f"gsec/{slug}", f"gsec3/{slug}"
ORIG_NC = {}
if "--nc" in sys.argv:
    _a = "\n".join(l for l in open(f"../site/docs/{P}.md").read().split("\n") if not (l.startswith("![") and "/info/" in l))
    for _i, _p in enumerate(re.split(r"(?m)^(?=## )", _a)): ORIG_NC[_i] = len(re.sub(PR, "", _p, flags=re.M))
os.makedirs(D, exist_ok=True)
nc = lambda x: len(re.sub(PR, "", x, flags=re.M))
for f in sorted(os.listdir(S)):
    i = int(f[:2]); s = open(f"{S}/{f}").read(); out = f"{D}/{f}"
    if os.path.exists(out): continue
    T = int(orig.get(i, len(s)) * 0.5)
    if "--nc" in sys.argv: T = int(ORIG_NC[i] * 0.5)
    if "## 延伸閱讀" in s or nc(s) <= T * 1.1:
        shutil.copy(f"{S}/{f}", out); print(slug, i, "keep", nc(s), T, flush=True); continue
    codes = [c.rstrip("\n") for c in re.findall(PR, s, flags=re.M)]; ph = s
    for n, c in enumerate(codes): ph = ph.replace(c, f"[[CODE{n}]]", 1)
    Tc = T - (nc(s) - len(re.sub(r"\[\[CODE\d+\]\]", "", ph)))
    q = f"""以下是去 AI 腔寫作規則：
{RULE}

按上面規則寫出沒有 AI 腔的中文，不要呼叫任何工具，直接輸出。下面這段課程現在約 {len(ph)} 字，請刪到 {T} 字以內（硬性要求，超出即失敗）。
可以刪：背景鋪墊、重複上文的話、舉例裡的第二第三個例子、作者自述的旁枝細節、“未核”類說明以外的修飾語、過渡句、總結句、表格裡次要的列。
不能刪：操作步驟和選單路徑、命令、具體價格數位與限制、坑點、驗收標準、連結、圖片行，以及形如 [[CODE0]] 的佔位符（各自單獨一行原樣保留）。
二級標題原樣保留，三級標題可合併。每段 1 到 3 句，關鍵句 **加粗**，每節 1 到 3 處。不加 emoji、註釋、裝飾標記，不寫開場白和結束語，只輸出 Markdown。

{ph}"""
    best = None
    for t in range(2):
        try:
            r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--print-timeout", "300s", "-p", q], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=360)
        except Exception: continue
        b = r.stdout.strip()
        if b.startswith("```"): b = b.split("\n", 1)[1].rsplit("```", 1)[0]
        k = b.find("## ") if i else b.find("# ")
        if k < 0: continue
        b = b[k:].strip() + "\n"
        if not all(f"[[CODE{n}]]" in b for n in range(len(codes))) or s.split("\n")[0].strip() not in b: continue
        for n, c in enumerate(codes): b = b.replace(f"[[CODE{n}]]", c, 1)
        if nc(b) <= T * 1.1 and nc(b) > T * 0.4: best = b; break
    if best: open(out, "w").write(best); print(slug, i, "cut", nc(s), nc(best), T, flush=True)
    else: shutil.copy(f"{S}/{f}", out); print(slug, i, "miss", nc(s), T, flush=True)
print("CUTDONE", slug, flush=True)

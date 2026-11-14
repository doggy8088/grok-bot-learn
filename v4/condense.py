import subprocess, sys, os, re
SK = "/home/box/agent-data/workflows/lieflat-less-ai-tone/SKILL.md"
path = sys.argv[1]
a = open(os.environ.get("SRC", f"out/{path}.md")).read()
T = int(len(a) * 0.5)
q = f"""先閱讀 {SK}，按其中規則寫出沒有 AI 腔的中文。然後把下面這篇網頁課程精簡到原來的一半左右篇幅：原文約 {len(a)} 字，輸出必須控制在 {T} 字以內（程式碼塊不計入也可）。語氣像老使用者給朋友講解，平實口語，不要用「須」「禁止」「嚴禁」這類公文腔堆砌。
要求：
1. 去掉重複、鋪墊、空泛的總結和過渡句，把事情講清楚。
2. 必須保留：所有操作步驟、可複製的提示詞程式碼塊、命令、具體數位與限制、容易踩的坑、驗收標準、連結和出處。
3. 保留一級標題和所有二級標題的文字與順序；三級標題可合併。
4. 每段 2 到 4 句；多用列表、編號步驟和表格。
5. 每段只把一個最關鍵的句子或結論用 **加粗** 標出，不是每段都必須有，全文加粗不要濫用。
6. 不加 emoji、HTML 註釋、裝飾性標記，不寫前言或結束語。只輸出完整 Markdown，不要用程式碼圍欄包住全文。

{a}"""
r = subprocess.run(["agy", "--model", "gemini-3.8-flash-high", "--dangerously-skip-permissions", "--add-dir", os.path.dirname(SK), "--print-timeout", "900s", "-p", q], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=1000)
b = r.stdout.strip()
if b.startswith("```"):
    b = b.split("\n", 1)[1].rsplit("```", 1)[0]
b = b[b.find("# "):].strip() + "\n"
H = lambda x: re.findall(r"^## .*", x, re.M)
os.makedirs(os.path.dirname(f"out5/{path}.md"), exist_ok=True)
open(f"out5/{path}.md", "w").write(b)
print(path, len(a), len(b), H(a) == H(b), b.count("**") // 2, r.stderr[-300:])

import os
import json
import requests
from datetime import datetime

# ---------------------------
# Configuration
# ---------------------------
DEFAULT_SQLMAP_PATH = r"C:\sqlmap\sqlmap.py"   # Adjust if installed elsewhere
DEFAULT_SQLMAP_OPTS = "--batch --dbs --level=1 --risk=1 --threads=3 --disable-coloring"
LLM_URL = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"  # Model Runner endpoint
MODEL_NAME = "ai/gemma3n:latest"


# ---------------------------
# Ask the AI model
# ---------------------------
def ask_llm(context_text, timeout=60):
    system = (
        "You are a penetration testing assistant. Only suggest non-destructive "
        "enumeration commands for authorized testing (nmap scripts, curl, nikto, sqlmap "
        "with --dbs etc.). Do NOT generate exploit payloads or instructions that "
        "would enable unauthorized access. Always remind the operator to have written permission."
    )

    user = (
        f"Context:\n{context_text}\n\n"
        "Task: Rank the candidate URLs by likelihood of SQL injection and for each "
        "return a short justification and a safe suggested sqlmap command "
        "(enumeration only, e.g., use --dbs, --batch). Keep answers concise."
    )

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    }

    try:
        r = requests.post(LLM_URL, json=payload, verify=False, timeout=timeout)
        resp = r.json()
        if "choices" in resp:
            return resp["choices"][0]["message"]["content"]
        return json.dumps(resp, indent=2)
    except Exception as e:
        return f"Error contacting LLM: {str(e)}"


# ---------------------------
# Build sqlmap commands
# ---------------------------
def build_sqlmap_cmds(target_urls, sqlmap_path=DEFAULT_SQLMAP_PATH, opts=DEFAULT_SQLMAP_OPTS):
    cmds = []
    for u in target_urls:
        cmd = f'python "{sqlmap_path}" -u "{u}" {opts}'
        cmds.append(cmd)
    return cmds


# ---------------------------
# Generate Markdown report
# ---------------------------
def generate_report(target_urls, ai_suggestions, cmds, outfile="sqlmap_wrapper_report.md"):
    lines = []
    lines.append("# SQL Injection Testing Report\n")
    lines.append(f"Generated on: {datetime.now().isoformat()}\n")

    lines.append("\n## Target URLs\n")
    for u in target_urls:
        lines.append(f"- {u}")

    lines.append("\n## AI Suggestions\n")
    lines.append(ai_suggestions if ai_suggestions else "No suggestions from AI.\n")

    lines.append("\n## Generated sqlmap Commands\n")
    for c in cmds:
        lines.append(f"```\n{c}\n```")

    with open(outfile, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[+] Report written to {outfile}")


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    # Example URLs to test
    target_urls = [
        "http://testphp.vulnweb.com/listproducts.php?cat=1",
        "http://testasp.vulnweb.com/showproduct.asp?id=2"
    ]

    context = "List of target URLs for SQL injection assessment:\n" + "\n".join(target_urls)

    print("[*] Asking LLM for guidance...")
    ai_suggestions = ask_llm(context)

    print("[*] Building sqlmap commands...")
    cmds = build_sqlmap_cmds(target_urls)

    print("[*] Generating report...")
    generate_report(target_urls, ai_suggestions, cmds)

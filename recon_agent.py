import subprocess
import xmltodict
import requests
import json

target = "scanme.nmap.org"
subprocess.run(f"nmap -sV -T4 -oX scan_result.xml {target}", shell=True)


with open("scan_result.xml") as f:
    data = xmltodict.parse(f.read())

open_ports = []
hosts = data["nmaprun"]["host"]
if isinstance(hosts, dict):  
    hosts = [hosts]

for host in hosts:
    if "ports" not in host:
        continue
    ports_info = host["ports"].get("port", [])
    if isinstance(ports_info, dict):  
        ports_info = [ports_info]
    for p in ports_info:
        if p["state"]["@state"] == "open":
            open_ports.append({
                "port": p["@portid"],
                "service": p["service"]["@name"]
            })

url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"  

payload = {
    "model": "ai/gemma3n:latest", 
    "messages": [
        {
            "role": "system",
            "content": "You are a penetration testing assistant."
        },
        {
            "role": "user",
            "content": f"Here are the open ports from an Nmap scan: {open_ports}. "
                       "Suggest the next reconnaissance steps in 50 words. Explain to me like a begineer"
        }
    ]
}

response = requests.post(url, json=payload, verify=False)

print("Status Code:", response.status_code)
print("AI Response:", response.json())

import http.client
import sys
import time
import os
import json
from colorama import Fore, Style, init
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

init(autoreset=True)
console = Console()

# =========================
# SCI-FI INTRO ANIMATION
# =========================
banner = r"""
██╗███╗   ██╗███████╗████████╗ █████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║
██║██║ ╚████║███████║   ██║   ██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
"""
os.system("cls" if os.name == "nt" else "clear")
for line in banner.splitlines():
    print(Fore.CYAN + Style.BRIGHT + line)
    time.sleep(0.05)
console.print(
    Panel.fit(
        "[bold magenta]PRIVATE ID INTELLIGENCE[/bold magenta]\n"
        "[green]TARGET ACQUISITION SYSTEM INITIALIZED[/green]",
        border_style="bright_blue",
    )
)
time.sleep(1)

# =========================
# USERNAME INPUT FROM CLI
# =========================
if len(sys.argv) < 2:
    console.print(
        "\n[bold red]USAGE:[/bold red] python insta.py <username>\n"
    )
    sys.exit()
username = sys.argv[1]

# =========================
# LOADING EFFECT
# =========================
tasks = [
    "Connecting to Instagram Node...",
    "Bypassing Public Gateway...",
    "Fetching Intelligence...",
    "Decrypting Metadata...",
]
for task in tasks:
    console.print(f"[cyan][+][/cyan] {task}")
    time.sleep(0.8)
for _ in track(range(100), description="[magenta]Scanning Target..."):
    time.sleep(0.01)

# =========================
# API REQUEST
# =========================
conn = http.client.HTTPSConnection("flashapi1.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "a4c29ee9f4msh1c7fae178701483p1f16dejsn6dcd32252130",
    'x-rapidapi-host': "flashapi1.p.rapidapi.com",
    'Content-Type': "application/json"
}
endpoint = f"/ig/info_username/?user={username}&nocors=false"
conn.request("GET", endpoint, headers=headers)
res = conn.getresponse()
data = res.read()

# =========================
# OUTPUT - CHAINING RESULTS (NO TABLE)
# =========================
console.print(
    Panel.fit(
        f"[bold green]TARGET:[/bold green] {username}\n"
        f"[bold cyan]STATUS:[/bold cyan] DATA ACQUIRED",
        border_style="green",
    )
)

try:
    json_data = json.loads(data.decode("utf-8"))
    user = json_data.get("user", {})
    chaining = user.get("chaining_results", [])

    if chaining:
        console.print("\n[bold cyan]📎 CHAINING RESULTS (Suggested accounts)[/bold cyan]\n")
        for idx, acc in enumerate(chaining, start=1):
            username_acc = acc.get("username", "N/A")
            is_private = "🔒 Private" if acc.get("is_private") else "🌐 Public"
            is_verified = "✅ Verified" if acc.get("is_verified") else "❌ Not verified"
            pic_url = acc.get("profile_pic_url", "N/A")
            
            console.print(f"[bold yellow]{idx}.[/bold yellow] [bold green]@{username_acc}[/bold green]")
            console.print(f"   {is_private} | {is_verified}")
            console.print(f"   [blue]Profile Pic URL:[/blue] {pic_url}")
            console.print("   " + "-" * 60)
        console.print(f"\n[dim]Total: {len(chaining)} accounts found.[/dim]")
    else:
        console.print("[yellow]⚠ No chaining results found for this user.[/yellow]")

except json.JSONDecodeError:
    console.print("[red]❌ Failed to parse API response. Raw data:[/red]")
    print(Fore.YELLOW + data.decode("utf-8"))
except KeyError as e:
    console.print(f"[red]❌ Unexpected response structure. Missing key: {e}[/red]")

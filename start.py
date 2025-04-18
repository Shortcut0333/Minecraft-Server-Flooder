import subprocess
import dns.resolver
from termcolor import colored
from colorama import init

init()

def resolve_minecraft_srv(domain):
    try:
        answers = dns.resolver.resolve(f'_minecraft._tcp.{domain}', 'SRV')
        for rdata in answers:
            return str(rdata.target).rstrip('.'), rdata.port
    except Exception:
        return domain, 25565

def print_banner():
    print(colored(r"""
   __ _                _             _    ___ _______________ 
  / _\ |__   ___  _ __| |_ ___ _   _| |_ / _ \___ /___ /___ / 
  \ \| '_ \ / _ \| '__| __/ __| | | | __| | | ||_ \ |_ \ |_ \ 
  _\ \ | | | (_) | |  | || (__| |_| | |_| |_| |__) |__) |__) |
  \__/_| |_|\___/|_|   \__\___|\__,_|\__|\___/____/____/____/
    """, "cyan"))

def start_bot_army(bot_count):
    """Start the bot army by running the PowerShell script with the bot count"""
    print(f"[Python] Starting {bot_count} bots...")

    try:
        
        subprocess.Popen(["powershell", "-ExecutionPolicy", "Bypass", "-File", "w.ps1", str(bot_count)])
        print("[Python] PowerShell script (w.ps1) is running...")

    except Exception as e:
        print(f"[Python] Error: {e}")

def main():
    print_banner()
    print(colored("[INPUT] Enter Minecraft server domain (e.g., minecraftserver.fun):", "yellow"))
    domain = input(colored(">> ", "green")).strip()

    print(colored(f"[LOOKUP] Resolving SRV for {domain}...", "blue"))
    ip, port = resolve_minecraft_srv(domain)
    print(colored(f"[RESOLVED] {domain} -> {ip}:{port}", "magenta"))

    # the amount of bots to spawn
    print(colored("[INPUT] Enter the number of bots to join the server:", "yellow"))
    try:
        bot_count = int(input(colored(">> ", "green")).strip())
        if bot_count <= 0:
            raise ValueError("Bot count must be a positive number.")
    except ValueError as e:
        print(colored(f"[ERROR] Invalid input: {e}", "red"))
        return

    print(colored("[LAUNCH] Starting bot control system...", "cyan"))
    
    
    start_bot_army(bot_count)

if __name__ == "__main__":
    main()
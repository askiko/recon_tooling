#!/usr/bin/env python3
#author -Askiko
import re, sys, subprocess
from pyfiglet import figlet_format
from colorama import Fore, Style, init

init()

def print_banner():
    print(Fore.YELLOW + figlet_format("AskikoHunter", font="slant"))
    print(Fore.RED + "Author:  Asbel Kosgei")
    print(Fore.RED + "Github:  github.com/askiko")
    print(Fore.GREEN + "Version: 2.1\n")

if __name__ == "__main__":
    print_banner()

def subdomain_enum(domain):
    try:
        result = subprocess.run(["subfinder", "-d", domain],
                                capture_output=True,
                                text=True
                                )
        global subdomains
        subdomains = result.stdout.splitlines()
        return subdomains
    except Exception as e:
        print(str(e))

subdomains = []

domain = input("Enter domain to hunt: ")

if domain:
    print("Enumerating subdomains.... 1...2...3...\n")
    subdomain_enum(domain)
else:
    print("No domain entered. Exiting...")
    sys.exit(1)

def filter_subdomains(subdomains, banned_words):
    pattern = re.compile(
            r"(" + "|".join(re.escape(word) for word in banned_words) + r")",
            re.IGNORECASE
            )
    total=0
    removed=0
    kept=0

    global filtered

    for line in subdomains:
        domain=line.strip()
        
        if not domain:
            continue
        total+=1

        if pattern.search(domain):
            removed+=1
            continue
        else:
            filtered.append(domain)
            kept+=1
    print("____Filtering Complete____")
    print(f"Total domains read: {total}")
    print(f"Domains removed: {removed}")
    print(f"Domains kept: {kept}\n")
    return filtered
filtered = []
banned_words = []
with open("banned_words.txt", "r") as infile:
    for l in infile:
        banned_words.append(l.strip())
print("Filtering subdomains.... 1...2...3...4...")
filter_subdomains(subdomains, banned_words)

def domain_checker(domain):
    try:
        result = subprocess.run(["curl", "-o", "/dev/null", "-s", "-w", "%{http_code}", "-m", "5", f"https://{domain}"],
                                capture_output=True,
                                text=True
                                )

        status_code = result.stdout.strip()

        if status_code.startswith("2") or status_code.startswith("3") or status_code == "403" or status_code == "401":
            return True, status_code
        else:
            return False, status_code
    except Exception as e:
        return False, None

print("Scanning hosts.... 1...2...3...4...5...")
with open("live_hosts.txt", "w") as outfile:
    for domain in filtered:
        is_up, code = domain_checker(domain)

        if is_up:
            print(f"[+] {domain} is UP (HTTP {code})\n")
            outfile.write(domain + "\n")
        else:
            print(f"[-] {domain} is DOWN or unreachable (HTTP {code})\n")


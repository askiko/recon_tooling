# Recon Automation Tool

Containerized reconnaissance automation framework for attack surface discovery, scope-aware filtering, and live-host validation.

---

## Overview

This project automates several stages of the reconnaissance workflow commonly used in security assessments and bug bounty engagements.<br/>
The application is written in Python and distributed as a Docker container for portability and simplified deployment.

---

## Features

- Automated subdomain enumeration
- Scope-aware filtering
- Out-of-scope subdomain exclusion
- HTTP and HTTPS probing
- Live host detection
- Status code reporting
- Export of responsive hosts to file
- Dockerized deployment
- Modular Python architecture
- Streamlined CLI workflow

---

## Architecture

```text
                ┌──────────────────┐
                │  Target Domain   │
                └────────┬─────────┘
                         │
                         ▼
               ┌──────────────────────┐
               │ Subdomain Enumeration│
               └────────┬─────────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │ Scope Validation     │
             └────────┬─────────────┘
                      │
                      ▼
             ┌──────────────────────┐
             │ Out-of-Scope Filter  │
             └────────┬─────────────┘
                      │
                      ▼
             ┌──────────────────────┐
             │ HTTP/HTTPS Probing   │
             └────────┬─────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
┌─────────────────┐    ┌────────────────────┐
│ Status Reporting│    │ Live Host Export   │
└─────────────────┘    └────────────────────┘
```

---

## Quick Start

### Pull the Docker Image

```bash
docker pull askiko/askikohunter:v2
```
---

## Example Usage

Create a file named banned.txt with a list of out of scope subdomains.<br/>
Run the command below and then type target domain to the prompt.

```bash
docker run --rm -it --network host -v "${PWD}:/app" askiko/askikohunter:v2
```
After it finishes, a file named live_hosts.txt will be created with a list of reachable subdomains

---

## Example Output

```text
[+] docs.google.com is UP (HTTP 200)
[+] drive.google.com is UP (HTTP 302)
[-] admin.google.com is DOWN or unreachable (HTTP 000)

```

---

## Methodology

The reconnaissance workflow follows these stages:

1. Enumerate subdomains from configured sources
2. Use RegEx to validate scope definitions
3. Filter out out-of-scope assets
4. Probe HTTP/HTTPS services
5. Extract responsive hosts
6. Export live hosts for downstream operations

---

## Technologies Used

- Python
- Docker
- asyncio
- requests
- curl
- subfinder
- Regex
- argparse
- Linux networking utilities

---

## Docker Deployment

The project is distributed as a portable Docker container to ensure:

- Consistent runtime behavior
- Simplified installation
- Dependency isolation
- Cross-platform deployment
- Reproducible execution environments

---

## Screenshots

### Terminal Workflow

<p align="center">
Enter your target domain to the prompt: <br/>
<img src="https://raw.githubusercontent.com/askiko/recon_tooling/main/screenShots/enterDomain.png" height="80%" width="80%" alt="Enumeration output"/>
<br />
<br />
Wait for enumeration and probing: <br/>
<img src="https://raw.githubusercontent.com/askiko/recon_tooling/main/screenShots/probingHosts.png" height="80%" width="80%" alt="Enumeration output"/>

</p>

---

## Disclaimer

This project is intended for authorized security testing and educational purposes only.

Users are responsible for complying with all applicable laws and obtaining proper authorization before testing any systems or domains.

---

## Author

Asbel Kosgei

---

## License

This project is licensed under the MIT License.

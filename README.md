# 🔐 SSH Log Analyzer — Incident Investigation Tool

**Cyber Security Capstone | Project 2 of 5**
**Program:** LaunchED Global — Cyber Security Internship

---

## 📌 Project Overview

This project performs a forensic investigation of a Linux server that was compromised via an SSH brute-force attack. Using `auth.log` and binary `wtmp` logs, the tool reconstructs the full attack timeline and identifies all post-compromise actions.

**Target System:** `ip-172-31-35-28` (AWS EC2 — Ubuntu Linux)
**Log Period:** January 25, 2024 – March 6, 2024

---

## 🔍 What This Tool Detects

| Detection | Description |
|-----------|-------------|
| ✅ Successful SSH logins | Shows user, source IP, timestamp |
| ❌ Failed login attempts | Grouped by IP and username |
| 🔴 Brute-force attacks | IPs with 10+ failed attempts flagged automatically |
| 👤 New user accounts | Created accounts that may be backdoors |
| ⬆️ Privilege escalation | `usermod` events adding users to `sudo`/`shadow` groups |
| 💻 Sensitive sudo commands | `/etc/shadow` reads, `curl`/`wget` downloads, etc. |
| 🚨 IoC extraction | Auto-generates Indicators of Compromise |

---

## 📁 Project Structure

```
ssh-log-analyzer/
│
├── analyzer.py          # Main log analysis script
├── scripts/
│   └── utmp.py          # Binary wtmp/utmp parser
├── logs/
│   └── auth.log         # Sample auth.log (from investigation)
├── output/              # Reports saved here
├── requirements.txt     # No external dependencies (stdlib only)
└── README.md
```

---

## 🚀 Usage

### 1. Analyze an auth.log file

```bash
python3 analyzer.py logs/auth.log
```

### 2. Save report to a file

```bash
python3 analyzer.py logs/auth.log --output output/report.txt
```

### 3. Customize brute-force threshold

```bash
python3 analyzer.py logs/auth.log --brute-threshold 5
```

### 4. Parse binary wtmp file

```bash
python3 scripts/utmp.py /var/log/wtmp
python3 scripts/utmp.py /var/log/wtmp -o output/wtmp_parsed.tsv
```

---

## 🧪 Sample Output

```
████████████████████████████████████████████████████████████
  SSH LOG ANALYSIS — INCIDENT INVESTIGATION REPORT
  Cyber Security Capstone | Project 2 | LaunchED Global
████████████████████████████████████████████████████████████

════════════════════════════════════════════════════════════
  1. SUCCESSFUL SSH LOGINS
════════════════════════════════════════════════════════════
  Timestamp              Username        Source IP
  -------------------------------------------------------
  Mar  6 06:19:54        root            203.101.190.9
  Mar  6 06:31:40        root            65.2.161.68      ← ATTACKER
  Mar  6 06:37:34        cyberjunkie     65.2.161.68      ← BACKDOOR

════════════════════════════════════════════════════════════
  4. BRUTE-FORCE ATTACK DETECTION
════════════════════════════════════════════════════════════
  [CRITICAL] 65.2.161.68 — 20 failed attempts (automated attack suspected)

════════════════════════════════════════════════════════════
  8. INDICATORS OF COMPROMISE (IoCs)
════════════════════════════════════════════════════════════
  Type  : IP Address
  Value : 65.2.161.68
  Note  : Brute-force source — 20 failed attempts

  Type  : Username
  Value : cyberjunkie
  Note  : New user created at Mar  6 06:34:18 (UID=1002) — possible backdoor

  Type  : Suspicious Command
  Value : /usr/bin/cat /etc/shadow
  Note  : Executed by cyberjunkie at Mar  6 06:37:57
```

---

## 🔎 Investigation Findings

### Attack Summary (March 6, 2024)

| Time | Event |
|------|-------|
| 06:17:15 | Server reboots (kernel 6.2.0-1018-aws) |
| 06:19:54 | Legitimate root login from `203.101.190.9` |
| 06:31:31 | **BRUTE FORCE BEGINS** — `65.2.161.68` fires 130+ attempts in seconds |
| 06:31:40 | **ROOT COMPROMISED** — attacker logs in as root |
| 06:34:18 | Backdoor account `cyberjunkie` (UID=1002) created |
| 06:35:15 | `cyberjunkie` added to `sudo` group |
| 06:37:34 | Attacker reconnects as `cyberjunkie` |
| 06:37:57 | `/etc/shadow` read — **credential harvesting** |
| 06:39:38 | `linper.sh` downloaded — **persistence toolkit deployed** |

---

## 🛡️ Indicators of Compromise (IoCs)

| Type | Value | Description |
|------|-------|-------------|
| IP Address | `65.2.161.68` | Attacker IP — brute-force & post-exploitation |
| Username | `cyberjunkie` | Backdoor account (UID=1002) |
| File | `/etc/shadow` | Credential harvesting target |
| URL | `github.com/montysecurity/linper` | Persistence toolkit |
| Group | `sudo`, `shadow` | Attacker-granted privilege escalation |

---

## 🔧 Hardening Recommendations

- ❌ **Disable SSH password auth** — enforce public key only
- 🚫 **Disable root SSH login** (`PermitRootLogin no` in sshd_config)
- 🔒 **Deploy fail2ban** to auto-block brute-force IPs
- 🌐 **Restrict SSH via AWS Security Groups** to known IPs only
- 👁️ **Enable CloudTrail + VPC Flow Logs** for AWS-level visibility
- 📋 **Audit /etc/passwd regularly** for unauthorized accounts

---

## 📚 Tools & Techniques Used

- `grep`, `awk`, `sort`, `uniq` — Linux command-line log parsing
- `last`, `lastb` — Login history from wtmp
- `utmp.py` — Custom binary wtmp/utmp parser (Python struct)
- Python 3 — No external dependencies required

---

## 👤 Author

**Cyber Security Internship — LaunchED Global**
Project 2 of 5 | Focus: Authentication Log Analysis & Intrusion Detection

---

## ⚠️ Disclaimer

This project is for educational purposes only. All log files are from a controlled lab environment. Do not use these tools against systems you do not own or have explicit permission to test.

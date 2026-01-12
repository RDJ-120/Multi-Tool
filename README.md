# 🛠️ Multi-Tool Cyber Security Script

A multi-purpose tool written in **Python** that contains several utilities related to  
**Cyber Security & Penetration Testing** (for educational purposes only).

---

## ⚙️ Features

This tool includes multiple modules such as:

### 📧 Email Tool
- Send emails using multiple accounts
- Supports multi-threading
- Uses environment variables to store passwords securely

### 🌐 DoS Testing Tool
- Sends repeated requests to test server load tolerance
- Random User-Agent rotation
- Multi-threaded requests

### 🔎 Sub-Paths / Sub-Domains Scanner
- Scans for hidden paths such as:
  - admin
  - login
  - config
  - backup
  - api
- Supports custom or default wordlists
- Uses ThreadPoolExecutor for faster scanning

### 🔐 Hash Tools
- Generate hashes:
  - MD5
  - SHA1
  - SHA256
  - SHA512
  - SHA3_512
- Identify and compare hash types

### ☠️ Jack The Reaper (Hash Cracker)
- Crack hashes using wordlists
- Salt support
- Auto-detect hash type based on length
- Calculates cracking speed and elapsed time

---

## 📦 Requirements

Install required packages:

```bash
pip install rich requests user-agent prompt_toolkit

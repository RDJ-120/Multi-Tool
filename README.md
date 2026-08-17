# Multi-Tool Cybersecurity & Utilities Suite

A modular, multi-threaded security testing and operational automation toolkit built in Python. Designed for system diagnostics, stress testing, hash analysis, and directory reconnaissance within controlled environments.

## Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/4553174e-fb26-4f44-9604-8ff4f86f1af9" alt="Multi-Tool Interface Preview" width="100%">
</p>

## Core Modules

* **Reconnaissance & Path Enumeration:** Concurrent web application directory scanner targeting exposed administrative panels, configuration files, and API endpoints using configurable wordlists.
* **Hash Processing & Analysis ("Jack The Reaper"):** Dynamic hash identifier, salt-aware cracker, and generator supporting MD5, SHA-1, SHA-256, SHA-512, and SHA3-512 with real-time throughput metrics.
* **Network Stress Testing:** Multi-threaded HTTP load testing module featuring dynamic User-Agent rotation for evaluating web server resilience under traffic bursts.
* **Automated SMTP Operations:** Threaded bulk email dispatcher supporting dynamic server authentication through secure environment variable isolation.

## Prerequisites

* Python 3.8+
* Third-party libraries: `rich`, `requests`, `user-agent`, `prompt_toolkit`

Install execution dependencies:

```bash
pip install -r requirements.txt
```

## Installation

Clone the repository and access the directory:

```bash
git clone https://github.com/RDJ-120/Multi-Tool.git
cd Multi-Tool
```

## Usage

Launch the main interactive CLI interface:

```bash
python main.py
```

Select the corresponding numerical option from the main menu to initiate specific operational modules.

## Disclaimer

This software is strictly intended for educational testing, authorized penetration testing, and internal infrastructure analysis. Unauthorized execution against third-party systems without prior explicit consent is strictly prohibited.

## License

Distributed under the MIT License. See `LICENSE` for details.

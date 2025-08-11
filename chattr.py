#!/usr/bin/env python3
import os
import time
import threading
from datetime import datetime

CHAT_FILE = "/tmp/chattr.txt"

USERNAME = "Anonymous"
STOP_EVENT = None
VERSION = "1.0.1"
USERNAME_COLOR = "\x1b[0m"
INPUT_COLOR = "\x1b[92m"
SYSTEM_MESSAGES = True

if not os.path.exists(CHAT_FILE):
    open(CHAT_FILE, "w").close()

def boolToString(bool):
    if bool:
        return "T"
    else:
        return "F"

def clear_terminal():
    """
    Clears the terminal screen based on the operating system.
    """
    # Check if the operating system is Windows ('nt') or Unix-like ('posix')
    if os.name == 'nt':
        _ = os.system('cls')  # Command for Windows
    else:
        _ = os.system('clear') # Command for Linux/macOS

def read_messages(se):
    with open(CHAT_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        while not se.is_set():
            line = f.readline()
            if line:
                if not SYSTEM_MESSAGES:
                    if line.startswith("-=-=") and line.rstrip().endswith("=-=-"):
                        continue
                
                if line.startswith("-=-=") and line.rstrip().endswith("=-=-"):
                    print(f"{INPUT_COLOR}{line.strip()}\n{INPUT_COLOR}> \x1b[0m", end="", flush=True)
                else:
                    print(f"\r{line.strip()}\n{INPUT_COLOR}> \x1b[0m", end="", flush=True)
            else:
                time.sleep(0.1)


def start():

    valid_options = {"0", "1", "2", "3"}

    option = ""
    while True:
        clear_terminal()
        header()
        user_input = input(
            "\x1b[31m[0]Chat         "
            "\x1b[34m[1]Settings\n"
            "\x1b[32m[2]Changelog    "
            "\x1b[33m[3]Quit\n"
            "\x1b[0m"
        )
        if user_input in valid_options:
            option = user_input
            break
    if option == "0":
        chat()
    if option == "1":
        settings()
    if option == "2":
        changelog()
    if option == "3":
        return
    
def changelog():
    clear_terminal()
    header()
    #For version number: \x1b[91m
    #For additions: \x1b[32m
    #For fixes: \x1b[38;5;208m
    print(
        "\x1b[91mV1.0.1:\n"
        "\x1b[32m   Added a settings menu\n"
        "\x1b[32m   Added customizations for the user\n"
        "\x1b[32m   Added customizations for the chat\n"
        "\x1b[38;5;208m   Fixed a bug where the input '>' only got colored the first time\n"
    )
    print("\x1b[0m Press enter to return to the menu...")
    input()
    start()

def settings():
    valid_options = {"0", "1", "2"}

    option = ""
    while True:
        clear_terminal()
        header()
        user_input = input(
            "\x1b[31m[0]User         "
            "\x1b[34m[1]Appearance\n"
            "\x1b[32m[2]Return\n"
            "\x1b[0m"
        )
        if user_input in valid_options:
            option = user_input
            break
    if option == "0":
        user()  
    if option == "1":
        appearance()
    if option == "2":
        start()
    
def appearance():
    valid_options = {"0", "1", "2", "3"}
    global INPUT_COLOR, SYSTEM_MESSAGES

    option = ""
    while True:
        clear_terminal()
        header()
        user_input = input(
            f"\x1b[31m[0]System Messages({boolToString(SYSTEM_MESSAGES)}) "
            "\x1b[34m[1]Secondary Color\n"
            "\x1b[32m[2]Return\n"
            "\x1b[0m"
        )
        if user_input in valid_options:
            option = user_input
            break

    if option == "0":
        clear_terminal()
        header()
        SYSTEM_MESSAGES = not SYSTEM_MESSAGES
        appearance()

    elif option == "1":
        clear_terminal()
        header()
        print("Choose a secondary color:\n")
        colors = {
            "0": ("\x1b[91m", "Red"),
            "1": ("\x1b[92m", "Green"),
            "2": ("\x1b[93m", "Yellow"),
            "3": ("\x1b[94m", "Blue"),
            "4": ("\x1b[95m", "Magenta"),
            "5": ("\x1b[96m", "Cyan"),
            "6": ("\x1b[0m", "Default/Reset")
        }
        for k, v in colors.items():
            print(f"{v[0]}[{k}] {v[1]}")

        choice = input("\nEnter choice: ").strip()
        if choice in colors:
            INPUT_COLOR = colors[choice][0]
            print(f"Secondary color changed to {colors[choice][1]}.\n")
        else:
            print("Invalid choice, color not changed.\n")
        appearance()
    elif option == "2":
        settings()

def user():
    global USERNAME, USERNAME_COLOR

    valid_options = {"0", "1", "2", "3"}

    option = ""
    while True:
        clear_terminal()
        header()
        user_input = input(
            "\x1b[31m[0]Username         "
            "\x1b[34m[1]Change Color\n"
            "\x1b[32m[2]Return\n"
            "\x1b[0m"
        )
        if user_input in valid_options:
            option = user_input
            break

    if option == "0":
        clear_terminal()
        header()
        USERNAME = input(f"\x1b[0mEnter a username (or press enter to remain '{USERNAME}'): ").strip() or USERNAME
        user()

    elif option == "1":
        clear_terminal()
        header()
        print("Choose a username color:\n")
        colors = {
            "0": ("\x1b[91m", "Red"),
            "1": ("\x1b[92m", "Green"),
            "2": ("\x1b[93m", "Yellow"),
            "3": ("\x1b[94m", "Blue"),
            "4": ("\x1b[95m", "Magenta"),
            "5": ("\x1b[96m", "Cyan"),
            "6": ("\x1b[0m", "Default/Reset")
        }
        for k, v in colors.items():
            print(f"{v[0]}[{k}] {v[1]}")

        choice = input("\nEnter choice: ").strip()
        if choice in colors:
            USERNAME_COLOR = colors[choice][0]
            print(f"Username color changed to {colors[choice][1]}.\n")
        else:
            print("Invalid choice, color not changed.\n")
        user()
    elif option == "2":
        settings()



def chat():
    clear_terminal()
    header()
    global stop_event
    stop_event = threading.Event()

    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(CHAT_FILE, "a") as f:
        f.write(f"-=-={USERNAME} connected=-=-\n")

    print("Type /leave to exit.\n")

    threading.Thread(target=read_messages, args=(stop_event,), daemon=True).start()

    while True:
        try:
            msg = input(f"{INPUT_COLOR}> \x1b[0m").strip()
            if msg.lower() == "/leave":
                timestamp = datetime.now().strftime("%H:%M:%S")
                with open(CHAT_FILE, "a") as f:
                    f.write(f"-=-={USERNAME} disconnected=-=-\n")

                # Signal the read_messages thread to stop
                stop_event.set()

                start()
                break  # break to exit the while loop after start()
            timestamp = datetime.now().strftime("%H:%M:%S")
            with open(CHAT_FILE, "a") as f:
                f.write(f"[{timestamp}] {USERNAME_COLOR}{USERNAME}\x1b[0m: {msg}\n")
        except (KeyboardInterrupt, EOFError):
            stop_event.set()
            break

def header():
    print("""\x1b[92m
     ▄████▄   ██░ ██  ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ██▀███        ██▓███ ▓██   ██▓
    ▒██▀ ▀█  ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▓██ ▒ ██▒     ▓██░  ██▒▒██  ██▒
    ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▓██ ░▄█ ▒     ▓██░ ██▓▒ ▒██ ██░
    ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ▒██▀▀█▄       ▒██▄█▓▒ ▒ ░ ▐██▓░
    ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░ ░██▓ ▒██▒ ██▓ ▒██▒ ░  ░ ░ ██▒▓░
    ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▓▒ ▒▓▒░ ░  ░  ██▒▒▒ 
      ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░   ░        ░      ░▒ ░ ▒░ ░▒  ░▒ ░     ▓██ ░▒░ 
    ░         ░  ░░ ░  ░   ▒    ░        ░        ░░   ░  ░   ░░       ▒ ▒ ░░  
    ░ ░       ░  ░  ░      ░  ░                    ░       ░           ░ ░     
    ░                                                      ░           ░ ░     
    """)
    print(f"\x1b[35mchattr v{VERSION}\x1b[0m" \
    "")

start()

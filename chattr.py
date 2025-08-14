#!/usr/bin/env python3
import os
import time
import threading
from datetime import datetime

DEFAULT_CHAT_FILE = "/tmp/chattr/chattr.txt"
CHAT_FILE = DEFAULT_CHAT_FILE
FILE_PATH ="chattr"
STOP_EVENT = None
VERSION = "1.4.0"

USERNAME = "Guest"
anon = False
USERNAME_COLOR = "\x1b[0m"
INPUT_COLOR = "\x1b[92m"
SYSTEM_MESSAGES = True

os.makedirs(os.path.dirname(CHAT_FILE), exist_ok=True)

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
        "\x1b[91mV1.4.0\n"
        "\x1b[38;5;208m   Changed channels that start with \".\" from hidden channels to password protected channels\n"
        "\x1b[38;5;208m   Changed default username from \"Anonymous\" to \"Guest\"\n"
        "\n"
        "\x1b[91mV1.3.1\n"
        "\x1b[38;5;208m   Fixed a bug where certain python versions couldn't run the program\n"
        "\n"
        "\x1b[91mV1.3.0\n"
        "\x1b[32m   Made /lv a shorthand for /leave\n"
        "\x1b[32m   Added the /help (/h) command\n"
        "\x1b[32m   Added the /channel (/ch) command\n"
        "\x1b[32m   Added the /remove (/rm) command\n"
        "\x1b[32m   Added the /name (/n) command\n"
        "\x1b[32m   Added the /list (/ls) command\n"
        "\x1b[32m   Added the /clear (/cl) command\n"
        "\x1b[32m   Added the /anonymous (/a) command\n"
        "\x1b[32m   Added the /secret (/s) command\n"
        "\n"
        "\x1b[91mV1.2.0\n"
        "\x1b[32m   Added the ability to save/load user profiles\n"
        "\n"
        "\x1b[91mV1.1.0:\n"
        "\x1b[32m   Added a settings menu\n"
        "\x1b[32m   Added customizations for the user\n"
        "\x1b[32m   Added customizations for the chat\n"
        "\x1b[38;5;208m   Fixed a bug where the input '>' only got colored the first time\n"
    )
    print("\x1b[0m Press enter to return to the menu...")
    input()
    start()

def settings():
    valid_options = {"0", "1", "2", "3"}

    option = ""
    while True:
        clear_terminal()
        header()
        user_input = input(
            "\x1b[31m[0]User         "
            "\x1b[34m[1]Appearance\n"
            "\x1b[32m[2]Save/Load    "
            "\x1b[33m[3]Return\n"
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
        saveload()
    if option == "3":
        start()
    
def saveload():

    valid_options = {"0", "1", "2"}

    option = ""
    while True:
        clear_terminal()
        header()
        user_input = input(
            "\x1b[31m[0]Save         "
            "\x1b[34m[1]Load\n"
            "\x1b[32m[2]Return\n"
            "\x1b[0m"
        )
        if user_input in valid_options:
            option = user_input
            break
    if option == "0":
        write_settings()
    if option == "1":
        load_settings()
    if option == "2":
        settings()

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
    global stop_event, anon, CHAT_FILE, DEFAULT_CHAT_FILE
    stop_event = threading.Event()

    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(CHAT_FILE, "a") as f:
        f.write(f"-=-={USERNAME} connected=-=-\n")

    print("Type /h or /help to list commands.\n")

    threading.Thread(target=read_messages, args=(stop_event,), daemon=True).start()

    while True:
        try:
            msg = input(f"{INPUT_COLOR}> \x1b[0m").strip()
            if msg.lower() == "/leave" or msg.lower() == "/lv":
                timestamp = datetime.now().strftime("%H:%M:%S")
                with open(CHAT_FILE, "a") as f:
                    f.write(f"-=-={USERNAME} disconnected=-=-\n")

                stop_event.set()

                start()
                break
            elif msg.lower() == "/help" or msg.lower() == "/h":
                print(
                    f"{INPUT_COLOR}/h /help - Lists all commands\n"
                    f"{INPUT_COLOR}/lv /leave - Disconnect from the chat\n"
                    f"{INPUT_COLOR}/ch /channel - Create or Join a channel (Leave arguments blank to join main channel)\n"
                    f"{INPUT_COLOR}/rm /remove - Delete the current channel (Cannot use in the main channel)\n"
                    f"{INPUT_COLOR}/n /name - Tell what channel you are currently in\n"
                    f"{INPUT_COLOR}/ls /list - list all open channels\n"
                    f"{INPUT_COLOR}/cl /clear - Clear the chat (User end)\n"
                    f"{INPUT_COLOR}/a /anonymous - Toggle anonymous mode\n\x1b[0m"
                    )
            elif msg.lower().startswith("/channel") or msg.lower().startswith("/ch"):
                channel_name = msg.split(maxsplit=1)[1].strip() if len(msg.split(maxsplit=1)) > 1 else "chattr"
                channel_name = channel_name.replace(" ", "-")

                if channel_name.lower() == "main":
                    channel_name = "chattr"

                if channel_name.startswith("."):
                    password = ""
                    if not os.path.exists(f"/tmp/chattr/{channel_name}.txt"):
                        password = input(f"{INPUT_COLOR}Enter Password to be used: \x1b[0m")
                        CHAT_FILE = f"/tmp/chattr/{channel_name}.txt"
                        with open(CHAT_FILE, "w") as f:
                            f.write(password + "\n")
                        stop_event.set()
                        stop_event = threading.Event()
                        threading.Thread(target=read_messages, args=(stop_event,), daemon=True).start()
                        print(f"{INPUT_COLOR}Joined channel {channel_name}\n\x1b[0m")
                    else:
                        password = input(f"{INPUT_COLOR}Enter Password: \x1b[0m")
                        with open(f"/tmp/chattr/{channel_name}.txt", "r") as f:
                            stored_password = f.readline().strip('\n')
                        if password == stored_password:
                            CHAT_FILE = f"/tmp/chattr/{channel_name}.txt"
                            stop_event.set()
                            stop_event = threading.Event()
                            threading.Thread(target=read_messages, args=(stop_event,), daemon=True).start()
                            if channel_name == "chattr":
                                print(f"{INPUT_COLOR}Joined main channel\n\x1b[0m")
                            else:
                                print(f"{INPUT_COLOR}Joined channel {channel_name}\n\x1b[0m")
                        else:
                            print(f"{INPUT_COLOR}Incorrect Password")

                else:
                    CHAT_FILE = f"/tmp/chattr/{channel_name}.txt"

                    if not os.path.exists(CHAT_FILE):
                        open(CHAT_FILE, "w").close()

                    stop_event.set()
                    stop_event = threading.Event()
                    threading.Thread(target=read_messages, args=(stop_event,), daemon=True).start()
                    if channel_name == "chattr":
                        print(f"{INPUT_COLOR}Joined main channel\n\x1b[0m")
                    else:
                        print(f"{INPUT_COLOR}Joined channel {channel_name}\n\x1b[0m")
            elif msg.lower() == "/name" or msg.lower() == "/n":
                channel_name = CHAT_FILE.removeprefix("/tmp/chattr/").removesuffix('.txt')
                if channel_name == "chattr":
                    channel_name = "Main"
                print(f"{INPUT_COLOR}Current Channel is: {channel_name}\n\x1b[0m")
            elif msg.lower() == "/clear" or msg.lower() == "/cl":
                clear_terminal()
                header()
                print("Type /h or /help to list commands.\n")
            elif msg.lower() == "/list" or msg.lower() == "/ls":
                channels = [f for f in os.listdir("/tmp/chattr") if f.endswith('.txt')]
                for channel in channels:
                    if channel == "chattr.txt":
                        print(f"{INPUT_COLOR}Main ")
                    else:
                        print(f"{INPUT_COLOR}{channel.removesuffix('.txt')} ")
            elif msg.lower() == "/anonymous" or msg.lower() == "/a":
                anon = not anon
                print(f"{INPUT_COLOR}Toggled anonymous mode\n")
            elif msg.lower() == "/remove" or msg.lower() == "/rm":
                channel_name = CHAT_FILE.removeprefix("/tmp/chattr/").removesuffix('.txt')
                if channel_name == "chattr":
                    print(f"{INPUT_COLOR}You cannot remove the main channel")
                else:
                    file_to_remove = CHAT_FILE
                    CHAT_FILE = DEFAULT_CHAT_FILE

                    stop_event.set()
                    stop_event = threading.Event()
                    threading.Thread(target=read_messages, args=(stop_event,), daemon=True).start()
                    try:
                        os.remove(file_to_remove)
                        print(f"Room removed successfully.")
                    except FileNotFoundError:
                        print(f"This should never run")
                    except Exception as e:
                        print(f"An error occurred: {e}")
            else:
                timestamp = datetime.now().strftime("%H:%M:%S")
                with open(CHAT_FILE, "a") as f:
                    if anon:
                        f.write(msg + "\n")
                    else:
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

def write_settings():
    global USERNAME, USERNAME_COLOR, INPUT_COLOR, SYSTEM_MESSAGES, FILE_PATH
    clear_terminal()
    header()

    name = input(f"\x1b[92mWhat would you like to save the profile as?\n{INPUT_COLOR}> \x1b[0m").replace(" ", "-")

    file_name = f"{name}.pf"

    file_path = f"{FILE_PATH}/{file_name}"

    os.makedirs(FILE_PATH, exist_ok=True)

    try:
        with open(file_path, "x") as f:
            f.write(
                f"{USERNAME}\n"
                f"{USERNAME_COLOR}\n"
                f"{INPUT_COLOR}\n"
                f"{SYSTEM_MESSAGES}\n"
            )
    except FileExistsError:
        with open(file_path, "w") as f:
            f.write(
                f"{USERNAME}\n"
                f"{USERNAME_COLOR}\n"
                f"{INPUT_COLOR}\n"
                f"{SYSTEM_MESSAGES}\n"
            )

    saveload()

def load_settings():
    global USERNAME, USERNAME_COLOR, INPUT_COLOR, SYSTEM_MESSAGES, FILE_PATH
    clear_terminal()
    header()

    os.makedirs(FILE_PATH, exist_ok=True)

    profiles = [f for f in os.listdir(FILE_PATH) if f.endswith(".pf")]
    if not profiles:
        print("No profiles found.")
        input("Press enter to return...")
        saveload()
        return

    print("Available profiles:")
    for idx, profile in enumerate(profiles):
        print(f"\x1b[94m[{idx}] {profile}")

    inp = int(input(f"\x1b[92mWhich profile would you like to load (put the number)?\n{INPUT_COLOR}> \x1b[0m"))
    
    if inp < 0 or inp >= len(profiles):
        load_settings()
        return

    file_name = f"{FILE_PATH}/{profiles[inp]}"
    with open(file_name, "r") as f:
        lines = f.readlines()
        if len(lines) >= 4:
            USERNAME = lines[0].strip()
            USERNAME_COLOR = lines[1].strip()
            INPUT_COLOR = lines[2].strip()
            SYSTEM_MESSAGES = lines[3].strip() == "True"

    print("\x1b[92mProfile loaded.")
    input("Press enter to return...\x1b[0m")
    start()

start()

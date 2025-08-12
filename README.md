# Chattr

`chattr` is a simple terminal-based chat application written in Python that allows multiple users to communicate in real-time via a shared text file.

## Features

- **Real-time Chat**: Messages are instantly shared between connected users via a shared file.
- **Customizable Appearance**:
  - Change your username and username color.
  - Change the secondary input color.
  - Toggle system messages on or off.
- **Channel System**:
  - Create or join custom channels.
  - List active channels.
  - Remove non-main channels.
  - See which channel you're currently in.
- **Anonymous Mode**: Option to hide your username when sending messages.
- **Settings Menu**: Modify chat and user settings directly in the application.
- **Profiles**: Save/Load user profiles so you don't need to manually change your preferences every time.
- **Changelog**: View updates and fixes for each version.
- **Clear Terminal UI**: Simple and clean interface with ASCII art header.

## Requirements

- Python 3.x
- A shared `/tmp/chattr` directory accessible to all participants (files are automatically created; just make sure all users can modify them).

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3 installed.
3. Place the script on a server or shared environment where all participants can access `/tmp/chattr`.

## Usage

1. Run the script:
   ```bash
   ./chattr.py
   ```
   Or:
   ```bash
   python3 chattr.py
   ```

2. Use the menu to select:
   - **[0] Chat**: Enter the chatroom.
   - **[1] Settings**: Change user or appearance settings.
   - **[2] Changelog**: View update history.
   - **[3] Quit**: Exit the application.

3. In chat mode, available commands:
   ```
   /h  /help       - Lists all commands
   /lv /leave      - Disconnect from the chat
   /ch /channel    - Create or join a channel (blank for main)
   /rm /remove     - Delete the current channel (cannot remove main)
   /n  /name       - Show the current channel name
   /ls /list       - List all available channels
   /cl /clear      - Clear the chat screen
   /a  /anonymous  - Toggle anonymous mode
   ```

4. Example:
   ```
   [12:00:01] User1: Hello!
   [12:00:05] User2: Hi there!
   ```

## Notes

- This chat system relies on a shared directory in `/tmp/chattr`.  
- Channels are stored as `.txt` files in that directory.  
- System messages (e.g., "User connected/disconnected") can be toggled in settings.  

## License

This project is open source and available under the MIT License.

# Chattr

`chattr` is a simple terminal-based chat application written in Python that allows multiple users to communicate in real-time via a shared text file.

## Features

- **Real-time Chat**: Messages are instantly shared between connected users via a shared file.
- **Customizable Appearance**:
  - Change your username and username color.
  - Change the secondary input color.
  - Toggle system messages on or off.
- **Settings Menu**: Modify chat and user settings directly in the application.
- **Changelog**: View updates and fixes for each version.
- **Clear Terminal UI**: Simple and clean interface with ASCII art header.
- **Users**: Chattr allows for multiple users, or even multiple poeple using ssh to connect to the same user
- **Profiles**: Save/Load user profiles so you don't need to manually change your preferences every time

## Requirements

- Python 3.x
- A shared `/tmp/chattr.txt` file accessible to all participants (this file is automatically created, just make sure all users can modify it).

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3 installed.
3. Place the script on a server or shared environment where all participants can access `/tmp/chattr.txt`.

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

3. In chat mode:
   - Type messages and press **Enter** to send.
   - Type `/leave` to exit the chat.

## Example

```
[12:00:01] User1: Hello!
[12:00:05] User2: Hi there!
```

## Notes

- This chat system relies on a shared file. It works best in environments where multiple users can read/write to `/tmp/chattr.txt`.
- System messages (e.g., "User connected/disconnected") can be toggled in settings.

## License

This project is open source and available under the MIT License.

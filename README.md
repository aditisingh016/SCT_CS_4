# SCT_CS_4
🔑 Keylogger (Educational Project)

This project is a simple keyboard event logger built with Python.
It captures keystrokes on your system and saves them to a file.

⚠️ Disclaimer:
This project is for educational purposes only as part of a cybersecurity internship task.
Do not use it on anyone else’s device without their knowledge and consent.

📌 Features

Records all keystrokes (alphabets, numbers, symbols).

Logs special keys (Enter, Space, Shift, etc.) with tags.

Saves data to key_log.txt.

Stops logging when ESC key is pressed.

🛠️ Requirements

Python 3.8+ (tested on Python 3.13)

pynput library

Install dependencies:

pip install pynput

📂 Project Structure
KeyLoggerProject/
│── keylogger.py     # Main script
│── key_log.txt      # Generated log file
│── README.md        # Documentation

▶️ How to Run

Clone/download this project or create the files manually.

Open terminal in VS Code.

Run:

python keylogger.py


Type in any window (Notepad, browser, etc.).

Press ESC to stop logging.

Open key_log.txt to view captured keystrokes.

📖 Example Output

If you type:

Hello World


The log file may look like:

H e l l o  [Key.space] W o r l d  [Key.enter]

🛡️ Ethical Usage

This project is meant to demonstrate how keylogging works for learning and security awareness.
Real-world attackers may use such tools maliciously, but as cybersecurity learners, we use it only:

On our own system

For practice and awareness

To understand how to defend against such attacks

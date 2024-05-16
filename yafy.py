import io
import subprocess
import sys
import threading
import tkinter
from tkinter import ttk
import os

import screeninfo
from screeninfo import *

class ConsoleRedirector(io.StringIO):
    def __init__(self, target_widget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_widget = target_widget

    def run_command_and_capture_output(self, command):
        # Run the command and capture its output
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                # Display only the last line of output
                self.target_widget.config(text=output.strip())
                self.target_widget.update_idletasks()  # Update the widget to show the output immediately

for i in screeninfo.get_monitors():
    if i.is_primary == True:
        scrWidth = i.width
        scrHeight = i.height
def systemUpdate():
    os.system("chmod +x askpass.py")
    os.environ['SUDO_ASKPASS'] = "askpass.py"
    threading.Thread(target=console_redirector.run_command_and_capture_output, args=("yay -Syu --noconfirm",)).start()

root = tkinter.Tk()
root.geometry(f"{int(scrWidth * 0.7)}x{int(scrHeight * 0.7)}")

syuButton = tkinter.Button(root, text="Update System", command=systemUpdate, font=("", int(scrHeight * 0.01)))
syuButton.pack(side="right", anchor="s", padx=f"{int(scrHeight * 0.01)}", pady=f"{int(scrHeight * 0.01)}")

console_label = tkinter.Label(root, wraplength=400)
console_label.pack(side="bottom", pady=f"{int(scrHeight * 0.01)}")

# Create a custom stream object
console_redirector = ConsoleRedirector(console_label)


root.mainloop()
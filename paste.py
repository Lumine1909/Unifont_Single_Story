import time
import pyautogui

user_input = input("Input string that need to paste: ")

print("Please switching in 5 sec...")
time.sleep(5)

pyautogui.write(user_input, interval=0.01)
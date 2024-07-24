from PIL import ImageGrab
import os
import time
import webbrowser
import pyautogui
import keyboard
import shutil

current='stockChartEvaluator/data/current'
toBeLabeled='stockChartEvaluator/data/toBeLabeled'
for name in os.listdir(current):
    shutil.move(os.path.join(current, name), os.path.join(toBeLabeled, name))

stocks = []
with open("/Users/Lorenzo/Desktop/code/stocks/stockChartEvaluator/stockList.txt",) as f:
    for line in f:
        stocks.append(line)
banner = True
if banner:
    for stock in stocks:
        pyautogui.moveTo(640, 650, duration = 0.1)
        webbrowser.open(f'https://ca.finance.yahoo.com/quote/{stock}/')
        time.sleep(2)
        pyautogui.click()
        time.sleep(0.5)
        # Capture the entire screen
        screenshot = ImageGrab.grab(bbox=(100, 500, 1020, 880))
        number = len([name for name in os.listdir(current) if os.path.isfile(os.path.join(current, name))])
        # Save the screenshot to a file
        screenshot.save(os.path.join(current, f'screenshot{number}.png'))
        # Close the screenshot
        screenshot.close()
        pyautogui.hotkey('command', 'w')
else:
    for stock in stocks:
        pyautogui.moveTo(645, 568, duration = 0.1)
        webbrowser.open(f'https://ca.finance.yahoo.com/quote/{stock}/')
        time.sleep(2)
        pyautogui.click()
        time.sleep(0.5)
        # Capture the entire screen
        screenshot = ImageGrab.grab(bbox=(100, 420, 1020, 840))
        number = len([name for name in os.listdir(current) if os.path.isfile(os.path.join(current, name))])
        # Save the screenshot to a file
        screenshot.save(os.path.join(current, f'screenshot{number}.png'))
        # Close the screenshot
        screenshot.close()
        pyautogui.hotkey('command', 'w')

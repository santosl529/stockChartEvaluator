from PIL import ImageGrab
import os
import time
import webbrowser

stocks = []
with open("stockList.txt",) as f:
    for line in f:
        stocks.append(line)

for stock in stocks:
    webbrowser.open(f'https://www.google.com/finance/quote/{stock}:NASDAQ?hl=en')
    time.sleep(5)

# Capture the entire screen
screenshot = ImageGrab.grab(bbox=(200, 360, 900, 800))

DIR = 'data/currentDay'
number = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
# Save the screenshot to a file
screenshot.save(f"data/currentDay/screenshot{number}.png")

# Close the screenshot
screenshot.close()


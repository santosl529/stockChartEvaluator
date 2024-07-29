import yfinance as yf
import os
import shutil
import random

toBeLabeled='data/toBeLabeled'
train = 'dataset/train'
valid = 'dataset/val'

stocks = []
with open("stockList.txt",) as f:
    for line in f:
        stocks.append(line.strip())

# Fetch historical market data for the past 5 days for each ticker
data = yf.download(stocks, period="5d")
changes = []
for stock in stocks:
    print(stock)
    percent_change = 100 * (data['Adj Close'][stock].iloc[4] - data['Adj Close'][stock].iloc[0]) / data['Adj Close'][stock].iloc[0]
    name = os.listdir(toBeLabeled)[0]
    if percent_change < -5:
        if random.randint(1,100) > 20:
            shutil.move(os.path.join(toBeLabeled, name), os.path.join(train, '-5AndUnder', f"{stock}{len(os.listdir(os.path.join(train, '-5AndUnder')))}.png"))  
        else:
            shutil.move(os.path.join(toBeLabeled, name), os.path.join(valid, '-5AndUnder', f"{stock}{len(os.listdir(os.path.join(train, '-5AndUnder')))}.png"))  
    elif percent_change <= 0:
        if random.randint(1, 100) > 20:
            shutil.move(os.path.join(toBeLabeled, name), os.path.join(train, '-5To0', f"{stock}{len(os.listdir(os.path.join(train, '-5To0')))}.png"))
        else: 
            shutil.move(os.path.join(toBeLabeled, name), os.path.join(valid, '-5To0', f"{stock}{len(os.listdir(os.path.join(train, '-5To0')))}.png"))
    elif percent_change <= 5:
        if random.randint(1, 100) > 20:
            shutil.move(os.path.join(toBeLabeled, name), os.path.join(train, '0To5', f"{stock}{len(os.listdir(os.path.join(train, '0To5')))}.png"))
        else: 
            shutil.move(os.path.join(toBeLabeled, name), os.path.join(valid, '0To5', f"{stock}{len(os.listdir(os.path.join(train, '0To5')))}.png"))
    elif percent_change > 5 :
        if random.randint(1, 100) > 20:
            shutil.move(os.path.join(toBeLabeled, name), os.path.join(train, '5AndOver', f"{stock}{len(os.listdir(os.path.join(train, '5AndOver')))}.png"))    
        else:
            shutil.move(os.path.join(toBeLabeled, name), os.path.join(valid, '5AndOver', f"{stock}{len(os.listdir(os.path.join(train, '0To5')))}.png"))


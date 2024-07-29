from ultralytics import YOLO

model = YOLO("runs/classify/train4/weights/best.pt")

results = model("data/current", save_txt=True , conf= 0.5)
counter = 0
file = open('stockList.txt')
content = file.readlines()
best = open('results/bestStocks.txt', 'a')
good =open('results/goodStocks.txt', 'a')
bad = open('results/badStocks.txt', 'a')
worst = open('results/worstStocks.txt', 'a')
highest_best = 0
highest_worst = 0
highest_good = 0
highest_bad = 0
for result in results:
    if result.probs.top1 == 2:
        good.write(f"2  {content[counter].strip()} {round(result.probs.data[result.probs.top1].item(), 4) * 100}%\n")
        highest_good = max(highest_good, round(result.probs.data[result.probs.top1].item()*100, 2))
        print(f"2  {content[counter].strip()} {round(result.probs.data[result.probs.top1].item(), 4) * 100}%") 
    elif result.probs.top1 == 3:
        best.write(f"3  {content[counter].strip()}  {round(result.probs.data[result.probs.top1].item(), 4) * 100}%\n")
        highest_best = max(highest_best, round(result.probs.data[result.probs.top1].item()*100, 2))
        print(f"3  {content[counter].strip()}  {round(result.probs.data[result.probs.top1].item(), 4) * 100}%") 
    elif result.probs.top1 == 1:
        bad.write(f"1  {content[counter].strip()} {round(result.probs.data[result.probs.top1].item(), 4) * 100}%\n")
        highest_bad = max(highest_bad, round(result.probs.data[result.probs.top1].item()*100, 2))
        print(f"1  {content[counter].strip()} {round(result.probs.data[result.probs.top1].item(), 4) * 100}%") 
    elif result.probs.top1 == 0:
        worst.write(f"0  {content[counter].strip()}  {round(result.probs.data[result.probs.top1].item(), 4) * 100}%\n")
        highest_worst = max(highest_worst, round(result.probs.data[result.probs.top1].item()*100, 2))
        print(f"0  {content[counter].strip()}  {round(result.probs.data[result.probs.top1].item(), 4) * 100}%") 
    counter+=1
good.write(f"Top percent: {highest_good}%")
bad.write(f"Top percent: {highest_bad}%")
best.write(f"Top percent: {highest_best}%")
worst.write(f"Top percent: {highest_worst}%")
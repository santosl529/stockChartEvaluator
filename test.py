import os
import shutil
current = "data/current"
train = 'dataset/train'
name = os.listdir(current)[0]

shutil.move(os.path.join(current, name), os.path.join(train, '-5AndUnder', f"{len(os.listdir(os.path.join(train, '-5AndUnder')))}.png"))
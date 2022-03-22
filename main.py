import numpy as np
import csv
import shutil
from PIL import Image


def read_data():
    with open('train.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    print(data)
    data = data[1:len(data)]
    for e in data:
        for v in e[1].split():
            try:
                image = Image.open("train_images/" + e[0])
                new_image = image.resize((400, 400))
                new_image.save("sorted_images/" + v+"/" + e[0])
            except(FileNotFoundError):
                pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_data()

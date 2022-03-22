import numpy as np
import csv
import shutil


def read_data():
    with open('train.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    print(data)
    data = data[1:len(data)]
    for e in data:
        for v in e[1].split():
            try:
                shutil.copy("train_images/" + e[0], "sorted_images/" + v+"/")
            except(FileNotFoundError):
                pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_data()

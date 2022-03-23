import os
import numpy as np
import matplotlib.pyplot as plt
import csv
from PIL import Image


csv_file_path = 'train.csv'
images_path = 'train_images/'
split_images_path = 'sorted_images/'

final_image_size = (400, 400)
    
def split_to_subdirectories():
    with open(csv_file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    print(data)
    data = data[1:len(data)]
    for e in data:
        for v in e[1].split():
            try:
                image = Image.open(images_path + e[0])
                new_image = image.resize(final_image_size)
                new_image.save(split_images_path + v + "/" + e[0])
            except(FileNotFoundError):
                pass


def get_classes():
    classes = set()
    with open(csv_file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = data[1:len(data)]
    for e in data:
        for v in e[1].split():
            classes.add(v)
    return classes


def get_classes_sets():
    classes_sets = set()
    with open(csv_file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    data = data[1:len(data)]
    for e in data:
        classes_sets.add(e[1])
    return classes_sets


def create_missing_directories():
    classes = get_classes()
    
    try:
        os.mkdir(split_images_path)
    except FileExistsError:
        pass
    
    for c in classes:
        try:
            os.mkdir(split_images_path + c)
        except FileExistsError:
            pass


def get_colors_vector(img_path: str) -> np.ndarray:
    image = Image.open(img_path)
    image = np.array(image)
    return image.flatten(order='C')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_missing_directories()
    split_to_subdirectories()

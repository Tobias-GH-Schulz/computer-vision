import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from skimage import io
from PIL import Image

class Coin_test_dataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.annotations = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.annotations.iloc[index, 0])
        image_array = io.imread(img_path)
        image = Image.fromarray(image_array)
        y_label = torch.LongTensor(float(self.annotations.iloc[index, 1]), requires_grad=True)

        if self.transform:
            image = self.transform(image)

        return (image, y_label)
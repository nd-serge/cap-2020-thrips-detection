import os
import pandas as pd
import numpy as np
from skimage.util import random_noise
from PIL import Image
import cv2



def get_files(path):
  print("collecting data...")
  filenames = []
  for filename in os.listdir(path):
      filenames.append(os.path.join(path, filename))
  return pd.Series(filenames)


def create_noise_from_series(filepaths_series, mode, output_dir, pct=0):
    print(f"Creating {mode} noise with pct={pct}...")
    if pct != 0:
      output_dir = os.path.join(output_dir, mode ,f"{pct}")
    else:
      output_dir = os.path.join(output_dir, mode)

    os.makedirs(output_dir, exist_ok=True)

    for filepath in filepaths_series:
        filename = os.path.basename(filepath)

        img = Image.open(filepath).convert("RGB")
        img_np = np.array(img)[...,::-1]/255.0

        if mode in ["salt", "pepper", "s&p"]:
            print(f"Applying noise {mode}")
            noisy_img = random_noise(img_np, mode=mode, amount=pct)
        
        elif mode == "blur":
           image = cv2.imread(filepath)
           median = cv2.medianBlur(image, 11)  
           noisy_img = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)  

        else:
            noisy_img = random_noise(img_np, mode=mode)

        noisy_img = (noisy_img * 255).astype(np.uint8)
        noisy_img = Image.fromarray(noisy_img, "RGB")

        output_path = os.path.join(output_dir, filename)
        noisy_img.save(output_path)
        print("Saved noisy image to:", output_path)


def save_image(image_array, output_path, filename):
    os.makedirs(output_path, exist_ok=True)
    noisy_img = (image_array * 255).astype(np.uint8)
    noisy_img = Image.fromarray(noisy_img, "RGB")
    noisy_img.save(os.path.join(output_path, filename))


def noise_image(filepath, mode, pct):
    img = Image.open(filepath).convert("RGB")
    img_np = np.array(img)[...,::-1]/255.0
    noisy_img = random_noise(img_np, mode=mode, amount=pct)
    return noisy_img
 

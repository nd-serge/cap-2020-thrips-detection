import cv2
import numpy as np
from PIL import Image

import os

image_path = '../data/AI4I_2026_JDD_V0/0_thrips/2022_close_up/blur/0.35/ASTREDHOR_TPR_2022-05-20_scan_15B_0_transmis_SP3500;1881;1899;642;660.png'

image = cv2.imread(image_path)
resized_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

median = cv2.medianBlur(image, 11)  
median_rgb = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)  

noisy_img = Image.fromarray(median_rgb)
noisy_img.save("blurred_image.png")


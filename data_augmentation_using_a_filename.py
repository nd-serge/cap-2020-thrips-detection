import os
from utils import noise_image, save_image
import yaml
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, './config.yml')

with open(CONFIG_PATH, "r") as f:
    CONFIG = yaml.load(f, Loader=yaml.SafeLoader)

INPUT = CONFIG["noise_params_file"]['filepath']
NUM_IMAGES = CONFIG["noise_params_file"]['num_samples']
MODE = CONFIG['noise_params_file']['mode']
AMOUNT = CONFIG['noise_params_file']['pct']
OUTPUT = CONFIG['noise_params_file']['output_dir']


if __name__ == "__main__":
    for i in range(NUM_IMAGES):
        img = noise_image(INPUT, mode=MODE, pct=AMOUNT)
        filename = os.path.basename(INPUT)
        DIR = os.path.join(OUTPUT, MODE, str(AMOUNT))
        save_image(img, DIR, filename=f"noisy_{i}_{filename}")



        
        
# -*- coding: utf-8 -*-

from utils import get_files, create_noise_from_series
import yaml
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, './config.yml')

with open(CONFIG_PATH, "r") as f:
    CONFIG = yaml.load(f, Loader=yaml.SafeLoader)

INPUT = CONFIG["datapath"]['input']

serie_2021 = get_files(INPUT)

if __name__ == "__main__":
    try:
        create_noise_from_series(
            filepaths_series=serie_2021,
            mode=CONFIG['noise_params']['mode'],
            pct=CONFIG['noise_params']['pct'],
            output_dir=CONFIG['datapath']['output']
        )
    except Exception as e:
        print("An error occurred:", e)



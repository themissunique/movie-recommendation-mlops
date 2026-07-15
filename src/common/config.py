from pathlib import Path
import yaml


class Config:

    def __init__(self, config_path="configs/config.yaml"):

        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def get(self):

        return self.config
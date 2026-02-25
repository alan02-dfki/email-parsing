from pathlib import Path

import yaml

with open(Path(__file__, "../../config.yaml").resolve()) as config_file:
    CONFIG = yaml.safe_load(config_file)

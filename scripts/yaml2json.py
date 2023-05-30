from pathlib import Path

import yaml
import json
def convertYAMLtoJSON(path):

        file_path = Path(''.join(path))
        with open(file_path, 'r') as file:
            configuration = yaml.safe_load(file)
        with open(f"./output/{file_path.stem}.json", 'w') as json_file:
            json.dump(configuration, json_file)




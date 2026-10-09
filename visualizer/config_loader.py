import json
from types import SimpleNamespace

CONFIG_PATH = 'visualizer_conf.json'

def load_config(filepath=CONFIG_PATH):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f, object_hook=lambda d: SimpleNamespace(**d))


config = load_config()

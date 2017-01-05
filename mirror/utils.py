import json
from itertools import zip_longest


def validate_config(config):
    rows = config['row_heights']
    if sum(rows) != 100:
        raise ValueError("Sum of row heights must total 100%")

    modules = config['modules']
    if len(modules) > len(rows):
        raise ValueError("More module rows than row heights.")
    for module_row in modules:
        widths = [int(m['width']) for m in module_row]
        if sum(widths) > 12:
            raise ValueError("Module total row width must be <= 12.")
    config['module_rows'] = list(zip_longest(rows, modules))


def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    validate_config(config)
    return config

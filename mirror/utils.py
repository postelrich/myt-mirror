import json
import os
from itertools import zip_longest
from toolz import thread_last, concat, get_in, curry


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


def add_module_files(config):
    for module_row in config['modules']:
        for module in module_row:
            module_name = module.get('name', '')
            module_base_path = os.path.join('modules', module_name)
            file_types = ['css', 'js', 'html', 'py']
            for file_type in file_types:
                module_file = os.path.join(module_base_path, '.'.join([module_name, file_type]))
                if os.path.exists(os.path.join(os.path.dirname(__file__), module_file)):
                    if file_type == 'html':
                        module[file_type] = '.'.join([module_name, file_type])
                    else:
                        module[file_type] = module_file


def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    validate_config(config)
    add_module_files(config)
    config['module_rows'] = list(zip_longest(config['row_heights'], config['modules']))
    config['module_names'] = thread_last(config['modules'],
                                         concat,
                                         (map, curry(get_in)(['name'])),
                                         (filter, lambda x: x is not None))
    return config

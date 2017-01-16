import json
import os
from itertools import chain, zip_longest
from toolz import thread_last, concat, get_in, curry, first, second


def format_config(config):
    """Format configuration file in a way useful to application."""
    config['module_rows'] = [] 
    grid_id_module_map = {m['grid_id']: m for m in config['modules']}

    # create list of list of modules for each row, adding a blank one for empty spaces
    grid_id = 1
    for row_height, col_widths in config['grid']:
        module_row = []
        
        total_row_width = 0
        for col_width in col_widths:
            module_row.append((col_width, grid_id_module_map.get(grid_id, {'grid_id': grid_id})))
            total_row_width += col_width
            grid_id += 1

        if total_row_width < 12:
            module_row.append((12 - total_row_width, grid_id_module_map.get(grid_id, {'grid_id': grid_id})))
            grid_id += 1

        config['module_rows'].append((row_height, module_row))
    config['grid_ids'] = list(range(1, grid_id))


def validate_config(config):
    grid = config['grid'] 
    row_heights = map(first, grid)
    row_col_widths = map(second, grid)

    if sum(row_heights) != 100:
        raise ValueError("Sum of row heights must total 100%")

    for row in row_col_widths:
        if sum(row) > 12:
            raise ValueError("Module total row width must be <= 12.")

    modules = config['modules']
    for module in modules:
        if 'name' not in module:
            raise KeyError("Module name required.")
        if not os.path.exists(os.path.join(os.path.dirname(__file__), 'modules', module['name'])):
            raise NotADirectoryError("No directory named {} found in the modules directory.".format(module['name']))
        if 'grid_id' not in module:
            raise KeyError("Module grid id required to know where to place module.")
        if module['grid_id'] not in config['grid_ids']:
            raise ValueError("Grid id {} does not exist in grid for module {}.".format(module['grid_id'], module['name']))


def add_module_files(config):
    """For each module, add the static and python files to the config."""
    for module in config['modules']:
        module_name = module.get('name', '')
        module_base_path = os.path.join('modules', module_name)
        file_types = ['css', 'js', 'html', 'py']
        for file_type in file_types:
            file_name = module_name
            if file_type == 'py':
                file_name = '__init__'
            module_file = os.path.join(module_base_path, '.'.join([file_name, file_type]))
            if os.path.exists(os.path.join(os.path.dirname(__file__), module_file)):
                if file_type == 'html':
                    module[file_type] = '.'.join([module_name, file_type])
                else:
                    module[file_type] = module_file


def load_config(config_path):
    """Load configuration file

    Parameters
    ----------
    config_path : str
        configuration file path

    Returns
    -------
    dict
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    format_config(config)
    validate_config(config)
    add_module_files(config)
    config['module_names'] = [m['name'] for m in config['modules']]
    return config

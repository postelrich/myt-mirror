# MyT-Mirror

A magic mirror application powered by python.

MyT-Mirror seeks to be a lean framework for making a magic mirror webpage with support for easily adding your own modules. It makes use of flask, socketio, and jinja. Materialize is being used for the grid, though any framework would probably do. A module can be written entirely with a jinja template and js, and optionally with python via websockets.

## Install

At the moment its not packaged so you need to clone and install the python packages. I am
running it on python 3.5, though 2.7 should work.

## Configuration

The configuration is in json format. At the moment, there are only two fields, `grid` and
`modules`.

### grid

The `grid` field defines the layout of the webpage. It is a list of tuples. Each tuple
defines a row. The first value in the tuple is the row height in percent. The second value is a list of the column widths where the max sum of the widths can be 12 (materialize grid limitation).This lets you define your own grid. 

You can view the grid by going to `127.0.0.1:5000?layout=1` while the application running.
It will display the grid with ids for each space. You will use these ids to tell which
module should be running in them.

Example:
```
    "grid": [
        [20, [3]], 
        [30, [2, 7, 3]], 
        [50, []], 
    ]
```

The above grid will have three rows with heights 20, 30, 50, respectively. The second
row will have 3 columns. If the column widths don't sum to 12, the remainder will be its
own space.

![layout mode](https://cloud.githubusercontent.com/assets/3619876/21972058/b1416f8c-db84-11e6-9c56-a21b9ac3d619.png)

### modules

The `modules` field is where you configure what is displayed in each space. It is a list of objects. Each object must have a `grid_id` and `name` key. The `grid_id` is an integer that comes from a space in `127.0.0.1:5000?layout=1`, discussed above. The `name` key is the name of the module. The `config` key is an object that is passed to configure the module when it is ran.

## Module Development



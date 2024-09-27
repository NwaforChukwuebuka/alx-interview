# Island Perimeter

## Description

The Island Perimeter project provides a function to calculate the perimeter of an island represented in a grid. The grid is composed of integers where:
- `0` represents water
- `1` represents land

The function `island_perimeter(grid)` returns the total perimeter of the island described in the grid.

## Features

- Calculates the perimeter of a single island.
- Handles rectangular grids with dimensions up to 100x100.
- Assumes the grid is surrounded by water and contains no internal lakes.

## Installation

To use this project, clone the repository and navigate to the directory:

```bash
git clone https://github.com/yourusername/alx-interview.git
cd alx-interview/0x09-island_perimeter


Usage
You can use the provided island_perimeter function in your Python scripts. Below is an example of how to use it:


#!/usr/bin/python3
"""
Example usage of island_perimeter
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12


Testing
To test the function, you can run the provided 0-main.py script:

python3 0-main.py


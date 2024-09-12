# 0x07. Rotate 2D Matrix

## Overview

This project, part of the ALX Interview Preparation series, challenges you to implement an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise using Python. This task requires a strong grasp of matrix manipulation techniques and in-place operations to optimize both space and time complexity.

### Key Concepts:

- **Matrix Representation**: Understanding how a 2D matrix is represented in Python using lists of lists.
- **In-place Operations**: Modifying data without creating additional copies, thus improving space complexity.
- **Matrix Transposition**: Swapping rows and columns as a preliminary step to rotating the matrix.
- **Row Reversal**: Reversing each row in the matrix to complete the 90-degree rotation.
- **Nested Loops**: Iterating over elements in a matrix using nested loops to perform the necessary modifications.


### Objective:
You will implement a function `rotate_2d_matrix(matrix)` that rotates a given `n x n` 2D matrix by 90 degrees clockwise. The function should modify the matrix in place, without returning anything.

```python
def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    """
```

### Task: Rotate 2D Matrix

#### Prototype:
```python
def rotate_2d_matrix(matrix):
    # Rotate the matrix in place
```

### Constraints:
- The matrix will always have 2 dimensions and will not be empty.

### Example:

Given the matrix:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

After rotation, the matrix should look like:
```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

### Execution:

To test your implementation, create a Python file (`main_0.py`) as follows:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

Running this script should produce the following output:
```bash
$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Repository Structure

- **GitHub Repository**: `alx-interview`
- **Directory**: `0x07-rotate_2d_matrix`
- **File**: `0-rotate_2d_matrix.py`

## Additional Resources:
To help you complete this project, you can consult the following resources:
- **Python Documentation**:
  - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html)
  - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- **GeeksforGeeks**:
  - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
  - [Transpose a Matrix in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- **TutorialsPoint**:
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)


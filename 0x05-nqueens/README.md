# N Queens Puzzle

The N Queens puzzle is a classic problem in combinatorial optimization that involves placing N non-attacking queens on an NxN chessboard. The challenge is to ensure that no two queens threaten each other, meaning that each queen must be placed in a unique row, column, and diagonal.

## Problem Description

On a chessboard, a queen can move any number of squares vertically, horizontally, or diagonally. Thus, to solve the puzzle, each queen must be positioned so that no two queens can attack each other.

This problem is efficiently solved using a **backtracking algorithm**. Backtracking is a general approach for finding solutions to computational problems by incrementally building candidates and abandoning them as soon as it is determined that they cannot lead to a valid solution.

## Usage

To run the N Queens program, use the following command:

```bash
nqueens N
```

Where `N` is the number of queens (and also the size of the chessboard). Note that `N` must be an integer greater than or equal to 4.

### Example

To find all solutions for 4 queens, execute:

```bash
$ ./0-nqueens 4
```

### Output Format

The program will print every possible solution in the following format:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Each inner list represents the coordinates of a queen on the NxN chessboard, where the first element is the row index and the second element is the column index.

## Requirements

- Python 3.x
- An integer N (N >= 4)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Prime Game

## Overview

This repository contains a solution to the "Prime Game" problem, a coding interview question. The problem involves two players, Maria and Ben, playing a game with a set of consecutive integers. The players take turns choosing a prime number from the set and removing that number along with its multiples. The player unable to make a move loses the game. The solution determines the winner of each round, assuming both players play optimally, with Maria always going first.

## Tasks

### Prime Game
**Task Requirements:**

Maria and Ben are playing a game where:

- They take turns choosing a prime number from a set of consecutive integers starting from `1` to `n`.
- The chosen prime and all its multiples are removed from the set.
- The player unable to make a move loses.

The game is played in `x` rounds, where `n` can vary for each round. The task is to determine the overall winner after `x` rounds. 

- **Function Prototype:** `def isWinner(x, nums)`
- **Inputs:** 
  - `x`: Number of rounds.
  - `nums`: List of `n` values representing the size of the integer set for each round.
- **Outputs:** 
  - The name of the player (Maria or Ben) who won the most rounds.
  - Return `None` if there's no clear winner.

### Example

For `x = 3` and `nums = [4, 5, 1]`:

1. **Round 1 (n = 4)**:
   - Maria picks 2, removing 2 and 4.
   - Ben picks 3, removing 3.
   - **Ben wins** (no primes left for Maria).

2. **Round 2 (n = 5)**:
   - Maria picks 2, removing 2 and 4.
   - Ben picks 3, removing 3.
   - Maria picks 5, removing 5.
   - **Maria wins** (no primes left for Ben).

3. **Round 3 (n = 1)**:
   - **Ben wins** (no primes left for Maria).

**Final Result:** Ben wins the majority of rounds.

### Solution File

- File: [0-prime_game.py](0-prime_game.py)

## Task Setup

To set up and run the solution:

```bash
# Create the solution file
touch 0-prime_game.py
chmod +x 0-prime_game.py

# Lint the solution
pep8 0-prime_game.py

# Create and run the test file
touch 0-main.py
chmod +x 0-main.py
./0-main.py
```

## Repository

- **GitHub repository:** `alx-interview`
- **Directory:** `0x0A-primegame`
- **File:** `0-prime_game.py`


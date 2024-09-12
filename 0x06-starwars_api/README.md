Star Wars API Project

## Overview
This project demonstrates how to interact with the Star Wars API to retrieve and display information about characters in a specific movie using JavaScript. The script fetches character data based on the movie ID provided as a command-line argument.

## Requirements
- **OS:** Ubuntu 20.04 LTS
- **Node Version:** 10.14.x
- **File requirements:**
  - All files should end with a new line.
  - The first line of every file should be `#!/usr/bin/node`.
  - Code must follow semistandard style.
  - Use `let` or `const`, not `var`.
  - All files must be executable.

## Installation

1. **Install Node.js 10**:
   ```bash
   $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   $ sudo apt-get install -y nodejs
   ```

2. **Install semistandard**:
   ```bash
   $ sudo npm install semistandard --global
   ```

3. **Install request module**:
   ```bash
   $ sudo npm install request --global
   ```

## Task: Star Wars Characters
### Objective:
Write a script that prints all characters of a Star Wars movie based on the movie ID provided as a command-line argument.

### Example Usage:
```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```

## Repository
- **GitHub repository:** `alx-interview`
- **Directory:** `0x06-starwars_api`
- **File:** `0-starwars_characters.js`

--- 

May the Force be with you!

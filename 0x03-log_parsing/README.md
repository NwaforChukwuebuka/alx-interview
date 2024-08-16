# Log Parsing Script

This repository contains a Python script that reads log data from standard input (stdin), parses it, and computes various metrics. The script is designed to handle log entries in a specific format and will output cumulative statistics after every 10 lines of input or upon receiving a keyboard interruption (CTRL + C).

## Features

- **Real-Time Log Processing:** The script processes logs in real-time, making it suitable for live monitoring scenarios.
- **Metrics Calculation:** It calculates the total file size and counts occurrences of specific HTTP status codes.
- **Robust Input Handling:** Only logs that match the expected format are processed, ensuring accurate metrics.

## Input Format

The script expects each log line to be in the following format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

- `<IP Address>`: The IP address from which the request originated.
- `<date>`: The date and time of the request in a standard log format.
- `<status code>`: The HTTP status code returned by the server.
- `<file size>`: The size of the requested file in bytes.

**Note:** Lines that do not conform to this format will be skipped.

## Output

The script outputs the following metrics:

- **Total File Size:** The cumulative sum of the file sizes processed.
  - Format: `File size: <total size>`
- **HTTP Status Code Count:** A count of each status code encountered, printed in ascending order of the status codes.
  - Format: `<status code>: <number>`

### Example Output

```
File size: 16384
200: 8
301: 1
404: 1
```

## Usage

### Running the Script

You can run the script by piping log data directly into it or by redirecting a log file:

```bash
cat your_log_file.log | python log_parsing.py
```

or

```bash
python log_parsing.py < your_log_file.log
```
Then, input the log lines one by one.

### Handling Interruptions

Press `CTRL + C` at any time to trigger the script to print the current statistics and then exit gracefully.

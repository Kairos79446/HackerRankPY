# Test Environment Project

## Overview
This is a simple Python project containing a function that classifies numbers as "Weird" or "Not Weird" based on specific criteria.

## Purpose
The `task()` function determines if a number is "Weird" or "Not Weird" based on these rules:
- Odd numbers are "Weird"
- Even numbers in range 2-5 are "Not Weird"
- Even numbers in range 6-20 are "Weird"
- Even numbers greater than 20 are "Not Weird"

## Project Structure
```
.
├── TestEnvironment.py    # Main Python script with task() function
├── .gitignore           # Python gitignore configuration
└── replit.md            # This documentation file
```

## Recent Changes
- **2025-11-06**: Initial import and Replit environment setup
  - Installed Python 3.11
  - Added main execution block with test cases
  - Created .gitignore for Python
  - Configured workflow to run the script

## How to Run
The project runs automatically via the configured workflow. The script tests the `task()` function with sample numbers (3, 4, 10, 24) and displays the results.

## Architecture
- **Language**: Python 3.11
- **Type**: Console application
- **Execution**: Direct script execution via workflow
- **Dependencies**: None (uses only Python standard library)

## User Preferences
None specified yet.

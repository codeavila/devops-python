#!/usr/bin/env python3

## 01 - Basic OS System Command Execution

import os

# Execute a basic system command
os.system("echo 'Hello from CodeCraftAvila'")

os.system("ls -l")  # List files in long format (Linux/Mac)
os.system("dir")  # List files (Windows)

# Execute clean command based on OS
if os.name == "nt":
    os.system("cls")  # For Windows
else:
    os.system("clear")  # For Linux/Mac

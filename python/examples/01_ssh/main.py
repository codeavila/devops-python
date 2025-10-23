#!/usr/bin/env python3

"""
SSH Connection Example using Paramiko
Step 1) Create a virtual environment:
python -m venv venv
Step 2) Install paramiko if not already installed:
pip install paramiko
Step 3) Install dotenv if not already installed:
pip install python-dotenv
Step 4) Create a .env file in the same directory with the following content:
    SSH_HOST=your_ssh_server_ip_or_hostname
    SSH_PORT=22
    SSH_USER=your_ssh_username
    SSH_PASSWORD=your_ssh_password
"""
import os
import argparse

import paramiko
from dotenv import load_dotenv

print("Loading environment variables from .env file...")
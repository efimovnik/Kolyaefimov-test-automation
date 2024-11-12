# playwright.config.py
import os

# Define your test directory or any other configurations you’d like
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(BASE_DIR, 'tests')

# This file is optional, as Playwright for Python generally uses pytest directly.

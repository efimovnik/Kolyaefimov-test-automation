import json

def load_test_data(file_path):
    with open(f"{file_path}", "r") as f:
        return json.load(f)
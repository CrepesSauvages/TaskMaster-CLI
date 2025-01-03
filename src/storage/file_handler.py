"""
File operations for reading and writing JSON data
"""
import json
import os
from typing import Any, Dict, List
from .exceptions import FileAccessError

def ensure_directory(filepath: str) -> None:
    """Ensure the directory exists for the given file path"""
    try:
        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)
    except OSError as e:
        raise FileAccessError(f"Failed to create directory: {e}")

def read_json_file(filename: str) -> List[Dict[str, Any]]:
    """Read and parse JSON data from a file"""
    try:
        if not os.path.exists(filename):  # Check if the file exists
            return []  # Return an empty list if the file doesn't exist
        if os.path.getsize(filename) == 0:  # Check if the file is empty
            return []  # Return an empty list
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise FileAccessError(f"Invalid JSON format: {e}")
    except OSError as e:
        raise FileAccessError(f"Failed to read file: {e}")


def write_json_file(filename: str, data: List[Dict[str, Any]]) -> None:
    """Write JSON data to a file"""
    try:
        ensure_directory(filename)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except OSError as e:
        raise FileAccessError(f"Failed to write file: {e}")
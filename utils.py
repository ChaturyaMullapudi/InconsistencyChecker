import hashlib
import json
import os
from pathlib import Path

CACHE_DIR = Path("./cache")
CACHE_DIR.mkdir(exist_ok=True)

def file_hash(filepath):
    """Generate a hash of file contents for caching."""
    if os.path.isfile(filepath):
        h = hashlib.md5()
        with open(filepath, 'rb') as f:
            h.update(f.read())
        return h.hexdigest()
    else:
        # For directories or lists, hash the string representation
        h = hashlib.md5()
        h.update(str(filepath).encode())
        return h.hexdigest()


def cache_load(hash_key):
    cache_file = CACHE_DIR / f"{hash_key}.json"
    if cache_file.exists():
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def cache_save(hash_key, data):
    cache_file = CACHE_DIR / f"{hash_key}.json"
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

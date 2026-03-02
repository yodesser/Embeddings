import json
import random
from pathlib import Path

def sample_dataset(source_file, dest_file, sample_ratio=0.4, seed=42):
    """
    Randomly sample a percentage of the EmoSet JSON dataset.
    """
    random.seed(seed)
    
    source_path = Path(source_file)
    
    if not source_path.exists():
        print(f"ERROR: Source file not found: {source_path.absolute()}")
        return
    
    # Load the JSON file
    print(f"Loading {source_file}...")
    with open(source_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Handle different JSON structures
    if isinstance(data, list):
        # If it's a list of items
        original_size = len(data)
        sample_size = max(1, int(original_size * sample_ratio))
        sampled_data = random.sample(data, sample_size)
    elif isinstance(data, dict):
        # If it's a dict, sample the keys
        keys = list(data.keys())
        original_size = len(keys)
        sample_size = max(1, int(original_size * sample_ratio))
        sampled_keys = random.sample(keys, sample_size)
        sampled_data = {k: data[k] for k in sampled_keys}
    else:
        print("Unknown data format")
        return
    
    # Save sampled data
    with open(dest_file, 'w', encoding='utf-8') as f:
        json.dump(sampled_data, f, indent=2)
    
    print(f"Original size: {original_size}")
    print(f"Sampled size: {sample_size} ({sample_ratio*100:.0f}%)")
    print(f"Saved to: {dest_file}")

if __name__ == "__main__":
    SOURCE_FILE = "emoset_challenge_1000_augmented.json"
    DEST_FILE = "half_dataset.json"
    
    sample_dataset(SOURCE_FILE, DEST_FILE, sample_ratio=0.4)
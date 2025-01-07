import os
import hashlib
import json

# Function to calculate hash of a file
def calculate_file_hash(file_path, hash_algorithm="sha256"):
    hasher = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

# Function to create initial hash database
def create_initial_hashes(directory, output_file, hash_algorithm="sha256"):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_file_hash(file_path, hash_algorithm)
    with open(output_file, "w") as f:
        json.dump(file_hashes, f, indent=4)
    print(f"Initial hash database created at {output_file}")

# Function to check for file integrity
def check_file_integrity(directory, hash_file, hash_algorithm="sha256"):
    with open(hash_file, "r") as f:
        stored_hashes = json.load(f)
    
    current_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hashes[file_path] = calculate_file_hash(file_path, hash_algorithm)
    
    # Compare hashes
    modified_files = []
    for file_path, file_hash in current_hashes.items():
        if file_path in stored_hashes:
            if file_hash != stored_hashes[file_path]:
                modified_files.append(file_path)
        else:
            print(f"New file detected: {file_path}")
    
    for file_path in stored_hashes:
        if file_path not in current_hashes:
            print(f"Deleted file detected: {file_path}")
    
    if not modified_files:
        print("No modifications detected.")
    else:
        print("Modified files:")
        for file in modified_files:
            print(file)

# Example Usage
if __name__ == "__main__":
    directory_to_monitor = "./test_files"  # Replace with your directory
    hash_file = "file_hashes.json"

    # Uncomment to create the initial hash database
    # create_initial_hashes(directory_to_monitor, hash_file)

    # Uncomment to check file integrity
    # check_file_integrity(directory_to_monitor, hash_file)

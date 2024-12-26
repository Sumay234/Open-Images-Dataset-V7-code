# Use This to download images:--
# Use this to download CSV:--

import os
import subprocess

# Define the class name and dataset type
class_names = ["Alpaca"]  # Replace with desired class names
dataset_type = "train"  # Use "train" as specified in the requirement
limit = 50  # Set the limit to 600 images

# Loop through the class names and download each class
for class_name in class_names:
    print(f"Downloading images for class: {class_name}")
    command = [
        "python",
        "main.py",
        "downloader",
        "--classes",
        class_name,
        "--type_csv",
        dataset_type,
        "--multiclasses",
        "0",  # Enable multi-class images 1 OR 0
        "--limit",
        str(limit),  # Ensure the limit is passed as a string
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading images for class {class_name}: {e}")

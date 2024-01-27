import os
import shutil
from django.conf import settings

# Define your source and destination directories
source_directory = settings.STATICFILES_DIRS[0]  # Assumes the first directory in STATICFILES_DIRS
destination_directory = settings.STATIC_ROOT

# Loop through files in the source directory
for root, _, files in os.walk(source_directory):
    for file in files:
        source_path = os.path.join(root, file)
        relative_path = os.path.relpath(source_path, source_directory)
        destination_path = os.path.join(destination_directory, relative_path)

        try:
            # Copy the file to the destination directory
            shutil.copy2(source_path, destination_path)
        except FileNotFoundError:
            # Skip missing files silently
            pass
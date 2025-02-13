import os
import shutil

# Define the target images directory
images_dir = os.path.join(os.getcwd(), "images")
os.makedirs(images_dir, exist_ok=True)

# Define allowed image file extensions
image_extensions = {".jpg", ".png", ".gif", ".svg", ".jpeg"}

# Walk through subdirectories from the current directory
for root, dirs, files in os.walk(os.getcwd()):
    # Skip the 'images' directory itself
    if os.path.abspath(root) == images_dir:
        continue

    # Copy image files to the target directory
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in image_extensions:
            source_path = os.path.join(root, file)
            target_path = os.path.join(images_dir, file)

            # Handle potential name collisions by renaming
            base_name, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(target_path):
                target_path = os.path.join(images_dir, f"{base_name}_{counter}{ext}")
                counter += 1

            shutil.copy2(source_path, target_path)
            print(f"Copied: {source_path} to {target_path}")

print("Image file copy operation complete.")

import os

def count_images_recursive(folder_path):
    image_count = 0

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            image_count += count_images_recursive(item_path)
        elif item.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_count += 1
    
    return image_count

def count_images_in_folders(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            total_image_count = count_images_recursive(folder_path)
            print(f"Total images in {folder_name}: {total_image_count}")

root_folder = "/home/duy/Documents/Competition/Video-Text-Retrieval/Database"
count_images_in_folders(root_folder)

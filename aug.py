from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

# Path to dataset
base_folder = 'archive'
target_size = (224, 224)  # Resize dimensions (height, width)

# Function to resize and save the image
def resize_image(img_path, save_to_dir, filename):
    try:
        img = load_img(img_path)  # Load the image
        img = img.resize(target_size)  # Resize the image to the target size
        img_array = img_to_array(img)  # Convert to array

        # Save the resized image
        save_path = os.path.join(save_to_dir, filename)
        img.save(save_path)  # Save the resized image
    except Exception as e:
        print(f"Error resizing {img_path}: {e}")

# Loop through each class folder and resize images
for class_folder in os.listdir(base_folder):
    class_path = os.path.join(base_folder, class_folder)
    if not os.path.isdir(class_path):
        continue  # Skip if not a directory

    print(f"Resizing images in class: {class_folder}")

    # Resize each image in the class folder
    for filename in os.listdir(class_path):
        img_path = os.path.join(class_path, filename)
        resize_image(img_path, class_path, filename)

print("Resizing completed.")


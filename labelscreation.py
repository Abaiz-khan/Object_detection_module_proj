import cv2
import os

# Path to the directory containing images
image_dir = '/images'
output_dir = '/labels'

# Define your class IDs here (for example: 0 for "Left Turn", 1 for "Steep Slope")
class_labels = {
    'left_turn': 0,
    'steep_slope': 1
}

# Define bounding box data for each image
# Each entry is: filename, class_label, (x_min, y_min, x_max, y_max)
# Replace with your actual bounding boxes
bounding_boxes = {
    'left.jpg': [('left_turn', (150, 100, 450, 400))],
    'steep.jpeg': [('steep_slope', (120, 80, 380, 350))]
}

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each image
for image_file, objects in bounding_boxes.items():
    # Load the image
    img_path = os.path.join(image_dir, image_file)
    image = cv2.imread(img_path)
    h, w, _ = image.shape

    # Prepare the .txt annotation file
    label_file = os.path.join(output_dir, f"{os.path.splitext(image_file)[0]}.txt")
    
    with open(label_file, 'w') as f:
        for label, (x_min, y_min, x_max, y_max) in objects:
            # Calculate YOLO format values
            class_id = class_labels[label]
            x_center = ((x_min + x_max) / 2) / w
            y_center = ((y_min + y_max) / 2) / h
            width = (x_max - x_min) / w
            height = (y_max - y_min) / h
            
            # Write the annotation line to file
            f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

    print(f"Created label file: {label_file}")

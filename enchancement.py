from PIL import Image, ImageEnhance
import os

# Set the input and output folder paths
input_folder = "/home/moil-dev002/Downloads/enhancement_FingerPrint/Dataset/eddy_png/"
output_folder = "/home/moil-dev002/Downloads/enhancement_FingerPrint/Dataset/eddy_enhancement/"

# Get a list of all PNG image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

# Loop through each PNG image file and enhance it
for image_file in image_files:
    # Open the image file using Pillow
    image_path = os.path.join(input_folder, image_file)
    image = Image.open(image_path)

    # Enhance the image
    enhancer = ImageEnhance.Sharpness(image)
    enhanced_image = enhancer.enhance(9.8)

    # Create the output file path by appending "_enhanced" to the file name
    enhanced_file = os.path.splitext(image_file)[0] + '_enhanced.png'
    enhanced_path = os.path.join(output_folder, enhanced_file)

    # Save the enhanced image as a PNG file
    enhanced_image.save(enhanced_path, 'PNG')
    print("success convert to enhanced")

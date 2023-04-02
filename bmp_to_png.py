from PIL import Image
import os

# Set the input and output folder paths
input_folder = "/home/moil-dev002/Downloads/finger_print/dataset/eddy/"
output_folder = "/home/moil-dev002/Downloads/finger_print/dataset/eddy_png/"

# Get a list of all BMP files in the input folder
bmp_files = [f for f in os.listdir(input_folder) if f.endswith('.bmp')]

# Loop through each BMP file and convert it to PNG
for bmp_file in bmp_files:
    # Open the BMP file using Pillow
    bmp_path = os.path.join(input_folder, bmp_file)
    bmp_img = Image.open(bmp_path)

    # Create the output file path by changing the extension to PNG
    png_file = os.path.splitext(bmp_file)[0] + '.png'
    png_path = os.path.join(output_folder, png_file)

    # Save the image as a PNG file
    bmp_img.save(png_path, 'PNG')
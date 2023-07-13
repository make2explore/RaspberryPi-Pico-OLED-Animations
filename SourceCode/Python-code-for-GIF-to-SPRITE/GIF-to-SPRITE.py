#================================== make2explore.com =================================#
# About Python Code  - This Python code Converts Animated icon GIF to SPRITE Sheet
#                      Bitmap Image
# Used in Following 
# Project/Tutorial   - Animations on SSD1306 Monochrome OLED Display interfaced
#                      Raspberry Pi Pico
# Referred by        - info@make2explore.com
# Last Modified      - 13/07/2023 04:30:00 @admin
# Software           - CircuitPython 8.2.0, Thonny IDE 4.1, Pico Lib Bundle 8.x
# Hardware           - Raspberry Pi Pico, SSD1306 Monochrome OLED Display
# Sensor Used        - Null
# Source Repo        - github.com/make2explore
#
# Source Code credits (@Nick) : http://educ8s.tv
#=====================================================================================#


from os import listdir
from PIL import Image

OUTPUT_SIZE = (64,64) # The output size of each frame (or tile or Sprite) of the animation
MONOCHROME = True # Do you want the output file to be b/w?

for file in listdir():
    if file.endswith('youtube-logo.gif'):
        gif = Image.open(file)
        print(f"Size: {gif.size}")
        print(f"Frames: {gif.n_frames}")

        if MONOCHROME:
            output = Image.new("1", (OUTPUT_SIZE[0] * gif.n_frames, OUTPUT_SIZE[1]), 0)
        else:
            output = Image.new("RGB", (OUTPUT_SIZE[0] * gif.n_frames, OUTPUT_SIZE[1]))

        output_filename = f"icon_{gif.n_frames}_frames.bmp"

        for frame in range(0,gif.n_frames):
            gif.seek(frame)
            extracted_frame = gif.resize(OUTPUT_SIZE)
            position = (OUTPUT_SIZE[0]*frame, 0)
            output.paste(extracted_frame, position)

        if not MONOCHROME:
            output = output.convert("P", colors = 8)
        output.save(output_filename)

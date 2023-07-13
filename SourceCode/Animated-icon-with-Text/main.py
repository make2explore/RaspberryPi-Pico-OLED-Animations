#================================== make2explore.com =================================#
# Project/Tutorial   - Animations on SSD1306 Monochrome OLED Display interfaced
#                      Raspberry Pi Pico
# Version            - (Animation With Text Label)
# Created By         - info@make2explore.com
# Last Modified      - 13/07/2023 04:30:00 @admin
# Software           - CircuitPython 8.2.0, Thonny IDE 4.1, Pico Lib Bundle 8.x
# Hardware           - Raspberry Pi Pico, SSD1306 Monochrome OLED Display
# Sensor Used        - Null
# Source Repo        - github.com/make2explore
#=====================================================================================#

# Import required libraries for Display, time and Font
import board, busio, displayio, time, terminalio
import adafruit_displayio_ssd1306
import adafruit_imageload
from adafruit_display_text import label

# Converted bitmap file - SPRITE Sheet image
IMAGE_FILE = "icon_28_frames.bmp"
SPRITE_SIZE = (64, 64)
FRAMES = 28

# Function for Monochrome displays to invert the background color
def invert_colors():
    temp = icon_pal[0]
    icon_pal[0] = icon_pal[1]
    icon_pal[1] = temp

displayio.release_displays()

# I2C pin mapping - SDA->GP0 & SCL->GP1 
sda, scl = board.GP0, board.GP1
i2c = busio.I2C(scl, sda)

# Initialize I2C display with device address 0x3C
# Display Width x Height for SSD1306 = 128x64 Pixels
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

group = displayio.Group()

# load the spritesheet
icon_bit, icon_pal = adafruit_imageload.load(IMAGE_FILE,
                                                 bitmap=displayio.Bitmap,
                                                 palette=displayio.Palette)
invert_colors()

# Cordinates x=32, y=0 To keep icon animation at the center of Display
icon_grid = displayio.TileGrid(icon_bit, pixel_shader=icon_pal,
                                 width=1, height=1,
                                 tile_height=SPRITE_SIZE[1], tile_width=SPRITE_SIZE[0],
                                 default_tile=0,
                                 x=32, y=0)

# Append the icon grid to Display(Image) group
group.append(icon_grid)

# Create Text label at location x=18, y=60 below animated icon
# We have used default terminalio font. If you want to use custom font, then 
# Create font folder in CIRCUITPY root directory and put related .bdf file into it
text = "make2explore.com"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=18, y=60)

# Append the text label to Text group
group.append(text_area)

# Display both SPRITE Sheet image and Text Label
display.show(group)

# Timer Variables
timer = 0
pointer = 0

# Following loop make sure that (SPRITE Sheet Images) Displayed 
# in continous sequence so that it will create Animation Effect

while True:
  if (timer + 0.1) < time.monotonic():
    icon_grid[0] = pointer
    pointer += 1
    timer = time.monotonic()
    if pointer > FRAMES-1:
      pointer = 0

#=====================================================================================#
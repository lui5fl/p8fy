# -*- coding: utf-8 -*-

# p8fy / by luisfl.me


from math import sqrt
from PIL import Image, ImageEnhance
import time


from . import constants


# Open image with PIL
def open_image(path):
    return Image.open(path)


# Crop image to a 1:1 aspect ratio
def crop_image(image):
    width, height = image.size
    shortest_dim = min(width, height)
    return image.crop((0, 0, shortest_dim, shortest_dim))


# Resize image to 128x128 px (PICO-8 screen size)
def resize_image(image):
    return image.resize((128, 128))


# Enhance color/saturation of the image by a factor
def saturate_image(image, factor):
    return ImageEnhance.Color(image).enhance(factor)


# Transform image to use PICO-8's color palette
def transform_image(image, rgb_weights_preset):
    return convert_colors_to(constants.PICO8_PALETTE, image, rgb_weights_preset)


# Save "p8fied" image
def save_image(image, path):
    date = time.strftime("%d%m%y-%H%M%S")
    image.save(f"_p8fied-{date}.".join(path.rsplit('.', 1)))


# Convert image to use a certain color palette
def convert_colors_to(palette, image, rgb_weights_preset):
    pixels = image.load()
    width, height = image.size
    for i in range(width):
        for j in range(height):
            color = pixels[i, j]
            pixels[i, j] = hex_color_to_rgb(closest_color_from(palette, color, rgb_weights_preset))
    return image


# Convert color from hexadecimal to RGB
def hex_color_to_rgb(color):
    hex_color = color.replace("#", "")
    hex_red, hex_green, hex_blue = "0x" + hex_color[0:2], "0x" + hex_color[2:4], "0x" + hex_color[4:6]
    r, g, b = int(hex_red, 0), int(hex_green, 0), int(hex_blue, 0)
    return (r, g, b)


# Get closest color from a certain palette to a specific color
def closest_color_from(palette, rgb_color, rgb_weights_preset):
    lowest_difference = -1
    closest_color = ""
    for palette_color in palette:
        rgb_weights = constants.RGB_WEIGHTS_PRESETS[rgb_weights_preset]
        difference = difference_between_colors(rgb_color, hex_color_to_rgb(palette_color), rgb_weights)
        if lowest_difference < 0 or difference < lowest_difference:
            lowest_difference = difference
            closest_color = palette_color
    return closest_color


# Calculate difference between two colors
def difference_between_colors(rgb0, rgb1, rgb_weight = None):
    if rgb_weight: r_w, g_w, b_w = rgb_weight
    else: r_w, g_w, b_w = 1, 1, 1
    r0, g0, b0 = rgb0[0], rgb0[1], rgb0[2]
    r1, g1, b1 = rgb1[0], rgb1[1], rgb1[2]
    return sqrt(((r1-r0)*r_w)**2 + ((g1-g0)*g_w)**2 + ((b1-b0)*b_w)**2)

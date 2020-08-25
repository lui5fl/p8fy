# -*- coding: utf-8 -*-

# p8fy / by luisfl.me


from . import helpers


def image(path, importable = False, saturation = 2.0, rgb_weights_preset = 0):
    """
    Transform an image to use PICO-8's color palette, taking into account a
    series of parameters

    # Arguments
        path: 
            Path of the image to be transformed
        importable: 
            Optional boolean value. If True the original image is cropped to a
            1:1 aspect ratio and resized to 128x128 pixels so that it can
            easily be imported into PICO-8
        saturation: 
            Optional float value. The original image's colors are saturated by
            this factor. A factor greater than 0 may increase the accuracy of 
            the image's colors conversion
        rgb_weights_preset: 
            Optional integer value. There are currently 3 RGB weights presets
            to choose from:
            - 0: nice balance of colors
            - 1: less green
            - 2: supposedly kind to the human eye

    # Returns
        Pillow Image instance

    # Raises
        ValueError: 
            Invalid value for argument `rgb_weights_preset`
    """
    
    if rgb_weights_preset not in [0, 1, 2]:
        raise ValueError('`rgb_weights_preset` must be 0, 1 or 2')

    image = helpers.open_image(path)
    if importable: 
        image = helpers.crop_image(image)
        image = helpers.resize_image(image)
    image = helpers.saturate_image(image, saturation)
    image = helpers.transform_image(image, rgb_weights_preset)
    helpers.save_image(image, path)
    return image

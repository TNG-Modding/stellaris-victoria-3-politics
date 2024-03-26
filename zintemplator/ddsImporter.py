import os
import shutil
import imageio
import numpy as np
from PIL import Image
from scipy.ndimage import zoom

spriteTypes = ""
sourceDir = "C:/Program Files (x86)/Steam/steamapps/common/Stellaris/gfx/interface/icons/buildings"
iconDestination = "C:/Users/User/Documents/Paradox Interactive/Stellaris/mod/victoria-3-revolutions/gfx/interface/icons/text_icons"

originalSize = 98
pixels_to_shift = 15
scale_factor = 2.5
def clipped_zoom(img, zoom_factor, **kwargs):

    h, w = img.shape[:2]

    # For multichannel images we don't want to apply the zoom factor to the RGB
    # dimension, so instead we create a tuple of zoom factors, one per array
    # dimension, with 1's for any trailing dimensions after the width and height.
    zoom_tuple = (zoom_factor,) * 2 + (1,) * (img.ndim - 2)

    # Zooming out
    if zoom_factor < 1:

        # Bounding box of the zoomed-out image within the output array
        zh = int(np.round(h * zoom_factor))
        zw = int(np.round(w * zoom_factor))
        top = (h - zh) // 2
        left = (w - zw) // 2

        # Zero-padding
        out = np.zeros_like(img)
        out[top:top+zh, left:left+zw] = zoom(img, zoom_tuple, **kwargs)

    # Zooming in
    elif zoom_factor > 1:

        # Bounding box of the zoomed-in region within the input array
        zh = int(np.round(h / zoom_factor))
        zw = int(np.round(w / zoom_factor))
        top = (h - zh) // 2
        left = (w - zw) // 2

        out = zoom(img[top:top+zh, left:left+zw], zoom_tuple, **kwargs)

        # `out` might still be slightly larger than `img` due to rounding, so
        # trim off any extra pixels at the edges
        trim_top = ((out.shape[0] - h) // 2)
        trim_left = ((out.shape[1] - w) // 2)
        out = out[trim_top:trim_top+h, trim_left:trim_left+w]

    # If zoom_factor == 1, just return the input array
    else:
        out = img
    return out

def resize_dds(input_path, output_path, new_width, new_height):
    # Read the .dds file
    image = imageio.imread(input_path)

    # Resize the image
    shifted_image = np.roll(image, -15, axis = 1)
    shifted_image = np.roll(shifted_image, 5, axis = 0)

    # shifted_image = np.zeros_like(image)

    # # Loop through each row and shift pixels to the left
    # for y in range(originalSize):
    #     shifted_row = np.roll(image[y], -pixels_to_shift, axis=0)
    #     shifted_image[y] = shifted_row

    zoomed_image = clipped_zoom(shifted_image, 1.4)

    resized_image = np.array(Image.fromarray(zoomed_image).resize((new_width, new_height)))
    imageio.imwrite(output_path, resized_image)

new_width = 32
new_height = 32

for filename in os.listdir(sourceDir):
    if not filename.endswith('.dds'):
        continue
    # print(filename)
    trait = filename.split(".")[0]
    spriteTypes += 'spriteType = { name = "GFX_text_%s" texturefile = "gfx/interface/icons/text_icons/%s" }\n' % (trait, filename)
    # shutil.copyfile(os.path.join(sourceDir, filename), os.path.join(iconDestination, filename))
    resize_dds(os.path.join(sourceDir, filename), os.path.join(iconDestination, filename), new_width, new_height)
    print(filename)
    # break

fileContents = """
spriteTypes = {
%s
}
""" % spriteTypes
print(fileContents)

graphicFileDestination = "C:/Users/User/Documents/Paradox Interactive/Stellaris/mod/victoria-3-revolutions/interface/00_text_icon_buildings.gfx"

f = open(graphicFileDestination, "w")
f.write(fileContents)
f.close()
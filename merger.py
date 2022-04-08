import os
import re
import argparse
from PIL import Image

# Simple image merger by Arik#2428

parser = argparse.ArgumentParser(description='Merge some images.')
parser.add_argument('-f', dest="file", type=str,
                    help='the output file')
args = parser.parse_args()

file_output = args.file

if file_output is None:
    file_output = "merged.png"

# From https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
images = [Image.open(x) for x in [file for file in os.listdir("./") if re.search("(\\.(png|jpeg|jpg|tif))$", file)]]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

new_im.save(file_output)

print(f"Saved merged image into {file_output}")

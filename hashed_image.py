#!/usr/bin/python3
# Takes a string, hashes it, and generates an image from it

from PIL import Image
import hashlib
import math


# https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
def hex_to_rgb(value):
    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))


block_size = 128, 128
hex_color_str_len = 6

bday_prefix = "Happy Birthday "
bday_suffix = "!"

bday_person = "Shaun Greene"

bday_message = bday_prefix + bday_person + bday_suffix
bday_hash = hashlib.sha384(str.encode(bday_message)).hexdigest()
blocks = len(bday_hash) // hex_color_str_len
block_sqrt = int(math.sqrt(blocks))

print(bday_hash)
print('#blocks: ', blocks)

# logic from https://gist.github.com/glombard/7cd166e311992a828675
result = Image.new('RGB', tuple(block_sqrt*x for x in block_size))
print("Final size: ", result)
for i in range(0, len(bday_hash), hex_color_str_len):
    rgb = hex_to_rgb(bday_hash[i:i+hex_color_str_len])
    print("i=", i)
    print('RGB = {}'.format(rgb))
    print(bday_hash[i:i+hex_color_str_len])
    img = Image.new('RGB', block_size, hex_to_rgb(bday_hash[i:i+5]))
    x = int(i / hex_color_str_len) // block_sqrt * block_size[0]
    y = int(i / hex_color_str_len) % block_sqrt * block_size[1]
    w, h = block_size
    print("x=%d, y=%d, w=%d, h=%d, x+w=%d, y+h=%d" % (x, y, w, h, x + w, y + h))
    result.paste(img, (x, y, x + w, y + h))

# img.save('pil_color.png')
result.show()
print("done")

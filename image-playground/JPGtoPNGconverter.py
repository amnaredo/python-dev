import sys
import os
from PIL import Image

# grab first and second argument
source_dir = sys.argv[1]
target_dir = sys.argv[2]

# check if directories exist
if not os.path.exists(source_dir):
    print(f'Directory {source_dir} does not exist')
    exit

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

for image_file in os.listdir(source_dir):
    filename, ext = os.path.splitext(image_file)
    image = Image.open(source_dir + '\\' + image_file)
    image.save(target_dir + '\\' + filename + '.png')
print('all done!')

import os
from PIL import Image
base_path = "ami/"
new_path = "ami/grayscale/"
for infile in os.listdir(base_path):
  if infile[-3:] == "jpg" or infile[-3:] == "jpeg" :
    print ("file : " + infile)
    im = Image.open(os.path.join(base_path, infile))
    outfile = new_path + infile
    im.thumbnail(im.size)
    im = im.convert('L')
    im.save(outfile, "JPEG", quality=100)
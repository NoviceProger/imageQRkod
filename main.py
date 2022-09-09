# pip install pillow
from PIL import Image

im1 = Image.open('QR1.png')
im2 = Image.open('DM-Sticker_Custom-12x16cm_blank-for-template.png')
newsize = (580, 580)
im1 = im1.resize(newsize)
# im1.save()
# im1.show()

im2.paste(im1, (178, 735))
im2.save('DM-Sticker_QR1.png', quality=95)

im1.close()
im2.close()

# pip install pillow
from PIL import Image
import os

im2 = Image.open('DM-Sticker_Custom-12x16cm_blank-for-template.png')
newsize = (580, 580)

dirPath = r"D:\ResultQR\QR"
extensions = (".jpg", ".png", ".jpeg", ".bmp")

for root, dirs, files in os.walk(dirPath):
	for filename in files:
		if os.path.isfile(os.path.join(dirPath, filename)):
			if filename.endswith(extensions):
				# filelist.append(os.path.join(dirPath, filename))
				im1 = Image.open(f"{os.path.join(dirPath, filename)}")
				im1 = im1.resize(newsize)
				# im1.save()
				# im1.show()
				im2.paste(im1, (178, 735))
				namefile = f"{str(filename).split('.')[0]}"
				im2.save(f"D:\ResultQR\{namefile}_DM-Sticker.png", quality=95)

im1.close()
im2.close()

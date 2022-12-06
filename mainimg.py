from PIL import Image
from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('img/whitetext.png')
im2 = Image.open('img/red.png')
im2.thumbnail((400, 400))

back_im = im1.copy()
back_im.paste(im2, (100, 50))
back_im.save('img/output.png', quality=95)


# #img.resize((400, 400))  --- ratio should be same for resize
# 
# # background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
# background = Image.new('RGBA', (1440, 900), 'img/white.png')
# background.paste(img, (720,0))
# background.save('img/out.png')
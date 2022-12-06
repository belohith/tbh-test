from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('img/whitetext.png')
im2 = Image.open('img/red.png')
im2.thumbnail((400, 400))

mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.rounded_rectangle((0,0,0,0), 10, "yellow")
mask_im.save('img/rect.png', quality=95)

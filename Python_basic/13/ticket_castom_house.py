

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


im_data = Image.open("images/ticket_sample.png")
print(im_data.format, im_data.size, im_data.mode)

w, h = im_data.size
im_upd = im_data.resize((w // 2, h // 2))
im_upd.format = 'PNG'
print(im_upd.format, im_upd.size, im_upd.mode)
im_upd = im_data
draw = ImageDraw.Draw(im_upd)
font_path = os.path.join("fonts", "ofont.ru_TimesET95N.ttf")
font = ImageFont.truetype(font_path, size=20)
draw.text((200, 125), "Clear to pass (Castom house)", font=font, fill=(255,0,0))

# im_upd.save("test/plane_ticket_hw.png")
im_upd.save("castom_house.png")














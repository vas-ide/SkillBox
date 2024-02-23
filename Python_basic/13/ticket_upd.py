import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketInfoAdd:

    def __init__(self, template=None, font_path=None, first_name=None, name=None, last_name=None, date=None,
                 departure=None, destination=None):
        self.template = Image.open("images/ticket_template.png")
        # self.template = Image.open("images/ticket_template.png") if template is None else template
        # self.font_path = os.path.join("fonts", "ofont.ru_TimesET95N.ttf") if font_path is None else font_path
        # self.first_name = f"Maximus" if first_name is None else first_name
        # self.name = f"Decie" if name is None else name
        # self.last_name = f"Meridie" if last_name is None else last_name
        # self.date = f"23.02.2024" if date is None else date
        # self.departure = "Earth" if departure is None else departure
        # self.destination = "Mars" if destination is None else destination

    def image(self):
        img = Image.open(self.template)
        # draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(self.font_path, size=20)
        #
        # draw.text((50, 150), f"{self.first_name}{self.name[0].upper()}.{self.last_name[0].upper()}.", font=font, fill=(47, 79, 79))
        # im.save(f"test_ticket", "PNG")
        img.show()



    def add_info(self):
        pass

    def run(self):
        self.image()
        # self.template.show()
        pass

    pass


if __name__ == '__main__':
    ticket = TicketInfoAdd()
    ticket.run()

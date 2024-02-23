import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketInfoAdd:

    def __init__(self, template=None, font_path=None, first_name=None, name=None, last_name=None, date=None,
                 departure=None, destination=None):
        self.template = template

        self.font_path = os.path.join("fonts", "ofont.ru_TimesET95N.ttf") if font_path is None else font_path
        self.first_name = f"Unknown" if first_name is None else first_name
        self.name = f"Unknown" if name is None else name
        self.last_name = f"Unknown" if last_name is None else last_name
        self.date = f"01.01.2000" if date is None else date
        self.departure = "Earth" if departure is None else departure
        self.destination = "Earth" if destination is None else destination

    def analize(self):
        if self.first_name is None:
            self.first_name = "Unknown"
        if self.name is None:
            self.name = "Unknown"
        if self.last_name is None:
            self.last_name = "Unknown"


    def img_writing(self):
        if self.template is None:
            img = Image.open("images/ticket_template.png")
        else:
            img = Image.open(self.template)
        height, wight = img.size

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font_path, size=18)
        color = (47, 79, 79)
        draw.text((wight // 9, height // 5.45),
                  f"{self.first_name} {self.name[0].upper()}.{self.last_name[0].upper()}.",
                  font=font, fill=color)
        draw.text((wight // 9, height // 3.5), f"{self.departure}.", font=font, fill=color)
        draw.text((wight // 9, height // 2.65 + 5), f"{self.destination}.", font=font, fill=color)
        draw.text((wight // 1.4, height // 2.65 + 5), f"{self.date[0:5]}", font=font, fill=color)
        img.show()

    def run(self):
        self.analize()
        self.img_writing()


if __name__ == '__main__':
    ticket = TicketInfoAdd(first_name=f"Maximus", name=f"Decie", last_name=f"Meridie")
    ticket.run()

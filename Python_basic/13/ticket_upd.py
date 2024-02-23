
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketInfoAdd:

    def __init__(self):
        self.im_data = Image.open("images/ticket_template.png")

    def image(self):
        pass

    def add_info(self):
        pass

    def run(self):
        self.im_data.show()
        pass
    pass

ticket = TicketInfoAdd()
ticket.run()
















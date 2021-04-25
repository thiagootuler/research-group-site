import os
from PIL import Image

class ImageEditor:
    def __init__(self, max_width, max_height, file_in, file_out):
        self.ratio = 1. * max_width / max_height
        self.im = Image.open(file_in)
        self.width, self.height = self.im.size
        self.max_width = max_width
        self.max_height = max_height
        self.fout = file_out
        self.ext = os.path.splitext(file_out)[1][1:]

    def crop(self):
        # crop the image on the left and right side and keep the height of the image
        if self.width > self.height * self.ratio:
            newwidth = int(self.height * self.ratio)
            left = self.width / 2 - newwidth / 2
            right = left + newwidth
            top = 0
            bottom = self.height
        # crop the image on the top and bottom and keep the width of the image
        elif self.width < self.height * self.ratio:
            newheight = int(self.width * self.ratio)
            top = self.height / 2 - newheight / 2
            bottom = top + newheight
            left = 0
            right = self.width
        if self.width != self.height * self.ratio:
            self.im = self.im.crop((left, top, right, bottom))

    def resize(self):
        self.im = self.im.resize((self.max_width, self.max_width), Image.ANTIALIAS)

    def save(self):
        self.im.save(self.fout, self.ext.upper(), quality=100)
        self.im.close()

if __name__ == "__main__":
    editor = ImageEditor(250, 250, "uploads/membro/download.png", "uploads/membro/download2.png")
    editor.crop()
    editor.resize()
    editor.save()

from zonemap import ZoneMap
from parse import Entry
from PIL import Image, ImageDraw, ImageColor, ImageFont
import os

class GifMap(ZoneMap):
   
    def __init__(self, mapID, framerate=5, suffix=""):
        self.framerate = framerate
        self.frames = []
        self.suffix = suffix
        super(GifMap, self).__init__(mapID) 

    
    def add_point(self, entry, draw_line=False):
        frame = self.img.copy()
        frameDraw = ImageDraw.ImageDraw(frame)
        ax = entry.pos[0] * self.img.width
        ay = entry.pos[1] * self.img.height
        fill, scale = self.get_params_by_event(entry.ID)
        frameDraw.ellipse(self.construct_ellipse(ax, ay, scale=scale), fill=fill, outline=(0, 0, 255))
        self.frames.append(frame)

    def get_file_save_name(self):
        return "maps/" + self.get_map_name() + "/", self.suffix + ".gif"
         
    def save(self):
        dir, file = self.get_file_save_name()
        if not os.path.exists(dir):
            os.makedirs(dir)
        print(self.frames)
        self.frames[0].save(dir + file, format='GIF', append_images=self.frames[1:], save_all=True, duration=self.framerate, loop=0)

if __name__ == '__main__':
    g = GifMap(1412)

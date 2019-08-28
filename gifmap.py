from zonemap import ZoneMap
from parse import Entry
from PIL import Image, ImageDraw, ImageColor, ImageFont
import os

class GifMap(ZoneMap):
   
    def __init__(self, mapID, framerate=5, suffix=None):
        self.framerate = framerate
        self.frames = []
        self.suffix = suffix
        super(GifMap, self).__init__(mapID) 

    

    
    def add_point(self, entry, draw_line=False, last_frame=False):
        frame = self.img.copy()
        ax = entry.pos[0] * self.img.width
        ay = entry.pos[1] * self.img.height
        if entry.ID < 200:
            frameDraw = ImageDraw.ImageDraw(frame)
        else:
            frameDraw = self.imgdraw
        fill, scale = self.get_params_by_event(entry.ID)
        frameDraw.ellipse(self.construct_ellipse(ax, ay, scale=scale), fill=fill, outline=(0, 0, 255))
        if not last_frame:
            ZoneMap.drawCow(self, frame, (int(ax), int(ay)))
        self.frames.append(frame)

    def get_file_name(self):
        if self.suffix and int(self.suffix) > 0:
            path = "maps/" + self.get_map_name() + "/" + str((int(self.suffix) - 1)) + ".png"
            while not os.path.exists(path):
                self.suffix = str(int(self.suffix) - 1)
                path = "maps/" + self.get_map_name() + "/" + str((int(self.suffix) - 1)) + ".png"
                if int(self.suffix) <= 0:
                    return ZoneMap.get_file_name(self)
            return path
        return ZoneMap.get_file_name(self)

    def get_file_save_name(self):
        return "maps/" + self.get_map_name() + "/", self.suffix + ".gif"
    
    def get_static_save_name(self, suffix=None):
        if not suffix:
            suffix = self.suffix
        return suffix + ".png"
         
    def save(self):
        dir, file = self.get_file_save_name()
        if not os.path.exists(dir):
            os.makedirs(dir)
        print(self.frames)
        self.frames[0].save(dir + file, format='GIF', append_images=self.frames[1:], save_all=True, duration=self.framerate, loop=0)
        self.frames[-1].save(dir + self.get_static_save_name())

if __name__ == '__main__':
    g = GifMap(1412)

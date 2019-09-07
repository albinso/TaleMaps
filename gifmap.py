import imageio
from zonemap import ZoneMap
from parse import Entry
from PIL import Image, ImageDraw, ImageColor, ImageFont
import os
import numpy as np

class GifMap(ZoneMap):
   
    def __init__(self, mapID, framerate=50, suffix=None, writer=None):
        self.framerate = framerate
        self.zoneid = mapID
        self.frames = []
        self.suffix = suffix
        self.lasttimestamp = None
        self.cornerfont = ImageFont.truetype("/usr/share/fonts/TTF/VeraMoBd.ttf", 35)
        super(GifMap, self).__init__(mapID) 
        if writer == None:
            path, name = self.get_file_save_name()
            os.mkdir(path)
            self.writer = imageio.get_writer(path + name, fps=20)
        else:
            self.writer = writer
    
    def add_point(self, entry, draw_line=False, last_frame=False):
        frame = self.img.copy()
        ax = entry.pos[0] * self.img.width
        ay = entry.pos[1] * self.img.height
        if entry.ID < 200:
            frameDraw = ImageDraw.ImageDraw(frame)
        else:
            frameDraw = self.imgdraw
        fill, outline, scale = self.get_params_by_event(entry.ID)
        frameDraw.ellipse(self.construct_ellipse(ax, ay, scale=scale), fill=fill, outline=outline)
        tx = 0.9*self.img.width
        ty = 0.9*self.img.height
        frameDraw.rectangle([(tx, ty), (tx+40, ty+40)], fill=(0, 0, 0))
        frameDraw.text((tx, ty), str(entry.level), fill=(255, 0, 0), font=self.cornerfont)
        if not last_frame:
            ZoneMap.drawCow(self, frame, (int(ax), int(ay)), entry.ID == 103)
        
        self.lasttimestamp = entry.timestamp
        self.writer.append_data(np.array(frame))
        self.lasttimestamp = entry.timestamp


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
        return "maps/" + self.get_map_name() + "/", self.suffix + ".mp4"
    
    def get_static_save_name(self, suffix=None):
        if not suffix:
            suffix = self.suffix
        return suffix + ".png"
         
    def save(self):
        self.writer.close()

if __name__ == '__main__':
    g = GifMap(1412)

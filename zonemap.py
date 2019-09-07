import sys
import math
from mappings import mapIDs 
from PIL import Image, ImageDraw, ImageColor, ImageFont
from entryids import ids as entryids, mapicons
from parse import StdEntry

class ZoneMap:

    def __init__(self, zoneid, dotsize=0.004):
        self.zoneid = zoneid
        self.load_map()
        self.prev_point = None
        self.previd = None
        self.dotsize = dotsize*self.img.width
        self.iconPath = "icons/tauren.png"
        self.font = ImageFont.truetype("/usr/share/fonts/TTF/VeraMoBd.ttf", 14)
        self.load_icon()
    
    def load_icon(self):
        self.icon = (Image.open(self.iconPath), Image.open("icons/ghostcow.png"))

    def get_map_name(self):
        return mapIDs[self.zoneid]

    def get_file_name(self):
        return "maps/" + self.get_map_name() + ".jpg"

    def get_file_save_name(self):
        return "maps/" + self.get_map_name() + ".png"

    def load_map(self):
        self.img = Image.open(self.get_file_name())
        self.imgdraw = ImageDraw.ImageDraw(self.img)

    def construct_ellipse(self, ax, ay, scale=1):
        dot = self.dotsize*math.sqrt(scale)
        x0 = ax - dot
        y0 = ay - dot
        x1 = ax + dot
        y1 = ay + dot
        return (x0, y0), (x1, y1)

    def get_params_by_event(self, event):
        return mapicons[event]

    def drawCow(self, img, pos, ghost):
        icon = self.icon[0]
        if ghost:
            icon = self.icon[1]
        ic = icon.resize((int(self.dotsize*9), int(self.dotsize*6)))
        pos = int(pos[0] - ic.width/2), int(pos[1] - ic.height/2)
        img.paste(ic, pos, mask=ic) 

    def add_text(self, entry, text):
        ax = entry.pos[0] * self.img.width
        ay = entry.pos[1] * self.img.height
        fill, outline, scale = self.get_params_by_event(entry.ID)
        dot = self.dotsize*math.sqrt(scale)
        self.imgdraw.text((ax+dot/2, ay+dot/2), text, fill=(0, 0, 0), font=self.font)

    def add_point(self, entry, draw_line=True):
        ax = entry.pos[0] * self.img.width
        ay = entry.pos[1] * self.img.height
        
        fill, outline, scale = self.get_params_by_event(entry.ID)

        
        self.imgdraw.ellipse(self.construct_ellipse(ax, ay, scale=scale), fill=fill, outline=outline)
        if self.prev_point and draw_line:
            width = 2 
            if self.previd == 101:
                self.imgdraw.line((self.prev_point, (ax, ay)), fill=(0, 0, 0), width=width)
            if self.previd == 102:
                self.imgdraw.line((self.prev_point, (ax, ay)), fill=(255, 255, 255), width=width)
            if self.previd == 103:
                self.imgdraw.line((self.prev_point, (ax, ay)), fill=(255, 0, 0), width=width)
        self.prev_point = ax, ay
        self.previd = entry.ID
    
    def save(self):
        self.img.save(self.get_file_save_name())



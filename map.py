import sys
import math
from mappings import mapIDs 
from PIL import Image, ImageDraw, ImageColor, ImageFont
from entryids import ids as entryids, mapicons
from parse import StdEntry

dotsize = 0.004

class ZoneMap:

    def __init__(self, zoneid):
        self.zoneid = zoneid
        self.load_map()
        self.prev_point = None
        self.previd = None

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
        dot = dotsize*self.img.width * math.sqrt(scale)
        x0 = ax - dot
        y0 = ay - dot
        x1 = ax + dot
        y1 = ay + dot
        return (x0, y0), (x1, y1)

    def get_params_by_event(self, event):
        return mapicons[event]

    def add_text(self, entry, text):
        ax = entry.pos[0] * self.img.width
        ay = entry.pos[1] * self.img.height
        font = ImageFont.truetype("/usr/share/fonts/TTF/VeraMoBd.ttf", 14)
        fill, scale = self.get_params_by_event(entry.ID)
        dot = dotsize*self.img.width * math.sqrt(scale)
        self.imgdraw.text((ax+dot/2, ay+dot/2), text, fill=(0, 0, 0), font=font)

    def add_point(self, entry, draw_line=True):
        ax = entry.pos[0] * self.img.width
        ay = entry.pos[1] * self.img.height
        
        fill, scale = self.get_params_by_event(entry.ID)

        
        self.imgdraw.ellipse(self.construct_ellipse(ax, ay, scale=scale), fill=fill, outline=(0, 0, 255))
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




def extractLog(fname):
    out = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('"'):
                out.append(line)
    return out

def formatLog(log):
    out = []
    funcs = [float, float, int, int, int, str] + [str] * (len(log[0])-6)
    for s in log:
        s = s.split('"')[1]
        entry = list(map(lambda x, y: x(y), funcs, s.split(",")))
        out.append(entry)
    return out

def main():
    logfilename = sys.argv[1]
    stringlog = extractLog(logfilename)

    zones = {}
    std_resolution = 1
    prevzone = 0
    i = -1
    log = [StdEntry(e) for e in stringlog]
    for entry in log:
        if prevzone != entry.mapID:
            i = -1
        i += 1
        if entry.ID > 200 or i % std_resolution != 0:
            continue
        if not entry.mapID in zones.keys():
            zones[entry.mapID] = ZoneMap(entry.mapID)
        zones[entry.mapID].add_point(entry, draw_line=entry.mapID == prevzone)
        prevzone = entry.mapID
    for entry in log:
        if entry.ID < 200:
            continue
        zones[entry.mapID].add_point(entry, draw_line=False)
    for entry in log:
        if entry.ID == 301:
            text = str(entry.level)
            zones[entry.mapID].add_text(entry, text)
    for zone in zones.values():
        zone.save()
if __name__ == "__main__":
    main()

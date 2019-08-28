import sys
import math
from mappings import mapIDs 
from PIL import Image, ImageDraw, ImageColor, ImageFont
from entryids import ids as entryids, mapicons
from parse import StdEntry
from zonemap import ZoneMap
from gifmap import GifMap





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

def makemap(log, suffix=""):
    std_resolution = 1
    prevzone = 0
    i = -1
    zones = {}
    last = len(log)-1
    revlog = reversed(log)
    for j, entry in enumerate(log):
        if prevzone != entry.mapID:
            i = -1
        i += 1
        if not entry.mapID in zones.keys():
            zones[entry.mapID] = GifMap(entry.mapID, suffix=suffix)
        
        last_point = next((i for i in reversed(log) if i.mapID == entry.mapID))
        last_frame = last_point.timestamp==entry.timestamp
        zones[entry.mapID].add_point(entry, draw_line=entry.mapID == prevzone, last_frame=last_frame)
        if entry.ID == 301:
            text = str(entry.level)
            zones[entry.mapID].add_text(entry, text)
        prevzone = entry.mapID
    for zone in zones.values():
        zone.save()


def main():
    logfilename = sys.argv[1]
    stringlog = extractLog(logfilename)

    batch = (int(sys.argv[2]), int(sys.argv[3]))
    log = [StdEntry(e) for e in stringlog[batch[0]:batch[1]]]
    makemap(log, suffix=sys.argv[4]) 
    
    


if __name__ == "__main__":
    main()

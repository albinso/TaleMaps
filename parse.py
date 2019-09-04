import sys

class Entry:

    def __init__(self, entry_string):

        self.funcs = [float, float, int, int, int, int] + [str] * 10
        self.entry = self.parse_entry(entry_string)
        self.pos = (None, None)
        self.mapID = None
        self.timestamp = None
        self.level = None
        self.ID = None
        self.fill_fields()
        self.fill_extra_fields()

    def parse_entry(self, entry_string):
        print(entry_string)
        entry = entry_string.split('"')[1]
        params = list(map(lambda x, y: x(y), self.funcs, entry.split(",")))
        return params

    def fill_fields(self):
        print(self.entry)
        self.pos = self.entry[0], self.entry[1]
        self.mapID = self.entry[2]
        self.timestamp = self.entry[3]
        self.level = self.entry[4]
        self.ID = self.entry[5]

    def fill_extra_fields(self):
        raise NotImplementedError("Entry subclasses must implement fill_extra_fields")


class StdEntry(Entry):

    def fill_extra_fields(self):
        pass

def main():
    out = []
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            print("Commas: " + line.count(","))
            if line.startswith('"') and line.count(",") >= 4:
                out.append(StdEntry(line))
    print(out[0].pos)


if __name__ == '__main__':
    main()


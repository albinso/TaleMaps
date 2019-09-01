## Usage

### Multipart gif
bash makegif.sh <Log file> <Number of entries to map> <Number of entries per gif>

I use 200 for the last parameter. Might be possible to go a bit higher though.

There are tools to combine gifs into one. I use gifsicle for this.

### All in one (SLOW!)
python map.py <Log file> <number of first entry> <number of last entry> <count>

Log file is found under _classic_/WTF/<Account>/<Realm>/<Character>/SavedVariables/Tale.lua

Second and third argument specify a range of mapped entries.

count must be a number. It's used when scripting to ensure that this run gets a unique number appended to filenames. Can be set to 0 if used standalone.


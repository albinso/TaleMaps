## Warning!
Making gifs using this tool is very slow. This scales exponentially with the size of the log you're trying to visualise, and the whole thing might crash or freeze if your log is too big. I use the makegif.sh script to reduce the immediate load on the computer and I suggest you do too. Making still pngs is much faster.

## Missing Maps
Some maps are not included here. This is just laziness from my part since there is no easy way to get them all bundled together. If you find that you need a map I haven't included you can find it yourself and save it in orgmaps. Make sure to make a mapping in mappings.py as well. MapID information for that can be found here: https://wow.gamepedia.com/UiMapID/Classic

## Usage

### Multipart gif
bash makegif.sh \<Log file\> \<Number of entries to map\> \<Number of entries per gif\>

I use 200 for the last parameter. Might be possible to go a bit higher though.

There are tools to combine gifs into one. I use gifsicle for this.

#### Example
bash makegif.sh Tale.lua 2000 200

### All in one (SLOW!)
python map.py <Log file> <number of first entry> <number of last entry> <count> <option>

Log file is found under _classic_/WTF/\<Account\>/\<Realm\>/\<Character\>/SavedVariables/Tale.lua

Second and third argument specify a range of mapped entries.

count must be a number. It's used when scripting to ensure that this run gets a unique number appended to filenames. Can be set to 0 if used standalone.

option can be either gif, lines or be left empty. gif makes an animated gif of the given log. If gif is not set then a png map will be created under maps. If lines is set the png map will have lines drawn between points corresponding to adjacent log entries.

#### Example
python map.py Tale.lua 0 200 0 line

## reset.sh
Deletes the maps folder and replaces it with the contents of orgmaps. This deletes any created images and gifs unless they have been moved from maps.

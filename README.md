## Missing Maps
Some maps are not included here. This is just laziness from my part since there is no easy way to get them all bundled together. If you find that you need a map I haven't included you can find it yourself and save it in orgmaps. Make sure to make a mapping in mappings.py as well. MapID information for that can be found here: https://wow.gamepedia.com/UiMapID/Classic

## Usage

#### Example
python map.py Tale.lua 0 500 mp4 60 foo.mp4

#### Parameters
python map.py \<Log file\> \<number of first entry\> \<number of last entry\> \<option\> (\<fps\> \<filename\>)

Log file is found under \_classic\_/WTF/\<Account\>/\<Realm\>/\<Character\>/SavedVariables/Tale.lua

Second and third argument specify a range of mapped entries. In the given example the log entries from 0 to 500 are mapped. We should be able to handle practically limitless logs provided enough processing time but we've tested it up to 50 000.

option can be either mp4, lines or be left empty. mp4 makes an mp4 timelapse video of the given log. If mp4 is not set then a png map will be created under maps. If lines is set the png map will have lines drawn between points corresponding to adjacent log entries.

fps should only be provided when making an mp4. If you think the cowhead is moving too quickly or slowly you can lower or increase this respectively.

filename should also only be provided when making an mp4. It determines the name of the output video file. Still images default to maps/<zonename>.png at the moment so this parameter is not necessary.

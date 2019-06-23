This program is for getting information about VDR-recordings without manually reading the info-file.
Another function is to move recordings named like "2019-03-28.23.13.30-0.rec" to a folder named like the episode ("episodename/2019-03-28.23.13.30-0.rec").



$ vdrrecinfo --help
usage: vdrrecinfo [-h] [--get-channel] [--get-channel-name] [--get-title]
                  [--get-subheading] [--get-description] [--contains-vdr-info]
                  [--move-to-subheading]
                  vdrfile [vdrfile ...]

positional arguments:
  vdrfile               Recording-directory or recinfo-file

optional arguments:
  -h, --help            show this help message and exit
  --get-channel         Prints channel
  --get-channel-name    Prints name of channel
  --get-title           Prints title
  --get-subheading      Prints subheading
  --get-description     Prints description
  --contains-vdr-info   Prints whether it's a valid file/directory
  --move-to-subheading  Moves recording to a folder named like the subheading


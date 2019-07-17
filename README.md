# vdrrecinfo

This program is for getting information about VDR-recordings without manually reading the info-file.
Another function is to move recordings named like "2019-03-28.23.13.30-0.rec" to a folder named like the episode ("episodename/2019-03-28.23.13.30-0.rec").


## Help output

```
$ vdrrecinfo --help
usage: vdrrecinfo [-h] [--get-channel] [--get-channel-name] [--get-title]
                  [--get-subheading] [--get-description] [--contains-vdr-info]
                  [--move-to-subheading] [--move-to-title]
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
  --move-to-title       Moves recording to a folder named like the title
```


## Examples

```
$ ls Weissensee
2018-03-13.23.00.1-0.rec  2018-05-19.20.15.6-0.rec  2018-05-19.21.00.6-0.rec  2018-05-20.21.00.6-0.rec  2018-05-22.00.05.6-0.rec  2018-05-22.00.50.6-0.rec
$ vdrrecinfo --get-subheading Weissensee/*
Operation Juninacht (1) / Die verlorene Tochter (2)
Alte Wunden
Geister
Blühendes Land
Alte Wunden
Geister
```

```
$ ls Weissensee
2018-03-13.23.00.1-0.rec  2018-05-19.20.15.6-0.rec  2018-05-19.21.00.6-0.rec  2018-05-20.21.00.6-0.rec  2018-05-22.00.05.6-0.rec  2018-05-22.00.50.6-0.rec
$ vdrrecinfo --move-to-subheading Weissensee/*
$ ls Weissensee
Alte_Wunden  Blühendes_Land  Geister  Operation_Juninacht_(1)____Die_verlorene_Tochter_(2)
```

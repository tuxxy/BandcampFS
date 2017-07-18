# BackupCamp
BackupCamp is a proof of concept that allows people to backup files to bandcamp

## Usage
### Encoding
Encoding a file to upload to bandcamp is simple:

`./backupcamp.py -e my_favorite_picture.jpg`

When it's done, you'll see:

`Data encoded to: my_favorite_picture.jpg.wav!`

Take the file generated here and upload it to a Bandcamp album.

### Decoding
Decoding is done the same way:

`./backupcamp.py -d my_favorite_picture.jpg.wav`

When it's done, you'll see:

`Data decoded to: my_favorite_picture.jpg!`

That's it!

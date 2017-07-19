# BandcampFS
BandcampFS is a proof of concept that allows people to backup files to bandcamp

## Usage
### Encoding
Encoding a file to upload to bandcamp is simple:

`./bandcampfs.py -e my_favorite_picture.jpg`

When it's done, you'll see:

`Data encoded to: my_favorite_picture.jpg.wav!`

Take the file generated here and upload it to a Bandcamp album.

### Decoding
Decoding is done the same way:

`./bandcampfs.py -d my_favorite_picture.jpg.wav`

When it's done, you'll see:

`Data decoded to: my_favorite_picture.jpg!`

That's it!

## How does this work?
BandcampFS simply converts any file into a WAV file. Go ahead and give your resume a listen.

## Best practices?
If you're going to do this, you should probably put all relevant files into one directory then tar gz them. Following that, you'll probably want to encrypt it. I would use gpg to do this. Then use BandcampFS to convert it to a WAV file and upload it.

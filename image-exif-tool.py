import exifread

with open(input('[*] Enter Image Name: '), 'rb') as f:
    tags = exifread.process_file(f)
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print(f'{tag:25}: {tags[tag]}')

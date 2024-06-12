from pytube import YouTube
from sys import argv


yt = YouTube(argv[1])

print(yt.title)

should_download = input('Download? (y/n) : ')
if not should_download or should_download.lower() in ['y', 'yes']:
    streams = yt.streams
    print('Downloading starts...')
    streams.get_highest_resolution().download()
    print('Download Complete')
elif should_download.lower() in ['n', 'no', 'q', 'quit']:
    print('OK! Download Canceled!')
else:
    print('Wrong input!')

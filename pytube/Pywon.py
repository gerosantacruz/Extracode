import pytube

videoList = []

print('Please enter the url of the videos, when done type "Stop" to terminate and Start downloading...')

while True:
    url = input("")
    if url.lower() == 'stop':
        break
    videoList.append(url)

for x, video in enumerate(videoList):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(18)
    print(f'Downloading video {x}...')
    stream.download(filename=f'{x}')
    print('Done')

print('The download had finish, Enjoy the videos.')
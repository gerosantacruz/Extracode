import pytube

url = 'https://www.youtube.com/watch?v=iYWzMvlj2RQ'

video = pytube.YouTube(url)

stream = video.streams.get_by_itag(22)

print("Downloading..")
stream.download(filename='test')
print('Done')



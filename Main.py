from pytube import YouTube
from pytube import Playlist

musicList = ("C:\\Users\\Ben\\Desktop\\musicFolderTest\\MusicList.txt")
musicFile = open(musicList,'a')

ytPlaylist = Playlist('https://www.youtube.com/playlist?list=PLiB4gGXb4mNJtS2gCVaAemHKVFHZmJDyS')


for url in ytPlaylist.video_urls:
    yt = YouTube(url)
    #dl = yt.streams.get_highest_resolution()
    hasFile = False

    with open(musicList, 'r') as file:
        for line in file:
            if url+"\n" == line:
                hasFile = True
                print("File already downloaded")


    if hasFile == False:
        print("Getting Video")
        dl = yt.streams.filter(only_audio = True)
        print("Video Got!")
        dl[0].download("C:\\Users\\Ben\\Desktop\\musicFolderTest\\Musics")
        musicFile.write(url+'\n')
        print("Downloading " + yt.title)



musicFile.close()
print("Download has been completed!")

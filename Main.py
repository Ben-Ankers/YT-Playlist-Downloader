from pytube import YouTube
from pytube import Playlist

musicList = ("C:\\Users\\Ben\\Desktop\\musicFolderTest\\MusicList.txt")
musicFile = open(musicList,'a')
ytPlaylist = Playlist('https://www.youtube.com/playlist?list=PLiB4gGXb4mNJOgroZ3ZjYI_PJvnUvk3y4')

for url in ytPlaylist.video_urls:
    yt = YouTube(url)
    #dl = yt.streams.get_highest_resolution()
    dl = yt.streams.filter(only_audio = True)
    print(yt.title)

    hasFile = False

    with open(musicList, 'r') as file:
        for line in file:
            if url+"\n" == line:
                hasFile = True


    if hasFile == False:
        dl[0].download("C:\\Users\\Ben\\Desktop\\musicFolderTest\\Musics")
        musicFile.write(url+'\n')


musicFile.close()



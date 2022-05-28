from pytube import YouTube
from pytube import Playlist

downloadPath = "C:\\Users\\Ben\\Desktop\\musicFolderTest\\Musics"
musicList = ("C:\\Users\\Ben\\Desktop\\musicFolderTest\\MusicList.txt")

youtubeURL = ""

def downloadPlaylist(playlist, musicFile, downloadDestination, musicList):

    for url in playlist.video_urls:
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
            dl[0].download(str(downloadDestination))
            musicFile.write(url+'\n')
            print("Downloading " + yt.title)

def downloadSong(songURL, downloadDestination):
    yt = YouTube(songURL)
    dl = yt.streams.filter(only_audio = True)
    print("Downloading " + yt.title)
    dl[0].download(str(downloadDestination))


def main():


    userInput = input("What would you like to do, Type 1 to download a song/video, Type 2 to download a playlist: ")
    
    hasValidLink = False

    musicFile = open(musicList,'a')

    ytPlaylist = Playlist('https://www.youtube.com/playlist?list=PLiB4gGXb4mNJOgroZ3ZjYI_PJvnUvk3y4')

    #downloadPlaylist(ytPlaylist, musicFile, downloadPath, musicList)

    if userInput == "1":
        while hasValidLink == False:
            youtubeURL = input("Paste a youtube URL to download: ")
            try:
                downloadSong(youtubeURL ,"C:\\Users\\Ben\\Desktop\\musicFolderTest")
                hasValidLink = True
            except:
                print("URL is not valid")
    
    if userInput == "2":
        while hasValidLink == False:
            youtubeURL = input("Paste a youtube URL to download: ")
            try:
                downloadPlaylist(Playlist(youtubeURL) , musicFile, downloadPath, musicList)
                hasValidLink = True
            except:
                print("URL is not valid")


    musicFile.close()
    print("Operation Complete!")

if __name__ == "__main__":
    main()




from turtle import update
from pytube import YouTube
import os
from pytube import Playlist

for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        updatefile = file   # update file exists
    else:
        # update file does not exist so make one
        f = open("updateFile.txt", "w")
        f.close()
       
# check update file if exists
# check if new urls are found

def getVid(link):
    # url input from user
    yt = link
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # check for destination to save file
    # print("Enter the destination (leave blank for current directory)")
    # destination = str(input(">> ")) or '.'

    destination =  '.'    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")

def getPlay(plList):
    for link in plList:

        # url input from user
        yt = YouTube(link)
        
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
        
        # check for destination to save file

        # print("Enter the destination (leave blank for current directory)")
        # destination = str(input(">> ")) or '.'

        destination =  '.'
        # download the file
        out_file = video.download(output_path=destination)
        
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        # result of success
        print(yt.title + " has been successfully downloaded.")
    
def getPlayNames(playlists):
    urls = []
 
    for playlist in playlists:
        purl = Playlist(playlist)

        for url in purl:
            urls.append(url)
    return(urls)

def updateList():
    f = open(updatefile, "w")
    for x in names:
        f.write("\n")
        f.write(x)
    f.close()
    print(updatefile)

prompt = str(input("Would you like a playlist or video: \n>> "))
pls = []

if prompt.upper()== "PLAYLIST":
    pl = str(input("Enter the URL of the playlist you want to download: \n>> "))
    pls.append(pl)
    # get list of all playlist URLs

    names = getPlayNames(pls)

    getPlay(getPlayNames(pls))
    updateList()

elif prompt.upper()== "VIDEO":
    vid = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))
    getVid(vid)
else:
    print("INVALID INPUT")

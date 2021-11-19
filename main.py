# A program to download Youtube videos using pytube with the help of multithreading
import pytube
# import progressbar from pytube-cli
from pytube.cli import on_progress

def download_video(url, path):
    try:
        # create a pytube object
        yt = pytube.YouTube(url, on_progress_callback=on_progress)
        #download the video using selected quality show the progressbar
        yt.streams.get_highest_resolution().download(path)
        #print success message
        print("\nDownloaded successfully")
    except Exception as e:
        print(e)

# download channel videos in highest audio format
def download_channel_audios(url, path):
    pass

# function to download youtube playlist using pytube and multithreading and selecting the video quality
def download_playlist(url, path):
    try:
        # create a pytube object
        yt = pytube.Playlist(url)
        # get the video list
        video_list = yt.videos()
        # create a threadpool
        pool = ThreadPool(4)
        # download the video using threadpool
        pool.map(download_video, [video.url for video in video_list], [path]*len(video_list))
        # close the threadpool
        pool.close()
        # wait for the threadpool to finish
        pool.join()
        # print success message
        print("\nDownloaded successfully")
    except Exception as e:
        print("Error in downloading the video")
        print(e)

# function to download youtube channel using pytube and multithreading
def download_channel(url, path):
    try:
        # create a pytube object
        yt = pytube.Channel(url)
        # get the video list
        video_list = yt.videos()
        # create a threadpool
        pool = ThreadPool(4)
        # download the video using threadpool
        pool.map(download_video, [video.url for video in video_list], [path]*len(video_list))
        # close the threadpool
        pool.close()
        # join the threadpool
        pool.join()
    except Exception as e:
        print("Error in downloading the video")
        print(e)

# User Option list
def list1():
    print("\n1. Download a single video")
    print("2. Download a playlist")
    print("3. Download a channel")
    print("4. Exit")

    # get the user option
    option = int(input("\nEnter your option: "))
    return option

if __name__ == "__main__":
    option = 1
    while(True):
        # get the user option
        option = list1()
        if option == 4:
            print('Exiting...')
            break
        else:
            # get the path
            path = input("Enter the path: ")
            # get the url
            url = input("Enter the url: ")

            if option == 1:
                # download the video
                download_video(url, path)
            elif option == 2:
                # download the playlist
                download_playlist(url, path)
            elif option == 3:
                # download the channel
                download_channel(url, path)
            else:
                print("Invalid option")
# Download video using python code
# install necessary package

from pytube import YouTube

link = input("Enter youtube url: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
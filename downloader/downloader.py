import os

from pytube import YouTube
import pathlib

def Download():
    cwd = pathlib.Path().resolve()
    target_link = input('Enter youtube link: ')
    destination_folder_path = input('Enter link to local directory: ')
    default_destination_folder = os.path.join(cwd, "downloaded")
    destination_folder_path = destination_folder_path if destination_folder_path != '' else default_destination_folder
    youtube_object = YouTube(target_link)
    youtube_stream = youtube_object.streams.get_highest_resolution()
    try:
        youtube_stream.download(destination_folder_path)
    except:
        print("An error has occurred")

    print("Download is completed successfully")
    print(destination_folder_path)

from pytube import YouTube
from moviepy.editor import *
import os
import shutil

def downloader(url:str):
    # Create a Youtube object
    yt = YouTube(url)
    # Select  quality
    quality = input(" Select your video quality (high or low) > ")
    if quality == "high":
        stream = yt.streams.get_highest_resolution()
    elif quality == "low":
        stream = yt.streams.get_lowest_resolution()
    else:
        print('Wrong choice')
    
    # Download the YouTube video
    output_path ="mp4/"
    stream.download(output_path=output_path)
    print('\nYoutube media downloaded\n')


def latest_download():
    mp4_dir ="mp4/"
    if not os.path.exists(mp4_dir):
        try:
            os.makedirs(mp4_dir)
        except OSError as e:
            print(f"Error creating directory: {e}")
        else:
            print(f"Directory '{mp4_dir}' created successfully.")
    # mp4 directory
    mp4_dir = os.path.join(os.getcwd(), mp4_dir)

    # Get a list of files with their full paths
    files = [os.path.join(mp4_dir, f) for f in os.listdir(mp4_dir) if os.path.isfile(os.path.join(mp4_dir, f))]

    # Return the file with the latest creation time
    return max(files, key=lambda f: os.path.getctime(f))

    # old code base
    # dir_list = os.listdir()
    # return str(max(dir_list, key=os.path.getctime))

def converter(media:str,title:str):
    # Create VideoFileClip object
    video = VideoFileClip(media)

    # Extract the audio
    audio = video.audio

    # Save the audio as MP3 file
    converted_dir ="mp3/"
    if not os.path.exists(converted_dir):
        try:
            os.makedirs(converted_dir)
        except OSError as e:
            print(f"Error creating directory: {e}")
        else:
            print(f"Directory '{converted_dir}' created successfully.")
    # Convert the file
    audio.write_audiofile(f"{title}.mp3")
    
    # Move the mp3 file
    dir_list = os.listdir()
    for f in dir_list:
        if f.endswith('.mp3'):
            shutil.move(f,converted_dir)
    print('\nFile converted and moved')



def main():
    url = input("Slot in your url > ")
    mp3_title = input("Give your Mp3 file a name > ")
    downloader(url=url)
    mp4_file = latest_download()
    converter(media=mp4_file,title=mp3_title)



if __name__ == "__main__":
    main()


# Mp3 name
# Omah Lay - Holy Ghost
# Youtube link
# https://www.youtube.com/watch?v=wBjHEkLlrEY

# Reference materials
# https://www.shiksha.com/online-courses/articles/convert-youtube-videos-to-mp3-using-python/
# https://pytube.io/en/latest/api.html?highlight=get_highest_resolution#caption-object
# https://realpython.com/python-main-function/
# https://www.digitalocean.com/community/tutorials/python-main-function
# https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder
# https://www.learndatasci.com/solutions/python-move-file/
# https://stackoverflow.com/questions/8858008/how-do-i-move-a-file-in-python
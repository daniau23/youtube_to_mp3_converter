from pytube import YouTube
from moviepy.editor import *
import os
import shutil

def downloader(url:str, quality:str):
    # Create a Youtube object
    yt = YouTube(url)
    # Select  quality
    if quality == "high":
        stream = yt.streams.get_highest_resolution()
    elif quality == "low":
        stream = yt.streams.get_lowest_resolution()
    else:
        print('Wrong choice')
    
    # Download the YouTube video
    output_path ="mp4_list/"
    if not os.path.exists(output_path):
        try:
            os.makedirs(output_path)
        except OSError as e:
            print(f"Error creating directory: {e}")
        else:
            print(f"Directory '{output_path}' created successfully.")
    stream.download(output_path=output_path)
    print('\nYoutube media downloaded\n')


def converter(media:str,title:str):
    # Create VideoFileClip object
    video = VideoFileClip(media)

    # Extract the audio
    audio = video.audio

    # Save the audio as MP3 file
    converted_dir ="mp3_list/"
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
    link_file = "links.txt"
    name_file = "names.txt"
    mp4_dir = "mp4_list/"
    converted_dir = "mp3_list/"

    # Create directories if they don't exist
    for directory in [mp4_dir, converted_dir]:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as e:
                print(f"Error creating directory: {e}")
            else:
                print(f"Directory '{directory}' created successfully.")

    # Read links from the link_file
    with open(link_file, 'r') as file:
        links = [line.strip() for line in file if line not in ['\n', '\r\n']]

    # Download videos
    quality = input(" Select your video quality (high or low) > ")
    for link in links:
        downloader(url=link, quality=quality)

    # Get the list of downloaded MP4 files
    mp4_names = [f for f in os.listdir(mp4_dir) if f.endswith('.mp4')]

    # Write the mp3 titles in the name_file
    with open(name_file, "w") as file:
        for line in mp4_names:
            print("line", line)
            file.write(line+"\n")


    # Read titles from the name_file
    with open(name_file, 'r') as file:
        titles = [line.strip() for line in file]

    # Convert and move files
    for mp4_file, mp3_title in zip(mp4_names, titles):
        mp4_file_path = os.path.join(mp4_dir, mp4_file)
        converter(media=mp4_file_path, title=mp3_title)

   

if __name__ == "__main__":
    main()



# Mp3 name
# Omah Lay - Holy Ghost
# Youtube link
# https://www.youtube.com/watch?v=wBjHEkLlrEY
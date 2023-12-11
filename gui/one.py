import tkinter,customtkinter
from pytube import YouTube
from moviepy.editor import *
import os
import shutil


def downloader():
    try:

        yt_link = link.get()
        yt = YouTube(yt_link)
        stream = yt.streams.get_lowest_resolution()

        output_path ="mp4/"
        os.makedirs(output_path, exist_ok=True)
        # title.configure(text=yt.title,text_color='white')    
        finish_label.configure(text="")
        stream.download(output_path=output_path)
        finish_label.configure(text="Downloaded!",text_color="white")
        print(f"Video downloaded successfully: {yt.title}")
    except Exception as e:
        print(f"Error during download: {str(e)}")
        finish_label.configure(text="Youtube link is invalid",text_color='red')

def latest_download():
    mp4_dir ="mp4/"
    os.makedirs(mp4_dir, exist_ok=True)
    # mp4 directory
    mp4_dir = os.path.join(os.getcwd(), mp4_dir)

    # Get a list of files with their full paths
    files = [os.path.join(mp4_dir, f) for f in os.listdir(mp4_dir) if os.path.isfile(os.path.join(mp4_dir, f))]

    # Return the file with the latest creation time
    return max(files, key=lambda f: os.path.getctime(f))


def converter(media,title):

    title = title.get()
    
    # Create VideoFileClip object
    video = VideoFileClip(media)

    # Extract the audio
    audio = video.audio

    # Save the audio as MP3 file
    converted_dir ="mp3/"
    if not os.path.exists(converted_dir):
        os.makedirs(converted_dir)
    # Convert the file
    audio.write_audiofile(f"{title}.mp3")
    
    # Move the mp3 file
    dir_list = os.listdir()
    for f in dir_list:
        if f.endswith('.mp3'):
            shutil.move(f,converted_dir)
    finish_label.configure(text="Youtube file converted and moved",text_color='green')
    # print('\nFile converted and moved')

def main():
    downloader()
    mp4_file = latest_download()
    converter(media=mp4_file,title=mp3_title_)


# APP CREATION
app = customtkinter.CTk()
app.geometry('720x400')

app.title("Youtube Converter")



# Title 
title = customtkinter.CTkLabel(app,text="Insert the Youtube Link",justify='center')
title.pack(padx=10,pady=20)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=20,textvariable=url_var)
link.pack()

# mp3 file name
mp3_title_label = customtkinter.CTkLabel(app,text="Name the mp3 file",justify='center')
mp3_title_label.pack(padx=10,pady=20)

# mp3 title
mp3_title = tkinter.StringVar()
mp3_title_ = customtkinter.CTkEntry(app,width=350,height=20,textvariable=mp3_title)
mp3_title_.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app,text="")
finish_label.pack(padx=10,pady=20)

# # Progress bar
# percentage = customtkinter.CTkLabel(app,text="0%")
# percentage.pack()

# progress_bar = customtkinter.CTkProgressBar(app,width=400)
# progress_bar.set(0)
# progress_bar.pack(padx=10,pady=10)

# Download and convert
converting = customtkinter.CTkButton(app,text="Convert",command=main)
converting.pack(padx=10,pady=10)

app.mainloop()


# Reference materials
# https://customtkinter.tomschimansky.com/documentation/packaging
# https://pypi.org/project/auto-py-to-exe/
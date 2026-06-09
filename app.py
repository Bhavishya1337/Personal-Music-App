import os
import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()

root = tk.Tk()
root.title("Personal Music App")
root.geometry("400x300")

song_list = tk.Listbox(root, width=50)
song_list.pack(pady=20)

music_folder = "songs"

for song in os.listdir(music_folder):
    if song.endswith(".mp3"):
        song_list.insert(tk.END, song)

def play_music():
    selected = song_list.get(tk.ACTIVE)
    path = os.path.join(music_folder, selected)

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

tk.Button(root, text="Play", command=play_music).pack()
tk.Button(root, text="Pause", command=pause_music).pack()
tk.Button(root, text="Resume", command=resume_music).pack()
tk.Button(root, text="Stop", command=stop_music).pack()

root.mainloop()
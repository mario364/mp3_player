import os
from func import choose, playlist_read

if os.path.exists('Playlist'):
    print('Все готово!')
    playlist = os.listdir("Playlist")
else:
    print("У тебя нет плейлиста! Сейчас исправим!)")
    playlist = os.listdir(os.mkdir('Playlist'))
    print("Теперь все есть!)")


playlist_read(playlist)
choose()


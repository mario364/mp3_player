import os
import shutil
import time
import pygame
from pygame import mixer
import random



# dir_playlist = False

events = ['Открыть твою музыку', "Проиграть твою музыку", "Включить случайную музыку",
          'Показать плейлист', 'Выход']

playlist_dir = False

print('Привет! Я музыкальный плеер  :)')

if os.path.exists('Playlist'):
    print('Все готово!')
    playlist = os.listdir("Playlist")
else:
    print("У тебя нет плейлиста! Сейчас исправим!)")
    playlist = os.listdir(os.mkdir('Playlist'))
    print("Теперь все есть!)")





def choose():
    while True:
        for num, event in enumerate(events, 1):
            print(num, event)
        action = int(input('Что сделать?: '))

        if action == 1:
            open()
            continue

        if action == 2:
            music_play()
            continue

        if action == 3:
            music_random_play()
            continue

        if action == 4:
            playlist_read(playlist)
            continue

        if action == 5:
            print("До встречи!")
            break

def open():
    path1 = input('Введите путь: ')
    shutil.move(str(path1), "C:\Python_Projects\mp3_palyer\Playlist")
    print('файл добавлена в плейлист!')


def playlist_read(play_list):
    print(*play_list)


def music_play():
    for num, music in enumerate(playlist):
        print(num, music)
    action = int(input("Что вы хотите включить? "))
    mixer.init()
    mixer.music.load(f'C:\Python_Projects\mp3_palyer\Playlist\{playlist[action]}')
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
        action1 = int(input('Хотите остановить?\n1 - Стоп\n2 - Продолжить '))
        if action1 == 1:
            pygame.mixer.music.stop()
        if action1 == 2:
            print('Музыка продолжает играть')
        action2 = int(input('Хотите включить следующий трек?\n1 - Да\n2 - Нет '))
        if action2 == 1:
            mixer.music.load(f'C:\Python_Projects\mp3_palyer\Playlist\{playlist[action + 1]}')
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)
                action1 = int(input('Хотите остановить?\n1 - Стоп\n2 - Продолжить '))
                if action1 == 1:
                    pygame.mixer.music.stop()
                if action1 == 2:
                    print('Музыка продолжает играть')
        if action2 == 2:
            continue


def music_random_play():
    print('Сейчас я сыграю случайную песню из твоего плейлиста :)')
    mixer.init()
    mixer.music.load(f'C:\Python_Projects\mp3_palyer\Playlist\{random.choice(playlist)}')
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
        action1 = int(input('Хотите остановить?\n1 - Стоп\n2 - Продолжить '))
        if action1 == 1:
            pygame.mixer.music.stop()
        if action1 == 2:
            print('Музыка продолжает играть')
        action2 = int(input('Хотите включить следующий трек?\n1 - Да\n2 - Нет '))
        if action2 == 1:
            mixer.music.load(f'C:\Python_Projects\mp3_palyer\Playlist\{random.choice(playlist)}')
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)
                action1 = int(input('Хотите остановить?\n1 - Стоп\n2 - Продолжить '))
                if action1 == 1:
                    pygame.mixer.music.stop()
                if action1 == 2:
                    print('Музыка продолжает играть')
        if action2 == 2:
            continue
import sqlite3
import time
import os
import pandas as pd

import pygame

start_directrory = r'F:\CloudMusic'
data = os.listdir(start_directrory)  # 读取文件夹里的文件名
os.startfile(start_directrory)  # 打开某路径的文件
h = pd.DataFrame(data, columns=['文件名'])
h.to_excel('data.xlsx')
print(h)

#  音乐播放器
pygame.mixer.init()
pygame.mixer.music.load("F:\CloudMusic\ROSÉ - GONE (Live).mp3")
pygame.mixer.music.play()
time.sleep(50)

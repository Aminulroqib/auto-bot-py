import pyautogui as pg
import time

txt = open('romantic.txt', 'r')
a = 'Jaanu, '

for i in txt:
    time.sleep(3)
    pg.typewrite(a+ ' ' +i)
    time.sleep(2)
    pg.press('Enter')
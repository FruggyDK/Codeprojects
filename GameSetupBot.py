#!/usr/bin/python3.6.7
# -*- coding: utf-8 -*-
#author FruggyDK

#imports
from selenium import webdriver
import time
import pyautogui

url = 'https://pyx-3.pretendyoure.xyz/zy/game.jsp'  # edit me

# initializing webdriver
driver = webdriver.Chrome()
driver.get(url)

# user inputs
username = str(input('''Nickname:
-> '''))
game_password = str(input('''Game password:
-> '''))

# login
print ('Logging', username, 'in')
login = driver.find_element_by_id('nickname')
login.send_keys(username)

submit = driver.find_element_by_id('nicknameconfirm')
submit.click()

time.sleep(.5)
print ('Logged in!')

# create game
print ('Creating game...')
create_game = driver.find_element_by_id('create_game')
create_game.click()

time.sleep(1)
print ('Created game')

#set game password
set_code = driver.find_element_by_class_name('game_password')
set_code.send_keys(game_password)

#def
def slash():
    pyautogui.keyDown('shift')
    pyautogui.press('7')
    pyautogui.keyUp('shift')


#cardpacks:
FuckedUpAndCancer = [
    'RBTVV',
    'RBTBK',
    'AX253',
    'E66JH',
    'MJFBW',
    'JDS32',
    'R7XYE',
    'UN32U',
    ]


#goto chat
chat = driver.find_element_by_class_name('chat')
pyautogui.click(x=537, y=1038, clicks=1, interval=0, button='left')

print ('importing cards ...')

#card import loop
i = 0
while i < len(FuckedUpAndCancer):
    keyString = 'addcardcast ' + FuckedUpAndCancer[i]
    print (keyString, i + 1, '/', len(FuckedUpAndCancer))
    slash()
    pyautogui.typewrite(keyString)
    pyautogui.press('enter')
    i += 1
else:
    print ('Done, enjoy your game')

			

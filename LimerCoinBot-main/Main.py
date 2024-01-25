import pyautogui
import time
import os
import cv2
import random
import keyboard
import numpy as np
import json
import cv2
import numpy as np

input("Başlıyoruz (Enter'a basın.)")  # Here we go (Press Enter.)

print("Geri sayım bitti!")  # The countdown is over!
os.system("cls")


def show_banner():
    banner = r'''
 _                     _ 
| |                   (_)
| |     ___  __ ___  ___ 
| |    / _ \/ _` \ \/ / |
| |___|  __/ (_| |>  <| |
|______\___|\__,_/_/\_\_|

  Limercoin Auto Game Bot =)
  Discord.gg/7WAe2ySZNN
  '''

    if os.name == 'nt':  # Check if running on Windows
        terminal_genislik = 80  # Set a default terminal width for Windows
    else:
        terminal_genislik = os.get_terminal_size().columns  # Terminal Width

    metin_genislik = max(len(satir) for satir in banner.splitlines())  # Text Width
    bosluk_miktari = (terminal_genislik - metin_genislik) // 2  # amount of space
    for satir in banner.splitlines():
        print(' ' * bosluk_miktari + satir)


show_banner()
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("Geri sayım bitti!")  # The countdown is over!
os.system("title ByLeaxi - Discord.gg/7WAe2ySZNN")


def perform_actions():
    with open('config.json', 'r') as file:
        config = json.load(file)
    lleaxi = int(config['Leaxi'])

    game_image_path = 'ff/Game.png'
    start_image_path = 'ff/Start.png'
    play_image_path = 'ff/Play.png'
    fins_image_path = 'ff/fins.png'
    res_image_path = 'ff/res.png'
    second_image_path = 'ff/Coin.png'
    third_image_path = 'ff/Puzzle.png'
    fourth_image_path = 'ff/2048.png'
    btc_image_path = 'ff/Coin/btc.png'
    eth_image_path = 'ff/Coin/eth.png'
    bnb_image_path = 'ff/Coin/bnb.png'
    x_image_path = 'ff/Coin/x.png'



    try:
        location = pyautogui.locateOnScreen(game_image_path, confidence=0.8)
        # Rest of your code
    except pyautogui.ImageNotFoundException:
        location = None  # Initialize location to None
    
    if location:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        time.sleep(2)

        try:
            play_locations = list(pyautogui.locateAllOnScreen(play_image_path, confidence=0.8))
        except:
            play_locations = None

        if play_locations:
            random_location = random.choice(play_locations)
            px, py = pyautogui.center(random_location)
            pyautogui.click(px, py)
            time.sleep(3)
        else:
            print("play location not found")
    else:
        print("game image not found")
    



    try:
        second_location = pyautogui.locateOnScreen(second_image_path, confidence=0.8)
    except pyautogui.ImageNotFoundException:
        second_location = None

    if second_location:
        time.sleep(1)
        print("(COIN CATCHER) Oynanıyor ")
        try:
            start = pyautogui.locateOnScreen(start_image_path, confidence=0.8)
        except:
            start = None

        if start is not None:
            px, py = pyautogui.center(start)
            pyautogui.click(px, py)
            time.sleep(1)
            pyautogui.click(px, py)
            time.sleep(1)   
            pyautogui.click(px, py)
        
        def click_on_image(temp):
            if temp:
                for location in temp:
                    x, y = pyautogui.center(location)
                    pyautogui.click(x, y + lleaxi)
            else:
                return None

        while True:
            try:
                fins = pyautogui.locateOnScreen(fins_image_path, confidence=0.5)
            except:
                fins = None
                
            try:
                res = pyautogui.locateOnScreen(res_image_path, confidence=0.5)
            except:
                res = None
            
            try:
                btc = list(pyautogui.locateAllOnScreen(btc_image_path, confidence=0.9))
            except:
                btc = None
                
            try:
                eth = list(pyautogui.locateAllOnScreen(eth_image_path, confidence=0.9))
            except:
                eth = None
            
            try:
                bnb = list(pyautogui.locateAllOnScreen(bnb_image_path, confidence=0.9))
            except:
                bnb = None
            
            try:
                x = list(pyautogui.locateAllOnScreen(x_image_path, confidence=0.9))
            except:
                x = None

            if fins is not None:
                px, py = pyautogui.center(fins)
                pyautogui.click(px, py)
                time.sleep(10)
                break
            elif res is not None:
                break
            else:
                pass    

            click_on_image(btc)
            click_on_image(eth)
            click_on_image(bnb)
            click_on_image(x)

            # if btc is not None:
            #     for location in btc:
            #         x, y = pyautogui.center(location)
            #         pyautogui.click(x, y + lleaxi)
            # elif eth is not None:
            #     for location in eth:
            #         x, y = pyautogui.center(location)
            #         pyautogui.click(x, y + lleaxi)
            # elif bnb is not None:
            #     for location in bnb:    
            #         x, y = pyautogui.center(location)
            #         pyautogui.click(x, y + lleaxi)
            # elif x is not None:
            #     for location in x:
            #         px, py = pyautogui.center(location)
            #         pyautogui.click(px, py + lleaxi) 
            # else:
            #     continue


    try:
        third_location = pyautogui.locateOnScreen(third_image_path, confidence=0.8)
    except pyautogui.ImageNotFoundException:
        third_location = None

    if third_location:
        print("(COIN PUZZLE) Bakım Aşamasında ")
        pass


    
    try:
        fourth_location = pyautogui.locateOnScreen(fourth_image_path, confidence=0.8)
    except pyautogui.ImageNotFoundException:
        fourth_location = None    
    
    if fourth_location:
        time.sleep(1)
        print("(2048) Oynanıyor ")
        start = pyautogui.locateOnScreen(start_image_path, confidence=0.8)
        if start:
            px, py = pyautogui.center(start)
            pyautogui.click(px, py)
            time.sleep(5)
        while True:
            movements = ['right', 'down', 'left', 'up']
            move = random.choice(movements)
            keyboard.press(move)
            keyboard.release(move)
            try:
                fins = pyautogui.locateOnScreen(fins_image_path, confidence=0.6)
            except pyautogui.ImageNotFoundException:
                fins = None

            try:
                res = pyautogui.locateOnScreen(res_image_path, confidence=0.6)
            except:
                res = None

            if fins is not None:
                px, py = pyautogui.center(fins)
                pyautogui.click(px, py)
                time.sleep(10)
                break

            elif res is not None:
                break


while True:
    perform_actions()

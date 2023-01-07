import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("smiley_paperclip.png")
#position1 = pt.locateOnScreen(r"C:\Users\ngkel\PycharmProjects\whatappsbot_yt\whatsapp\smiley_paperclip.png")
#, confidence=.6)
#position1 is none
print(position1)
x = position1[0]
y = position1[1]


# get message
def get_message():
    global x, y

    position = pt.locateOnScreen(r"C:\Users\ngkel\PycharmProjects\whatappsbot_yt\whatsapp\smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=0.5)
    pt.moveTo(x + 40, y - 70, duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    print("Message received:" + whatsapp_message)

    return whatsapp_message

# #Posts
# def post_response(message)
#     global x,y
#
#     position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
#     x=position[0]
#     y=position[1]
#     pt.moveTo(x+200, y+20, duration=0.5)
#     pt.click()
#     pt.typewrite(message, interval=0.01)
#
#     pt.typewrite("\n", interval=0.01)
#
# get_message()
#
# post_response()
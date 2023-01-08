import pyautogui as pt
from time import sleep
import pyperclip
import random

#it is working now, you just need to ensure your image is shown on the screen
position1 = pt.locateOnScreen(r"C:\Users\ngkel\PycharmProjects\whatappsbot_yt\whatsapp\smiley_paperclip.png", confidence=.6)
print(position1)

sleep(3)
print(position1)
x = position1[0]
y = position1[1]
print(x)

# if position1 == None:
#     print("image not found")
# else:
#     x1 = position1[0]
#     y1 = position1[1]
#     #print(x1)


def get_message():
    global x, y

    position = pt.locateOnScreen(r"C:\Users\ngkel\PycharmProjects\whatappsbot_yt\whatsapp\smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=0.5)
    pt.moveTo(x + 40, y - 70, duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    print("Message received:" + whatsapp_message)

    return whatsapp_message

#Post
def post_response(message):
    global x, y

    position = pt.locateOnScreen(r"C:\Users\ngkel\PycharmProjects\whatappsbot_yt\whatsapp\smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=0.5)
    pt.click()
    pt.typewrite(message, interval=0.01)

    pt.typewrite("\n", interval=0.01)


#post_response(get_message())

#process response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any question!"

    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no == 1:
            return "Remember to subscribe to Code Palace!"
        else:
            return "I want to eat something"

processed_message = process_response(get_message())
post_response(processed_message)

# Check for new messages
def check_for_new_messages():
    pt.moveTo(x + 50, y - 35, duration=0.5)

    while True:
        #Continuously checks for green dot and new messages
        try:
            position = pt.locateOnScreen(r"C:\Users\ngkel\PycharmProjects\whatappsbot_yt\whatsapp\greendot.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No new other users with new messages located")

        if pt.pixelMatchesColor(int(x + 50), int(y), (255, 255, 255), tolerance=10):
            print("is_white")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("No new message yet...")
        sleep(5)


# get control of our keyboard
from pynput.keyboard import Listener, Key, Controller
# time variables
import time
# use to mimic human typing
import numpy as np
# initially we use this to retrive text from textboard, but the access of clipboard is banned by LOL,
# Thus, we decide to mimic human typing and type our retrived text to the chatbox in LOL.
# import win32clipboard as w  (no linger needed)

def yxcMethod():
    text = "Gee Gee~"
    # setClipboard(text)
    return str(text)

# +
#def setClipboard(text):
#    w.OpenClipboard()
#    w.EmptyClipboard()
#    w.SetClipboardText(text) # set clipboard data
#    w.CloseClipboard()
# -

def press(k):
    try :
        # print(k)
        if k == Key.f8 :
            print('Loading result from gpt......')
            # retriving text from ChatGPT           
            cheerText = yxcMethod()
            # wait for gpt to generate texts
            time.sleep(5)
            
            keyboard = Controller()            
            keyboard.press(Key.enter)
            time.sleep(0.5)
            keyboard.release(Key.enter)
            # type texts into chatbox
            for x in range(len(cheerText)):
                for y in cheerText[x]:
                    keyboard.press(y)
                    time.sleep(np.random.uniform(low=0.02, high=0.05))
                    keyboard.release(y)
                    time.sleep(np.random.uniform(low=0.03, high=0.07))

            keyboard.press(Key.enter)
            time.sleep(0.23)
            keyboard.release(Key.enter)
            
            
    # diagnose
    except Exception as e:
        print("The following error occurred: ", e)

with Listener(on_press=press) as listener:
    listener.join()

#



import pywhatkit as p
import webbrowser as web
import pyautogui as pg
import time
message="This is a TEST MESSAGE."
first = True
# def search(x,a):
#     time.sleep(4)
#     web.open("https://web.whatsapp.com/send?phone="+x+"&text="+message)
#     time.sleep(2)
#     if(a%2!=0):
#         time.sleep(6)
#     width,height = pg.size()
#     pg.click(width/2,height/2)
#     time.sleep(15)
#     pg.press('enter')
#     time.sleep(8)
#     pg.hotkey('ctrl', 'w')




f=open(r'C:\Users\tanis\Desktop\fo\text.txt',"r")
a=1
for x in f:
    time.sleep(4)  #can change time lag according to the users device capablity
    web.open("https://web.whatsapp.com/send?phone="+x+"&text="+message)

    time.sleep(6)  #can change time lag according to the users device capablity

    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)  #can change time lag according to the users device capablity 
    pg.press('enter')
    time.sleep(8)  #can change time lag according to the users device capablity
    pg.hotkey('ctrl', 'w')

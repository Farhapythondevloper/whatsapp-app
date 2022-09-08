from cgitb import text
from tkinter.tix import IMMEDIATE
from django.http import HttpResponse
from django.shortcuts import render
# from .forms import MessageForm
from django.contrib import messages


# # Create your views here.

def home(request):
    return render(request, 'home.html')







def whatsappData(Ph,Message):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = Ph
    # Message = "my message"
    web.open(f"https://web.whatsapp.com/send?phone="+Phone+'&text='+Message)
    time.sleep(30)
    pg.press('enter')

def SendData(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message= request.POST['Message']
        print(Ph,Message)
        whatsappData(Ph,Message)
        msg = 'Message has successfully sent....'
        return render(request,'home.html',{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


# import random
# import pyautogui as pg
# import time

# animal = ('monkey','dog','donkey')
# time.sleep(8)

# for item in range(500):
#     a = random.choice(animal)
#     pg.write("you are a "+ a)
#     pg.press('emter')

# import pywhatkit
# pywhatkit.sendwhatmsg('+918602590029', 'You are special in my heart, sweetie. Forever will you, darling.', 16, 7)

# import pywhatkit
# from datetime import datetime 

# today = datetime.now()

# shour = today.strftime("%H")
# mobile_no = input('Enter Mobile Number of Receiver: ')
# message = input('Enter Message you want to send : ')
# hour = int(input('Enter hour : '))
# minute = int(input('Enter minute : '))

# pywhatkit.sendwhatmsg(mobile_no,message,hour,minute)
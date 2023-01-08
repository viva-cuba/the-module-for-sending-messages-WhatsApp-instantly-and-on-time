
import time
import os
import keyboard as ked
from time import strftime
import datetime

def message_now_whatsys(name_tel: str, message: str, time_start: int, time_s: int) -> None:
    """ПРИМЕР
    import vivacuba_librari as vcl

    a = input('номер телефона или контакт из списка : ')
    b = input('сообщение: ')
    vcl.message_now_whatsys(a, b, 15, 3)

    открывает установленный на компьютере whatsapp и отправляет сообщение по номеру телефона
    или контакт из списка. функция принимает 4 параметра: 1 номер телефона(или контакт из списка),
    2 текстовое сообщение, 3 время в секундах чтобы whatsapp полностью открылся(у каждого время
    открывания разное)
    4 время в секундах чтобы после отправки сообщения закрыть whatsapp """

# путь к файлу указывам свой
    os.startfile("C:/Users/msi_dima/AppData/Local/WhatsApp/WhatsApp.exe") 
    time.sleep(time_start)
    ked.send('tab')
    time.sleep(0.5)
    ked.send('tab')
    time.sleep(0.5)
    ked.send('tab')
    time.sleep(0.5)
    ked.send('tab')
    time.sleep(0.5)
    ked.write(' '+name_tel, delay=0.25)
    time.sleep(2)
    ked.send('enter')
    time.sleep(0.5)
    ked.write(message, delay=0.25)
    time.sleep(0.5)
    ked.send('enter')
    time.sleep(time_s)
    ked.send('alt + f4')

def message_launch_by_time_whatsys(name_tel: str, message: str, time_start: int, time_s: int, launch_by_time: str) -> None:
    '''ПРИМЕР
    import vivacuba_librari as vcl

    a = input('номер телефона или контакт из списка : ')
    b = input('сообщение: ')
    c = input('введи время в формате 00:00: ')
    vcl.message_launch_by_time_whatsys(a, b, 15, 3, c)

    открывает установленный на компьютере whatsapp и отправляет сообщение по номеру телефона
    или контакт из списка. функция принимает 5 параметров: 1 номер телефона(или контакт из списка),
    2 текстовое сообщение, 3 время в секундах чтобы whatsapp полностью открылся(у каждого время
    открывания разное)
    4 время в секундах чтобы после отправки сообщения закрыть whatsapp
    5 время в формате 00:00 для отправки сообщения в заданное время'''
    
    now = strftime("%H:%M") 
   
    while True:
        now = datetime.datetime.now()
        time.sleep(10)
        now = strftime("%H:%M")
        if  now == launch_by_time:
            # путь к файлу указывам свой
            os.startfile("C:/Users/msi_dima/AppData/Local/WhatsApp/WhatsApp.exe") 
            time.sleep(time_start)
            ked.send('tab')
            time.sleep(0.5)
            ked.send('tab')
            time.sleep(0.5)
            ked.send('tab')
            time.sleep(0.5)
            ked.send('tab')
            time.sleep(0.5)
            ked.write(' '+name_tel, delay=0.25)
            time.sleep(2)
            ked.send('enter')
            time.sleep(0.5)
            ked.write(message, delay=0.25)
            time.sleep(0.5)
            ked.send('enter')
            time.sleep(time_s)
            ked.send('alt + f4')
            exit()

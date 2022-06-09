from __future__ import with_statement
from asyncore import loop
from random import seed
from timeit import repeat
from wsgiref import headers
import requests
import time
from threading import Thread
import json






heal = {
        'content': "rpg heal"    
    }

adventure = {
        'content': "rpg adventure"    

    }

hunt = {
        'content': "rpg hunt"    
    }

training = {
        'content': "<@{userid}> DO RPG TRAINING NOW !!!!!!!! "    
        }

work = {
        'content': "rpg ladder"    
        }

farm = {
        'content': "rpg farm"    
        }

seed = {
        'content': "rpg buy seed 1"   

        }
guild = {
        'content': "rpg guild upgrade"   
        }




headers ={ 'authorization': '{DiscordAuth}'   
    }

def funktion_1():
    while True:
	
	
        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = hunt, headers = headers   )
        time.sleep(2)

        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = heal, headers = headers   )
        time.sleep(60)

def funktion_2():
    while True:

        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = adventure, headers = headers   )
        time.sleep(2)
    
        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = heal, headers = headers   )
        time.sleep(3600)

def funktion_3():   
    while True:

        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = training, headers = headers   )

        time.sleep(900) 

def funktion_4():   
    while True:

        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = work, headers = headers   )
        time.sleep(300) 

def funktion_5():   
    while True:

        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = farm, headers = headers   )
        time.sleep(2)

        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = seed, headers = headers   )
        time.sleep(600) 

def funktion_6():   
    while True:

        r =  requests.post("https://discord.com/api/v9/channels/{ChannelId}/messages", data = guild, headers = headers   )
        time.sleep(7200)




thread_1 = Thread(target=funktion_1)
thread_2 = Thread(target=funktion_2)
thread_3 = Thread(target=funktion_3)
thread_4 = Thread(target=funktion_4)
thread_5 = Thread(target=funktion_5)
thread_6 = Thread(target=funktion_6)

thread_1.start()
time.sleep(2)

thread_2.start()
time.sleep(2)

thread_3.start() 
time.sleep(2)

thread_4.start() 
time.sleep(2)

thread_5.start() 
time.sleep(2)

thread_6.start() 
time.sleep(2)

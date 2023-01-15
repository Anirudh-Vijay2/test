from instagrapi import Client
from instagrapi.types import Usertag, Location
import config
from datetime import datetime, date
import time
from pytz import timezone 
import requests
import json
import textwrap
import os
import platform
from PIL import Image, ImageDraw, ImageFont
cl = Client()
cl.login("thenewssage", "u4njF!kAt4Di7SF")
# API Related things
limit = 3
joke = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
key = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=8127727ffc49478ab6685dd16fadc301"
i = 0
News = requests.get(key).json()
done = []
hour = datetime.now(timezone("Asia/Kolkata")).strftime('%H')
jokeUpl = 0

style = ImageFont.truetype("arialbd.ttf", 34)
if int(hour) == 15 or int(hour) == 9:
    while jokeUpl != 2:
        response = requests.get(joke, headers={'X-Api-Key': '57iBM3Q7okzZZgRM9y3eqw==pTf0jE6UdQrkcjle'}).json()
        new = response[0]['joke']
        print(new)
        textx = textwrap.fill(text=new, width=27.5)
        scnd = time.localtime().tm_sec
        JokeIMg = Image.open('MainJoke.jpg') 
        jk = ImageDraw.Draw(JokeIMg)
        jk.text((50, 225), textx, font=style, fill="black")
        pathNameJ = f"{scnd}joke.jpg"
        JokeIMg.save(pathNameJ)
        cl.photo_upload(path=pathNameJ, caption="Fun Jokes Powered By The News Sage", location=Location(name="India, Kerala"))
        print("Joke Uploaded")
        if platform.system() == "Windows":
            os.system(f"del {pathNameJ}")
        else:
            os.system(f"rm -rf {pathNameJ}")
        jokeUpl = jokeUpl+1
        if jokeUpl == 1:
            print("Joke closed")
            i = 0
            time.sleep(3600)
curn = 0 
listOfCurn = ["EUR_INR", "USD_INR"]
listOfImg = ["ExchangeRate.jpg", "ExchangeRateUSD.jpg"]      
if int(hour) ==  5:
    today = date.today()
    dateEx = today.strftime("%d/%m/%y")
    while curn != 2:
         currency = f"https://api.api-ninjas.com/v1/exchangerate?pair={listOfCurn[curn]}"
         curencyRate = requests.get(currency, headers={'X-Api-Key': '57iBM3Q7okzZZgRM9y3eqw==pTf0jE6UdQrkcjle'}).json()
         rate = f"1 USD = {curencyRate['exchange_rate']} INR. Exchange rate on {dateEx}"
         rateInfo = textwrap.fill(text=rate, width=26)
         scndOfRate = time.localtime().tm_sec
         imgOfRate = Image.open(listOfImg[curn]) 
         dOfRate = ImageDraw.Draw(imgOfRate)
         dOfRate.text((50, 225), rateInfo, font=style, fill="black")
         pathNameofRate = f"{scndOfRate}img.jpg"
         imgOfRate.save(pathNameofRate)
         cl.photo_upload(path=pathNameofRate, caption="Exchange Rate Powered By The News Sage")
         print("Currency exchange uploaded")
         curn = curn+1
         if curn == 2:
            curn = 0
            time.sleep(3600)
         
while True:
    if int(hour) == 19 or int(hour) == 7 or int(hour) == 14:
        Heading = News['articles'][i]["title"]
        description = News['articles'][i]['description']
        Url = "Read the complete news from here:- ",News['articles'][i]['url']
        textx = textwrap.fill(text=Heading, width=27.5)
        scnd = time.localtime().tm_sec
        Eimg = Image.open('Main.jpg') 
        d = ImageDraw.Draw(Eimg)
        d.text((50, 225), textx, font=style, fill="black")
        pathName = f"{scnd}img.jpg"
        Eimg.save(pathName)
        cl.photo_upload(path=pathName, caption=description, location=Location(name="India, Kerala"))
        print("In Sleep will post again in 60 seconds.. Please be patient")
        if platform.system() == "Windows":
            os.system(f"del {pathName}")
        else:
            os.system(f"rm -rf {pathName}")
        print(f"Value of i is {i}")
        print("In sleep mode will wake in 60 seconds...!")
        time.sleep(60)
        i = i+1    
        if i == 19:
            time.sleep(3600)
            i = 0
    else:
        print("The news updation time is 7:00 AM, 1:00 PM and 6:00 PM")
        print("Waiting...!")
        for x in range(0, 2):
            starter = News['articles'][x]["title"]
            description = News['articles'][x]['description']
            if starter not in done:
                done.append(starter)
                textx = textwrap.fill(text=starter, width=27.5)
                scnd = time.localtime().tm_sec
                Eimg = Image.open('Main.jpg') 
                d = ImageDraw.Draw(Eimg)
                d.text((50, 225), textx, font=style, fill="black")
                pathName = f"{scnd}img.jpg"
                Eimg.save(pathName)
                cl.photo_upload(path=pathName, caption=description, location=Location(name="India, Kerala"))
                if platform.system() == "Windows":
                    os.system(f"del {pathName}")
                else:
                    os.system(f"rm -rf {pathName}")
            else:
                print("Already Exsists..!")
                print("Will fetch again in 500 seconds")
                time.sleep(500)
                x = 0
            if x == 1:
                time.sleep(700)
                x = 0

import matplotlib.pyplot as plt
import requests
import urllib, json
from datetime import date


def GetData(name, cookie, header, data):
    realData = json.loads(data.content)


    fullList = []
    editedList = []

    x = 0
    try:
        for i in realData:
            fullList.append(realData['prices'][x][1])
            x=x+1

        x = 0

        timeframe = 0
        timeframe = int(input("Press (1) for 1 week data, (2) for last month data, or (3) for all time data: "))

        def weekData():
            for i in range(len(realData['prices']) - 7, len(realData['prices']) ):
                editedList.append(realData['prices'][i][1])

        def monthData():
            Date = date.today()
            today = int(Date.strftime("%d"))
            print("Today's date:", today)
            for i in range(len(realData['prices']) - today, len(realData['prices']) ):
                editedList.append(realData['prices'][i][1])

        def alltimeData():
            for i in range(len(realData['prices'])):
                editedList.append(realData['prices'][i][1])

        if timeframe == 1:
            weekData()
        elif timeframe == 2:
            monthData()
        elif timeframe == 3:
            alltimeData()

        print(editedList)
        plt.plot(editedList)
        plt.title("Showing results for " + name)
        plt.ylabel('Price(Euros)')
        plt.xlabel('Timeframe(Days)')
        plt.show()
    except:
        print("Name not found, enter X to exit!")
        StartApp()
#for i in realData['prices']:


def StartApp():


    print("Input name! ")
    name = input()
    if name== "X" or name == "x":
        exit()
    cookie = {'steamLoginSecure': ' '}#Input your steamLoginSecure header here!
    header = {"Content-type":"application.json"}
    data = requests.get('https://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid=730&market_hash_name='+name, cookies=cookie, headers=header)
    #request a full json history price from Steam

    GetData(name, cookie, header, data)

StartApp()

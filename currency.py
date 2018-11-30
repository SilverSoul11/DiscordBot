import discord
from discord.ext import commands
import asyncio
import time
import random
import requests
import disc
import re


  def currencyConvert():
    if message.content.startswith('!convert'): 
      currencyMessage = message.content[9:]       #splices the input from the 9th element
      intFound = re.findall(r'\d+', currencyMessage) #saves the integers in the input to a separate variable
      intFound = list(map(int, intFound)) #converts this to a list
      currencyCode = re.findall(r'\w+', currencyMessage) #saves the letters as a separate variable
      print(intFound) 
      print (currencyCode)
      response = requests.get('https://v3.exchangerate-api.com/bulk/d277fcb6694e5aaf7e32ca68/GBP') #api key
      data = response.json()
      ratesDic = data['rates'] #sets a variable for the json dictionary
      if currencyMessage == "": 
        await client.send_message(message.channel, "Converts a selected currency to GBP,")
        await client.send_message(message.channel, "Format: !convert <amount> <currency code>")
      else:
        for key in ratesDic.keys():
          if currencyCode[1].strip().upper() in key: #strips the message to remove unneccesary spaces and makes it uppercase
            conversion = intFound[0] / (ratesDic[currencyCode[1].strip().upper()])
            msg = f"1 GBP is currently worth {round(ratesDic[currencyCode[1].strip().upper()], 2)} {currencyCode[1].strip().upper()}"
            await client.send_message(message.channel, msg)
            msg = f"{intFound[0]} {currencyCode[1].strip().upper()} is worth {round(conversion,2)} GBP"
            await client.send_message(message.channel, msg)

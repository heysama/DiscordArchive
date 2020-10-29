# Disgusting code
# I take responsibility for most of the spaget code
# Original Author: CodeDiseaseDev
# This is not all the files you need to run the gen!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import socket
import os
import random
from colorama import Fore, Back, init 
init(convert=True)

class DiscordBot:
  def __init__(self):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    self.bot = webdriver.Firefox(options=fireFoxOptions)
  
  def createAccount(self):
    bot = self.bot
    bot.get('https://discord.com')
    time.sleep(2)
    bot.find_element_by_class_name('openButton-McADyK').click()
    time.sleep(2)
    username = bot.find_element_by_class_name('username-27KRPU')
    time.sleep(2)
    username.clear()
    time.sleep(2)
    username.send_keys("Discord Oofed")
    time.sleep(2)
    username.send_keys(Keys.RETURN)
    time.sleep(5)
    try:
      with open("script.js", 'r') as file:
        bot.execute_script(file.read())
        print("Made an account!")
    except Exception as error:
      print(error)
    time.sleep(3)
    bot.close()

def Bot():
  lol = DiscordBot()
  lol.createAccount()

while True:
  Bot()
  time.sleep(120) # Avoid ratelimit

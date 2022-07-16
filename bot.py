import os 
from dotenv import load_dotenv
import telebot
from generateQrCode import createWifiQrCode

load_dotenv()
TOKEN_KEY = os.getenv('TOKEN_KEY')

bot = telebot.TeleBot(TOKEN_KEY)

@bot.message_handler(commands=['/start','/help'])
def start(message):
    bot.send_message(message.chat.id, '''Welcome to Qrcode Hub !! 
                                        \nLet start to generate wifi Qrcode 
                                        \nHow to generate wifi Qrcode ? 
                                        \n  - <your_wifi>:<your_wifi_password>
                                        \n  - Example: qrcode wifi:@1234567'
                                        
                                        ''')

@bot.message_handler()
def wifi(message):
    print(message.text)
    if  ":" in message.text :
        data = (message.text).split(':')
        print(f'Wifi name: {data[0]}, Pwd : {data[1]}')
        tmp_filename=createWifiQrCode(data[0],data[1])
        bot.send_message(message.chat.id,f'Wifi Name: {data[0]} \nWifi Password : {data[1]}')
        bot.send_photo(message.chat.id, photo=open(f'./{tmp_filename}','rb'))
    else:
        bot.send_message(message.chat.id, 'Wrong Format. Please Try again \nFormat: <your_wifi>:<your_wifi_password> \nExample: qrcode wifi:@1234567')
bot.polling()
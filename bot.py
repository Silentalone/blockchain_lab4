import os
import config
import telebot
import bitcoinrpc
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

bot = telebot.TeleBot(config.token)

RPC_USER = 'kzcashrpc'
RPC_PASSWORD = 'i5bDw6PHHP1122UjjwnmPaip'
RPC_HOST = '127.0.0.1' 
RPC_PORT = '8277'  

rpc_connection = AuthServiceProxy(f'http://{RPC_USER}:{RPC_PASSWORD}@{RPC_HOST}:{RPC_PORT}')

@bot.message_handler(commands=['getnewaddress', 'getbalance', 'send'])
def handle_command(message):
   if message.text.startswith('/getnewaddress'):
        get_new_address(message)
   elif message.text.startswith('/getbalance'):
        get_balance(message)

@bot.message_handler(commands=['getnewaddress'])

def get_new_address(message):

   new_address = os.popen("/home/kzcash/kzcash-cli getnewaddress").read()

   bot.send_message(message.chat.id, f"New address: {new_address}")

@bot.message_handler(commands=['getbalance'])
def get_balance(message):
    
   balance = os.popen("/home/kzcash/kzcash-cli getbalance").read()
    
   bot.send_message(message.chat.id, f"Balance: {balance}")

   
if __name__ == '__main__':
     bot.infinity_polling()
#encoding:UTF-8
import sys, time, telepot
from datetime import datetime

def format_timedelta(timedelta):
    days_str = '{0} days '.format(timedelta.days)
    hours, remainder = divmod(timedelta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return days_str + '{0} hours, {1} minutes, {2} seconds'.format(hours, minutes, seconds)

def command_response(command):
    command = command.split("@")[0]
    if command == "forstarwars":
        starwars_date = datetime(2015, 12, 18, 23, 15)
        countdown = starwars_date - datetime.now()
        return "{0} remaining to Star Wars".format(format_timedelta(countdown))
    elif command == "formybloodyass":
        return "Shrino's ass has already been broken"
    elif command == "help":
        return help_text()
    elif command == "start":
        return "Hi there! You can know about my commands asking for /help :)"
    else:
        return "Don't know that command :("

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance2(msg)
    text = msg["text"]

    last_chat = chat_id
    print(content_type, chat_type, chat_id)

    if text[0] == "/":
        response = command_response(text.lower()[1:])
    else:
        response = "aloha, I am countdownforbot."

    bot.sendMessage(chat_id, response)

def help_text():
    return ("This bot allows you to create countdowns for whatever date you want. (Still working...)\r\n"
            "  Meanwhile, you can use this commands:\r\n"
            "    /forstarwars - See countdown to the Star Wars movie\r\n"
            "    /formybloodyass - See countdown to Shrino's ass to be broken"
            )



try:
    TOKEN = sys.argv[1]  # get token from command-line
except IndexError:
    print("You must provide bot's token as first argument")
    exit()

last_chat = None
bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print('Listening ...')

def perform_action(action):
    if action == "1":
        # bots cannot create a new conversation
        msg = input("Please, tell me the message to send: ")
        if last_chat is not None:
            bot.sendMessage(last_chat, msg)
        else:
            print("You have no last chat. Please, wait until a conversation is created")
    else:
        print("action out of range")

# Keep the program running.
while 1:
    print("What do you wanna do? \r\n"
          "1. Send message to last chat")
    action = input("")
    perform_action(action)
    time.sleep(2)
    print("\r\n")
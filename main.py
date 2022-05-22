from driver import Driver
from telegramSender import TelegramSender
from time import sleep

TIMEOUT = 1
TOKEN = '5265503049:AAG-ko-ifOBTIc0X8gQEIzquSBHDpe7NUEs'
CHAT_ID = '367335715'
ts = TelegramSender(TOKEN)
d = Driver()
d.login()
sent = []


def checkUpdates():
    for order in d.parseOrders():
        if order['id'] not in sent:
            sent.append(order['id'])
            ts.sendMessage(CHAT_ID, str(order))
            sleep(2)


def main():
    while True:
        print("Checking updates!")
        checkUpdates()
        sleep(TIMEOUT * 60)


if __name__ == "__main__":
    main()

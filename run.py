import json
import random
from src.instadm import InstaDM

f = open('infos/accounts.json', )
accounts = json.load(f)

with open('infos/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

message = "Beiens(a 10-year brand that aims at baby products) is looking for brand partners!\n" \
          "As a brand partner of Beiens you will:\n" \
          "✔️Get FREE beiens products for your little\n" \
          "✔️Receive 10% OFF promo code and earn commission on every sale\n" \
          "✔️Be promoted on our different social networks\n" \
          "✔️Get a chance to become our brand ambassador\n\n" \
          "Hey, I’m Jack, the Brand Manager of @beiens_official. Your little is so cute and interests us. We have " \
          "limited " \
          "monthly spots and want to give you a chance to enroll.\n" \
          "beiens-world.com is our website (not all the products) \n" \
          "Let us know by sending us a DM if you are interested! "

while True:
    if not usernames:
        print('Finished usernames.')
        break

    for account in accounts:
        if not usernames:
            break
        # Auto login
        insta = InstaDM(username=account["username"],
                        password=account["password"], headless=False)

        while True:
            if not usernames:
                break

            username = usernames.pop()
            # Send message
            insta.sendMessage(
                user=username, message=message)

        insta.teardown()

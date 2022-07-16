import json
import random
from src.instadm import InstaDM

f = open('infos/accounts.json',)
accounts = json.load(f)

with open('infos/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

message = "Hello, I was interested in collaborating with you.\n\n" \
          "test\n\n" \
          "have something to test\n\n" \
          "test"
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

# Simple game that will return
# random item for list

import random

message = ['It is cerain',
           'Yes definitely',
           'Reply hazy try again',
           'Ash again later',
           'Concatinate and ask again',
           'My reply is no',
           'Outlook not so good',
           'Very doubtful']

print(message[random.randint(0, len(message) - 1)])
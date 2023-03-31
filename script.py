import csv
import re
import time

import keyboard


def write_text(text: str, short_name: str) -> None:
    if '{name}' in text:
        keyboard.write(text.format(name=short_name), delay=0.01)
    else:
        keyboard.write(text, delay=0.01)
    time.sleep(0.1)


# load message template
message_template = open("message_template.txt", "r",
                        encoding='utf-8').read().splitlines()

# load recipients
recipients = list(csv.reader(open("recipients.csv", "r", newline='',
                  encoding='utf-8'), delimiter=',', dialect='excel'))[1:]

# open WA and wait
keyboard.send('win')
time.sleep(0.5)
keyboard.write('WhatsApp')
time.sleep(0.1)
keyboard.send('enter')
time.sleep(10)

for full_name, short_name in recipients:
    print(f"Writing message to {full_name} ({short_name}) ...")
    time.sleep(1)
    # selecting chat
    keyboard.send('ctrl+f')
    time.sleep(0.3)
    keyboard.send('ctrl+a')
    keyboard.write(full_name)
    time.sleep(2)
    keyboard.send('tab')
    time.sleep(0.3)
    keyboard.send('enter')
    time.sleep(1)
    # writing text
    for line in message_template:
        # check for emojis
        emojis = re.finditer(r':[A-Za-z_-]+', line)
        if emojis:
            cursor = 0
            for emoji in emojis:
                emoji_end = emoji.span()[1]
                write_text(line[cursor:emoji_end], short_name)
                time.sleep(1)
                keyboard.send('shift+enter')
                cursor = emoji_end
            write_text(line[cursor:], short_name)
        else:
            write_text(line, short_name)
        keyboard.send('shift+enter')
    # send message
    time.sleep(5)
    keyboard.send('enter')
    print(f"... sent message to {full_name} ({short_name}).")
